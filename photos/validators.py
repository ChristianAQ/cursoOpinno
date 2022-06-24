from rest_framework.exceptions import ValidationError

#lista de palabras mal sonantes u ofensivas
BADWORDS = ("tonto", "caraanchoa", "bobo", "cabrón", "pendejo", "idiota")


def badwords(description):
    """
    Valida que la descripcion no contenga ninguna palabrota
    :return:
    """
    for badword in BADWORDS:
        if badword in description:
            raise ValidationError("La palabra {0} no está permitida".format(badword))
    return True