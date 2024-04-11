from . import Operation

def delete_console():
    read_console()
    while True:
        no_book = int(input("Select a book you want to delete!: "))
        data_book = Operation.read(index=no_book)

        if data_book:
            data_break = data_book.split(",")
            pk = data_break[0]
            date_add = data_break[1]
            title = data_break[2]
            author = data_break[3]
            year = data_break[4][:-1]

            print(f"\n{100*'='}")
            print(f"Please select the data you want to update!")
            print(f"1. Title\t: {title:.40}")
            print(f"2. Author\t: {author:.40}")
            print(f"3. Year\t\t: {year:4}")

            is_done = input("\nIs it the data that you want to delete (Y/n)? : ")
            if is_done == "y" or is_done == "Y":
                Operation.delete(no_book)
                break
        else:
            print(f"Invalid number, please select a new one")
    
    print(f"\nSuccesfully deleting data")

def update_console():
    read_console()
    while True:
        no_book = int(input("Select a book you want to update!: "))
        data_book = Operation.read(index=no_book)

        if data_book:
            break
        else:
            print(f"Invalid number, please select a new one")

    data_break = data_book.split(",")
    pk = data_break[0]
    date_add = data_break[1]
    title = data_break[2]
    author = data_break[3]
    year = data_break[4][:-1]

    while True:
        # data that wanted to update
        print(f"\n{100*'='}")
        print(f"Please select the data you want to update!")
        print(f"1. Title\t: {title:.40}")
        print(f"2. Author\t: {author:.40}")
        print(f"3. Year\t\t: {year:4}")

        # select mode to update
        user_option = input("\nSelect a data[1,2,3]: ")
        print(f"\n{100*'='}")
        match user_option:
            case "1" : title = input("Title of the book\t: ")
            case "2" : author = input("Author's name\t: ")
            case "3" :
                while True:
                    try:
                        year = int(input("Year published\t\t: "))
                        if len(str(year)) == 4 :
                            break
                        else :
                            print(f"The year's you input doesn't exist")
                    except:
                        print(f"The year's data must be the following number format (yyyy)")
            case _: print(f"Invalid index selected")
        
        print(f"Here's the new databases")
        print(f"1. Title\t: {title:.40}")
        print(f"2. Author\t: {author:.40}")
        print(f"3. Year\t\t: {year:4}")
        is_done = input("\nIs the data that you inputted are correct (Y/n)? : ")
        if is_done == "y" or is_done == "Y":
            break

    Operation.update(no_book,pk,date_add,title,author,year)

def create_console():
    print(f"\n\n{100*'='}")
    print(f"Please add a new book")

    title = input("Title of the book\t: ")
    author = input("Name of the author\t: ")
    while True:
        try:
            year = int(input("Year published\t\t: "))
            if len(str(year)) == 4 :
                break
            else :
                print(f"The year's you input doesn't exist")
        except:
            print(f"The year's data must be a nunber (yyyy)")

    Operation.create(title,author,year)
    print(f"\nHere's yout new databases")
    read_console()

def read_console():
    data_file = Operation.read()

    index  = "No"
    title  = "Title"
    author = "Author"
    year   = "Year"

    # Header
    print(f"\n{100*'='}")
    print(f"{index:4} | {title:40} | {author:40} | {year:5}")
    print(f"{'-'*100}")

    # Data
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        title = data_break[2]
        author = data_break[3]
        year = data_break[4]
        print(f"{index+1:4} | {title:.40} | {author:.40} | {year:4}", end="")

    # Footer
    print(f"\n{100*'='}\n")