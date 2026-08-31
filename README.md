# Patient Management System

## What It Does

The **Patient Management System** is a Python-based command-line application for managing basic patient records.

It allows users to create, view, search, update, and delete patient information. Patient records are stored in a structured JSON file.

---

## Problem

Managing patient information manually can make it difficult to organize, find, and update records efficiently.

This project provides a simple structured system for managing patient records and demonstrates the basic workflow of digital patient information management.

---

## Features

* Add new patient records
* View patient records
* Search patients by Patient ID
* Update patient information
* Delete patient records
* Prevent duplicate Patient IDs
* Validate required fields
* Store patient data in JSON
* Handle missing or corrupted JSON files
* Modular code organization

---

## Workflow

```text
Start Application
       ↓
Main Menu
       ↓
Select Operation
       ↓
Add / View / Search / Update / Delete
       ↓
Validate Input
       ↓
Load Patient Data
       ↓
Perform Operation
       ↓
Save Changes to JSON
       ↓
Display Result
```

---

## Project Structure

```text
Patient-Management-System/
│
├── main.py
│   └── Application entry point and menu control
│
├── patient_management.py
│   └── Patient management operations
│
├── database.py
│   └── JSON data loading and saving
│
├── patients.json
│   └── Patient records
│
├── requirements.txt
│   └── Project dependencies
│
└── .gitignore
    └── Ignored files
```

---

## Technologies

* **Python 3** — Application development
* **JSON** — Patient data storage
* **Git** — Version control
* **GitHub** — Repository hosting

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/mariahabib-ai/Patient-Management-System.git
```

### 2. Navigate to the Project

```bash
cd Patient-Management-System
```

### 3. Run the Application

```bash
python main.py
```

The application will start in the terminal and display the patient management menu.

---

## Author

**Maria Habib**

BS Artificial Intelligence
University of Management and Technology

**AI Developer Bootcamp — Project**
