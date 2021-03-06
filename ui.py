from tkinter import *
from quiz_brain import QuizBrain
import sys
import os


THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        #canvas
        self.canvas = Canvas()
        self.canvas.config(width=300,height=250,bg="white")
        self.question_text = self.canvas.create_text(
                                150,
                                125,
                                text="Text",font=("Arial",20,"italic"),
                                fill=THEME_COLOR,
                                width=280
                            )
        self.canvas.grid(row=1,column=0,columnspan=2,pady=20)

        #labels
        self.score_label = Label(text="Score: 0",bg=THEME_COLOR,fg="white")
        self.score_label.grid(row=0,column=1,pady=20)

        #buttons
        true_image =PhotoImage(file = "images/true.png")
        false_image = PhotoImage(file = "images/false.png")
        self.button_true= Button(image=true_image,highlightthickness=0,bg=THEME_COLOR,command=self.true_pressed)
        self.button_true.grid(row=2,column=0,pady=20)
        self.button_false= Button(image=false_image,highlightthickness=0,bg=THEME_COLOR,command=self.false_pressed)
        self.button_false.grid(row=2,column=1,pady=20)
        self.new_quiz_button = Button(text="New Quiz",bg="white",highlightthickness=0,command=self.new_quiz)
        self.new_quiz_button.grid(row=0,column=0,pady=20)

        self.get_next_question()

        self.window.lift()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text ="You've reached the end of the quiz")
            self.button_true.config(state=DISABLED)
            self.button_false.config(state=DISABLED)

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def new_quiz(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)
