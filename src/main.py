import customtkinter as ctk
from modules.chrono_view import ChronoView
from modules.chrono_controller import ChronoController
ctk.set_appearance_mode("Dark"); ctk.set_default_color_theme("blue")
class App(ctk.CTk):
    def __init__(self): 
        super().__init__(); self.title("Cronómetro Pro"); self.geometry("400+480"); self.resizable(False, False)
        self.view = ChronoView(self)
        self.controller = ChronoController(self, self.view)
        self.view.set_controller(self.controller)
if __name__ == "__main__": App().mainloop()