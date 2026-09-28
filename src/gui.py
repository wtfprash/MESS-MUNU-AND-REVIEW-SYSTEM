import tkinter as tk
from tkinter import ttk, messagebox
from src.constants import DAYS, MEALS, CATERERS
from src.scraper import fetch_mess_menu
from src.storage import load_ratings, save_ratings

class VitMessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("VIT Bhopal Mess Menu & Rating System")
        self.root.geometry("600x680")
        self.root.resizable(False, False)

        self.menu_data = fetch_mess_menu()
        self.ratings_data = load_ratings()

        self.create_widgets()

    def create_widgets(self):
        header = tk.Label(
            self.root, 
            text="🍽️ VIT Bhopal Mess Menu App", 
            font=("Helvetica", 16, "bold"), 
            bg="#2c3e50", 
            fg="white", 
            pady=10
        )
        header.pack(fill="x")

        control_frame = ttk.LabelFrame(self.root, text=" Select Options ", padding=10)
        control_frame.pack(fill="x", padx=15, pady=10)

        ttk.Label(control_frame, text="Mess Caterer:").grid(row=0, column=0, sticky="w", pady=5)
        self.caterer_var = tk.StringVar(value=CATERERS[0])
        caterer_cb = ttk.Combobox(control_frame, textvariable=self.caterer_var, values=CATERERS, state="readonly", width=15)
        caterer_cb.grid(row=0, column=1, pady=5)
        caterer_cb.bind("<<ComboboxSelected>>", self.update_display)

        ttk.Label(control_frame, text="Day of Week:").grid(row=0, column=2, sticky="w", pady=5, padx=(15, 0))
        self.day_var = tk.StringVar(value=DAYS[0])
        day_cb = ttk.Combobox(control_frame, textvariable=self.day_var, values=DAYS, state="readonly", width=12)
        day_cb.grid(row=0, column=3, pady=5)
        day_cb.bind("<<ComboboxSelected>>", self.update_display)

        ttk.Label(control_frame, text="Meal Type:").grid(row=1, column=0, sticky="w", pady=5)
        self.meal_var = tk.StringVar(value=MEALS[0])
        meal_cb = ttk.Combobox(control_frame, textvariable=self.meal_var, values=MEALS, state="readonly", width=15)
        meal_cb.grid(row=1, column=1, pady=5)
        meal_cb.bind("<<ComboboxSelected>>", self.update_display)

        display_frame = ttk.LabelFrame(self.root, text=" Today's Menu ", padding=10)
        display_frame.pack(fill="both", expand=True, padx=15, pady=5)

        self.menu_listbox = tk.Listbox(display_frame, font=("Helvetica", 11), bg="#f8f9fa", selectbackground="#3498db")
        self.menu_listbox.pack(fill="both", expand=True)

        rating_frame = ttk.LabelFrame(self.root, text=" Rate & Review This Meal ", padding=10)
        rating_frame.pack(fill="x", padx=15, pady=10)

        ttk.Label(rating_frame, text="Rating (1-5 Stars):").grid(row=0, column=0, sticky="w", pady=5)
        self.rating_var = tk.IntVar(value=5)
        rating_spin = ttk.Spinbox(rating_frame, from_=1, to=5, textvariable=self.rating_var, width=5)
        rating_spin.grid(row=0, column=1, sticky="w", pady=5)

        ttk.Label(rating_frame, text="Review/Feedback:").grid(row=1, column=0, sticky="w", pady=5)
        self.review_entry = ttk.Entry(rating_frame, width=40)
        self.review_entry.grid(row=1, column=1, columnspan=2, pady=5, sticky="w")

        submit_btn = ttk.Button(rating_frame, text="Submit Rating", command=self.submit_rating)
        submit_btn.grid(row=2, column=1, pady=8, sticky="w")

        self.avg_rating_label = ttk.Label(rating_frame, text="Average Rating: N/A", font=("Helvetica", 10, "italic"))
        self.avg_rating_label.grid(row=2, column=2, pady=8, sticky="e")

        self.update_display()

    def update_display(self, event=None):
        caterer = self.caterer_var.get()
        day = self.day_var.get()
        meal = self.meal_var.get()

        self.menu_listbox.delete(0, tk.END)
        items = self.menu_data.get(day, {}).get(meal, ["No menu available."])
        for item in items:
            self.menu_listbox.insert(tk.END, f"• {item}")

        key = f"{caterer}_{day}_{meal}"
        if key in self.ratings_data and self.ratings_data[key]:
            ratings = [entry["rating"] for entry in self.ratings_data[key]]
            avg = sum(ratings) / len(ratings)
            count = len(ratings)
            self.avg_rating_label.config(text=f"Rating: {avg:.1f}/5⭐ ({count} reviews)")
        else:
            self.avg_rating_label.config(text="Rating: No reviews yet")

    def submit_rating(self):
        caterer = self.caterer_var.get()
        day = self.day_var.get()
        meal = self.meal_var.get()
        rating = self.rating_var.get()
        review = self.review_entry.get().strip()

        key = f"{caterer}_{day}_{meal}"
        if key not in self.ratings_data:
            self.ratings_data[key] = []

        self.ratings_data[key].append({"rating": rating, "review": review})
        save_ratings(self.ratings_data)

        messagebox.showinfo("Success", f"Rating saved for {caterer} - {day} {meal}!")
        self.review_entry.delete(0, tk.END)
        self.update_display()
