from tkinter import *
from quiz_brain import QuizBrain

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
        self.score = Label(text="Score: 0",bg=THEME_COLOR,fg="white")
        self.score.grid(row=0,column=1,pady=20)

        #buttons
        true_image =PhotoImage(file = "images/true.png")
        false_image = PhotoImage(file = "images/false.png")
        self.button_true= Button(image=true_image,highlightthickness=0,bg=THEME_COLOR)
        self.button_true.grid(row=2,column=0,pady=20)
        self.button_false= Button(image=false_image,highlightthickness=0,bg=THEME_COLOR)
        self.button_false.grid(row=2,column=1,pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text = q_text)