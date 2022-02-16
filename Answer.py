class Answer:

    def __init__(self, question, answer_text, right, score):
        self.question = question
        self.answer_text = answer_text
        self.right = right
        self.score = score

    def get_question(self):
        return self.question

    def set_question(self, question):
        self.question = question

    def get_answer_text(self):
        return self.answer_text

    def set_answer_text(self, answer_text):
        self.answer_text = answer_text

    def get_right(self):
        return self.right

    def set_right(self, right):
        self.right = right

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    @property
    def __repr__(self):
        return f'Ответ: текст вопроса: {self.question}, верный ответ: {self.answer_text}, дан верный ответ: ' \
               f'{self.right}, количество очков: {self.score} '
