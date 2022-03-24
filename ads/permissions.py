from rest_framework.permissions import BasePermission

from users.models import User


class AdCreatePermission(BasePermission):
    message = "Adding adverts for non hr user not allowed"

    def has_permission(self, request, view):
        return request.user.role == User.HR
