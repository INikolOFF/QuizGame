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

