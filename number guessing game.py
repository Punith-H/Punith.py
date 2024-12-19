import random
number = random.randint(1,10)
print("Guess The number between 1 to 10: ")
while True:
  guess = int(input("Enter Your Guess: "))
  if guess < number:
    print("Too low")
  elif guess > number:
    print("Too High")
  else:
    print("Correct Guess")
    break
print("You Win")
