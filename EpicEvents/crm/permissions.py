from rest_framework import permissions
from rest_framework import exceptions
from django.shortcuts import get_object_or_404, get_list_or_404

SUPPORT = 1
SELLER = 2

class Seller(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == SELLER:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        method = request.method
        if request.user.role == SELLER and method in ('PATCH', 'DELETE', 'GET'):
            try:
                if obj.sales_contact == request.user:
                    return True
                else:
                    raise exceptions.PermissionDenied(detail="not your client")
            except AttributeError:
                if obj.client.sales_contact == request.user:
                    return True
                else:
                    raise exceptions.PermissionDenied(detail="this event is not one of your client")
        else:
            return False


class Support(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == SUPPORT:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        method = request.method
        if request.user.role == SUPPORT and method in ('PATCH', 'DELETE', 'GET'):
            try:
                if obj.support_contact == request.user:
                    return True
                else:
                    raise exceptions.PermissionDenied(detail="this event is not one of your client")
            except AttributeError:
                raise exceptions.PermissionDenied(detail="you are not allow to edit clients or contracts / only events")
        else:
            return False