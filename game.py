import random
def get_choices():
      player_choice =input(" Please Enter your choice :(Rock,Paper,Scissor)")
      options=["Rock","Paper","Scissor"]
      computer_choice=random.choice(options)
      choices={"player":player_choice,"computer":computer_choice}
      return choices

def check_win(player,computer):
      print(f"You chose {player} ,computer chose {computer}")
      if player == computer:
       return "It's a Tie"
      
      elif player == "Rock" :
       if   computer == "Scissor":
          return "Rock Smashes Scissor! You Win!"
       else :
          return "Paper cover rocks! you win!"
       
      elif player == "Rock" :
         if   computer == "Paper":
          return "Paper covers Rock! You Lose!"
         else :
            return "Rock smashes scissor! You Win!"
       
      elif player == "Paper" :
        if   computer == "Scissor":
          return "Scissor cuts Paper! You Lose"
        else :
           return "Paper covers rock! You win!"
       
      elif player == "Scissor" :
       if   computer == "Paper":
          return "Scissor cuts the Paper! You Win!"
       else :
          return "Rock smashes scissor! you Lose"
       
choices =get_choices()

{"player":"Rock","computer":"Paper"}
result = check_win(choices["player"],choices["computer"])
print(result)