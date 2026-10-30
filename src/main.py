import customtkinter as ctk
from modules.chrono_view import ChronoView
from modules.chrono_controller import ChronoController
ctk.set_appearance_mode("System"); ctk.set_default_color_theme("blue")
class App(ctk.CTk):
    def __init__(self): 
        super().__init__(); self.title("Cronómetro Profesional")
        self.geometry("380x440"); self.resizable(False, False)
        self.controller = ChronoController(self, ChronoView(self, None))
        self.controller.view.controller = self.controller
if __name__ == "__main__": App().mainloop()