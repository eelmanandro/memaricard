from PyQt5.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel, QPushButton

menu_win = QWidget()
lb_question_m = QLabel("Введіть запитання:)")
lb_right_ans_m = QLabel("Введіть правильну відповідь:)")
lb_wrong_ans1 = QLabel("Введіть першу хибну відповідь:(")
lb_wrong_ans2 = QLabel("Введіть другу хибну відповідь:((")
lb_wrong_ans3 = QLabel("Введіть третю хибну відповідь:(((")

le_question = QLineEdit()
le_right_ans = QLineEdit()
le_wrong_ans1 = QLineEdit()
le_wrong_ans2 = QLineEdit()
le_wrong_ans3 = QLineEdit()

lb_header_stat = QLabel("Статистика")
lb_statistic = QLabel()

vl_labels = QVBoxLayout()
vl_labels.addWidget(lb_question_m)
vl_labels.addWidget(lb_right_ans_m)
vl_labels.addWidget(lb_wrong_ans1)
vl_labels.addWidget(lb_wrong_ans2)
vl_labels.addWidget(lb_wrong_ans3)

vl_line_edits = QVBoxLayout()
vl_line_edits.addWidget(le_question)
vl_line_edits.addWidget(le_right_ans)
vl_line_edits.addWidget(le_wrong_ans1)
vl_line_edits.addWidget(le_wrong_ans2)
vl_line_edits.addWidget(le_wrong_ans3)

hl_question = QHBoxLayout()
hl_question.addLayout(vl_labels)
hl_question.addLayout(vl_line_edits)

back_btn = QPushButton("Назад")
add_question_btn = QPushButton("Додати запитання")
clear_btn = QPushButton("Очистити Батон")

hl_buttons = QHBoxLayout()
hl_buttons.addWidget(add_question_btn)
hl_buttons.addWidget(clear_btn)

vl_res = QVBoxLayout()
vl_res.addLayout(hl_question)
vl_res.addLayout(hl_buttons)
vl_res.addWidget(lb_header_stat)
vl_res.addWidget(lb_statistic)
vl_res.addWidget(back_btn)

menu_win.setLayout(vl_res)
menu_win.resize(400, 300)

