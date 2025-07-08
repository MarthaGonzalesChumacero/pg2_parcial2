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
        toppings_set = set(self.toppings)
        if not toppings_set.issubset(TOPPINGS_VALIDOS):
            raise ValidationError(f"Toppings inválidos: {toppings_set - TOPPINGS_VALIDOS}")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cliente} - {self.variante} - {self.tamanio_cono}"
