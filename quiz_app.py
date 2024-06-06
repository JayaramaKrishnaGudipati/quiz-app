# import tkinter as tk
# from tkinter import messagebox
# import json

# class QuizApp:
#     def __init__(self, root, questions):
#         self.root = root
#         self.root.title("Quiz Application")
#         self.questions = questions
#         self.current_question_index = 0
#         self.score = 0
#         self.user_answers = [None] * len(self.questions)  # Initialize the user_answers list with None

#         self.create_widgets()
#         self.update_question()  # Initialize the first question properly

#     def create_widgets(self):
#         self.question_label = tk.Label(self.root, text="")
#         self.question_label.pack(pady=10)

#         self.answer_var = tk.StringVar()

#         self.radio_buttons = []
#         for _ in range(4):  # Assuming there are always 4 options
#             rb = tk.Radiobutton(self.root, text="", variable=self.answer_var)
#             rb.pack(anchor="w")
#             self.radio_buttons.append(rb)

#         self.navigation_frame = tk.Frame(self.root)
#         self.navigation_frame.pack(pady=10)

#         self.prev_button = tk.Button(self.navigation_frame, text="Previous", command=self.prev_question)
#         self.prev_button.grid(row=0, column=0, padx=5)

#         self.next_button = tk.Button(self.navigation_frame, text="Next", command=self.next_question)
#         self.next_button.grid(row=0, column=1, padx=5)

#         self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_quiz)
#         self.submit_button.pack(pady=10)
#         self.submit_button.pack_forget()  # Hide submit button initially

#     def next_question(self):
#         if not self.answer_var.get():
#             messagebox.showwarning("Warning", "Please select an answer before moving to the next question.")
#             return

#         self.user_answers[self.current_question_index] = self.answer_var.get()
#         self.current_question_index += 1

#         if self.current_question_index == len(self.questions):
#             self.current_question_index -= 1  # Stay on the last question
#             self.show_submit_button()
#         else:
#             self.update_question()

#     def prev_question(self):
#         if self.current_question_index > 0:
#             self.user_answers[self.current_question_index] = self.answer_var.get()  # Save the current answer
#             self.current_question_index -= 1
#             self.update_question()
#         self.hide_submit_button()

#     def update_question(self):
#         self.question_label.config(text=self.questions[self.current_question_index]["question"])
#         options = self.questions[self.current_question_index]["options"]
#         for i, rb in enumerate(self.radio_buttons):
#             rb.config(text=options[i]["text"], value=options[i]["key"])
#             rb.deselect()

#         # Set the previously selected answer if it exists
#         if self.user_answers[self.current_question_index] is not None:
#             self.answer_var.set(self.user_answers[self.current_question_index])
#         else:
#             self.answer_var.set(None)

#     def submit_quiz(self):
#         if None in self.user_answers:
#             messagebox.showwarning("Warning", "Please answer all the questions before submitting.")
#             return

#         self.score = sum([1 for i, answer in enumerate(self.user_answers) if answer == self.questions[i]["answerKey"]])

#         result_message = f"You scored {self.score} out of {len(self.questions)}\n\n"
#         for i, answer in enumerate(self.user_answers):
#             result_message += f"Question {i + 1}: {'Correct' if answer == self.questions[i]['answerKey'] else 'Incorrect'}\n"

#         result_message += "\nWhat would you like to do next?"
#         response = messagebox.askquestion("Quiz Result", result_message, icon='info', type=messagebox.YESNO, default=messagebox.YES, detail="Yes: Restart Quiz\nNo: Exit")

#         if response == 'yes':
#             self.reset_quiz()
#         else:
#             self.root.quit()

#     def reset_quiz(self):
#         self.current_question_index = 0
#         self.score = 0
#         self.user_answers = [None] * len(self.questions)
#         self.update_question()
#         self.hide_submit_button()

#     def show_submit_button(self):
#         self.next_button.grid_forget()
#         self.submit_button.pack()

#     def hide_submit_button(self):
#         self.submit_button.pack_forget()
#         self.next_button.grid(row=0, column=1, padx=5)

# def load_questions(filename):
#     with open(filename, "r", encoding="utf-8") as file:
#         return json.load(file)

