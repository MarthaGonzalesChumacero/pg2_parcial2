from api_conos.modelos_conos import ConoCarnivoro, ConoVegetariano, ConoSaludable

class ConoFactory:
    @staticmethod
    def crear_cono(variante, tamanio):
        opciones = {
            'carnivoro': ConoCarnivoro,
            'vegetariano': ConoVegetariano,
            'saludable': ConoSaludable,
        }
        clave = variante.lower().replace('í', 'i')
        clase_cono = opciones.get(clave)
        if clase_cono is None:
            raise ValueError(f"Variante desconocida: {variante}")
        return clase_cono(tamanio)
