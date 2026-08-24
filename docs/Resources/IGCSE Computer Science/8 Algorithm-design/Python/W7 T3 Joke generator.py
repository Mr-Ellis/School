import random
import math

jokeQuestions = ["What do you call a boomerang that won't come back?",
                 "What building in a town has the most stories?",
                 "Why did the child cross the road?"]
                 


jokeAnswers = ["A stick",
               "The library",
               "To get to the other side"]

randomNumber = random.random()

jokeNumber = math.ceil(randomNumber*3)

input(jokeQuestions[jokeNumber-1])

print(jokeAnswers[jokeNumber-1])
