from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 18, "bold")


class QuizzInterface:
    def __init__(self, quizz_brain: QuizBrain):
        self.quizz = quizz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score = Label(text="Score: 0")
        self.score.config(bg=THEME_COLOR, fg="white", padx=20, pady=20)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,width=280, text="Hi", fill=THEME_COLOR, font=FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="true.png")
        false_img = PhotoImage(file="false.png")

        self.right_button = Button(image=true_img, bg=THEME_COLOR, command=self.true_button)
        self.right_button.config(padx=20, pady=20)
        self.right_button.grid(column=0, row=2)

        self.wrong_button = Button(image=false_img, bg=THEME_COLOR, command=self.false_button)
        self.wrong_button.config(padx=20, pady=20)
        self.wrong_button.grid(column=1, row=2)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        if self.quizz.still_has_questions():
            quiz_text = self.quizz.next_question()
            self.score.config(text=f"Score: {self.quizz.score}")
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text=quiz_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text="You've Reached The End of This Quizz!!")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_button(self):
        self.give_feedback(self.quizz.check_answer("True"))

    def false_button(self):
        self.give_feedback(self.quizz.check_answer("False"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)

