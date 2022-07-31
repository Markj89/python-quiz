from random import choice
import time
import sys

defaultPoint = 1
point = 1
 # Lets make some questions
questions = {
    "Where were The Lord of the Rings movies filmed?":
    [
        "New Zealand",
        "Austalia",
        "Ireland",
        "Iceland"
    ],
    "Who directed the hit 2017 movie Get Out?":
    [
        "Jordan Peele",
        "Steven Spielberg",
        "Sam Raimi",
        "George Lucas"
    ],
    "What’s the name of the planet Obi-Wan Kenobi and Anakin Skywalker duel on in Star Wars Episode III: Revenge of the Sith?": 
    [
        "Mustafar",
        "Yavin 4",
        "Hoth",
        "Tatooine",
    ],
    "What was the highest-grossing movie of 2005?":
    [
        "Harry Potter and the Goblet of Fire",
        "War of the Worlds",
        "Star Wars: Episode III: Revenge of the Sith",
        "The Chronicles of Narnia: The Lion, The Witch, and the Wardrobe"
    ],
}

def sayHello():
    question = input("What is your name? ")
    answers = []
    if (not question):
        print("Hmm, I didn't get that, could you try again?")
        sayHello()
    else:
        answers.append(question)
        print("Hello, ", question)
        sys.stdout.flush()
        time.sleep(2)
        introduceMyself()

def addPoint(value, pointsAccumulated):
    if (defaultPoint == point or defaultPoint > point):
        if (value == "add"): 
            pointsAccumulated = point + defaultPoint

    return pointsAccumulated

def removePoint(value, pointsAccumulated):
    if (defaultPoint == point or defaultPoint > point):
        if (value == "remove"): 
            pointsAccumulated = point - defaultPoint

    return pointsAccumulated


def introduceMyself():
    print("I'm Rob bot. Now that we've introductions out of the way. lets get to got good stuff.")
    sys.stdout.flush()
    time.sleep(2)
    question = input("Are you ready? Y/N: ")
    if (question.lower().strip() == "y"):
        print("Let's go!")
        sys.stdout.flush()
        time.sleep(1)
        print("I will ask a set of questions, you'll have to answer correctly. If you answer right, you get a point. If you don't you lose a point.")
        print("Seem simple enough, right?")
        sys.stdout.flush()
        time.sleep(3)
        question = input("..., Right? Y/N ")
        if (question.lower().strip() == "y"):
            print("Good")
            quiz()
    else:
        print("Ok, well good luck")

def quiz():
    for question, alternatives in questions.items():
        correct_answer = alternatives[0]
        sorted_alternatives = sorted(alternatives)
        for label, alternative in enumerate(sorted_alternatives):
            print(f" {label}: {alternative}")

        answer_label = int(input(f"{question} "))
        answer = sorted_alternatives[answer_label]
        if (answer == correct_answer):
            setQuip()
            sys.stdout.flush()
            time.sleep(2)
        else:
            print(f"The answer is {correct_answer!r}, not {answer!r}")
        
    sys.stdout.flush()
    time.sleep(2)
    print("You are actually smart! Well here's a point. Now good, get out of here!")

def setQuip():
    quips = [
        "Good job on, I'm surprised you got that one",
        "Whoa! That's correct. Good job",
        "That's correct!",
        "Correct!",
        "Nice one!"
    ]
    say_quip = choice(quips)
    print(say_quip)


if __name__ == "__main__":
    sayHello()