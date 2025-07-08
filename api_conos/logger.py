import datetime

class LoggerSingleton:
    _instance = None
    _logs = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LoggerSingleton, cls).__new__(cls)
        return cls._instance

    def log(self, mensaje):
        timestamp = datetime.datetime.now().isoformat()
        self._logs.append(f"[{timestamp}] {mensaje}")

    def obtener_logs(self):
        return self._logs