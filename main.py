import patient_management


while True:
    print(".....Patient Management System.....")

    print("1- Add Patient")
    print("2- View Patients")
    print("3- Search Patient")
    print("4- Update Patient Record")
    print("5- Delete Patient")
    print("6- Exit")

    print("................................")

    print("\nWhich service do you need?")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        print("Add Patient Feature Selected")
        patient_management.add_patient()

    elif choice == 2:
        print("View Patient Feature Selected")
        patient_management.view_patients()

    elif choice == 3:
        print("Search Patient Feature Selected")
        patient_management.search_patient()

    elif choice == 4:
        print("Update Patient Record Feature Selected")
        patient_management.update_patient()

    elif choice == 5:
        print("Delete Patient Feature Selected")
        patient_management.delete_patient()

    elif choice == 6:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")