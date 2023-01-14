import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class ToDoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List")
        self.geometry("400x500")

        self.tasks = []
        self.task_var = tk.StringVar()
        self.priority_var = tk.StringVar()
        self.due_date_var = tk.StringVar()
      
        # Create widgets for entering task
        self.task_label = tk.Label(self, text="Task")
        self.task_label.grid(row=0, column=0, padx=5, pady=5)
        self.task_entry = tk.Entry(self, textvariable=self.task_var)
        self.task_entry.grid(row=0, column=1, padx=5, pady=5)

        # Create widgets for entering priority
        self.priority_label = tk.Label(self, text="Priority (1-3)")
        self.priority_label.grid(row=1, column=0, padx=5, pady=5)
        self.priority_entry = tk.Entry(self, textvariable=self.priority_var)
        self.priority_entry.grid(row=1, column=1, padx=5, pady=5)

        # Create widgets for entering due date
        self.due_date_label = tk.Label(self, text="Due date (dd-mm-yy)")
        self.due_date_label.grid(row=2, column=0, padx=5, pady=5)
        self.due_date_entry = tk.Entry(self, textvariable=self.due_date_var)
        self.due_date_entry.grid(row=2, column=1, padx=5, pady=5)

        self.add_task_button = tk.Button(self, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self.task_entry.bind('<Return>', self.add_task)
        
        self.task_list = tk.Listbox(self)
        self.task_list.grid(row=4, column=0, columnspan=2, padx=5, pady=5, ipadx=200, ipady=200)

        self.remove_task_button = tk.Button(self, text="Remove Task", command=self.remove_task)
        self.remove_task_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def add_task(self):
        task = self.task_input.text()
        self.tasks[task] = False
        self.task_list.addItem(task)
        self.task_input.setText("")

    def delete_task(self):
        selected = self.task_list.selectedItems()
        for item in selected:
            task = item.text()
            self.tasks.pop(task)
            self.task_list.takeItem(self.task_list.row(item))

    def toggle_completion(self, item):
        task = item.text()
        self.tasks[task] = not self.tasks[task]
        if self.tasks[task]:
            item.setForeground(QtGui.QColor('green'))
        else:
            item.setForeground(QtGui.QColor('black'))

if __name__ == "__main__":
    app = ToDoApp()
    app.mainloop()
