import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os
from datetime import datetime

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo App")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Set theme colors
        self.bg_color = "#f0f0f0"
        self.header_color = "#4a6572"
        self.accent_color = "#344955"
        self.text_color = "#232f34"
        self.button_color = "#f9aa33"
        
        self.root.configure(bg=self.bg_color)
        
        # Initialize tasks
        self.tasks = []
        self.file_path = "tasks.json"
        self.load_tasks()
        
        # Create main frame
        self.main_frame = tk.Frame(self.root, bg=self.bg_color)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create header
        self.header_frame = tk.Frame(self.main_frame, bg=self.header_color)
        self.header_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.title_label = tk.Label(
            self.header_frame, 
            text="TODO APP", 
            font=("Arial", 24, "bold"), 
            bg=self.header_color, 
            fg="white"
        )
        self.title_label.pack(pady=10)
        
        # Create task input frame
        self.input_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.input_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Task title input
        self.title_label = tk.Label(
            self.input_frame, 
            text="Task Title:", 
            font=("Arial", 12), 
            bg=self.bg_color, 
            fg=self.text_color
        )
        self.title_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        self.title_entry = tk.Entry(self.input_frame, font=("Arial", 12), width=30)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        # Task description input
        self.desc_label = tk.Label(
            self.input_frame, 
            text="Description:", 
            font=("Arial", 12), 
            bg=self.bg_color, 
            fg=self.text_color
        )
        self.desc_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        
        self.desc_entry = tk.Entry(self.input_frame, font=("Arial", 12), width=30)
        self.desc_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        # Due date input
        self.due_label = tk.Label(
            self.input_frame, 
            text="Due Date (YYYY-MM-DD):", 
            font=("Arial", 12), 
            bg=self.bg_color, 
            fg=self.text_color
        )
        self.due_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        
        self.due_entry = tk.Entry(self.input_frame, font=("Arial", 12), width=30)
        self.due_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        
        # Priority input
        self.priority_label = tk.Label(
            self.input_frame, 
            text="Priority:", 
            font=("Arial", 12), 
            bg=self.bg_color, 
            fg=self.text_color
        )
        self.priority_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        
        self.priority_var = tk.StringVar(value="medium")
        self.priority_options = ["low", "medium", "high"]
        self.priority_menu = ttk.Combobox(
            self.input_frame, 
            textvariable=self.priority_var, 
            values=self.priority_options, 
            font=("Arial", 12), 
            width=28, 
            state="readonly"
        )
        self.priority_menu.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        
        # Add task button
        self.add_button = tk.Button(
            self.input_frame, 
            text="Add Task", 
            font=("Arial", 12, "bold"), 
            bg=self.button_color, 
            fg=self.text_color,
            command=self.add_task,
            padx=10,
            pady=5
        )
        self.add_button.grid(row=0, column=2, rowspan=2, padx=20, pady=5, sticky="ns")
        
        # Clear button
        self.clear_button = tk.Button(
            self.input_frame, 
            text="Clear", 
            font=("Arial", 12), 
            bg="#cccccc", 
            fg=self.text_color,
            command=self.clear_inputs,
            padx=10,
            pady=5
        )
        self.clear_button.grid(row=2, column=2, rowspan=2, padx=20, pady=5, sticky="ns")
        
        # Filter frame
        self.filter_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.filter_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.show_completed_var = tk.BooleanVar(value=True)
        self.show_completed_check = tk.Checkbutton(
            self.filter_frame, 
            text="Show Completed Tasks", 
            variable=self.show_completed_var, 
            font=("Arial", 12), 
            bg=self.bg_color, 
            fg=self.text_color,
            command=self.refresh_task_list
        )
        self.show_completed_check.pack(side=tk.LEFT, padx=5)
        
        # Filter by priority
        self.filter_priority_label = tk.Label(
            self.filter_frame, 
            text="Filter by Priority:", 
            font=("Arial", 12), 
            bg=self.bg_color, 
            fg=self.text_color
        )
        self.filter_priority_label.pack(side=tk.LEFT, padx=(20, 5))
        
        self.filter_priority_var = tk.StringVar(value="all")
        self.filter_priority_options = ["all", "low", "medium", "high"]
        self.filter_priority_menu = ttk.Combobox(
            self.filter_frame, 
            textvariable=self.filter_priority_var, 
            values=self.filter_priority_options, 
            font=("Arial", 12), 
            width=10, 
            state="readonly"
        )
        self.filter_priority_menu.pack(side=tk.LEFT, padx=5)
        self.filter_priority_menu.bind("<<ComboboxSelected>>", lambda e: self.refresh_task_list())
        
        # Create task list frame
        self.list_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.list_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create task list with scrollbar
        self.list_columns = ("id", "title", "priority", "due_date", "status")
        self.task_list = ttk.Treeview(
            self.list_frame, 
            columns=self.list_columns, 
            show="headings", 
            selectmode="browse"
        )
        
        # Define column headings
        self.task_list.heading("id", text="ID")
        self.task_list.heading("title", text="Title")
        self.task_list.heading("priority", text="Priority")
        self.task_list.heading("due_date", text="Due Date")
        self.task_list.heading("status", text="Status")
        
        # Define column widths
        self.task_list.column("id", width=50, anchor="center")
        self.task_list.column("title", width=300, anchor="w")
        self.task_list.column("priority", width=100, anchor="center")
        self.task_list.column("due_date", width=150, anchor="center")
        self.task_list.column("status", width=100, anchor="center")
        
        # Add scrollbar
        self.scrollbar = ttk.Scrollbar(self.list_frame, orient=tk.VERTICAL, command=self.task_list.yview)
        self.task_list.configure(yscrollcommand=self.scrollbar.set)
        
        # Pack list and scrollbar
        self.task_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Bind double-click event to view task details
        self.task_list.bind("<Double-1>", self.view_task_details)
        
        # Create buttons frame
        self.buttons_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.buttons_frame.pack(fill=tk.X, pady=(10, 0))
        
        # Action buttons
        self.complete_button = tk.Button(
            self.buttons_frame, 
            text="Mark as Completed", 
            font=("Arial", 12), 
            bg="#4caf50", 
            fg="white",
            command=self.mark_completed,
            padx=10,
            pady=5
        )
        self.complete_button.pack(side=tk.LEFT, padx=5)
        
        self.pending_button = tk.Button(
            self.buttons_frame, 
            text="Mark as Pending", 
            font=("Arial", 12), 
            bg="#2196f3", 
            fg="white",
            command=self.mark_pending,
            padx=10,
            pady=5
        )
        self.pending_button.pack(side=tk.LEFT, padx=5)
        
        self.edit_button = tk.Button(
            self.buttons_frame, 
            text="Edit Task", 
            font=("Arial", 12), 
            bg="#ff9800", 
            fg="white",
            command=self.edit_task,
            padx=10,
            pady=5
        )
        self.edit_button.pack(side=tk.LEFT, padx=5)
        
        self.delete_button = tk.Button(
            self.buttons_frame, 
            text="Delete Task", 
            font=("Arial", 12), 
            bg="#f44336", 
            fg="white",
            command=self.delete_task,
            padx=10,
            pady=5
        )
        self.delete_button.pack(side=tk.LEFT, padx=5)
        
        # Populate task list
        self.refresh_task_list()
    
    def load_tasks(self):
        """Load tasks from the JSON file if it exists."""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as file:
                    self.tasks = json.load(file)
            except json.JSONDecodeError:
                messagebox.showerror("Error", "Error loading tasks. Starting with an empty task list.")
                self.tasks = []
        else:
            self.tasks = []
    
    def save_tasks(self):
        """Save tasks to the JSON file."""
        with open(self.file_path, "w") as file:
            json.dump(self.tasks, file, indent=4)
    
    def add_task(self):
        """Add a new task to the list."""
        title = self.title_entry.get().strip()
        description = self.desc_entry.get().strip()
        due_date = self.due_entry.get().strip()
        priority = self.priority_var.get()
        
        if not title:
            messagebox.showerror("Error", "Task title cannot be empty!")
            return
        
        if not due_date:
            due_date = None
        
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "due_date": due_date,
            "priority": priority,
            "completed": False
        }
        
        self.tasks.append(task)
        self.save_tasks()
        self.clear_inputs()
        self.refresh_task_list()
        messagebox.showinfo("Success", f"Task '{title}' added successfully!")
    
    def clear_inputs(self):
        """Clear all input fields."""
        self.title_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.due_entry.delete(0, tk.END)
        self.priority_var.set("medium")
    
    def refresh_task_list(self):
        """Refresh the task list display."""
        # Clear existing items
        for item in self.task_list.get_children():
            self.task_list.delete(item)
        
        # Filter tasks
        filtered_tasks = self.tasks
        
        # Filter by completion status
        if not self.show_completed_var.get():
            filtered_tasks = [task for task in filtered_tasks if not task["completed"]]
        
        # Filter by priority
        priority_filter = self.filter_priority_var.get()
        if priority_filter != "all":
            filtered_tasks = [task for task in filtered_tasks if task["priority"] == priority_filter]
        
        # Add tasks to the list
        for task in filtered_tasks:
            status = "Completed" if task["completed"] else "Pending"
            due_date = task["due_date"] if task["due_date"] else "Not set"
            
            # Set row color based on priority
            tag = f"priority_{task['priority']}"
            
            self.task_list.insert(
                "", 
                tk.END, 
                values=(task["id"], task["title"], task["priority"], due_date, status),
                tags=(tag,)
            )
        
        # Configure row colors
        self.task_list.tag_configure("priority_high", background="#ffcccc")
        self.task_list.tag_configure("priority_medium", background="#ffffcc")
        self.task_list.tag_configure("priority_low", background="#ccffcc")
    
    def get_selected_task_id(self):
        """Get the ID of the selected task."""
        selection = self.task_list.selection()
        if not selection:
            messagebox.showerror("Error", "No task selected!")
            return None
        
        item = self.task_list.item(selection[0])
        task_id = int(item["values"][0])
        return task_id
    
    def get_task_by_id(self, task_id):
        """Get a task by its ID."""
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None
    
    def view_task_details(self, event=None):
        """View details of the selected task."""
        task_id = self.get_selected_task_id()
        if task_id is None:
            return
        
        task = self.get_task_by_id(task_id)
        if task:
            details = f"Task ID: {task['id']}\n\n"
            details += f"Title: {task['title']}\n\n"
            details += f"Description: {task['description']}\n\n"
            details += f"Created at: {task['created_at']}\n\n"
            details += f"Due date: {task['due_date'] if task['due_date'] else 'Not set'}\n\n"
            details += f"Priority: {task['priority']}\n\n"
            details += f"Status: {'Completed' if task['completed'] else 'Pending'}"
            
            messagebox.showinfo("Task Details", details)
    
    def mark_completed(self):
        """Mark the selected task as completed."""
        task_id = self.get_selected_task_id()
        if task_id is None:
            return
        
        task = self.get_task_by_id(task_id)
        if task:
            task["completed"] = True
            self.save_tasks()
            self.refresh_task_list()
            messagebox.showinfo("Success", f"Task {task_id} marked as completed!")
    
    def mark_pending(self):
        """Mark the selected task as pending."""
        task_id = self.get_selected_task_id()
        if task_id is None:
            return
        
        task = self.get_task_by_id(task_id)
        if task:
            task["completed"] = False
            self.save_tasks()
            self.refresh_task_list()
            messagebox.showinfo("Success", f"Task {task_id} marked as pending!")
    
    def edit_task(self):
        """Edit the selected task."""
        task_id = self.get_selected_task_id()
        if task_id is None:
            return
        
        task = self.get_task_by_id(task_id)
        if task:
            # Create a dialog for editing
            edit_window = tk.Toplevel(self.root)
            edit_window.title(f"Edit Task {task_id}")
            edit_window.geometry("400x300")
            edit_window.resizable(False, False)
            edit_window.configure(bg=self.bg_color)
            edit_window.transient(self.root)
            edit_window.grab_set()
            
            # Create form
            form_frame = tk.Frame(edit_window, bg=self.bg_color)
            form_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
            
            # Title
            tk.Label(
                form_frame, 
                text="Title:", 
                font=("Arial", 12), 
                bg=self.bg_color, 
                fg=self.text_color
            ).grid(row=0, column=0, padx=5, pady=5, sticky="w")
            
            title_var = tk.StringVar(value=task["title"])
            title_entry = tk.Entry(form_frame, textvariable=title_var, font=("Arial", 12), width=25)
            title_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
            
            # Description
            tk.Label(
                form_frame, 
                text="Description:", 
                font=("Arial", 12), 
                bg=self.bg_color, 
                fg=self.text_color
            ).grid(row=1, column=0, padx=5, pady=5, sticky="w")
            
            desc_var = tk.StringVar(value=task["description"])
            desc_entry = tk.Entry(form_frame, textvariable=desc_var, font=("Arial", 12), width=25)
            desc_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
            
            # Due date
            tk.Label(
                form_frame, 
                text="Due Date:", 
                font=("Arial", 12), 
                bg=self.bg_color, 
                fg=self.text_color
            ).grid(row=2, column=0, padx=5, pady=5, sticky="w")
            
            due_var = tk.StringVar(value=task["due_date"] if task["due_date"] else "")
            due_entry = tk.Entry(form_frame, textvariable=due_var, font=("Arial", 12), width=25)
            due_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
            
            # Priority
            tk.Label(
                form_frame, 
                text="Priority:", 
                font=("Arial", 12), 
                bg=self.bg_color, 
                fg=self.text_color
            ).grid(row=3, column=0, padx=5, pady=5, sticky="w")
            
            priority_var = tk.StringVar(value=task["priority"])
            priority_options = ["low", "medium", "high"]
            priority_menu = ttk.Combobox(
                form_frame, 
                textvariable=priority_var, 
                values=priority_options, 
                font=("Arial", 12), 
                width=23, 
                state="readonly"
            )
            priority_menu.grid(row=3, column=1, padx=5, pady=5, sticky="w")
            
            # Buttons
            buttons_frame = tk.Frame(form_frame, bg=self.bg_color)
            buttons_frame.grid(row=4, column=0, columnspan=2, pady=20)
            
            def save_changes():
                task["title"] = title_var.get().strip()
                task["description"] = desc_var.get().strip()
                task["due_date"] = due_var.get().strip() if due_var.get().strip() else None
                task["priority"] = priority_var.get()
                
                self.save_tasks()
                self.refresh_task_list()
                messagebox.showinfo("Success", f"Task {task_id} updated successfully!")
                edit_window.destroy()
            
            save_button = tk.Button(
                buttons_frame, 
                text="Save Changes", 
                font=("Arial", 12, "bold"), 
                bg=self.button_color, 
                fg=self.text_color,
                command=save_changes,
                padx=10,
                pady=5
            )
            save_button.pack(side=tk.LEFT, padx=5)
            
            cancel_button = tk.Button(
                buttons_frame, 
                text="Cancel", 
                font=("Arial", 12), 
                bg="#cccccc", 
                fg=self.text_color,
                command=edit_window.destroy,
                padx=10,
                pady=5
            )
            cancel_button.pack(side=tk.LEFT, padx=5)
    
    def delete_task(self):
        """Delete the selected task."""
        task_id = self.get_selected_task_id()
        if task_id is None:
            return
        
        confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete task {task_id}?")
        if confirm:
            task = self.get_task_by_id(task_id)
            if task:
                self.tasks.remove(task)
                # Reassign IDs to maintain sequence
                for i, task in enumerate(self.tasks):
                    task["id"] = i + 1
                self.save_tasks()
                self.refresh_task_list()
                messagebox.showinfo("Success", f"Task {task_id} deleted successfully!")

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
