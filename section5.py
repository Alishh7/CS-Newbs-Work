#other on 19th Feb
from random import choice

print("lets play rock paer scissors!")
input("what do you choose? ")
roc = ["rock", "paper", "scissors"]
print("The computer's choice is: ", choice(roc))

#Section 5a task 1
from random import randint

lower = int(input("What is the lowest number? "))
upper = int(input("What is the highest number? "))

number = randint(lower,upper)

print("A random number between" , lower , "and" , upper , "is" , number)

#other
from random import choice
letters = "abcdefghijklmnopqrstuvwxyz"
print("A random letter is" , choice(letters))

#other
from random import sample

days = ["Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday"]
two_days = sample(days , 2)

print("You will be set homework on:" , *two_days)

#other
from time import sleep

​print("Hello!")
sleep(2)
print("Goodbye!")

#other
from time import ctime
print("Current time:" , ctime())

