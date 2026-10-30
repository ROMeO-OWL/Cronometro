import customtkinter as ctk
class ChronoView(ctk.CTkFrame):
    def __init__(self, master, controller): super().__init__(master, fg_color="transparent"); self.controller = controller; self._build()
    def _build(self):
        self.pack(fill="both",
                  expand=True,
                  padx=20,
                  pady=20)
        ctk.CTkLabel(self,
                     text="CRONÓMETRO",
                     font=ctk.CTkFont(family="Helvetica",
                                      size=14, weight="bold")).pack(pady=(0, 10))
        card = ctk.CTkFrame(self, 
                            corner_radius=16, 
                            fg_color=("gray85", "gray17"))
        card.pack(fill="x", pady=10)
        self.lbl_time = ctk.CTkLabel(card, 
                                     text="00:00:00", 
                                     font=ctk.CTkFont(family="Consolas", size=40, weight="bold")); self.lbl_time.pack(pady=25)
        self.btn = ctk.CTkButton(self, 
                                 text="INICIAR", 
                                 command=self.controller.toggle, 
                                 font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"), height=45, corner_radius=10, fg_color="#2b825c", hover_color="#216648"); self.btn.pack(fill="x", pady=15)
        stats = ctk.CTkFrame(self, 
                             corner_radius=12, 
                             fg_color=("gray90", "gray13")); stats.pack(fill="x", pady=10)
        ctk.CTkLabel(stats, 
                     text="MEJOR TIEMPO / REGISTRO", 
                     font=ctk.CTkFont(family="Helvetica", size=11, weight="bold"), text_color="gray50").pack(pady=(10, 0))
        self.lbl_min = ctk.CTkLabel(stats, 
                                    text="--:--", 
                                    font=ctk.CTkFont(family="Consolas", size=20, weight="bold")); self.lbl_min.pack(pady=(2, 12))
    def update_time(self, t): self.lbl_time.configure(text=t)
    def set_stop_state(self): self.btn.configure(text="DETENER / GUARDAR", 
                                                 fg_color="#c93b3b", 
                                                 hover_color="#a32f2f")
    def set_start_state(self, m): self.lbl_time.configure(text="00:00:00"); self.lbl_min.configure(text=m); self.btn.configure(text="INICIAR", 
                                                                                                                               fg_color="#2b825c", 
                                                                                                                               hover_color="#216648")