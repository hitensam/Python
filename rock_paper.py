import random
container = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]
def game():
    global comp_score, player_score;
    while (comp_score <5 and player_score <5):
        comp_choice = random.randrange(0,3,1)
            # a = print("ENTER A CHOICE ", input(int()));
        print(f"---------SCORE BOARD---------\nPLAYER : {player_score}\nCOMPUTER : {comp_score}\n")
        print("SELECT A VALUE FROM 0, 1, 2\n0 : ROCK\n1 : PAPER\n2 : SCISSORS"); print("The computer has already chosen it's value\n")
        player = int(input("Enter a value ")); print("\n")
        if (player == 0 or player == 1 or player == 2):
            print("YOU CHOOSE ", container[player])
            print("The computer chooses ", container[comp_choice]);

            if(comp_choice ==  player):
                print("It's a tie.")

            else:
                if (player==0 and comp_choice==1 or player==1 and comp_choice==0):
                    if (player==0 and comp_choice==1):
                        print("YOU LOOSE");
                        comp_score +=1 
                    if(player==1 and comp_choice==0):
                        print("YOU WIN")
                        player_score +=1

                if (player==0 and comp_choice==2 or player==2 and comp_choice==0):
                    if (player==0 and comp_choice==2):
                        print("YOU WIN");
                        player_score +=1
                    if (player==2 and comp_choice==0):
                        print("YOU LOOSE")
                        comp_score +=1

                if (player==1 and comp_choice==2 or player==2 and comp_choice==1):
                    if(player==1 and comp_choice==2):
                        print("YOU LOOSE")
                        comp_score +=1
                    if(player==2 and comp_choice==1):
                        print("YOU WIN")
                        player_score +=1
                
        else:
            print("ENTER A VALID CHOICE")
            game()

        # else:
        #     if (comp_score == 5):
        #         print("COMPUTER WON")
        #         return 
        #     if (player_score == 5):
        #         print("YOU WIN")
        #         return


while (True):
    choice = input("PRESS ANY KEY TO PLAY OR PRESS E TO EXIT FROM THE CODE "); print("\n")
    choice = choice.upper()
    if (choice == 'E'):
        print("EXITING FROM GAME")
        break;
    else:
        comp_score, player_score = 0, 0; 
        game()
       
exit
