import tkinter as tk



class MainApplication(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("student managment system")
        self.geometry("900x600")
        self.create_widgets()


    def create_widgets(self):
        title_lable=tk.Label(self,text="student managment system",font=('Helvetica',16))
        title_lable.pack(side='top',fill='x')

        self.registration_form=registrationForm()




if __name__=="__main__":
    app=MainApplication()    #instance of the main application
    app.mainloop()