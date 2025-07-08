class EstrategiaBase:
    def calcular_precio(self, tamanio):
        raise NotImplementedError

    def ingredientes_extra(self, toppings):
        raise NotImplementedError


class EstrategiaCarnivoro(EstrategiaBase):
    def calcular_precio(self, tamanio):
        base = {'Pequeño': 20, 'Mediano': 30, 'Grande': 40}
        return base[tamanio] + 10

    def ingredientes_extra(self, toppings):
        return ['carne'] + toppings


class EstrategiaVegetariano(EstrategiaBase):
    def calcular_precio(self, tamanio):
        base = {'Pequeño': 18, 'Mediano': 27, 'Grande': 36}
        return base[tamanio] + 5

    def ingredientes_extra(self, toppings):
        return ['tofu'] + toppings


class EstrategiaSaludable(EstrategiaBase):
    def calcular_precio(self, tamanio):
        base = {'Pequeño': 15, 'Mediano': 22, 'Grande': 30}
        return base[tamanio] + 2

    def ingredientes_extra(self, toppings):
        return ['espinaca'] + toppings


class EstrategiaFactory:
    @staticmethod
    def obtener_estrategia(variante):
        estrategias = {
            'Carnívoro': EstrategiaCarnivoro(),
            'Vegetariano': EstrategiaVegetariano(),
            'Saludable': EstrategiaSaludable(),
        }
        return estrategias[variante]