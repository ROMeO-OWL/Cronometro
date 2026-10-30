import customtkinter as ctk
class ChronoView(ctk.CTkFrame):
    def __init__(self, master, controller=None): super().__init__(master, fg_color="transparent"); self.controller = controller; self._build()
    def set_controller(self, controller): self.controller = controller; self.btn.configure(command=self.controller.toggle)
    def _build(self):
        self.pack(fill="both", expand=True, padx=20, pady=15)
        ctk.CTkLabel(self, text="CRONÓMETRO PRO", font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"), text_color="#38bdf8").pack(pady=(0, 5))
        card = ctk.CTkFrame(self, corner_radius=16, fg_color=("#1e293b", "#0f172a"), border_width=2, border_color="#38bdf8"); card.pack(fill="x", pady=5)
        self.lbl_time = ctk.CTkLabel(card, text="00:00:00", font=ctk.CTkFont(family="Consolas", size=36, weight="bold"), text_color="#f8fafc"); self.lbl_time.pack(pady=15)
        self.btn = ctk.CTkButton(self, text="INICIAR", command=self.controller.toggle if self.controller else None, font=ctk.CTkFont(family="Helvetica", size=14, weight="bold"), height=40, corner_radius=10, fg_color="#10b981", hover_color="#059669"); self.btn.pack(fill="x", pady=10)
        grid_frame = ctk.CTkFrame(self, fg_color="transparent"); grid_frame.pack(fill="x", pady=5); grid_frame.grid_columnconfigure((0, 1), weight=1)
        
        c_min = ctk.CTkFrame(grid_frame, corner_radius=10, fg_color=("#e0f2fe", "#1e293b")); c_min.grid(row=0, column=0, padx=3, pady=3, sticky="nsew")
        ctk.CTkLabel(c_min, text="MÁS CORTO", font=ctk.CTkFont(family="Helvetica", size=10, weight="bold"), text_color="#0284c7").pack(pady=(6, 0))
        self.lbl_min = ctk.CTkLabel(c_min, text="--:--", font=ctk.CTkFont(family="Consolas", size=14, weight="bold"), text_color="#38bdf8"); self.lbl_min.pack(pady=(0, 6))

        c_max = ctk.CTkFrame(grid_frame, corner_radius=10, fg_color=("#fee2e2", "#1e293b")); c_max.grid(row=0, column=1, padx=3, pady=3, sticky="nsew")
        ctk.CTkLabel(c_max, text="MÁS LARGO", font=ctk.CTkFont(family="Helvetica", size=10, weight="bold"), text_color="#dc2626").pack(pady=(6, 0))
        self.lbl_max = ctk.CTkLabel(c_max, text="--:--", font=ctk.CTkFont(family="Consolas", size=14, weight="bold"), text_color="#f87171"); self.lbl_max.pack(pady=(0, 6))

        c_avg = ctk.CTkFrame(grid_frame, corner_radius=10, fg_color=("#fef9c3", "#1e293b")); c_avg.grid(row=1, column=0, columnspan=2, padx=3, pady=3, sticky="nsew")
        ctk.CTkLabel(c_avg, text="PROMEDIO", font=ctk.CTkFont(family="Helvetica", size=10, weight="bold"), text_color="#ca8a04").pack(pady=(6, 0))
        self.lbl_avg = ctk.CTkLabel(c_avg, text="--:--", font=ctk.CTkFont(family="Consolas", size=14, weight="bold"), text_color="#facc15"); self.lbl_avg.pack(pady=(0, 6))

    def update_time(self, t): self.lbl_time.configure(text=t)
    def set_stop_state(self): self.btn.configure(text="DETENER / GUARDAR", fg_color="#ef4444", hover_color="#dc2626")
    def set_start_state(self, m, x, a): 
        self.lbl_time.configure(text="00:00:00")
        self.lbl_min.configure(text=m); self.lbl_max.configure(text=x); self.lbl_avg.configure(text=a)
        self.btn.configure(text="INICIAR", fg_color="#10b981", hover_color="#059669")