import tkinter as tk
from database_handler import DatabaseHandler
class registrationForm(tk.Frame):
    
    def __init__(self,parent): 
        super().__init__(parent,padx=10,pady=10)

        tk.Label(self,text="full name").pack()
        self.name_entry=tk.Entry(self)
        self.name_entry.pack(fill='x')


        tk.Label(self,text="Email").pack()
        self.email_entry=tk.Entry(self)
        self.email_entry.pack(fill='x')

        tk.Label(self,text="Age").pack()
        self.age_var = tk.StringVar()
        self.age_spinbox=tk.Spinbox(self,from_=10,to=100,textvariable=self.age_var)
        self.age_spinbox.pack(fill='x')


        tk.Label(self,text="gender").pack(fill='x')
        self.gender_var=tk.StringVar()
        tk.Radiobutton(self,text="Male",variable=self.gender_var,value="Male").pack(anchor='w')
        tk.Radiobutton(self,text="Female",variable=self.gender_var,value="Female").pack(anchor='w')

        
        self.submit_button=tk.Button(self,text="submit",command=self.submit_form)
        self.submit_button.pack(fill='x')

    def submit_form(self):
        name=self.name_entry.get()
        email=self.email_entry.get()
        age=self.age_var.get()
        gender=self.gender_var.get()
        
        if name and email and age and gender:
            DatabaseHandler.insert_student(name,email,age,gender)

            self.reset_form()
    
    def reset_form(self):
        self.name_entry.delete(0,'end')
        self.email_entry.delete(0,'end')
        self.age_var.set("10")
        self.gender_var.set(None)






