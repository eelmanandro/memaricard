from PyQt5.QtWidgets import QApplication
app = QApplication([])
from main_window import *
from menu_window import *
from random import shuffle, choice
import time
import webbrowser
class Question():
    def __init__(self, que, ans, w_ans1, w_ans2, w_ans3):
        self.question = que
        self.answer = ans
        self.wrong_answer1 = w_ans1
        self.wrong_answer2 = w_ans2
        self.wrong_answer3 = w_ans3
        self.count_ask = 0
        self.count_right = 0
    
    def answerRight(self):
        self.count_ask += 1
        self.count_right += 1
    def answerWrong(self):
        self.count_ask += 1


q1 = Question("Яке справжнє ім'я Кіри?", "Ягамі Лайт", "Ягамі Оболонь Світле Нефільтроване", "Рюга Хіхідекі", "Міска Ріса")
q2 = Question("Скільки?", "Стільки", "Ніскільки", "А скільки треба?", "Скількись")

radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
questions = [q1, q2]

def new_question():
    global cur_q
    cur_q = choice(questions)
    lb_question.setText(cur_q.question)
    lb_right_ans.setText(cur_q.answer)
    shuffle(radio_buttons)
    radio_buttons[0].setText(cur_q.answer) 
    radio_buttons[1].setText(cur_q.wrong_answer1)
    radio_buttons[2].setText(cur_q.wrong_answer2)
    radio_buttons[3].setText(cur_q.wrong_answer3)

def check():
    radioGroup.setExclusive(False)
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lb_right_ans.text():
                cur_q.answerRight()
                lb_result.setText("Virno")
                answer.setChecked(False)
                break
            else:
                cur_q.answerWrong()
                lb_result.setText("NootVirno")
                answer.setChecked(False) 
    radioGroup.setExclusive(True)


def click_ok():
    if next_btn.text() == "Answer":
        check() 
        gb_question.hide()
        gb_answer.show()
        next_btn.setText("Next")
    else:
        new_question()
        gb_answer.hide()
        gb_question.show()
        next_btn.setText("Answer")

next_btn.clicked.connect(click_ok)

def rest():
    window.hide()
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1", new = 2)
    time.sleep(sp_rest.value()*60)
    window.show()
rest_btn.clicked.connect(rest)

def openMenu():
    if cur_q.count_ask == 0:
        c = 0
    else:
        c = (cur_q.count_right/cur_q.count_ask)*100
    text = f"Разів відповіли:{cur_q.count_ask}\n"\
    f"Вірних відповідей:{cur_q.count_right}\n"\
    f"Успішність:{c:.2f}%"
    lb_statistic.setText(text)
    menu_win.show()
    window.hide()
    

def backButtonMenu():
    menu_win.hide()
    window.show()

def clearMenu():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()

def addQuestion():
    new_q = Question(le_question.text(), le_right_ans.text(),
                     le_wrong_ans1.text(), le_wrong_ans2.text(),
                     le_wrong_ans3.text())
    questions.append(new_q)
    clearMenu()
clear_btn.clicked.connect(clearMenu)
add_question_btn.clicked.connect(addQuestion)
menu_btn.clicked.connect(openMenu)
back_btn.clicked.connect(backButtonMenu)

new_question()
window.show()
app.exec_()