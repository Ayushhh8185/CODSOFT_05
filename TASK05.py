import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f8ff")  # Light blue background

        self.contacts = {}

        # Title Label
        self.title_label = tk.Label(
            root, text="Contact Book", font=("Helvetica", 24, "bold"), bg="#f0f8ff", fg="#4682b4"
        )
        self.title_label.pack(pady=10)

        # Input Frame
        self.input_frame = tk.Frame(root, bg="#f0f8ff")
        self.input_frame.pack(pady=10)

        self.name_label = tk.Label(
            self.input_frame, text="Name:", font=("Helvetica", 12), bg="#f0f8ff", fg="#4682b4"
        )
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.input_frame, font=("Helvetica", 12), bg="#ffffff", fg="#000000")
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label = tk.Label(
            self.input_frame, text="Phone:", font=("Helvetica", 12), bg="#f0f8ff", fg="#4682b4"
        )
        self.phone_label.grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(self.input_frame, font=("Helvetica", 12), bg="#ffffff", fg="#000000")
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        # Button Frame
        self.button_frame = tk.Frame(root, bg="#f0f8ff")
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(
            self.button_frame, text="Add Contact", font=("Helvetica", 12, "bold"), bg="#4682b4", fg="#ffffff",
            command=self.add_contact
        )
        self.add_button.grid(row=0, column=0, padx=10)
        self.add_button.bind("<Enter>", lambda e: self.on_hover(self.add_button))
        self.add_button.bind("<Leave>", lambda e: self.on_leave(self.add_button))

        self.delete_button = tk.Button(
            self.button_frame, text="Delete Contact", font=("Helvetica", 12, "bold"), bg="#4682b4", fg="#ffffff",
            command=self.delete_contact
        )
        self.delete_button.grid(row=0, column=1, padx=10)
        self.delete_button.bind("<Enter>", lambda e: self.on_hover(self.delete_button))
        self.delete_button.bind("<Leave>", lambda e: self.on_leave(self.delete_button))

        self.search_button = tk.Button(
            self.button_frame, text="Search Contact", font=("Helvetica", 12, "bold"), bg="#4682b4", fg="#ffffff",
            command=self.search_contact
        )
        self.search_button.grid(row=0, column=2, padx=10)
        self.search_button.bind("<Enter>", lambda e: self.on_hover(self.search_button))
        self.search_button.bind("<Leave>", lambda e: self.on_leave(self.search_button))

        # Output Frame
        self.output_frame = tk.Frame(root, bg="#f0f8ff")
        self.output_frame.pack(pady=10)

        self.output_text = tk.Text(
            self.output_frame, font=("Helvetica", 12), bg="#ffffff", fg="#000000", height=10, width=50
        )
        self.output_text.pack(pady=10)

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        if name and phone:
            if name in self.contacts:
                messagebox.showwarning("Warning", "Contact already exists!")
            else:
                self.contacts[name] = phone
                messagebox.showinfo("Success", f"Contact {name} added successfully!")
                self.name_entry.delete(0, tk.END)
                self.phone_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill in both fields.")

    def delete_contact(self):
        name = self.name_entry.get().strip()
        if name:
            if name in self.contacts:
                del self.contacts[name]
                messagebox.showinfo("Success", f"Contact {name} deleted successfully!")
                self.name_entry.delete(0, tk.END)
                self.phone_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Contact not found.")
        else:
            messagebox.showerror("Error", "Please enter a name to delete.")

    def search_contact(self):
        name = self.name_entry.get().strip()
        if name:
            if name in self.contacts:
                phone = self.contacts[name]
                self.output_text.delete(1.0, tk.END)
                self.output_text.insert(tk.END, f"Name: {name}\nPhone: {phone}\n")
            else:
                self.output_text.delete(1.0, tk.END)
                self.output_text.insert(tk.END, "Contact not found.")
        else:
            messagebox.showerror("Error", "Please enter a name to search.")

    def on_hover(self, button):
        button.configure(bg="#87ceeb")  # Lighter blue on hover

    def on_leave(self, button):
        button.configure(bg="#4682b4")  # Original color

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
