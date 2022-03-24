from rest_framework.permissions import BasePermission

from ads.models import Compilation
from users.models import User


class AdCreatePermission(BasePermission):
    message = "Adding adverts for non hr user not allowed"

    def has_permission(self, request, view):
        return request.user.role == User.HR


class CompilationUpdatePermission(BasePermission):
    message = 'You can not manage not your compilations'

    def has_permission(self, request, view):
        entity = Compilation.objects.get(pk=view.kwargs["pk"])
        if entity.owner_id == request.user.id:
            return True
        return False


class IsAuthenticatedAndOwner(BasePermission):
    message = 'You must be the owner of this object.'

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class AdUpdatePermission(BasePermission):
    message = 'Managing others ads not permitted.'

    def has_permission(self, request, view):
        if request.user.role in [User.HR, User.EMPLOYEE]:
            return True
        return False
