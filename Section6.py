#14th Feb
import time

#section 6A
for i in range(5):
    print("This is a loop!")

for i in range(18,0,-3):
    print(i)

loop = int(input("Times to repeat: "))
word = input("Word to repeat: ")

for i in range(loop):
    time.sleep(0.5)
    print(word)

#section 6B

# ==   equal to
# !=   not equal to
# <    less than
# <=   less than or equal to
# >    greater than
# >=   greater than or equal to

number = 1
while number <= 10:
    print(number)
    number = number + 1

#
    age = 0
while age < 18:
    print("Only adults allowed to the casino.")
    age = int(input("Enter your age: "))
print("Welcome and enjoy your visit.")

#while true loops
guesses = 0

while True:
    guesses = guesses + 1
    password = input("Enter the password: ")

    if password == "goat7":
        print("Correct Password! It took",guesses,"attempts!")
        break
    else:
        print("Incorrect. Try again!")

#
total = 0

while True:
    choice = input("\nType 1 to enter, 2 for a total and 3 to stop: ")
    if choice == "1":
        number = int(input("Enter a number: "))
        total = total + number
        continue

    elif choice == "2":
        print("The total is" , total)
        continue

    elif choice == "3":
        break
print("\nProgram finished.")
