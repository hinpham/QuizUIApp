from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
  
  def __init__(self, quiz: QuizBrain):
    self.quiz = quiz
    self.window = Tk()
    self.window.title("Quizzler")
    self.window.config(bg=THEME_COLOR)
    self.window.config(padx=20, pady=20)

    
    
    self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
    self.score_label.grid(row=0, column=1)
    
    self.canvas = Canvas(width=300, height=250, bg="white")
    self.question_text = self.canvas.create_text(150, 125, width=280, text="Some Question Text", fill=THEME_COLOR, font=("Arial", 20, "italic"))
    self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
    
    
    true_image = PhotoImage(file="images/true.png")
    false_image = PhotoImage(file="images/false.png")
    self.true_button = Button(image=true_image, highlightthickness=0, command=lambda: self.button_choice("True"))
    self.true_button.grid(row=2, column=0)
    self.false_button = Button(image=false_image, highlightthickness=0, command=lambda: self.button_choice("False"))
    self.false_button.grid(row=2, column=1)
    
    self.get_next_question()
    
    self.window.mainloop()
    
    
  def get_next_question(self):
    self.canvas.config(bg="white")
    if self.quiz.still_has_questions():
      
      self.score_label.config(text=f"Score: {self.quiz.score}")
      q_text = self.quiz.next_question()
      self.canvas.itemconfig(self.question_text, text=q_text)
    else:
      self.canvas.itemconfig(self.question_text, text="You've finished the Quiz!")
      self.true_button.config(state="disabled")
      self.false_button.config(state="disabled")
      
    
  def button_choice(self, answer):
    is_correct = self.quiz.check_answer(answer)
    self.give_feedback(is_correct)
    
  def give_feedback(self, correct):
    if correct:
      self.canvas.config(bg="green")
    else:
      self.canvas.config(bg="red")
      
    self.window.after(1000, self.get_next_question)
