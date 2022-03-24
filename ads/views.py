import json

from django.core.paginator import Paginator
from django.db.models import Count
from django.http import JsonResponse, request
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from rest_framework.generics import RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models import Ad, Category
from ads.permissions import AdCreatePermission
from ads.serializers import AdSerializer
from avito import settings
from users.models import User


class CategoryListView(ListView):
    model = Category
    queryset = Category.objects.all()

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object_list = self.object_list.order_by("name")

        response = []
        for category in self.object_list:
            response.append({
                "id": category.id,
                "name": category.name,
            })

        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ["name"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        ad_data = json.loads(request.body)
        self.object.name = ad_data["name"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    fields = ["name"]

    def post(self, request, *args, **kwargs):
        category_data = json.loads(request.body)

        category = Category.objects.create(
            name=category_data["name"],
        )

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })


class AdListView(ListView):
    model = Ad
    queryset = Ad.objects.all()

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.queryset =self.get_queryset()

        category_id = request.GET.getlist("catt", [])
        if category_id:
            self.queryset = self.queryset.filter(cat__in=category_id)
        if r := request.GET.get("text", None):
            self.queryset = self.queryset.filter(description__contains=r).annotate(Count('author'))
        if r := request.GET.get("location", None):
            self.queryset = self.queryset.filter(author__locations__name__icontains=r).annotate(Count('author'))
        if r := request.GET.get("price_from", None):
            self.queryset = self.queryset.filter(price__gte=r)
        if r := request.GET.get("price_to", None):
            self.queryset = self.queryset.filter(price__lte=r)

        self.object_list = self.object_list.select_related('author').order_by('-price')
        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        ads = []
        for ad in page_obj:
            ads.append({
                "id": ad.id,
                "name": ad.name,
                "author_id": ad.author_id,
                "author": ad.author.first_name,
                "price": ad.price,
                "description": ad.description,
                "is_published": ad.is_published,
                "category_id": ad.category_id,
                "image": ad.image.url if ad.image else None,
            })

        response = {
            "items": ads,
            "num_pages": page_obj.paginator.num_pages,
            "total": page_obj.paginator.count,
        }
        return JsonResponse(response, safe=False)


class AdCreateView(CreateAPIView):
    queryset = Ad
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, AdCreatePermission]


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]


class AdUpdateView(UpdateAPIView):
    request = Ad
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]


class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, AdCreatePermission]


@method_decorator(csrf_exempt, name='dispatch')
class AdImageView(UpdateView):
    model = Ad
    fields = ["name", "price", "description", "is_published", "image"]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.logo = request.FILES["image"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author_id": self.object.author_id,
            "author": self.object.author.first_name,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "image": self.object.image.url if self.object else None,
            "category_id": self.object.category_id,
        })