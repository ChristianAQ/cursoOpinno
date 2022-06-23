from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, User
from datetime import date
from django.urls import reverse



class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField("Nombre",max_length=35, null=True, blank=True)
    ap1 = models.CharField("Apellido 1",max_length=35, null=True, blank=True)
    ap2 = models.CharField("Apellido 2", max_length=35, null=True, blank=True)
    email = models.CharField("Email",max_length=25)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)  # requerido desde django 2.0

    def __str__(self):
        return '%s,%s,%s,%s,%s,%s' % (self.id, self.nombre, self.ap1, self.ap2, self.email, self.user)


class Registrado(models.Model):
    id = models.AutoField(primary_key=True)
    telefono = models.CharField("Telefono", max_length=9,null=True, blank=True)
    fecha_registro = models.DateField("Fecha Registro", null=True, blank=True)
    usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return '%s,%s,%s,%s' % (
        self.id, self.historial, self.fecha_registro, self.usuario)


class Administrador(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Registrado, null=True, blank=True, on_delete=models.PROTECT)
    def __str__(self):
        return '%s,%s' % (
        self.id, self.usuario)


class PerfilSocial(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_creacion = models.DateField("Fecha Creación", null=True, blank=True)
    # reseñas
    nombre = models.ForeignKey(Registrado, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return '%s,%s,%s' % (
        self.id, self.fecha_creacion, self.nombre)
class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    perfilsocial = models.ForeignKey(PerfilSocial, null=True, blank=True, on_delete=models.PROTECT)
    class Meta:
        abstract = True


