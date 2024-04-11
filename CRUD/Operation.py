from . import Database
from .Utility import random_string
import time
import os

def delete(no_book):
    try:
        with open(Database.DB_NAME,"r") as file:
            counter = 0
            while True:
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_book - 1:
                    pass
                else:
                    with open("data_temp.txt","a",encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1
    except:
        print("DATABASE ERROR")
    
    os.rename("data_temp.txt",Database.DB_NAME)

def update(no_book,pk,date_add,title,author,year):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = date_add
    data["title"] = title + Database.TEMPLATE["title"][len(title):]
    data["author"] = author + Database.TEMPLATE["author"][len(author):]
    data["year"] = str(year)

    data_str = f'{data["pk"]},{data["date_add"]},{data["title"]},{data["author"]},{data["year"]}\n'

    data_length = len(data_str)

    try:
        with open(Database.DB_NAME,"r+",encoding="utf-8") as file:
            file.seek(data_length*(no_book-1))
            file.write(data_str)
    except:
        print(f"Error occured while updating data")

def create(title,author,year):
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-$H.$M-%S%z",time.gmtime())
    data["title"] = title + Database.TEMPLATE["title"][len(title):]
    data["author"] = author + Database.TEMPLATE["author"][len(author):]
    data["year"] = str(year)

    data_str = f'{data["pk"]},{data["date_add"]},{data["title"]},{data["author"]},{data["year"]}\n'

    try:
        with open(Database.DB_NAME,"a",encoding="utf-8") as file:
            file.write(data_str)
    except:
        print(f"Input error")


def create_first_data():
    title  = input("Title of the book\t: ")
    author = input("Author name\t: ")
    while True:
        try:
            year = int(input("Year published\t: "))
            if len(str(year)) == 4 :
                break
            else :
                print(f"\nThe year's you input doesn't exist\n")
        except:
            print(f"The year's data must be a nunber (yyyy)")

    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-$H.$M-%S%z",time.gmtime())
    data["title"] = title + Database.TEMPLATE["title"][len(title):]
    data["author"] = author + Database.TEMPLATE["author"][len(author):]
    data["year"] = str(year)

    data_str = f'{data["pk"]},{data["date_add"]},{data["title"]},{data["author"]},{data["year"]}\n'
    print(data_str)
    try:
        with open(Database.DB_NAME,"w",encoding="utf-8") as file:
            file.write(data_str)
    except:
        print(f"Programme Error")

def read(**kwargs):
    try:
        with open(Database.DB_NAME,"r") as file:
            content = file.readlines()
            amount_of_books = len(content)
            if "index" in kwargs:
                book_index = kwargs["index"]-1
                if book_index < 0 or book_index > amount_of_books:
                    return False
                else:
                    return content[book_index]
            else:
                return content
    except:
        print(f"Error reading databases")
        return False