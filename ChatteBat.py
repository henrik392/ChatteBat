import random

class Word:
    def __init__(self, wordName, wordType):
        self.wordName = wordName
        self.wordType = wordType
    
propertyVars = [[Word("name", "property"), ""], [Word("age", "property"), ""], [Word("brother", "property"), ""]]

def aksQuestion ():
    questionWords = propertyVars.copy()
    questionWord = None

    while len(questionWords) > 0:
        randomNumber = random.randint(0, len(questionWords)-1)
        if questionWords[randomNumber][1] == "":
            questionWord = questionWords[randomNumber]
            input("What is your " + questionWord.wordName + "?")
            break

print("Hello, my name is chatter.")

print("I would like to have little chat!")

aksQuestion()