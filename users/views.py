import json

from django.core.paginator import Paginator
from django.db.models import Count
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from avito import settings
from users.models import User, Location
from users.serializers import UserRetrieveSerializer, UserCreateSerializer, UserListSerializer, UserDeleteSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    # def get(self, request, *args, **kwargs):
    #     super().get(request, *args, **kwargs)
    #     self.object_list = self.object_list.annotate(total_ads=Count('ad'))
    #
    #     paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
    #     page_number = request.GET.get('page')
    #     page_obj = paginator.get_page(page_number)
    #
    #     # users = []
    #     # for user in page_obj:
    #     #     users.append({
    #     #         "id":user.id,
    #     #         "username": user.first_name,
    #     #         "first_name": user.first_name,
    #     #         "last_name": user.last_name,
    #     #         "role": user.role,
    #     #         "age": user.age,
    #     #         "total_ads": user.total_ads,
    #     #         "locations": list(map(str, user.location.all()))
    #     #     })
    #     users = UserListSerializer(page_obj, many=True)
    #     response = {
    #         "items": users.data,
    #         "num_pages": page_obj.paginator.num_pages,
    #         "total": page_obj.paginator.count,
    #     }
    #
    #     return JsonResponse(response, safe=False)


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieveSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDeleteSerializer
