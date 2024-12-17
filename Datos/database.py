class Database:
    def __init__(self):
        self.db_connection = None

    def connect(self):
        print("Conectando a la base de datos...")
        self.db_connection = True

    def disconnect(self):
        print("Desconectando la base de datos...")
        self.db_connection = False
