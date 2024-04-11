from pymongo import MongoClient


def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb://localhost:27017"

    # Cree una conexión con MongoClient. Puede importar MongoClient o usar pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Cree la base de datos para nuestro ejemplo (usaremos la misma base de datos en todo el tutorial
    return client['prueba']


# Esto se agrega para que muchos archivos pueden reutilizar la función get_database()
if __name__ == "__main__":
    # Get the database
    dbname = get_database()