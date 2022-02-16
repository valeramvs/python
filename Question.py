class Question:

    def __init__(self, question_text, author, level, answer_text, theme):
        self.question_text = question_text
        self.author = author
        self.level = level
        self.answer_text = answer_text
        self.theme = theme

    def get_question_text(self):
        return self.question_text

    def set_question_text(self, question_text):
        self.question_text = question_text

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_level(self):
        return self.level

    def set_level(self, level):
        self.level = level

    def get_answer_text(self):
        return self.answer_text

    def set_answer_text(self, answer_text):
        self.answer_text = answer_text

    def get_theme(self):
        return self.theme

    def set_theme(self, theme):
        self.theme = theme

    def __repr__(self):
        return f'Вопрос: текст вопроса: {self.question_text}, автор: {self.author}, сложность: {self.level}, верный ' \
               f'ответ: {self.answer_text}, тема: {self.theme} '
