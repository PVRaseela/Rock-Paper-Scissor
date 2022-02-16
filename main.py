from ast import Break, Not
import random
import getpass

class RockPaperScissor:

    def __init__(self,mode):
        self.mode=mode

    @staticmethod
    def GameMode(mode):
        if mode==1:
            print("***************SINGLE PLAYER MODE***************\n")
            
        if mode==2:
            print("***************TWO PLAYER MODE***************\n")
        

    def twoPlayer(self,player1,player2):

        self.player1=player1
        self.player2=player2
        

        print(f"Player I Entered: {player1}")
        print(f"Player II Entered: {player2}")

        #Calls winner function to evaluate winner
        GameWin=RockPaperScissor.winner(player1,player2)
        if GameWin !=None:
            print(f"\n****{GameWin} WON!!****\n")

    def SinglePlayer(self,player):
        
        self.player=player

        GameList=['R','P','S']
        # Using Random Function to Generate Random input for computer
        Computer=random.choice(GameList)

        print(f"You Entered: {player}")
        print(f"Computer Entered: {Computer}")

        #Calls winner function to evaluate winner
        GameWinner=RockPaperScissor.winner(player,Computer)
        if GameWinner !=None:  
            if GameWinner=='PLAYER I':
                print("YOU WON!!")
            else: 
                print("YOU LOSE!!")

    def winner(User1,User2):

            if (User1==User2):
                print("YOU ARE ON TIE!")
            elif (User1=='R' and User2=='S'):
                return 'PLAYER I'
            elif (User1=='R' and User2=='P'):
                return 'PLAYER II'
            elif (User1=='S' and User2=='P'):
                return 'PLAYER I'
            elif (User1=='S' and User2=='R'):
                return 'PLAYER II'
            elif (User1=='P' and User2=='R'):
                return 'PLAYER I'
            elif (User1=='P' and User2=='S'):
                return 'PLAYER II'
    





UserGameMode=int(input("Selecte Game Mode: Play with Computer Mode(1) Or 2-Player Mode(2)\n"))#User Selects the Game Mode to Play

#Creating Instance for the class RockPaperScissor
gameObj= RockPaperScissor(UserGameMode)
gameObj.GameMode(UserGameMode)

if UserGameMode==1:
    Splayer=getpass.getpass(prompt="Enter Rock(R), Paper(P), Scissor(S) or Quit(Q).\n Your Turn: ")
    Player=Splayer.upper() #Capitalize User Input
    if Player not in ['R','S','P','Q']:
           print("Invalid Input!\tSelect R,S OR P")

    #Player Quits Game
    elif Player =='Q':
        print("PLAYER QUIT, GAME OVER!!")
        
    else: 
        gameObj.SinglePlayer(Player)

if UserGameMode==2:
    UserOne=getpass.getpass(prompt="Enter Rock(R), Paper(P), Scissor(S) or Quit(Q).\nPlayer I: ")
    PlayerOne=UserOne.upper() #Capitalize User Input

    if PlayerOne not in ['R','S','P','Q']:
           print("Invalid Input!\tSelect R,S OR P")
    #If User1 Quits the Game
    elif PlayerOne =='Q':
        print("PLAYER I QUIT, GAME OVER!!")

    else :
        UserTwo=getpass.getpass(prompt="Player II: ")
        PlayerTwo=UserTwo.upper() #Capitalize User Input

        if PlayerTwo not in ['R','S','P','Q']:
            print("Invalid Input!\tSelect R,S OR P")
        #If User2 Quits the Game
        elif PlayerTwo=='Q':
            print("PLAYER II QUIT, GAME OVER!!")
        else:
            gameObj.twoPlayer(PlayerOne,PlayerTwo) 
    
    






