# Individual Project - Task 1

from tkinter import *

root = Tk()
root.title("Grading System")

group = LabelFrame(root, text="Fill in the blanks", font='Roboto 10', padx=15, pady=15)
Label(group, text="Name: ", font='Roboto 10').grid(row=0)
Label(group, text="Mid-term: ", font='Roboto 10').grid(row=1)
Label(group, text="Final-term: ", font='Roboto 10').grid(row=2)
Label(group, text="Attendance: ", font='Roboto 10').grid(row=3)
Label(group, text="Assignment: ", font='Roboto 10').grid(row=4)
Label(group, text="Quiz: ", font='Roboto 10').grid(row=5)
Label(group, text="Discussion: ", font='Roboto 10').grid(row=6)
Label(group, text="Etc: ", font='Roboto 10').grid(row=7)

name = Entry(group, font='Roboto 10')
mid = Entry(group, font='Roboto 10')
fin = Entry(group, font='Roboto 10')
att = Entry(group, font='Roboto 10')
assig = Entry(group, font='Roboto 10')
quiz = Entry(group, font='Roboto 10')
disc = Entry(group, font='Roboto 10')
etc = Entry(group, font='Roboto 10')

entryList = [name, mid, fin, att, assig, quiz, disc, etc]

n = 0
for i in entryList:
    i.grid(row=n, column=1)
    n += 1

resultFrm = Frame(root,  borderwidth=3, relief="ridge")

class Lecture:

    def __init__(self, name, mid, fin, att, assig, quiz, disc, etc):
        self.name = name.get()
        self.mid = float(mid.get())
        self.fin = float(fin.get())
        self.att = float(att.get())
        self.assig = float(assig.get())
        self.quiz = float(quiz.get())
        self.disc = float(disc.get())
        self.etc = float(etc.get())

    def grading_system(self):
        mid = (self.mid / 100) * 15
        fin = (self.fin / 100) * 15
        att = (self.att / 100) * 20
        assig = (self.assig / 100) * 40
        quiz = (self.quiz / 100) * 10
        disc = (self.disc / 100) * 0
        etc = (self.etc / 100) * 0
        total = round(mid + fin + att + assig + quiz + disc + etc, 2)

        Label(resultFrm, text=f"{self.name}'s overall score is {total}", font='Roboto 10', width=35).grid(row=0)

def start():
    student = Lecture(name, mid, fin, att, assig, quiz, disc, etc)
    student.grading_system()

myBtn = Button(root, text="Calculate", font='Roboto 10 bold', command=start, padx=10)

group.pack(padx=15, pady=15)
resultFrm.pack()
myBtn.pack(padx=10, pady=10)
root.mainloop()