import customtkinter
from PIL import Image


class TopLevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.my_image=customtkinter.CTkImage(light_image=Image.open("UDL.png"),dark_image=Image.open("UDL.png"),size=(100 , 50))
        self.label= customtkinter.CTkLabel(self, text="TopLevelWindow")
        self.label.pack(padx=20, pady=20)
        self.image_label=customtkinter.CTkLabel(self, image= self.my_image, text="")
        self.image_label.pack(padx= 20,pady=20)
        
        
class App(customtkinter.CTk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x400")
        self.button_1=customtkinter.CTkButton(self,text="open toplevel",command=self.open_toplevel)
        self.button_1.pack(side="top",padx=20,pady=20)
        
        self.toplevel_window - None
        
    
    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exist():
            self.toplevel_window= TopLevelWindow(self)
        else:
            self.toplevel_window.focus()
            

app = App()
app.mainloop()