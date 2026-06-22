# Local Address Book Using Python and Tkinter

A locally operated desktop address book developed in Python using the Tkinter graphical user interface toolkit. The application allows users to add, view, search, edit, and delete contact records while storing the data in a local text file.

This project was developed as the **Object-Oriented Programming Final Requirement** of BSCpE 1-2 and was submitted on **July 19, 2023**.

## Project Overview

The application demonstrates introductory object-oriented programming, event-driven programming, graphical user interface development, input validation, and local file handling in Python.

Each contact stores the following information:

- First name
- Last name
- Address
- Contact number

The application runs entirely on the user's computer. It does not require an internet connection, web server, cloud service, or external database.

## Features

- Add new contacts
- Edit an existing contact using its entry number
- Delete an existing contact using its entry number
- View all saved contacts in a tabular interface
- Search contacts by:
  - First name
  - Last name
  - Address
  - Contact number
- Load saved contacts when the application starts
- Save contacts to a local file when the application is exited through its **Exit** button
- Display validation, error, and success messages through dialog boxes
- Limit the address book to a maximum of 100 contacts

## Input Validation

The application performs the following checks when adding or editing a contact:

- All fields must contain a value.
- First and last names must not contain numbers.
- Contact numbers may contain digits and a leading `+` symbol.
- Contact numbers must not exceed 13 characters, including the `+` symbol.
- Entry numbers used for editing or deleting must be valid integers within the current contact list.

## Technologies Used

- **Python 3**
- **Tkinter** for the graphical user interface
- **ttk.Treeview** for tabular contact and search-result displays
- **CSV module** for reading and writing local contact records
- **Object-oriented programming** through the `Contact` and `AddressBook` classes

The application only uses Python standard-library modules, so a `requirements.txt` file is not necessary.

## Object-Oriented Design

### `Contact`

Represents one address book record and stores:

- `first_name`
- `last_name`
- `address`
- `contact_number`

### `AddressBook`

Manages the application's:

- Contact collection
- File loading and saving
- Main window and secondary windows
- Add, edit, delete, view, and search operations
- User input validation
- Program lifecycle

## How the Application Works

1. The program creates an empty in-memory contact list.
2. It checks for a local `contacts.txt` file.
3. Existing records are loaded into `Contact` objects.
4. The Tkinter main window displays the available operations.
5. User changes are applied to the in-memory contact list.
6. Selecting the application's **Exit** button writes the current records to `contacts.txt`.
7. The saved records are loaded again the next time the program starts.

Although the file uses a `.txt` extension, its rows are written and read using CSV formatting.

## Repository Structure

```text
tkinter-address-book/
├── address_book.py
├── README.md
└── .gitignore
```

The application creates this local file after contacts are saved:

```text
contacts.txt
```

`contacts.txt` is intentionally excluded from Git because it may contain personal contact information.

## Getting Started

### Prerequisites

Install Python 3 on your computer.

You can confirm that Python is installed by running:

```bash
python --version
```

On some systems, the command may be:

```bash
python3 --version
```

Tkinter is normally included with standard Python installations on Windows and macOS. Some Linux distributions may require the separate `python3-tk` system package.

### Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/tkinter-address-book.git
cd tkinter-address-book
```

Replace `YOUR-USERNAME` with your GitHub username.

### Run the Application

Windows:

```bash
python address_book.py
```

macOS or Linux:

```bash
python3 address_book.py
```

The main Address Book window should open after the command is executed.

## Usage

### Add a Contact

1. Select **Add Contact**.
2. Enter the first name, last name, address, and contact number.
3. Select **Save Contact**.

### View Contacts

Select **View Contacts** to display the current contact records in a table.

### Edit a Contact

1. Determine the contact's position in the current contact list.
2. Select **Edit Contact**.
3. Enter the corresponding entry number.
4. Update the desired fields.
5. Select **Edit Contact** to apply the changes.

### Delete a Contact

1. Select **Delete Contact**.
2. Enter the contact's entry number.
3. Select **Delete**.

### Search the Address Book

1. Select **Search Address Book**.
2. Choose a field.
3. Enter the complete search value.
4. Select **Search**.

The current implementation uses exact and case-sensitive matching.

### Save and Exit

Use the application's **Exit** button to save the contacts before closing the program.

## Local Data Format

A saved row in `contacts.txt` follows this structure:

```text
first_name,last_name,address,contact_number
```

Example:

```text
Juan,Dela Cruz,Manila,+639123456789
```

The application does not add a header row.

## Privacy and Data Handling

All contact records are stored locally in `contacts.txt`. The application does not transmit the records over the internet.

Because the file can contain personally identifiable information:

- Do not commit `contacts.txt` to a public repository.
- Do not upload real contact records as sample data.
- Use fictional information when creating demonstrations or screenshots.

## Current Limitations

- Data is saved only when the application's **Exit** button is used.
- Closing the main window through the operating system's close control may not save the latest changes.
- Search uses exact, case-sensitive field matching.
- Editing and deletion rely on a numeric position in the contact list.
- The contact table does not currently display an entry-number column.
- Duplicate contacts are allowed.
- The contact limit is fixed at 100 records.
- Data is stored in a plain local text file without encryption.
- The interface is designed for local desktop use and is not optimized for multiple users.

## Possible Improvements

- Save records immediately after every add, edit, or delete operation.
- Handle the main window's close event so unsaved changes are preserved.
- Display entry numbers in the contacts table.
- Add partial and case-insensitive search.
- Add duplicate-contact detection.
- Sort contacts alphabetically.
- Replace the text file with SQLite.
- Add import and export support.
- Add automated tests.
- Package the application as a desktop executable.
- Improve keyboard navigation, resizing, and accessibility.

## Contributors

Developed by:

- Leslind G. Agahan
- Jasmine Daphne R. Baybayan
- Emman Ray S. Rodriguez
- Justine Marc C. Villanueva

**Program:** Bachelor of Science in Computer Engineering  
**Section:** BSCpE 1-2  
**Academic requirement:** Object-Oriented Programming Final Requirement  
**Date submitted:** July 19, 2023

## Academic Project Notice

This repository preserves an early college group project for educational and portfolio purposes. It demonstrates the programming concepts and implementation decisions used at the time of submission.

Before applying an open-source license, all project contributors should agree on the intended licensing terms.
