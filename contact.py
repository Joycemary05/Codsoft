import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

FILE_NAME = "contacts.json"

def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    with open(FILE_NAME, 'w') as f:
        json.dump(contacts, f, indent=4)

class ContactApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("650x500")
        self.root.configure(bg="#f6f0fa")

        self.contacts = load_contacts()

        title = tk.Label(root, text="📒 Contact Book", font=("Segoe UI", 24, "bold"), fg="#b347cc", bg="#f6f0fa")
        title.pack(pady=10)

        self.search_var = tk.StringVar()
        search_box = tk.Entry(root, textvariable=self.search_var, font=("Segoe UI", 12), width=30)
        search_box.pack()
        search_box.bind("<KeyRelease>", self.search_contact)

        frame = tk.Frame(root, bg="#f6f0fa")
        frame.pack(pady=10)

        tk.Label(frame, text="Name", bg="#f6f0fa").grid(row=0, column=0)
        tk.Label(frame, text="Phone", bg="#f6f0fa").grid(row=0, column=1)
        tk.Label(frame, text="Email", bg="#f6f0fa").grid(row=0, column=2)
        tk.Label(frame, text="Address", bg="#f6f0fa").grid(row=0, column=3)

        self.name_entry = tk.Entry(frame)
        self.name_entry.grid(row=1, column=0, padx=5)

        self.phone_entry = tk.Entry(frame)
        self.phone_entry.grid(row=1, column=1, padx=5)

        self.email_entry = tk.Entry(frame)
        self.email_entry.grid(row=1, column=2, padx=5)

        self.address_entry = tk.Entry(frame)
        self.address_entry.grid(row=1, column=3, padx=5)

        tk.Button(root, text="Add Contact", command=self.add_contact, bg="#c77dff", fg="white", font=("Segoe UI", 12)).pack(pady=5)

        self.contact_listbox = tk.Listbox(root, font=("Segoe UI", 12), width=80, height=10)
        self.contact_listbox.pack(pady=10)
        self.contact_listbox.bind("<<ListboxSelect>>", self.on_select)

        tk.Button(root, text="Update Contact", command=self.update_contact, bg="#ff66b2", fg="white", font=("Segoe UI", 11)).pack(side=tk.LEFT, padx=30)
        tk.Button(root, text="Delete Contact", command=self.delete_contact, bg="#ff4d6d", fg="white", font=("Segoe UI", 11)).pack(side=tk.LEFT)
        tk.Button(root, text="Refresh List", command=self.refresh_contacts, bg="#a64ac9", fg="white", font=("Segoe UI", 11)).pack(side=tk.RIGHT, padx=30)

        self.refresh_contacts()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if not name or not phone:
            messagebox.showwarning("Warning", "Name and Phone are required.")
            return

        self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        save_contacts(self.contacts)
        self.clear_entries()
        self.refresh_contacts()
        messagebox.showinfo("Success", "Contact added!")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def refresh_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            display = f"{contact['name']} | {contact['phone']} | {contact['email']} | {contact['address']}"
            self.contact_listbox.insert(tk.END, display)

    def search_contact(self, event=None):
        query = self.search_var.get().lower()
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            if query in contact['name'].lower() or query in contact['phone']:
                display = f"{contact['name']} | {contact['phone']} | {contact['email']} | {contact['address']}"
                self.contact_listbox.insert(tk.END, display)

    def on_select(self, event):
        if not self.contact_listbox.curselection():
            return
        index = self.contact_listbox.curselection()[0]
        contact_text = self.contact_listbox.get(index)
        contact_parts = contact_text.split(" | ")
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, contact_parts[0])
        self.phone_entry.delete(0, tk.END)
        self.phone_entry.insert(0, contact_parts[1])
        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, contact_parts[2])
        self.address_entry.delete(0, tk.END)
        self.address_entry.insert(0, contact_parts[3])

    def update_contact(self):
        selected = self.contact_listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a contact to update.")
            return
        index = selected[0]
        self.contacts[index] = {
            "name": self.name_entry.get(),
            "phone": self.phone_entry.get(),
            "email": self.email_entry.get(),
            "address": self.address_entry.get()
        }
        save_contacts(self.contacts)
        self.refresh_contacts()
        messagebox.showinfo("Success", "Contact updated!")

    def delete_contact(self):
        selected = self.contact_listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a contact to delete.")
            return
        index = selected[0]
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this contact?")
        if confirm:
            self.contacts.pop(index)
            save_contacts(self.contacts)
            self.refresh_contacts()
            messagebox.showinfo("Deleted", "Contact deleted.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()
