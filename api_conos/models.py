from django.db import models
from django.core.exceptions import ValidationError

TOPPINGS_VALIDOS = {
    'queso_extra', 'papas_al_hilo', 'salchicha_extra',
    'tomate', 'aceitunas', 'pimientos'
}

VARIANTES = [
    ('Carnívoro', 'Carnívoro'),
    ('Vegetariano', 'Vegetariano'),
    ('Saludable', 'Saludable'),
]

TAMANIOS = [
    ('Pequeño', 'Pequeño'),
    ('Mediano', 'Mediano'),
    ('Grande', 'Grande'),
]

class PedidoCono(models.Model):
    cliente = models.CharField(max_length=100)
    variante = models.CharField(max_length=20, choices=VARIANTES)
    toppings = models.JSONField()
    tamanio_cono = models.CharField(max_length=20, choices=TAMANIOS)
    fecha_pedido = models.DateField(auto_now_add=True)

    def clean(self):
        if not isinstance(self.toppings, list):
            raise ValidationError("Toppings debe ser una lista.")

        for topping in self.toppings:
            if topping not in TOPPINGS_VALIDOS:
                raise ValidationError(f"Topping inválido: {topping}")

    def save(self, *args, **kwargs):
        self.full_clean()  # Valida antes de guardar
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cliente} - {self.variante} - {self.tamanio_cono}"