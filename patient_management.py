
import database 

patients=[]             # Store multiple patient records
 

# Validate empty input
def get_required_input(message):
    while True:
        value = input(message)

        if value.strip() == "":
            print("This field cannot be empty. Please try again.")
        else:
            return value

def add_patient():
    global patients       

    print("..............................")

     # Load existing patients first
    patients = database.load_patients()

    patient = {}

    # Check duplicate Patient ID

    while True:
        patient["Patient ID"] = get_required_input("Enter Patient ID: ")

        duplicate = False

        for existing_patient in patients:
         if existing_patient["Patient ID"] == patient["Patient ID"]:
            duplicate = True
            print("Patient ID already exists. Use another ID.")
            break

        if not duplicate:
         break
     #  Collect remaining details

    patient["Full Name"]= get_required_input("Enter Patient Name: ")
    patient["Date Of Birth"]  = get_required_input("Enter Patient Date Of Birth: ")
    patient["Gender"] = get_required_input("Enter Patient Gender: ")
    patient["Blood Group"] =get_required_input("Enter Patient Blood Group: ")
    patient["Contact Number"] = get_required_input("Enter Patient Contact Number: ")
    patient["Email"] = get_required_input("Enter Patient Email: ")
    patient["Address"] = get_required_input("Enter Patient Address: ")
    patient["Emergency Contact"] = get_required_input("Enter Patient Emergency Contact: ")
    patient["Registered Date"] = get_required_input("Enter Patient Registered Date: ")

     
    
     # Add one patient dictionary into patients list
        

    patients.append(patient)

     # Save data

    database.save_patients(patients)

    print("\nPatient Record Created:\n")
    for key, value in patient.items():
        print(f"{key}: {value}")
    

        
    print("...........................")

def view_patients():
    global patients
    
    patients = database.load_patients()

    if not patients:
        print("No patient records found.")

    else:
        print("\n--- Patient Records ---")

        for patient in patients:
            print("----------------------")
            print("Patient ID:", patient["Patient ID"])
            print("Full Name:", patient["Full Name"])
            print("Date Of Birth:", patient["Date Of Birth"])
            print("Gender:", patient["Gender"])
            print("Blood Group:", patient["Blood Group"])
            print("Contact Number:", patient["Contact Number"])
            print("Email:", patient["Email"])
            print("Address:", patient["Address"])
            print("Emergency Contact:", patient["Emergency Contact"])
            print("Registered Date:", patient["Registered Date"])
            ``
            print("\n----------------------\n")

def search_patient():
    global patients
    
    patients = database.load_patients()

    entered_ID = get_required_input("Enter Patient ID to search: ")

    for patient in patients:
        if patient["Patient ID"] == entered_ID:
            print("\nPatient Record Found:")
            
            for key, value in patient.items():
                print(f"{key}: {value}")
            return
          
    print("Patient not found.")

def update_patient():
    global patients
        
    patients = database.load_patients()

    entered_ID = get_required_input("Enter Patient ID to update : ")

    found = False

    for patient in patients:
        if str(patient["Patient ID"]) == str(entered_ID):
            found = True 

            print("\nWhat do you want to update")
            print("1- Full Name")
            print("2- Date Of Birth")
            print("3- Gender")
            print("4- Blood Group")
            print("5- Contact Number")
            print("6- Email")
            print("7- Address")
            print("8- Emergency Contact")
            print("9- Registered Date")

            try:
                choice = int(input("Which field do you want to update? "))

            except:
                print("Please enter number")
                return


            if choice == 1:
                patient["Full Name"] = get_required_input("Enter new Full Name: ")

            elif choice == 2:
                patient["Date Of Birth"] = get_required_input("Enter new Date Of Birth: ")

            elif choice == 3:
                patient["Gender"] = get_required_input("Enter new Gender: ")

            elif choice == 4:
                patient["Blood Group"] = get_required_input("Enter new Blood Group: ")

            elif choice == 5:
                patient["Contact Number"] = get_required_input("Enter new Contact Number: ")

            elif choice == 6:
                patient["Email"] = get_required_input("Enter new Email: ")

            elif choice == 7:
                patient["Address"] = get_required_input("Enter new Address: ")

            elif choice == 8:
                patient["Emergency Contact"] = get_required_input("Enter new Emergency Contact: ")

            elif choice == 9:
                patient["Registered Date"] = get_required_input("Enter new Registered Date: ")

            else:
                print("Invalid choice. No updates made.")
                return


            database.save_patients(patients)

            print("\nPatient Record Updated Successfully.")
            return


    if found == False:
        print("\nPatient record not found.")

        print("\n................................\n")

def delete_patient():
    global patients
            
    patients = database.load_patients()

    delete_ID = get_required_input("Enter Patient ID to delete:")
    found = False 
    for patient in patients:
            if patient["Patient ID"] == delete_ID:
              found = True
              print("\nPatient Record Found:")
              for key, value in patient.items():
                print(f"{key}: {value}")

              confirm = input("\nAre you sure you want to delete? (yes/no): ")

              if confirm.lower() == "yes":
                patients.remove(patient)

                database.save_patients(patients)

                print("Patient deleted successfully!")
                return
              else :
                 print("Deletion cancelled.")
                 return
    if found == False:       
     print("Patient not found!")


