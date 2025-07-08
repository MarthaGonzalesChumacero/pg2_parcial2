class ConoBase:
    def __init__(self, tamanio):
        self.tamanio = tamanio
        self.precio = 0
        self.ingredientes = []

class ConoCarnivoro(ConoBase):
    def __init__(self, tamanio):
        super().__init__(tamanio)
        self.precio += {'Pequeño': 20, 'Mediano': 30, 'Grande': 40}[tamanio]
        self.ingredientes.append('carne')

class ConoVegetariano(ConoBase):
    def __init__(self, tamanio):
        super().__init__(tamanio)
        self.precio += {'Pequeño': 18, 'Mediano': 27, 'Grande': 36}[tamanio]
        self.ingredientes.append('tofu')

class ConoSaludable(ConoBase):
    def __init__(self, tamanio):
        super().__init__(tamanio)
        self.precio += {'Pequeño': 15, 'Mediano': 22, 'Grande': 30}[tamanio]
        self.ingredientes.append('espinaca')


