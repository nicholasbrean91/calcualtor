# Created by Nick, Justin
# Created on Nov 2017
# Created to show grades of levels

import ui

def calculate_grades(grade):
    if grade == "4":
        grade_mark = "95"
    elif grade == "4+":
        grade_mark = "97"
    elif grade == "4-":
        grade_mark = "90"
    elif grade == "3":
        grade_mark = "85"
    elif grade == "3+":
        grade_mark = "89"
    elif grade == "3-":
        grade_mark = "80"
    elif grade == "2":
        grade_mark = "75"
    elif grade == "2+":
        grade_mark = "79"
    elif grade == "2-":
        grade_mark = "70"
    elif grade == "1":
        grade_mark = "65"
    elif grade == "1+":
        grade_mark = "69"
    elif grade == "1-":
        grade_mark = "60"
    elif grade == "R":
        grade_mark = "50"
    elif grade == "NE":
        grade_mark = "0"
    else:
        grade_mark = "-1"
    return grade_mark

def four_plus_button_touch_up_inside(sender):
    level = "4+"
    view['answer_label'].text =str(calculate_grades(level))

def four_button_touch_up_inside(sender):
    level = "4"
    view['answer_label'].text =str(calculate_grades(level))

def four_minus_button_touch_up_inside(sender):
    level = "4-"
    view['answer_label'].text =str(calculate_grades(level))

def three_plus_button_touch_up_inside(sender):
    level = "3+"
    view['answer_label'].text =str(calculate_grades(level))

def three_button_touch_up_inside(sender):
    level = "3"
    view['answer_label'].text =str(calculate_grades(level))

def three_minus_button_touch_up_inside(sender):
    level = "3-"
    view['answer_label'].text =str(calculate_grades(level))
def two_plus_button_touch_up_inside(sender):
    level = "2+"
    view['answer_label'].text =str(calculate_grades(level))

def two_button_touch_up_inside(sender):
    level = "2"
    view['answer_label'].text =str(calculate_grades(level))

def two_minus_button_touch_up_inside(sender):
    level = "2-"
    view['answer_label'].text =str(calculate_grades(level))
def one_plus_button_touch_up_inside(sender):
    level = "1+"
    view['answer_label'].text =str(calculate_grades(level))

def one_button_touch_up_inside(sender):
    level = "1"
    view['answer_label'].text =str(calculate_grades(level))

def one_minus_button_touch_up_inside(sender):
    level = "1-"
    view['answer_label'].text =str(calculate_grades(level))

def r_button_touch_up_inside(sender):
    level = "R"
    view['answer_label'].text =str(calculate_grades(level))

def ne_button_touch_up_inside(sender):
    level = "NE"
    view['answer_label'].text =str(calculate_grades(level))

view = ui.load_view()
view.present('sheet')