# if __name__ == "__main__":
#     try:
#         questions = load_questions("quiz_questions.json")
#         root = tk.Tk()
#         app = QuizApp(root, questions)
#         root.mainloop()
#     except Exception as e:
#         tk.messagebox.showerror("Error", f"Failed to load questions: {str(e)}")


import tkinter as tk
from tkinter import messagebox
import json

class QuizApp:
    def __init__(self, root, questions):
        self.root = root
        self.root.title("Quiz Application")
        self.questions = questions
        self.current_question_index = 0
        self.score = 0
        self.user_answers = [None] * len(self.questions)  # Initialize the user_answers list with None

        self.create_widgets()
        self.update_question()  # Initialize the first question properly

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="")
        self.question_label.pack(pady=10)

        self.answer_var = tk.StringVar()

        self.radio_buttons = []
        for _ in range(4):  # Assuming there are always 4 options
            rb = tk.Radiobutton(self.root, text="", variable=self.answer_var)
            rb.pack(anchor="w")
            self.radio_buttons.append(rb)

        self.navigation_frame = tk.Frame(self.root)
        self.navigation_frame.pack(pady=10)

        self.prev_button = tk.Button(self.navigation_frame, text="Previous", command=self.prev_question)
        self.prev_button.grid(row=0, column=0, padx=5)

        self.next_button = tk.Button(self.navigation_frame, text="Next", command=self.next_question)
        self.next_button.grid(row=0, column=1, padx=5)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_quiz)
        self.submit_button.pack(pady=10)
        self.submit_button.pack_forget()  # Hide submit button initially

    def next_question(self):
        self.user_answers[self.current_question_index] = self.answer_var.get() or None or ""
        print(self.user_answers)
        if not self.answer_var.get():
            messagebox.showwarning("Warning", "Please select an answer before moving to the next question.")
            return

        self.current_question_index += 1

        if self.current_question_index == len(self.questions):
            self.current_question_index -= 1  # Stay on the last question
            self.show_submit_button()
        else:
            self.update_question()

    def prev_question(self):
        if self.current_question_index > 0:
            self.user_answers[self.current_question_index] = self.answer_var.get() or None  # Save the current answer
            self.current_question_index -= 1
            self.update_question()
        self.hide_submit_button()

    def update_question(self):
        question_number = self.current_question_index + 1
        self.question_label.config(text=f"{question_number}. {self.questions[self.current_question_index]['question']}")
        options = self.questions[self.current_question_index]["options"]
        for i, rb in enumerate(self.radio_buttons):
            rb.config(text=options[i]["text"], value=options[i]["key"])
            rb.deselect()

        # Set the previously selected answer if it exists
        if self.user_answers[self.current_question_index] is not None:
            self.answer_var.set(self.user_answers[self.current_question_index])
        else:
            self.answer_var.set(None)

    def submit_quiz(self):
        if 'None' in self.user_answers:
            messagebox.showwarning("Warning", "Please answer all the questions before submitting.")
            return

        self.score = sum([1 for i, answer in enumerate(self.user_answers) if answer == self.questions[i]["answerKey"]])

        result_message = f"You scored {self.score} out of {len(self.questions)}\n\n"
        for i, answer in enumerate(self.user_answers):
            result_message += f"Question {i + 1}: {'Correct' if answer == self.questions[i]['answerKey'] else 'Incorrect'}\n"

        result_message += "\nWhat would you like to do next?"
        response = messagebox.askquestion("Quiz Result", result_message, icon='info', type=messagebox.YESNO, default=messagebox.YES, detail="Yes: Restart Quiz\nNo: Exit")

        if response == 'yes':
            self.reset_quiz()
        else:
            self.root.quit()

    def reset_quiz(self):
        self.current_question_index = 0
        self.score = 0
        self.user_answers = [None] * len(self.questions)
        self.update_question()
        self.hide_submit_button()

    def show_submit_button(self):
        self.next_button.grid_forget()
        self.submit_button.pack()

    def hide_submit_button(self):
        self.submit_button.pack_forget()
        self.next_button.grid(row=0, column=1, padx=5)

def load_questions(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

if __name__ == "__main__":
    try:
        questions = load_questions("quiz_questions.json")
        root = tk.Tk()
        app = QuizApp(root, questions)
        root.mainloop()
    except Exception as e:
        tk.messagebox.showerror("Error", f"Failed to load questions: {str(e)}")
