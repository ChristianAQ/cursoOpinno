from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from photos.validators import badwords

LICENSE_COPYRIGHT = 'Copyright'
LICENSE_COPYLEFT = 'Copyleft'
LICENSE_CC = 'Creative commons'

LICENSES = (
    (LICENSE_COPYRIGHT, 'Copyright'),
    (LICENSE_COPYLEFT, 'Copyleft'),
    (LICENSE_CC, 'Creative commons')
)

VISIBILITY_PUBLIC = 'Pública'
VISIBILITY_PRIVATE = 'Privada'

VISIBILITY = (
    (VISIBILITY_PUBLIC, 'Pública'),
    (VISIBILITY_PRIVATE, 'Privada')
)


class Photo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    url = models.URLField(null=True, blank=False)
    description = models.TextField(null=True, blank=False, validators=[badwords])
    license = models.CharField(max_length=16, choices=LICENSES, default=LICENSE_CC)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) #las dos ultimas lineas    poner la fecha creada y actualizada automaticamente
    visibility = models.CharField(max_length=7, choices=VISIBILITY, default=VISIBILITY_PUBLIC)

    def __str__(self):
        return self.name
