#4a task 2 
weather = input("What is the weather like today? (sunny, rainy, other) ")

if weather == "sunny":
  sunny = input("how hot is it?!?! (very hot, alright, other) ")

  if sunny == "very hot":
    print("GL surving that heat!")
  elif sunny == "alright":
    print("Its a nice day isnt it?")
  else:
    print("have a great day!")

elif weather == "rainy":
  print("dont forget your umbrella!")
else:
  print("have a good day then!")

#4a task 3
score = int(input("Enter the maths test score: "))

if score == 50:
  print("You scored top marks!")
elif score >= 40 and score < 50:
  print("You scored a great grade!")
elif score >= 20 and score < 40:
  print("You did okay in the test.")
else:
  print("You have to try harder next time!")

#4a task 4
ans = input("There are 140 million miles between Earth and Mars. TRUE or FALSE? ")
if ans != "TRUE":
  print("That is incorrect!")
else:
  print("That is correct! It is really that far!")

#4b task 1
num = int(input("Enter a number: "))
print("the remainder when", num, "is divided by 5 is", num % 5)

#other
print(20 / 3)
print(20 // 3)

#other
base = 5
exponent = 4
print(base**exponent)

#4c task 1
print("lets see how smart you are...(:")
capital = input("What is the capital of Germany? ")
chemical = input("What is the chemical formula for water? ")
war = input("What year did World War Two end? ")

if capital == "Berlin" and chemical == "H2O" and war == "1945":
  print("what a genius!")
else:
  print("you are not very smart are you?")

#4c task 2
letter = input("Enter a letter: ")

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
  print("You entered a vowel.")
else:
  print("You entered a consonant.")
