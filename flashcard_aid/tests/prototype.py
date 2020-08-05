class prototype():
    """Bare bones prototype of the basic functionality for flashcard_aid"""
    def __init__(self):
        self.init_questions_answers={'What is your name?':'John','What is your height?':'6 ft',
                             'What is your favorite color?':'red'}
        self.facts=['The sky is blue','Water is wet','Fire is hot']


    def ask_questions(self):
        for i,y in self.init_questions_answers.items():
            print(i)
            answer=input("Type your answer")
            if answer==y:
                print("correct")
            else:
                print("false")

x=prototype()
x.ask_questions()


