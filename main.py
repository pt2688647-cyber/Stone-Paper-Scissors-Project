import random
def Game():
    while True:
       
        print("\n1.STONE")
        print("\n2.PAPER")
        print("\n3.SCISSOR")
        
        player=input(f"\nEnter the choice : ")
        robot=random.randint(1,3)
        
        if player.isdigit():
            player=int(player)
            if player==0:
                print("\nGame is over")
                break
            if player not in[1,2,3]:
                 print("\nInvalid Choice")

            print(f"\nRobot choice is: {robot}")

            if player==1 and robot==2 or player==2 and robot==3 or player==3 and robot==1:
                print("\nResult :ROBOT is the Winner")
            elif player==1 and robot==3 or player==2 and robot==1 or player==3 and robot==2:
                print("\nResult :player is the Winner")
            else: 
                print("\nResult :Match is DRAWN")
            
               
        else:
            print("\nEnter a valid Choice")

print("__WELCOME IN THE GAME-STONE,PAPER,SCISSOR__")
Game()