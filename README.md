# EHR Nexus

## Overview
EHR Nexus is an Electronic Health Record (EHR) platform designed to enable connected healthcare by providing a unified approach to managing and organizing healthcare information.

The platform focuses on improving collaboration between healthcare organizations by supporting structured health data management and creating a foundation for seamless healthcare workflows.

Currently, EHR Nexus is in the prototype development phase, with the first implemented module being Patient Management. This module provides the foundation for future expansion of the system.


---

## Current Implemented Module

### Patient Management Module

The current version of EHR Nexus provides a command-line-based patient management system that allows users to manage basic patient records.

The module focuses on creating, storing, retrieving, updating, and managing patient information using structured data handling.

---

## Current Features

- Add new patient records
- View patient records
- Search patient records
- Update patient information
- Delete patient records
- JSON-based patient data storage
- Data validation for required fields
- Modular code organization

---

## Technologies Used

- Python 3
- JSON for data storage
- Git & GitHub for version control

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/mariahabib-ai/EHR_Nexus.git
```

### 2. Navigate to project directory

```bash
cd EHR_Nexus
```

### 3. Run the application

```bash
python main.py
```

---

## Project Structure

```
EHR_Nexus/
│
├── main.py
│   └── Application entry point and menu control
│
├── patient_management.py
│   └── Patient record management operations
│
├── database.py
│   └── Data loading and saving functionality
│
├── requirements.txt
│   └── Project dependencies
│
├── .gitignore
│   └── Ignored files configuration

```

---

## Development Status

EHR Nexus is currently under active development.

The current prototype represents the first foundation of a larger healthcare software platform, with future development focused on expanding healthcare management capabilities.

---

## Author

Maria Habib