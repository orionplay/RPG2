import tkinter as tk
from tkinter import messagebox

class RPGSkillApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RPG Skill Manager")

        self.skills = []

        # Interface de usuário
        self.label_name = tk.Label(root, text="Skill Name:")
        self.label_name.grid(row=0, column=0, padx=10, pady=10)
        
        self.entry_name = tk.Entry(root)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        self.label_description = tk.Label(root, text="Skill Description:")
        self.label_description.grid(row=1, column=0, padx=10, pady=10)
        
        self.entry_description = tk.Entry(root)
        self.entry_description.grid(row=1, column=1, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Skill", command=self.add_skill)
        self.add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.skill_listbox = tk.Listbox(root)
        self.skill_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.view_button = tk.Button(root, text="View Skill", command=self.view_skill)
        self.view_button.grid(row=4, column=0, padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Delete Skill", command=self.delete_skill)
        self.delete_button.grid(row=4, column=1, padx=10, pady=10)

    def add_skill(self):
        name = self.entry_name.get()
        description = self.entry_description.get()

        if name and description:
            self.skills.append((name, description))
            self.skill_listbox.insert(tk.END, name)
            self.entry_name.delete(0, tk.END)
            self.entry_description.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter both name and description.")

    def view_skill(self):
        selected_index = self.skill_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            skill = self.skills[selected_index]
            messagebox.showinfo("Skill Details", f"Name: {skill[0]}\nDescription: {skill[1]}")
        else:
            messagebox.showwarning("Selection Error", "Please select a skill to view.")

    def delete_skill(self):
        selected_index = self.skill_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            self.skills.pop(selected_index)
            self.skill_listbox.delete(selected_index)
        else:
            messagebox.showwarning("Selection Error", "Please select a skill to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = RPGSkillApp(root)
    root.mainloop()
