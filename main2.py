import random
while True:
   instruction = '"R" for "rock",\n"P" for "paper",\n"S" for "scissors".'
   print(instruction)
   user_play = input('Pick an option ["R", "P" or "S"] : ')
   user_play_lower = user_play.lower()
   if user_play_lower == "r":
      user_choice = 'Rock'
   elif user_play_lower == "p":
      user_choice = 'Paper'
   elif user_play_lower == "s":
      user_choice = 'Scissors'
   else:
      print("ERROR!!! ---- Invalid Option Entered!\n TRY AGAIN...")
      continue
   game = ["Rock","Paper","Scissors"]
   computer_play = random.choice(game)
   print(f"Player ({user_choice}) : CPU ({computer_play})")
   if user_choice == computer_play:
      print(f'Both Players played "{user_play}", IT IS A TIE!!!')
      continue
   elif user_choice == 'Rock':
      if computer_play == 'Scissors':
         print("Rock smashes Scissors, YOU WIN!!!")
         break
      if computer_play == 'Paper':
         print("Paper covers Rock, COMPUTER WINS!!!")
         break
         
   elif user_choice == 'Paper':
      if computer_play == 'Scissors':
         print("Scissors cuts Paper, COMPUTER WINS!!!")
         break
      if computer_play == 'Rock':
         print("Paper covers Rock, YOU WIN!!!")
         break
         
   elif user_choice == 'Scissors':
      if computer_play == 'Paper':
         print("Scissors cuts Paper, YOU WIN!!!")
         break
      if computer_play == 'Rock':
         print("Rock smashes Scissors, COMPUTER WINS!!!")
         break
   else:
      continue

   
      

      
      
         
      
   
      
  
      
