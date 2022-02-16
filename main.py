import json
import random

from project_7.Answer import Answer
from project_7.Question import Question

questions_list = []
answer_list = []


def create_question_list():
    with open("questions.json", "r", encoding="UTF-8") as f:
        questions = json.load(f)
    for k, v in questions.items():
        text = v[list(v.keys())[0]]
        author = v[list(v.keys())[1]]
        level = v[list(v.keys())[2]]
        answer = v[list(v.keys())[3]]
        theme = v[list(v.keys())[4]]
        question = Question(text, author, level, answer, theme)
        questions_list.append(question)


def add_answer_to_list(question_text, answer_text, right, score):
    answer = Answer(question_text, answer_text, right, score)
    answer_list.append(answer)


def start_game():
    create_question_list()
    for i in range(len(questions_list)):
        random_quest = random.choice(questions_list)
        questions_list.remove(random_quest)
        if random_quest.get_level() == '1/5':
            complicity = 'легко'
        elif (random_quest.get_level() == '2/5') | (random_quest.get_level() == '3/5'):
            complicity = 'средне'
        else:
            complicity = 'сложно'
        print(f'Вопрос {i + 1}, тема: {random_quest.get_theme()}, сложность: {complicity}')
        answer = input(random_quest.get_question_text() + "\n")
        score = int(random_quest.get_level()[0]) * 10
        if answer in random_quest.get_answer_text():
            right = True
            print(f'Ответ верный, получено {score} баллов')
        else:
            right = False
            print(f'Ответ неверный. Верный ответ – {random_quest.get_answer_text()[0]}')
        add_answer_to_list(random_quest.get_question_text(), answer, right, score)
    show_result()


def show_result():
    total_score = 0
    count_right_answers = 0
    for i in answer_list:
        if i.get_right():
            total_score += i.get_score()
            count_right_answers += 1
    print(f'Вот и все!\nОтвечено {count_right_answers} вопроса из {len(answer_list)} и набрано {total_score} баллов')


start_game()
