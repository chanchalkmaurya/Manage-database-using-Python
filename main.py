import coursedb

if __name__ == "__main__":
    print("**" * 25)
    print("\n           :: Course Management ::          \n")
    print("**" * 25)

    print("\n\n\n")

    # create object of coursedb.ManageDatabase
    db = coursedb.ManageDatabase()
    
    print("#" * 50)
    print("\n           :: User Guide/Manual ::          \n")
    print("#" * 50)
    print("\n")

    print("Press 1. Insert a course")
    print("Press 2. Show all course")
    print("Press 3. Delete a course (Need Course ID)")
    print("Press 4. stop the execution \n")

    print("#"*50)
    print("\n")

    while(True):
        choice = int(input("Enter a choice: "))

        if choice == 1:
            name = input("\nEnter name of the course : ")
            desc = input("\nEnter Description of the course : ")
            price = input("\nEnter Price of the course : ")
            is_private = int(input("\nIs this course is private : (If yes press 1, otherwise press 0) : "))
            
            if db.insert_data([name, desc, price, is_private]):
                print("Course added successfully")
            else:
                print("OOPS Something went wrong")

        elif choice == 2:
            course_detail = db.fetch_data()
            print("*"*50)
            print("\n           :: Course Details ::            \n ")
            print("*"*50)

            for idx, item in enumerate(course_detail):
                print('Serial No. : ' + str(idx + 1))
                print('Course ID : ' + str(item[0]))
                print('Course name : ' + str(item[1]))
                print('Course Description : ' + str(item[2]))
                print('Price : ' + str(item[3]))
                private = "Yes" if item[4] else "No"
                print('Private : ' + private)

                print("\n")


        elif choice == 3:
            id = int(input("Enter the course ID"))
            if db.delete_data(id):
                print("Course deleted Successfully")
            else:
                print("OOPS Something went wrong")
        
        elif choice == 4:
            break

        else:
            print("Enter a valid choice")

        print("\n")
