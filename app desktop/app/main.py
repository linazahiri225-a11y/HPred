"""
Application Desktop de Prédiction des Prix Immobiliers
Interface graphique moderne avec Tkinter
ISTA NTIC SYBA - Formation IA - 2025/2026
"""



import tkinter as tk
from tkinter import ttk, messagebox
import sys, os
from turtle import left

from PIL import Image, ImageTk
import tkinter as tk

def load_icon(path, size=None):
    """Load an image icon with good quality resizing."""
    try:
        img = Image.open(path)
        
        if size:
            img = img.resize(size, Image.LANCZOS)  # haute qualité
        
        return ImageTk.PhotoImage(img)

    except (tk.TclError, OSError):
        return tk.PhotoImage()

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.predictor import RealEstatePredictor

# ─── Color Palette (LIGHT MODE) ───
BG_DARK       = "#f5f7fb"   # fond principal (clair)
BG_CARD       = "#ffffff"   # cartes blanches
BG_INPUT      = "#f1f3f9"   # champs input

ACCENT        = "#4f46e5"   # violet moderne
ACCENT_HOVER  = "#6366f1"
ACCENT_GLOW   = "#4338ca"

TEXT_PRIMARY   = "#111827"  # texte principal (noir doux)
TEXT_SECONDARY = "#6b7280"
TEXT_MUTED     = "#9ca3af"

SUCCESS        = "#10b981"
ERROR_CLR      = "#ef4444"

BORDER         = "#e5e7eb"  # bordures claires
GOLD           = "#f59e0b"


