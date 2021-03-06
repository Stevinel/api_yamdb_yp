from rest_framework import permissions


class AdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_superuser
            or request.user.is_admin
        )


class GeneralPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and (
                request.user.is_staff
                or request.user.is_admin
            )
            or request.method in permissions.SAFE_METHODS
        )


class ReviewPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser or request.user.is_admin


class ReviewsPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["POST", "DELETE", "PATCH"]:
            return (
                request.user.is_moderator
                or obj.author == request.user
            )
        else:
            return permissions.IsAuthenticatedOrReadOnly


class ModeratorPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_moderator
        )
