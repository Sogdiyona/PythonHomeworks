import random

player_score=0
computer_score=0

while True:
    
    if computer_score==5:
        print("Game over. You lost the match.Scores:",'you', player_score,'computer', computer_score)
        break
    elif player_score==5:
        print("Congratulations! You won the match.Scores:",'you', player_score,'computer', computer_score)
        break

    computer=random.choice(['rock','paper','scissors'])
    player=input("Enter:rock, paper or scissors - ").strip().lower()
    print("Computer chose: ",computer)
    
    if player!='scissors' and player!='rock' and player!='paper':
        print("You can choose oly: rock,paper or scissors")
        continue

    if computer==player:
        print("IT's a tie")
        continue
    elif computer=='rock' and player=='scissors':
        computer_score+=1
        print("You lost.Scores:",'you', player_score,'computer', computer_score )
        continue
    elif computer=='scissors' and player=='rock':
        player_score+=1
        print("You win.Scores:",'you', player_score,'computer', computer_score )
        continue
    elif computer=='paper' and player=='scissors':
        player_score+=1
        print("You win.Scores:",'you', player_score,'computer', computer_score )
        continue
    elif computer=='scissors' and  player=='paper':
        computer_score+=1
        print("You lost.Scores:",'you', player_score,'computer', computer_score )
        continue
    elif computer=='rock' and player=='paper':
       player_score+=1
       print("You win.Scores:",'you', player_score,'computer', computer_score)
       continue
    elif computer=='paper' and player=='rock':
       computer_score+=1
       print("You lost.Scores:",'you', player_score,'computer', computer_score )
       continue 

    if computer_score==5:
        print("Game over. You lost the match.Scores:",'you', player_score,'computer', computer_score)
        break
    elif player_score==5:
        print("Congratulations! You won the match.Scores:",'you', player_score,'computer', computer_score)
        break
    