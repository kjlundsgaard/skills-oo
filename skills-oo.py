class Student(object):
    """Student class"""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class QuestionMixin(object):
    """Question class"""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        print self.question,
        answer = raw_input(' > ')
        if answer == self.correct_answer:
            return True
        else:
            return False


class Exam(QuestionMixin, object):
    """Exam class using QuestionMixin"""

    def __init__(self, name):
        self.name = name
        self.questions = []

    # struggling to find a way to add a question to the exam's question list and also add it as a Question class
    def add_question(self, question, correct_answer):
        new_question = QuestionMixin(question, correct_answer)
        self.questions.append(new_question)

    def administer(self):
        score = 0
        for question in self.questions:
            if question.ask_and_evaluate() is True:
                score += 1
        return score
