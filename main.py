import  patient_management


while True:
    print(".....EHR_Nexus.......")

    print("1- Add Patient")
    print("2- View Patients")
    print("3- Search Patient")
    print("4- Add Medical Visit")
    print("5- View Medical History")
    print("6- Update Patient Record")
    print("7- Delete Patient ")
    print("8- Exit ")

    print("................................")

    print("\nWhich service do you need?")
    choice = int(input("enter your choice:"))
    if choice == 1:
        print("ADD Patient Feature Selected ")
        patient.add_patient()
    elif choice == 2:
        print("View Patient Feature Selected ")
        patient.view_patients()
    elif choice == 3:
        print("Search Patient Feature Selected ")
        patient.search_patient()
    elif choice == 4:
         print("Add Medical Visit Feature Selected ")
    elif choice == 5:
        print("View Medical History Feature Selected ")
    elif choice == 6:
        print("Update Patient Record Feature Selected ")
        patient.update_patient()
    elif choice == 7:
        print("Delete Patient Feature Selected ")
        patient.delete_patient()
    elif choice == 8:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

