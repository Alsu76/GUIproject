# Python tkinter quiz app

from tkinter import *
import json
from tkinter import messagebox as mb


class  Quiz(object):
    """ this is a quiz that uses JSON object to import questions."""

    #this is a template for quiz
    def __init__(self):
        # set question number to 0
        self.question_number = 0
        # assigns ques to the display_question function to update later.
        self.display_title()
        self.display_question()
        # option_selected holds an integer value which is used for
        # selected option in a question.
        self.option_selected=IntVar()
        # displaying radio button for the current question and used to
        # display options for the current question
        self.opts=self.radio_buttons()
        # display options for the current question
        self.display_options()
        # displays the button for next and exit.
        self.buttons()
        # no of questions
        self.data_size=len(question)
        # keep a counter of correct answers
        self.correct=0

    def display_result(self):
        # calculates the wrong count
        count_wrong = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {count_wrong}"
        # calcultaes the percentage of correct answers
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        # Shows a message box to display the result
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    def check_ans(self,question_number):
        if self.option_selected.get() == answer[question_number]:
            return True

    def next_button(self):
        if self.check_ans(self.question_number):
            self.correct+=1
            #next #  QUESTION
        self.question_number +=1
            #check if it is the last questx
        if self.question_number == self.data_size:
             self.display_result()
             gui.destroy()
        #if answer is incorrect and it is not the last question
        else:
            self.display_question()
            self.display_options()

    def buttons(self):
        # The first button is the Next button to move to the
        # next Question
        next_button = Button(gui, text="Next",command=self.next_button,
        width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
        # palcing the button  on the screen
        next_button.place(x=350,y=380)
        # This is the second button which is used to Quit the GUI
        quit_button = Button(gui, text="Quit", command=gui.destroy,
        width=5,bg="black", fg="white",font=("ariel",16," bold"))
        # placing the Quit button on the screen
        quit_button.place(x=700,y=50)

    def display_options(self):
        val=0
        # deselecting the options
        self.option_selected.set(0)
        # looping over the options to be displayed for the
        # text of the radio buttons.
        for option in options[self.question_number]:
            self.opts[val]['text']=option
            val+=1

    # This method shows the current Question on the screen
    def display_question(self):
        # setting the Quetion properties
        question_number = Label(gui, text=question[self.question_number], wraplength=500, justify="center",
        font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
        #placing the option on the screen
        question_number.place(x=70, y=100)

    # This method is used to Display Title
    def display_title(self):
        # The title to be shown
        title = Label(gui, text="Quiz",
        width=70, bg="blue",fg="white", font=("ariel", 20, "bold"))
        # place of the title
        title.place(x=0, y=0)


    # This method shows the radio buttons to select the Question
    # on the screen at the specified position. It also returns a
    # lsit of radio button which are later used to add the options to
    # them.
    def radio_buttons(self):
        # initialize the list with an empty list of options
        q_list = []
        # position of the first option
        y_pos = 200
        # adding the options to the list
        while len(q_list) < 4:
            # setting the radio button properties
            radio_btn = Radiobutton(gui,text=" ",variable=self.option_selected,
            value = len(q_list)+1,font = ("ariel",14))
            # adding the button to the list
            q_list.append(radio_btn)
            # placing the button
            radio_btn.place(x = 100, y = y_pos)
            # incrementing the y-axis position by 40
            y_pos += 40
        # return the radio buttons
        return q_list

# Create a GUI Window
gui = Tk()
# set the size of the GUI Window
gui.geometry("850x650")
# set the title of the Window
gui.title("Quiz")
# get the data from the json file
with open('data.json') as f:
    data = json.load(f)
# set the question, options, and answer
question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])
# create an object of the Quiz Class.
quiz = Quiz()
# Start the GUI
gui.mainloop()
