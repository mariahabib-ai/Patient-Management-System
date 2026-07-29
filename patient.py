
patients=[]               # Store multiple patient records
def add_patient():
    
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
    
    patients.append(patient)

    print("\nPatient Record Created:\n")
    for key, value in patient.items():
        print(f"{key}: {value}")
