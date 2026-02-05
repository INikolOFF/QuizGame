import customtkinter as ctk
from tkinter import messagebox
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class QuizGame:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Ultimate Quiz Game")
        self.window.geometry("700x750")
        self.window.resizable(False, False)
        self.window.configure(fg_color="#0a0a15")

        self.categories = {
            "General Knowledge": [
                ("What is the capital of France?", ["Paris", "London", "Berlin", "Madrid"], "Paris"),
                ("How many legs does a spider have?", ["6", "8", "10", "12"], "8"),
                ("What is the largest ocean on Earth?", ["Atlantic", "Indian", "Arctic", "Pacific"], "Pacific"),
                ("Who painted the Mona Lisa?", ["Picasso", "Da Vinci", "Van Gogh", "Monet"], "Da Vinci"),
                ("What year did World War II end?", ["1943", "1944", "1945", "1946"], "1945"),
            ],
            "Math": [
                ("What is 5 + 7?", ["10", "11", "12", "13"], "12"),
                ("What is 15 x 3?", ["40", "45", "50", "55"], "45"),
                ("What is 100 / 4?", ["20", "25", "30", "35"], "25"),
                ("What is the square root of 64?", ["6", "7", "8", "9"], "8"),
                ("What is 2 to the power of 3?", ["6", "8", "10", "12"], "8"),
            ],
            "Science": [
                ("What is H2O?", ["Oxygen", "Hydrogen", "Water", "Carbon"], "Water"),
                ("How many planets are in our solar system?", ["7", "8", "9", "10"], "8"),
                ("What is the speed of light (approx)?", ["299,792 km/s", "150,000 km/s", "500,000 km/s", "1,000,000 km/s"], "299,792 km/s"),
                ("What gas do plants absorb?", ["Oxygen", "Nitrogen", "CO2", "Hydrogen"], "CO2"),
                ("What is the smallest unit of life?", ["Atom", "Cell", "Molecule", "Organ"], "Cell"),
            ],
            "Geography": [
                ("What is the largest country by area?", ["China", "USA", "Russia", "Canada"], "Russia"),
                ("Which continent is the Sahara Desert in?", ["Asia", "Africa", "Australia", "Americas"], "Africa"),
                ("What is the capital of Japan?", ["Osaka", "Kyoto", "Tokyo", "Nagoya"], "Tokyo"),
                ("How many continents are there?", ["5", "6", "7", "8"], "7"),
                ("What is the longest river in the world?", ["Amazon", "Nile", "Yangtze", "Mississippi"], "Nile"),
            ],
            "Random": []
        }

        self.current_category = None
        self.current_questions = []
        self.current_question_index = 0
        self.score = 0
        self.total_questions = 0
        self.selected_answer = ctk.StringVar()
        self.time_limit = 15
        self.time_remaining = self.time_limit
        self.timer_active = False
        self.best_scores = {cat: 0 for cat in self.categories.keys()}
        self.option_widgets = []

        self.setupUI()
        self.show_category_selection()

    def setupUI(self):
        header = ctk.CTkFrame(self.window, fg_color="#1e1e3f", height=100)
        header.pack(fill="x")
        header.pack_propagate(False)

        ctk.CTkLabel(header, text="ULTIMATE QUIZ", font=("Arial", 28, "bold"),
                     fg_color="#1e1e3f", text_color="#ffffff").pack(pady=10)

        self.score_label = ctk.CTkLabel(header, text="Score: 0/0", font=("Arial", 14, "bold"),
                                        fg_color="#1e1e3f", text_color="#ffeb3b")
        self.score_label.pack()

        self.main_container = ctk.CTkFrame(self.window, fg_color="#0a0a15")
        self.main_container.pack(expand=True, fill="both", padx=20, pady=20)

    def show_category_selection(self):
        self.clear_container()

        ctk.CTkLabel(self.main_container, text="Select a Category",
                     font=("Arial", 22, "bold"), fg_color="#0a0a15", text_color="#00e5ff").pack(pady=15)

        cat_frame = ctk.CTkFrame(self.main_container, fg_color="#0a0a15")
        cat_frame.pack(expand=True)

        category_list = ["General Knowledge", "Math", "Science", "Geography", "Random"]

        # colors for each button, picked these manually
        cat_colors = {
            "General Knowledge": ("#c62828", "#a01e1e"),
            "Math": ("#0d47a1", "#093478"),
            "Science": ("#1b5e20", "#134516"),
            "Geography": ("#e65100", "#b33d00"),
            "Random": ("#6a1b9a", "#4e1272"),
        }

        for category in category_list:
            color, hover = cat_colors[category]
            btn_frame = ctk.CTkFrame(cat_frame, fg_color="#0a0a15")
            btn_frame.pack(pady=6)

            btn = ctk.CTkButton(btn_frame, text=category,
                                command=lambda c=category: self.start_quiz(c),
                                font=("Arial", 15, "bold"), fg_color=color, text_color="#ffffff",
                                width=280, height=40, cursor="hand2", corner_radius=15,
                                hover_color=hover, border_width=0)
            btn.pack()

            if category != "Random":
                best = self.best_scores[category]
                if best > 0:
                    ctk.CTkLabel(btn_frame, text=f"Best: {best}/{len(self.categories[category])}",
                                 font=("Arial", 9, "bold"), fg_color="#0a0a15", text_color="#ffeb3b").pack()

        settings_frame = ctk.CTkFrame(self.main_container, fg_color="#1e1e3f",
                                      border_width=2, border_color="#1e1e3f", corner_radius=15)
        settings_frame.pack(pady=10, fill="x", padx=15)

        ctk.CTkLabel(settings_frame, text="Timer per question:", font=("Arial", 11, "bold"),
                     fg_color="#1e1e3f", text_color="#00e5ff").pack(side="left", padx=5, pady=10)

        self.timer_var = ctk.StringVar(value="15")

        for opt in ["10", "15", "20", "30", "Off"]:
            label = f"{opt}s" if opt != "Off" else opt
            ctk.CTkRadioButton(settings_frame, text=label,
                               variable=self.timer_var, value=opt,
                               font=("Arial", 10, "bold"), fg_color="#00e5ff",
                               text_color="#ffffff", border_color="#00e5ff",
                               hover_color="#00b8d4").pack(side="left", padx=5)

    def start_quiz(self, category):
        self.current_category = category
        print(f"Starting quiz: {category}")

        if category == "Random":
            all_q = []
            for cat_name, questions in self.categories.items():
                if cat_name != "Random":
                    all_q.extend(questions)
            random.shuffle(all_q)
            self.current_questions = all_q[:10]
        else:
            self.current_questions = self.categories[category].copy()
            random.shuffle(self.current_questions)

        self.current_question_index = 0
        self.score = 0
