import json

def load_patients():

    try:
        with open("patients.json", "r") as f:
            patients = json.load(f)

    except FileNotFoundError:
        patients = []

    except json.JSONDecodeError:
        print("Database file is corrupted. Starting with empty database.")
        patients = []

    return patients


def save_patients(patients):

    with open("patients.json", "w") as f:
        json.dump(patients, f, indent=4)