class ModernEntry(tk.Canvas):
    """Custom styled entry with floating label effect."""

    def __init__(self, parent, label_text, width=280, **kw):
        super().__init__(parent, width=width, height=52, bg=BG_CARD,
                         highlightthickness=0, **kw)
        self.label_text = label_text
        self.focused = False

        # Background rounded rect
        self._draw_bg(BORDER)

        # Entry widget
        self.entry = tk.Entry(self, font=("Segoe UI", 11), bg=BG_INPUT,
                              fg=TEXT_PRIMARY, insertbackground=TEXT_PRIMARY,
                              relief="flat", bd=0)
        self.create_window(width // 2, 30, window=self.entry, width=width - 24, height=24)

        # Label
        self.label_id = self.create_text(14, 10, text=label_text,
                                         font=("Segoe UI", 8), fill=TEXT_SECONDARY, anchor="w")

        self.entry.bind("<FocusIn>", self._on_focus_in)
        self.entry.bind("<FocusOut>", self._on_focus_out)

    def _draw_bg(self, color):
        self.delete("bg")
        w, h, r = self.winfo_reqwidth(), 52, 10
        self.create_rectangle(2, 2, w - 2, h - 2, outline=color, fill=BG_INPUT,
                              width=1.5, tags="bg")
        self.tag_lower("bg")

    def _on_focus_in(self, e):
        self._draw_bg(ACCENT)

    def _on_focus_out(self, e):
        self._draw_bg(BORDER)

    def get(self):
        return self.entry.get()

    def set_error(self):
        self._draw_bg(ERROR_CLR)

    def reset_style(self):
        self._draw_bg(BORDER)


class ModernToggle(tk.Frame):
    """Modern toggle switch with better UI."""

    def __init__(self, parent, label_text, **kw):
        super().__init__(parent, bg=BG_CARD, **kw)
        self.var = tk.BooleanVar(value=False)

        self.configure(cursor="hand2")

        # Label
        self.label = tk.Label(
            self, text=label_text,
            font=("Segoe UI", 10, "bold"),
            fg=TEXT_MUTED, bg=BG_CARD
        )
        self.label.pack(side="left", padx=(0, 12))

        # Canvas switch
        self.canvas = tk.Canvas(
            self, width=50, height=26,
            bg=BG_CARD, highlightthickness=0
        )
        self.canvas.pack(side="right")

        self._draw()

        # Bind click
        self.canvas.bind("<Button-1>", self._toggle)
        self.label.bind("<Button-1>", self._toggle)
        self.bind("<Button-1>", self._toggle)

    def _draw(self):
        self.canvas.delete("all")

        if self.var.get():
            bg_color = ACCENT
            circle_x = 26
            self.label.config(fg=TEXT_PRIMARY)
        else:
            bg_color = "#d1d5db"  # gris doux
            circle_x = 2
            self.label.config(fg=TEXT_MUTED)

        # Background (rounded style)
        self.canvas.create_oval(2, 2, 48, 26, fill=bg_color, outline=bg_color)

        # Circle (knob)
        self.canvas.create_oval(
            circle_x, 2, circle_x + 22, 24,
            fill="#e5e7eb", outline=""
        )

    def _toggle(self, event=None):
        self.var.set(not self.var.get())
        self._draw()

    def get(self):
        return 1 if self.var.get() else 0

class RealEstateApp:
    """Main application class."""

    def __init__(self):
        self.root = tk.Tk()
        # Charger les icônes
        base_path = os.path.join(os.path.dirname(__file__), "assets")
        
        self.icon_app = load_icon(os.path.join(base_path, "home.png"), (128, 128))
        self.root.iconphoto(True, self.icon_app)

        self.icon_section = load_icon(os.path.join(base_path, "section.png"), (20, 20))
        self.icon_info = load_icon(os.path.join(base_path, "info.png"), (20, 20))
        self.icon_model = load_icon(os.path.join(base_path, "model.png"), (16, 16))
        self.icon_file = load_icon(os.path.join(base_path, "file.png"), (16, 16))
        self.icon_school = load_icon(os.path.join(base_path, "school.png"), (16, 16))
        self.icon_predict = load_icon(os.path.join(base_path, "search.png"), (20, 20))
        self.icon_reset = load_icon(os.path.join(base_path, "reset.png"), (20, 20))
        self.icon_success = load_icon(os.path.join(base_path, "success.png"), (80, 80))
        self.icon_error = load_icon(os.path.join(base_path, "error.png"), (80, 80))
        self.icon_home = load_icon(os.path.join(base_path, "home.png"), (80, 80))
        self.icon_result= load_icon(os.path.join(base_path, "money.png"), (40, 40))
        self.icon_bigresult = load_icon(os.path.join(base_path, "money.png"), (80, 80))
        self.icon_options = load_icon(os.path.join(base_path, "option.png"), (20, 20))
        
        self.icons = [
    self.icon_section, self.icon_result, self.icon_info,
    self.icon_model, self.icon_file, self.icon_school,
    self.icon_predict, self.icon_reset
]
        self.root.title("HPred")
        self.root.configure(bg=BG_DARK)
        self.root.resizable(True, True)

        # Center window
        w, h = 980, 760
        x = (self.root.winfo_screenwidth() - w) // 2
        y = (self.root.winfo_screenheight() - h) // 2
        self.root.geometry(f"{w}x{h}+{x}+{y}")
        self.root.minsize(900, 700)

        # Load predictor
        try:
            self.predictor_fast = RealEstatePredictor(model_type="fast")
            self.predictor_accurate = RealEstatePredictor(model_type="accurate")
        except FileNotFoundError as e:
            messagebox.showerror("Erreur", str(e))
            sys.exit(1)

        self._build_ui()

    def _build_ui(self):
        """Build the complete UI."""
        # ─── Scrollable container ───
        main_canvas = tk.Canvas(self.root, bg=BG_DARK, highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=main_canvas.yview)
        self.scroll_frame = tk.Frame(main_canvas, bg=BG_DARK)

        self.scroll_frame.bind("<Configure>",
            lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all")))
        main_canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
        main_canvas.configure(yscrollcommand=scrollbar.set)

        # Mouse wheel scrolling
        def _on_mousewheel(e):
            main_canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")
        main_canvas.bind_all("<MouseWheel>", _on_mousewheel)

        scrollbar.pack(side="right", fill="y")
        main_canvas.pack(side="left", fill="both", expand=True)

        # Make scroll_frame expand to canvas width
        def _configure_width(e):
            main_canvas.itemconfig(main_canvas.find_all()[0], width=e.width)
        main_canvas.bind("<Configure>", _configure_width)

        container = self.scroll_frame

        # ─── Header ───
        header = tk.Frame(container, bg=BG_DARK)
        header.pack(fill="x", padx=30, pady=(25, 5))

        tk.Label(header, image=self.icon_home, bg=BG_DARK).pack(side="left", padx=(0, 12))
        title_frame = tk.Frame(header, bg=BG_DARK)
        title_frame.pack(side="left")
        tk.Label(title_frame, text="Bienvenue à HPred ",
                 font=("Segoe UI", 24, "bold"), fg=TEXT_PRIMARY,
                 bg=BG_DARK).pack(anchor="w")
        tk.Label(title_frame, text="Estimer le prix de votre bien immobilier  en quelques clics à l'aide d'un modèle ML",
                 font=("Segoe UI", 10), fg=TEXT_SECONDARY,
                 bg=BG_DARK).pack(anchor="w")

        # Accent line
        accent_line = tk.Frame(container, bg=ACCENT, height=2)
        accent_line.pack(fill="x", padx=30, pady=(10, 20))

        # ─── Main content area ───
        content = tk.Frame(container, bg=BG_DARK)
        content.pack(fill="both", expand=True, padx=30)

        # LEFT COLUMN - Input form
        left = tk.Frame(content, bg=BG_CARD, padx=25, pady=20)
        left.pack(side="left", fill="both", expand=True, padx=(0, 10))

        # Section title
        title_frame = tk.Frame(left, bg=BG_CARD)
        title_frame.pack(anchor="w", pady=(0, 15))

        tk.Label(title_frame, image=self.icon_section, bg=BG_CARD).pack(side="left", padx=(0, 8))

        tk.Label(title_frame, text="Caractéristiques du bien",
         font=("Segoe UI", 14, "bold"), fg=TEXT_PRIMARY,
         bg=BG_CARD).pack(side="left")
        # ── Numeric inputs ──
        nums_frame = tk.Frame(left, bg=BG_CARD)
        nums_frame.pack(fill="x")

        # Row 1
        row1 = tk.Frame(nums_frame, bg=BG_CARD)
        row1.pack(fill="x", pady=4)

        self.area_entry = ModernEntry(row1, "Surface (m²)", width=200)
        self.area_entry.pack(side="left", padx=(0, 10))
        self.bedrooms_entry = ModernEntry(row1, "Chambres", width=200)
        self.bedrooms_entry.pack(side="left", padx=(0, 10))

        # Row 2
        row2 = tk.Frame(nums_frame, bg=BG_CARD)
        row2.pack(fill="x", pady=4)

        self.bathrooms_entry = ModernEntry(row2, "Salles de bain", width=200)
        self.bathrooms_entry.pack(side="left", padx=(0, 10))
        self.stories_entry = ModernEntry(row2, "Étages", width=200)
        self.stories_entry.pack(side="left", padx=(0, 10))

        # Row 3
        row3 = tk.Frame(nums_frame, bg=BG_CARD)
        row3.pack(fill="x", pady=4)

        self.parking_entry = ModernEntry(row3, "Places de parking", width=200)
        self.parking_entry.pack(side="left", padx=(0, 10))

        # ── Furnishing status dropdown ──
        furn_frame = tk.Frame(left, bg=BG_CARD)
        furn_frame.pack(fill="x", pady=(10, 5))

        tk.Label(furn_frame, text="État d'ameublement",
                 font=("Segoe UI", 10), fg=TEXT_SECONDARY,
                 bg=BG_CARD).pack(anchor="w")

        self.furnishing_var = tk.StringVar(value="Non meublé")
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Custom.TCombobox",
                        fieldbackground=BG_INPUT, background=BG_INPUT,
                        foreground=TEXT_PRIMARY, borderwidth=1,
                        arrowcolor=ACCENT)
        style.map("Custom.TCombobox",
                  fieldbackground=[("readonly", BG_INPUT)],
                  foreground=[("readonly", TEXT_PRIMARY)])

        self.furnishing_combo = ttk.Combobox(
            furn_frame, textvariable=self.furnishing_var,
            values=["Non meublé", "Semi-meublé", "Meublé"],
            state="readonly", style="Custom.TCombobox",
            font=("Segoe UI", 11), width=25
        )
        self.furnishing_combo.pack(anchor="w", pady=(5, 0))

        # ── Toggle switches ──
        title_frame = tk.Frame(left, bg=BG_CARD)
        title_frame.pack(anchor="w", pady=(20, 10))

        tk.Label(title_frame, image=self.icon_options, bg=BG_CARD).pack(side="left", padx=(0, 8))

        tk.Label(title_frame, text="Options du bien",
         font=("Segoe UI", 13, "bold"),
         fg=TEXT_PRIMARY, bg=BG_CARD)\
            .pack(side="left")

        toggles_frame = tk.Frame(left, bg=BG_CARD)
        toggles_frame.pack(fill="x")

        # Two columns of toggles
        tcol1 = tk.Frame(toggles_frame, bg=BG_CARD)
        tcol1.pack(side="left", fill="x", expand=True)
        tcol2 = tk.Frame(toggles_frame, bg=BG_CARD)
        tcol2.pack(side="left", fill="x", expand=True)

        self.mainroad_toggle = ModernToggle(tcol1, "Route principale")
        self.mainroad_toggle.pack(anchor="w", pady=6)
        self.guestroom_toggle = ModernToggle(tcol1, "Chambre d'amis")
        self.guestroom_toggle.pack(anchor="w", pady=6)
        self.basement_toggle = ModernToggle(tcol1, "Sous-sol")
        self.basement_toggle.pack(anchor="w", pady=6)

        self.hotwater_toggle = ModernToggle(tcol2, "Chauffe-eau")
        self.hotwater_toggle.pack(anchor="w", pady=6)
        self.ac_toggle = ModernToggle(tcol2, "Climatisation")
        self.ac_toggle.pack(anchor="w", pady=6)
        self.prefarea_toggle = ModernToggle(tcol2, "Zone préférentielle")
        self.prefarea_toggle.pack(anchor="w", pady=6)

        # RIGHT COLUMN - Results
        right = tk.Frame(content, bg=BG_CARD, padx=25, pady=20)
        right.pack(side="left", fill="both", expand=True)

        title_frame = tk.Frame(right, bg=BG_CARD)
        title_frame.pack(anchor="w", pady=(0, 20))

        tk.Label(title_frame, image=self.icon_result, bg=BG_CARD).pack(side="left", padx=(0, 8))

        tk.Label(title_frame, text="Résultat de l'estimation",
         font=("Segoe UI", 14, "bold"), fg=TEXT_PRIMARY,
         bg=BG_CARD).pack(side="left")

        # Result display card
        self.result_frame = tk.Frame(right, bg="#f9fafb", padx=20, pady=30)
        self.result_frame.pack(fill="x", pady=(0, 20))

        self.result_icon = tk.Label(self.result_frame, image=self.icon_bigresult, bg="#f9fafb")
        self.result_icon.pack()

        info_frame = tk.Frame(right, bg=BG_CARD, padx=20, pady=20)
        info_frame.pack(fill="x", pady=(0, 20))

        self.result_label = tk.Label(
            self.result_frame, text="En attente...",
            font=("Segoe UI", 13), fg=TEXT_MUTED, bg="#f9fafb"
        )
        self.result_label.pack(pady=(10, 5))

        self.price_label = tk.Label(
            self.result_frame, text="— — —",
            font=("Segoe UI", 28, "bold"), fg=TEXT_MUTED, bg="#f9fafb"
        )
        self.price_label.pack(pady=(0, 5))

        self.detail_label = tk.Label(
            self.result_frame, text="",
            font=("Segoe UI", 9), fg=TEXT_SECONDARY, bg="#f9fafb",
            wraplength=280, justify="center"
        )
        self.detail_label.pack()

        # Info section
        title_frame = tk.Frame(info_frame, bg=BG_CARD)
        title_frame.pack(anchor="w", pady=(0, 8))

        tk.Label(title_frame, image=self.icon_info, bg=BG_CARD).pack(side="left", padx=(0, 8))

        tk.Label(title_frame, text="Informations",
         font=("Segoe UI", 10, "bold"),
         fg=TEXT_PRIMARY, bg=BG_CARD).pack(side="left")

        # ── Info dynamique PRO ──
        self.info_model_row = tk.Frame(info_frame, bg=BG_CARD)
        self.info_model_row.pack(fill="x", pady=2)

        tk.Label(self.info_model_row, image=self.icon_model, bg=BG_CARD).pack(side="left", padx=(0, 8))
        self.model_label = tk.Label(
            self.info_model_row,
            text="Modèle : —",
            font=("Segoe UI", 10, "bold"),
            fg=ACCENT,
            bg=BG_CARD
        )
        self.model_label.pack(side="left")


        self.info_file_row = tk.Frame(info_frame, bg=BG_CARD)
        self.info_file_row.pack(fill="x", pady=2)

        tk.Label(self.info_file_row, image=self.icon_file, bg=BG_CARD).pack(side="left", padx=(0, 8))
        self.file_label = tk.Label(
            self.info_file_row,
            text="Fichier : —",
            font=("Segoe UI", 9),
            fg=TEXT_SECONDARY,
            bg=BG_CARD
        )
        self.file_label.pack(side="left")


        # Ligne description modèles
        self.info_desc_row = tk.Frame(info_frame, bg=BG_CARD)
        self.info_desc_row.pack(fill="x", pady=4)

        self.desc_label = tk.Label(
            self.info_desc_row,
            text="⚡ Rapide / 🎯 Précis",
            font=("Segoe UI", 9),
            fg=TEXT_MUTED,
            bg=BG_CARD
        )
        self.desc_label.pack(anchor="w")


        # École / footer
        self.info_school_row = tk.Frame(info_frame, bg=BG_CARD)
        self.info_school_row.pack(fill="x", pady=(5, 0))

        tk.Label(self.info_school_row, image=self.icon_school, bg=BG_CARD).pack(side="left", padx=(0, 8))
        tk.Label(
            self.info_school_row,
            text="ISTA NTIC SYBA — Projet IA",
            font=("Segoe UI", 9),
            fg=TEXT_MUTED,
            bg=BG_CARD
        ).pack(side="left")

    
            

        # ─── Bottom buttons ───
        btn_frame = tk.Frame(container, bg=BG_DARK)
        btn_frame.pack(fill="x", padx=30, pady=25)

        # Predict button
        self.predict_btn = tk.Button(
            btn_frame,
            text="  Prédire le prix",
            image=self.icon_predict,
            compound="left",
            font=("Segoe UI", 13, "bold"),
            bg=ACCENT, fg="white",
            activebackground=ACCENT_HOVER,
            relief="flat", cursor="hand2",
            padx=20, pady=10,
            command=self._on_predict
        )
        self.predict_btn.pack(side="left", padx=(0, 10))

        # ── Model selection ──

        model_frame = tk.Frame(left, bg=BG_CARD)
        model_frame.pack(fill="x", pady=(15, 5))

        tk.Label(model_frame, text="Choisir le modèle",
         font=("Segoe UI", 12), fg=TEXT_SECONDARY,
         bg=BG_CARD).pack(anchor="w")

        self.model_var = tk.StringVar(value="Rapide")

        self.model_combo = ttk.Combobox(
            model_frame,
            textvariable=self.model_var,
            values=["Rapide", "Précis"],
            state="readonly",
            style="Custom.TCombobox",
            font=("Segoe UI", 11),
            width=25
        )

        self.model_combo.pack(anchor="w", pady=(5, 0))

        # Hover effect
        self.predict_btn.bind("<Enter>",
            lambda e: self.predict_btn.configure(bg=ACCENT_HOVER))
        self.predict_btn.bind("<Leave>",
            lambda e: self.predict_btn.configure(bg=ACCENT))

        # Reset button
        reset_btn = tk.Button(
    btn_frame,
    text="  Réinitialiser",
    image=self.icon_reset,
    compound="left",
    font=("Segoe UI", 11),
    bg=BG_CARD, fg=TEXT_SECONDARY,
    relief="flat", cursor="hand2",
    padx=15, pady=10,
    command=self._on_reset
)
        reset_btn.pack(side="left")
        reset_btn.bind("<Enter>",
            lambda e: reset_btn.configure(bg=BG_INPUT, fg=TEXT_PRIMARY))
        reset_btn.bind("<Leave>",
            lambda e: reset_btn.configure(bg=BG_CARD, fg=TEXT_SECONDARY))

        # Footer
        tk.Label(container,
                 text="© 2025 HPred - Formation IA - Promotion 2025/2026 ",
                 font=("Segoe UI", 8), fg=TEXT_MUTED,
                 bg=BG_DARK).pack(pady=(0, 15))

    def _get_numeric(self, entry, field_name):
        """Parse numeric value from entry, return (value, error)."""
        val = entry.get().strip()
        if not val:
            return None, f"Le champ '{field_name}' est requis."
        try:
            num = float(val)
            if num < 0:
                return None, f"'{field_name}' ne peut pas être négatif."
            return num, None
        except ValueError:
            return None, f"'{field_name}' doit être un nombre valide."

    def _on_predict(self):
        """Handle prediction button click."""
        # Reset styles
        entries = [self.area_entry, self.bedrooms_entry,
                   self.bathrooms_entry, self.stories_entry, self.parking_entry]
        for e in entries:
            e.reset_style()

        # Parse inputs
        errors = []
        fields = [
            (self.area_entry, "Surface"),
            (self.bedrooms_entry, "Chambres"),
            (self.bathrooms_entry, "Salles de bain"),
            (self.stories_entry, "Étages"),
            (self.parking_entry, "Parking"),
        ]

        values = []
        for entry, name in fields:
            val, err = self._get_numeric(entry, name)
            if err:
                errors.append(err)
                entry.set_error()
            values.append(val)

        if errors:
            self._show_error("\n".join(errors))
            return

        area, bedrooms, bathrooms, stories, parking = values

        # Validate ranges
        # Choix du modèle
        model_choice = self.model_var.get()

        if model_choice == "Rapide":
            predictor = self.predictor_fast
        else:
            predictor = self.predictor_accurate

        # Validation avec le bon modèle
        is_valid, err_msg = predictor.validate_inputs(
            area, bedrooms, bathrooms, stories, parking )

        if not is_valid:
            self._show_error(err_msg)
            return

        # Get toggle values
        mainroad = self.mainroad_toggle.get()
        guestroom = self.guestroom_toggle.get()
        basement = self.basement_toggle.get()
        hotwater = self.hotwater_toggle.get()
        ac = self.ac_toggle.get()
        prefarea = self.prefarea_toggle.get()

        # Furnishing status
        furn_map = {"Non meublé": 0, "Semi-meublé": 1, "Meublé": 2}
        furnishing = furn_map.get(self.furnishing_var.get(), 0)

        # Choix du modèle
        model_choice = self.model_var.get()

        if model_choice == "Rapide":
            predictor = self.predictor_fast
        else:
            predictor = self.predictor_accurate
        
        # Update info section
        model_choice = self.model_var.get()

        if model_choice == "Rapide":
            self.model_label.config(text="Modèle : Linear Regression ⚡")
            self.file_label.config(text="Fichier : linear_model.pkl")
            self.desc_label.config(text="Modèle rapide (faible latence)")
        else:
            self.model_label.config(text="Modèle : Gradient Boosting 🎯")
            self.file_label.config(text="Fichier : gradient_boosting_model.pkl")
            self.desc_label.config(text="Modèle précis (meilleure performance)") 

        # Predict
        try:
            price = predictor.predict(
                area, bedrooms, bathrooms, stories,
                mainroad, guestroom, basement, hotwater,
                ac, parking, prefarea, furnishing
            )
            self._show_result(price, area, bedrooms)
        except Exception as e:
            self._show_error(f"Erreur de prédiction :\n{str(e)}")

    def _show_result(self, price, area, bedrooms):
        """Display prediction result with animation."""
        self.result_frame.configure(bg="#ecfdf5")
        self.result_icon.configure(image=self.icon_success)
        self.result_label.configure(
            text="Prix estimé du bien",
            fg=SUCCESS, bg="#f9fafb"
        )

        formatted = f"{price:,.0f}".replace(",", " ")
        self.price_label.configure(
            text=f"{formatted} MAD",
            fg=SUCCESS, bg="#f9fafb"
        )

        price_per_m2 = price / area if area > 0 else 0
        self.detail_label.configure(
            text=f"Surface: {area:.0f} m²  •  {bedrooms:.0f} chambres\n"
                 f"Prix/m²: {price_per_m2:,.0f} MAD",
            bg="#f9fafb"
        )

    def _show_error(self, message):
        """Display error in result area."""
        self.result_frame.configure(bg="#fef2f2")
        self.result_icon.configure(image=self.icon_error)
        self.result_label.configure(
            text="Erreur de validation", fg=ERROR_CLR, bg="#f9fafb"
        )
        self.price_label.configure(
            text="Veuillez corriger", fg=ERROR_CLR, bg="#f9fafb"
        )
        self.detail_label.configure(text=message, bg="#f9fafb")

    def _on_reset(self):
        """Reset all fields."""
        for entry in [self.area_entry, self.bedrooms_entry,
                      self.bathrooms_entry, self.stories_entry,
                      self.parking_entry]:
            entry.entry.delete(0, tk.END)
            entry.reset_style()

        for toggle in [self.mainroad_toggle, self.guestroom_toggle,
                       self.basement_toggle, self.hotwater_toggle,
                       self.ac_toggle, self.prefarea_toggle]:
            toggle.var.set(False)
            toggle._draw()

        self.furnishing_var.set("Non meublé")

        self.result_frame.configure(bg="#f9fafb")
        self.result_icon.configure(image=self.icon_money)
        self.result_label.configure(text="En attente...", fg=TEXT_MUTED, bg="#f9fafb")
        self.price_label.configure(text="— — —", fg=TEXT_MUTED, bg="#f9fafb")
        self.detail_label.configure(text="", bg="#f9fafb")

    def run(self):
        """Start the application."""
        self.root.mainloop()


if __name__ == "__main__":
    app = RealEstateApp()
    app.run()
