import random
while True:
  randomised=random.randint(1,100)
  attempts=0
  won = False
  print("Guess the number between 1 and 100. You have 10 attempts.")
  while attempts<10:
      number=int(input("enter your guess(1-100): "))
      
      if number>100 or number<1:
       print("The number should be between 1 and 100")
       continue

      attempts+=1
      
      if number>randomised:
       print("Too high")
      elif number<randomised:
       print("Too low")
      else  :
           print("You guessed it right!")
           won=True
           break
  if not won:
          print("You lost.")
          break
  answer=input("Do you want to try again?: ").strip().lower()
  if answer not in ['y', 'yes','ye', 'ok', 'ha', 'da']:
    print("Thanks for playing")
    break
     
     