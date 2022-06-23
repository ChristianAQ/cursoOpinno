from django.contrib import admin
from django.utils.safestring import mark_safe
from photos.models import Photo
from users.models import Usuario, Registrado, Administrador, PerfilSocial, Review


class UsuarioAdmin(admin.ModelAdmin):
    list_display = [po.name for po in Usuario._meta.get_fields()]
    search_fields = ('id', 'nombre')  # siempre tienen que ser una tupla
    list_filter = ('id', 'nombre')  # siempre tienen que ser una tupla
admin.site.register(Usuario, UsuarioAdmin)

class RegistradoAdmin(admin.ModelAdmin):
    list_display = [po.name for po in Registrado._meta.get_fields()]
    search_fields = ('id', 'telefono')  # siempre tienen que ser una tupla
    list_filter = ('id', 'telefono')  # siempre tienen que ser una tupla
admin.site.register(Registrado, RegistradoAdmin)

class PerfilSocialAdmin(admin.ModelAdmin):
    list_display = [po.name for po in PerfilSocial._meta.get_fields()]
    search_fields = ('id', 'nombre')  # siempre tienen que ser una tupla
    list_filter = ('id', 'nombre')  # siempre tienen que ser una tupla
admin.site.register(PerfilSocial, PerfilSocialAdmin)

