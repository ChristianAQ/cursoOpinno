from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        """
        DEfine si un usuario puede accedes al emtodo o accede a la vista/controlador que quiere accedes
        :param request:
        :param view:
        :return:
        """
        if request.method == "POST":
            return True
        if request.user.is_superuser:
            return True
        if view.action in ("retrieve", "update", "destroy"):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """
        Define si un usuario puede realizar la operacion que quiera sobre  el objeto 'obj'
        :param request:
        :param view:
        :param obj:
        :return:
        """
        return request.user.is_superuser or request.user == obj
