
import json 
patients=[]               # Store multiple patient records
def add_patient():
    global patients
    print("..............................")
    
    patient={}            # One patient record
    patient["Patient ID"]= input("Enter Patient ID: ")
    patient["Full Name"]= input("Enter Patient Name: ")
    patient["Date Of Birth"]  = input("Enter Patient Date Of Birth: ")
    patient["Gender"] = input("Enter Patient Gender: ")
    patient["Blood Group"] =input("Enter Patient Blood Group: ")
    patient["Contact Number"] = input("Enter Patient Contact Number: ")
    patient["Email"] = input("Enter Patient Email: ")
    patient["Address"] = input("Enter Patient Address: ")
    patient["Emergency Contact"] = input("Enter Patient Emergency Contact: ")
    patient["Registered Date"] = input("Enter Patient Registered Date: ")

     # Add one patient dictionary into patients list
    

    f=open("patients.json", "r")
    patients= json.load(f)
    f.close()

    patients.append(patient)

    f=open("patients.json", "w")
    json.dump(patients, f, indent=4)
    f.close()

    print("\nPatient Record Created:\n")
    for key, value in patient.items():
        print(f"{key}: {value}")
    

        
    print("...........................")

def view_patients():
    global patients
    
    f=open("patients.json", "r")
    patients= json.load(f)
    f.close()

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
            print("----------------------")
def search_patient():
    global patients
    
    f=open("patients.json", "r")
    patients= json.load(f)
    f.close()
    entered_ID = input("Enter Patient ID to search: ")
    for patient in patients:
        if patient["Patient ID"] == entered_ID:
            print("\nPatient Record Found:")
            
            for key, value in patient.items():
                print(f"{key}: {value}")
            return
          
    print("Patient not found.")

def update_patient():
    global patients
        
    f=open("patients.json", "r")
    patients= json.load(f)
    f.close()
    entered_ID = input("Enter Patient ID to search: ")
    for patient in patients:
        if patient["Patient ID"] == entered_ID:
            print("\n what do you want to update")
            print("1- Full Name")
            print("2- Date Of Birth")
            print("3- Gender")
            print("4- Blood Group")
            print("5- Contact Number")
            print("6- Email")
            print("7- Address")
            print("8- Emergency Contact")
            print("9- Registered Date")
            choice=int(input("which field do you want to update? "))
            if choice == 1:
                patient["Full Name"] = input("Enter new Full Name: ")
            elif choice == 2:
                patient["Date Of Birth"] = input("Enter new Date Of Birth: ")
            elif choice == 3:
                patient["Gender"] = input("Enter new Gender: ")
            elif choice == 4:
                patient["Blood Group"] = input("Enter new Blood Group: ")
            elif choice == 5:
                patient["Contact Number"] = input("Enter new Contact Number: ")
            elif choice == 6:
                patient["Email"] = input("Enter new Email: ")
            elif choice == 7:
                patient["Address"] = input("Enter new Address: ")
            elif choice == 8:
                patient["Emergency Contact"] = input("Enter new Emergency Contact: ")
            elif choice == 9:
                patient["Registered Date"] = input("Enter new Registered Date: ")
            else:
                print("Invalid choice. No updates made.")
                return
            f=open("patients.json", "w")
            json.dump(patients, f, indent=4)
            f.close()
    print("\nPatient Record Updated Successfully.")
def delete_patient():
    global patients
            
    f=open("patients.json", "r")
    patients= json.load(f)
    f.close()
    delete_ID = input("Enter Patient ID to delete:")
    for patient in patients:
            if patient["Patient ID"] == delete_ID:
                patients.remove(patient)
                print("Patient deleted successfully!")
                return 
    else:
        print("Patient not found!")
    f=open("patients.json", "w")
    json.dump(patients, f, indent=4)
    f.close()


