from . import Operation

DB_NAME = "data.txt"
TEMPLATE = {
    "pk":"XXXXXX",
    "date_add":"yyyy-mm-dd",
    "title":255*" ",
    "author":255*" ",
    "year": "yyyy",
}

def init_console():
    try:
        with open(DB_NAME,"r") as file:
            print("Database available, init done")
    except:
            print(f"Databases not found, please make a new one")
            Operation.create_first_data()