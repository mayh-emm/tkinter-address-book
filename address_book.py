# Program Title: Object-Oriented Programming Final Requirement
# Programmed by: Agahan, Leslind G.
#                Baybayan, Jasmine Daphne R.
#                Rodriguez, Emman Ray S.
#                Villanueva, Justine Marc C.
# BSCpE 1-2
# Date Submitted: July 19, 2023

import tkinter as tk
from tkinter import messagebox, ttk
import csv


class Contact:
    def __init__(self, first_name, last_name, address, contact_number):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.contact_number = contact_number


class AddressBook:
    def __init__(self):
        self.contacts = []
        self.load_contacts()
        self.window = tk.Tk()
        self.window.title("Address Book")
        self.window.geometry("600x400")
        self.window.configure(bg="#F8EAD8")
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.window, bg="#F8EAD8")
        frame.pack(expand=True)

        tk.Label(frame, text="ADDRESS BOOK", font=("Century Gothic", 16, "bold"), bg="#F8EAD8").grid(row=0, column=0,
                                                                                                     columnspan=3)
        tk.Label(frame, text="What would you like to do?", font=("Century Gothic", 12, "italic"), bg="#F8EAD8").grid(row=1, column=0, columnspan=3)
        tk.Button(frame, text="Add Contact", command=self.add_contact, font=("Century Gothic", 12), bg="#FFC3A1",
                  height=2, width=20).grid(row=2, column=0, pady=5)
        tk.Button(frame, text="Edit Contact", command=self.edit_contact, font=("Century Gothic", 12), bg="#FFC3A1",
                  height=2, width=20).grid(row=2, column=2, padx=10, pady=5)
        tk.Button(frame, text="Delete Contact", command=self.delete_contact, font=("Century Gothic", 12), bg="#FFC3A1",
                  height=2, width=20).grid(row=3, column=0, pady=5)
        tk.Button(frame, text="View Contacts", command=self.view_contacts, font=("Century Gothic", 12), bg="#FFC3A1",
                  height=2, width=20).grid(row=3, column=2, padx=10, pady=5)
        tk.Button(frame, text="Search Address Book", command=self.search_address_book, font=("Century Gothic", 12),
                  bg="#FFC3A1", height=2, width=20).grid(row=5, column=0, pady=5)
        tk.Button(frame, text="Exit", command=self.exit, font=("Century Gothic", 12), bg="#FFC3A1", height=2,
                  width=20).grid(row=5, column=2, padx=10, pady=5)

    def load_contacts(self):
        try:
            with open("contacts.txt", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    try:
                        first_name, last_name, address, contact_number = row
                        contact = Contact(first_name, last_name, address, contact_number)
                        self.contacts.append(contact)
                    except ValueError:
                        pass
        except FileNotFoundError:
            pass

    def save_contacts(self):
        with open("contacts.txt", "w") as f:
            writer = csv.writer(f)
            for contact in self.contacts:
                writer.writerow([contact.first_name, contact.last_name, contact.address, contact.contact_number])

    def back(self, window, other):
        window.destroy()
        other.deiconify()

    def add_contact(self):
        self.window.withdraw()
        if len(self.contacts) >= 100:
            messagebox.showerror("Error", "Address book is full.", font=("Century Gothic", 12))
            return

        add_window = tk.Toplevel(self.window)
        add_window.title("Add Contact")
        add_window.geometry("300x300")
        add_window.configure(bg="#F8EAD8")

        first_name_label = tk.Label(add_window, text="First Name:", font=("Century Gothic", 12), bg="#F8EAD8")
        first_name_entry = tk.Entry(add_window, font=("Century Gothic", 12))
        last_name_label = tk.Label(add_window, text="Last Name:", font=("Century Gothic", 12), bg="#F8EAD8")
        last_name_entry = tk.Entry(add_window, font=("Century Gothic", 12))
        address_label = tk.Label(add_window, text="Address:", font=("Century Gothic", 12), bg="#F8EAD8")
        address_entry = tk.Entry(add_window, font=("Century Gothic", 12))
        contact_number_label = tk.Label(add_window, text="Contact Number:", font=("Century Gothic", 12), bg="#F8EAD8")
        contact_number_entry = tk.Entry(add_window, font=("Century Gothic", 12))

        first_name_label.pack()
        first_name_entry.pack()
        last_name_label.pack()
        last_name_entry.pack()
        address_label.pack()
        address_entry.pack()
        contact_number_label.pack()
        contact_number_entry.pack()

        def save_contact():
            first_name = first_name_entry.get().strip()
            last_name = last_name_entry.get().strip()
            address = address_entry.get().strip()
            contact_number = contact_number_entry.get().strip()

            if not first_name or not last_name or not address or not contact_number:
                messagebox.showerror("Error", "All fields are required.")
                add_window.grab_set()
                return

            if not all(char.isdigit() or char == '+' for char in contact_number):
                messagebox.showerror("Error", "Contact number must contain only digits and the '+' symbol.")
                return

            if any(char.isdigit() for char in first_name):
                messagebox.showerror("Error", "Name must not contain numbers.")
                add_window.grab_set()
                return

            if any(char.isdigit() for char in last_name):
                messagebox.showerror("Error", "Name must not contain numbers.")
                add_window.grab_set()
                return

            if len(contact_number) > 13:
                messagebox.showerror("Error", "Maximum length of contact number should be 13 digits only including the '+' symbol.")
                return

            try:
                int(contact_number)
            except ValueError:
                messagebox.showerror("Error", "Contact number must be a valid integer.")
                add_window.grab_set()
                return

            contact = Contact(first_name, last_name, address, contact_number)
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully.")
            add_window.destroy()
            self.window.deiconify()

        save_button = tk.Button(add_window, text="Save Contact", command=save_contact, font=("Century Gothic", 12), bg="#FFC3A1")
        save_button.pack(anchor="center")

        back_button = tk.Button(add_window, text="Back", command=lambda: self.back(add_window, self.window), font=("Century Gothic", 12), bg="#BA704F")
        back_button.pack(anchor="center")

    def edit_contact(self):
        if not self.contacts:
            messagebox.showerror("Error", "Address book is empty.")
            return

        self.window.withdraw()
        edit_window = tk.Toplevel(self.window)
        edit_window.title("Edit Contact")
        edit_window.geometry("300x150")
        edit_window.configure(bg="#F8EAD8")

        entry_number_label = tk.Label(edit_window, text="Entry Number:", font=("Century Gothic", 12), bg="#F8EAD8")
        entry_number_entry = tk.Entry(edit_window, font=("Century Gothic", 12))

        entry_number_label.pack()
        entry_number_entry.pack()

        def edit():
            entry_number = entry_number_entry.get().strip()

            if not entry_number:
                messagebox.showerror("Error", "Entry number is required.")
                edit_window.grab_set()
                return

            try:
                entry_number = int(entry_number)
            except ValueError:
                messagebox.showerror("Error", "Entry number must be a valid integer.")
                edit_window.grab_set()
                return

            if entry_number < 1 or entry_number > len(self.contacts):
                messagebox.showerror("Error", "Invalid entry number.")
                edit_window.grab_set()
                return

            contact = self.contacts[entry_number - 1]

            edit_contact_window = tk.Toplevel(edit_window)
            edit_contact_window.title("Edit Contact")
            edit_contact_window.geometry("300x350")
            edit_contact_window.configure(bg="#F8EAD8")

            first_name_label = tk.Label(edit_contact_window, text="First Name:", font=("Century Gothic", 12), bg="#F8EAD8")
            first_name_entry = tk.Entry(edit_contact_window, font=("Century Gothic", 12))
            first_name_entry.insert(0, contact.first_name)
            last_name_label = tk.Label(edit_contact_window, text="Last Name:", font=("Century Gothic", 12), bg="#F8EAD8")
            last_name_entry = tk.Entry(edit_contact_window, font=("Century Gothic", 12))
            last_name_entry.insert(0, contact.last_name)
            address_label = tk.Label(edit_contact_window, text="Address:", font=("Century Gothic", 12), bg="#F8EAD8")
            address_entry = tk.Entry(edit_contact_window, font=("Century Gothic", 12))
            address_entry.insert(0, contact.address)
            contact_number_label = tk.Label(edit_contact_window, text="Contact Number:", font=("Century Gothic", 12),
                                            bg="#F8EAD8")
            contact_number_entry = tk.Entry(edit_contact_window, font=("Century Gothic", 12))
            contact_number_entry.insert(0, contact.contact_number)

            first_name_label.pack()
            first_name_entry.pack()
            last_name_label.pack()
            last_name_entry.pack()
            address_label.pack()
            address_entry.pack()
            contact_number_label.pack()
            contact_number_entry.pack()

            edit_window.withdraw()

            def save_contact():
                first_name = first_name_entry.get().strip()
                last_name = last_name_entry.get().strip()
                address = address_entry.get().strip()
                contact_number = contact_number_entry.get().strip()

                if not first_name or not last_name or not address or not contact_number:
                    messagebox.showerror("Error", "All fields are required.")
                    edit_window.grab_set()
                    return

                if not all(char.isdigit() or char == '+' for char in contact_number):
                    messagebox.showerror("Error", "Contact number must contain only digits and the '+' symbol.")
                    return

                if any(char.isdigit() for char in first_name):
                    messagebox.showerror("Error", "Name must not contain numbers.")
                    edit_window.grab_set()
                    return

                if any(char.isdigit() for char in last_name):
                    messagebox.showerror("Error", "Name must not contain numbers.")
                    edit_window.grab_set()
                    return

                if len(contact_number) > 13:
                    messagebox.showerror("Error", "Maximum length of contact number should be 13 digits only including the ' +' symbol.")
                    return

                try:
                    int(contact_number)
                except ValueError:
                    messagebox.showerror("Error", "Contact number must be a valid integer.")
                    edit_window.grab_set()
                    return

                contact.first_name = first_name
                contact.last_name = last_name
                contact.address = address
                contact.contact_number = contact_number
                messagebox.showinfo("Success", "Contact edited successfully.")
                edit_window.destroy()
                self.window.deiconify()

            save_button = tk.Button(edit_contact_window, text="Edit Contact", command=save_contact, font=("Century Gothic", 12),
                                    bg="#FFC3A1")
            save_button.pack(anchor="center")

            back_button = tk.Button(edit_contact_window, text="Back", command=lambda: self.back(edit_contact_window, edit_window),
                                    font=("Century Gothic", 12), bg="#BA704F")
            back_button.pack(anchor="center")

        edit_button = tk.Button(edit_window, text="Submit", command=edit, font=("Century Gothic", 12), bg="#FFC3A1")
        edit_button.pack(anchor="center")

        back_button = tk.Button(edit_window, text="Back", command=lambda: self.back(edit_window, self.window), font=("Century Gothic", 12), bg="#BA704F")
        back_button.pack(anchor="center")

    def delete_contact(self):
        if not self.contacts:
            messagebox.showerror("Error", "Address book is empty.")
            return

        self.window.withdraw()
        delete_window = tk.Toplevel(self.window)
        delete_window.title("Delete Contact")
        delete_window.geometry("300x150")
        delete_window.configure(bg="#F8EAD8")

        entry_number_label = tk.Label(delete_window, text="Entry Number:", font=("Century Gothic", 12), bg="#F8EAD8")
        entry_number_entry = tk.Entry(delete_window, font=("Century Gothic", 12))

        entry_number_label.pack()
        entry_number_entry.pack()

        def delete():
            entry_number = entry_number_entry.get().strip()

            if not entry_number:
                messagebox.showerror("Error", "Entry number is required.")
                delete_window.grab_set()
                return

            try:
                entry_number = int(entry_number)
            except ValueError:
                messagebox.showerror("Error", "Entry number must be a valid integer.")
                delete_window.grab_set()
                return

            if entry_number < 1 or entry_number > len(self.contacts):
                messagebox.showerror("Error", "Invalid entry number.")
                delete_window.grab_set()
                return

            delete_window.destroy()
            del self.contacts[entry_number - 1]
            messagebox.showinfo("Success", "Contact deleted successfully.")
            delete_window.destroy()
            self.window.deiconify()

        delete_button = tk.Button(delete_window, text="Delete", command=delete, font=("Century Gothic", 12), bg="#FFC3A1")
        delete_button.pack(anchor="center")

        back_button = tk.Button(delete_window, text="Back", command=lambda: self.back(delete_window, self.window), font=("Century Gothic", 12), bg="#BA704F")
        back_button.pack(anchor="center")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showerror("Error", "Address book is empty.")
            return

        view_window = tk.Toplevel(self.window)
        view_window.title("View Contacts")
        view_window.geometry("800x200")
        view_window.configure(bg="#F8EAD8")

        style = ttk.Style()
        style.configure("Custom.Treeview", background="#F8EAD8", font=("Century Gothic", 12))
        style.configure("Custom.Treeview.Heading", fieldbackground="#FFC3A1", font=("Century Gothic", 12, "bold"))

        tree = ttk.Treeview(view_window, columns=("First Name", "Last Name", "Address", "Contact Number"),
                            show="headings", style="Custom.Treeview")
        tree.heading("First Name", text="First Name")
        tree.heading("Last Name", text="Last Name")
        tree.heading("Address", text="Address")
        tree.heading("Contact Number", text="Contact Number")

        for contact in self.contacts:
            tree.insert("", "end",
                        values=(contact.first_name, contact.last_name, contact.address, contact.contact_number))

        tree.pack()
        self.window.deiconify()

    def search_address_book(self):
        if not self.contacts:
            messagebox.showerror("Error", "Address book is empty.")
            return

        self.window.withdraw()
        search_window = tk.Toplevel(self.window)
        search_window.title("Search Address Book")
        search_window.geometry("300x350")
        search_window.configure(bg="#F8EAD8")

        search_by_label = tk.Label(search_window, text="Search by:", font=("Century Gothic", 12), bg="#F8EAD8")
        search_by_var = tk.StringVar(value="first_name")
        search_by_first_name_rb = tk.Radiobutton(search_window, text="First Name", variable=search_by_var,
                                                 value="first_name", font=("Century Gothic", 12), bg="#F8EAD8")
        search_by_last_name_rb = tk.Radiobutton(search_window, text="Last Name", variable=search_by_var,
                                                value="last_name", font=("Century Gothic", 12), bg="#F8EAD8")
        search_by_address_rb = tk.Radiobutton(search_window, text="Address", variable=search_by_var, value="address",
                                              font=("Century Gothic", 12), bg="#F8EAD8")
        search_by_contact_number_rb = tk.Radiobutton(search_window, text="Contact Number", variable=search_by_var,
                                                     value="contact_number", font=("Century Gothic", 12), bg="#F8EAD8")
        query_label = tk.Label(search_window, text="Query:", font=("Century Gothic", 12), bg="#F8EAD8")
        query_entry = tk.Entry(search_window, font=("Century Gothic", 12))

        search_by_label.pack()
        search_by_first_name_rb.pack()
        search_by_last_name_rb.pack()
        search_by_address_rb.pack()
        search_by_contact_number_rb.pack()
        query_label.pack(pady=10)
        query_entry.pack(pady=10)

        def search():
            search_by = search_by_var.get()
            query = query_entry.get().strip()

            if not query:
                messagebox.showerror("Error", "Query is required.")
                search_window.grab_set()
                return

            results = []

            for contact in self.contacts:
                if getattr(contact, search_by) == query:
                    results.append(contact)

            if not results:
                messagebox.showinfo("No Results", "No results found.")
                return

            search_window.withdraw()
            results_window = tk.Toplevel(search_window)
            results_window.title("Search Results")
            results_window.geometry("800x200")
            results_window.configure(bg="#F8EAD8")

            style = ttk.Style()
            style.configure("Custom.Treeview", background="#F8EAD8", font=("Century Gothic", 12))
            style.configure("Custom.Treeview.Heading", fieldbackground="#FFC3A1", font=("Century Gothic", 12, "bold"))

            tree = ttk.Treeview(results_window, columns=("First Name", "Last Name", "Address", "Contact Number"),
                                show="headings", style="Custom.Treeview")
            tree.heading("First Name", text="First Name")
            tree.heading("Last Name", text="Last Name")
            tree.heading("Address", text="Address")
            tree.heading("Contact Number", text="Contact Number")

            for contact in results:
                tree.insert("", "end",
                            values=(contact.first_name, contact.last_name, contact.address, contact.contact_number))

            tree.pack()

            self.window.deiconify()

        search_button = tk.Button(search_window, text="Search", command=search, font=("Century Gothic", 12), bg="#FFC3A1")
        search_button.pack()

        back_button = tk.Button(search_window, text="Back", command=lambda: self.back(search_window, self.window), font=("Century Gothic", 12), bg="#BA704F")
        back_button.pack(anchor="center")

    def exit(self):
        self.save_contacts()
        self.window.destroy()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    address_book = AddressBook()
    address_book.run()
