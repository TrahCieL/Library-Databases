import os
import CRUD as CRUD

if __name__ == "__main__":
    operation_system = os.name

    match operation_system :
            case "posix" : os.system("clear")
            case "nt" : os.system("cls")

    print(f"WELCOME TO".center(23,'-'))
    print(f"UNDIP LIBRARY DATABASES")
    print(f"{23*'='}")

    # check database ada atau tidak
    CRUD.init_console()

    while True:

        match operation_system :
            case "posix" : os.system("clear")
            case "nt" : os.system("cls")

        print(f"WELCOME TO".center(23,'-'))
        print(f"UNDIP LIBRARY DATABASES")
        print(f"{23*'='}")

        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data\n")

        user_option = input("Select An Option Above: ")

        match user_option:
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": CRUD.update_console()
            case "4": CRUD.delete_console()

        is_done = input("\nContinue (Y/n)? : ")
        if is_done == "n" or is_done == "N":
            break

    print(f"\nEND OF THE PROGRAM, THANK YOU")


        
        
