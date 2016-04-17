class Student(object):
    """Student class"""

    def __init__(self, first_name=None, last_name=None, address=None):
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
        answer = raw_input(' > ').lower()
        if answer == self.correct_answer:
            return True
        else:
            return False


class Exam(QuestionMixin, object):
    """Exam class using QuestionMixin"""

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        new_question = QuestionMixin(question, correct_answer)
        self.questions.append(new_question)

    def administer(self):
        score = 0
        for question in self.questions:
            if question.ask_and_evaluate() is True:
                score += 1
        return score


class Quiz(Exam):
    """Quiz class that returns True if at least half of questions returned are correct"""

    def administer(self):
        passed = False
        self.score = super(Quiz, self).administer()
        if self.score / float(len(self.questions)) >= 0.5:
            passed = True
        return passed


def take_test(exam, student):
    """takes in a student and exam and administers test"""
    student.score = exam.administer()


def example():
    """creates example exam"""

    example_exam = Exam('example')
    example_exam.add_question('What is the name of the villain in Harry Potter?', 'voldemort')
    example_exam.add_question('Who starred in the movie Groundhog Day and Caddy Shack?', 'bill murray')
    example_exam.add_question('Which Game of Thrones house\'s motto involves always paying their debts', 'lannister')
    student = Student()
    student.first_name = raw_input('What\'s your first name? ')
    student.last_name = raw_input('What\'s your last name? ')
    student.address = raw_input('What\'s your address? ')
    take_test(example_exam, student)
    print "Congratulations {}, you received a score of {}!".format(student.first_name, student.score)

example()
