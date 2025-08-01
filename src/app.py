#cli

from ETL.extract import Extract_from_API
from ETL.tranform import Transform

def main_menu():
    while True:

        print("\nweather app\n".upper())
        print("\t0. Exit")
        print("\t1. Your location")
        print("\t2. Select a different location")

        user_selection = input("\nSelect An Option: ")

        if user_selection == "1":
            extractor = Extract_from_API()
            extractor.run()

            transformer = Transform()
            transformer.transform()
            transformer.summary()
        elif user_selection == "2":
            pass #print locations list menu
        elif user_selection == "0":
            print("\nClosing application, have a good day!\n")
            break
        else:
            print("\n[ERROR] Invalid entry, please try again.\n")

main_menu()








