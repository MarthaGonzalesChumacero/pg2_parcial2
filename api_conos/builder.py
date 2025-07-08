from .logger import LoggerSingleton

class ConoBuilder:
    def __init__(self, cono):
        self.cono = cono
        self.logger = LoggerSingleton()

    def agregar_toppings(self, toppings):
        self.cono.ingredientes.extend(toppings)
        self.cono.precio += len(toppings) * 2
        return self

    def resultado(self):
        self.logger.log(f"Cono construido: ${self.cono.precio} - {self.cono.ingredientes}")
        return self.cono
