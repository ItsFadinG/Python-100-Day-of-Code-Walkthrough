#!/usr/bin/python3
"""
- welcoming
- r, p, s
- Possabilities
"""
import random
class Game:
    def __init__(self):
        print("-------------------------------------------")
        print('Welcome to The Rock, paper, Scissors Game')
        print("-------------------------------------------")
        P_result = 0
        C_result = 0
        while True:
            Player_choise = input("Choose r for Rock, p For Paper and s For Scissors: ")
            Player_choise = Player_choise.lower()
            Comp_choise = random.choice(['r', 'p', 's'])    
                                                # Check a Valid Choises
            if Player_choise not in ['r', 'p', 's']:
                print("Please, Enter a valid Choise")
                break
                                                # Tied
            if Player_choise == Comp_choise:
                print("you have chosen {} and the computer have chosen {}. you Tied".format(Player_choise, Comp_choise))
                print("> Player result is: {} \n> Computer result is: {} ".format(P_result, C_result))
                                                # Player wins
            if Player_choise == 'r' and Comp_choise == 's':
                print("you have chosen {} and the computer have chosen {}. Player wins!!".format(Player_choise, Comp_choise))
                P_result += 1
                print("> Player result is: {} \n> Computer result is: {} ".format(P_result, C_result))
            if Player_choise == 's' and Comp_choise == 'p':
                print("you have chosen {} and the computer have chosen {}. Player wins!!".format(Player_choise, Comp_choise))
                P_result += 1
                print("> Player result is: {} \n> Computer result is: {} ".format(P_result, C_result))
            if Player_choise == 'p' and Comp_choise == 'r':
                print("you have chosen {} and the computer have chosen {}. Player wins!!".format(Player_choise, Comp_choise))
                P_result += 1                 
                print("> Player result is: {} \n> Computer result is: {} ".format(P_result, C_result))
            '''------------------------------------------------------------------------------------------'''
                                                # Computer wins
            if Comp_choise == 'p' and Player_choise == 'r':
                print("you have chosen {} and the computer have chosen {}. Computer wins!!".format(Player_choise, Comp_choise))
                C_result += 1                 
                print("> Player result is: {} \n> Computer result is: {} ".format(P_result, C_result))
            if Comp_choise == 'r' and Player_choise == 's':
                print("you have chosen {} and the computer have chosen {}. Computer wins!!".format(Player_choise, Comp_choise))
                C_result += 1                 
                print("> Player result is: {} \n> Computer result is: {} ".format(P_result, C_result))
            if Comp_choise == 's' and Player_choise == 'p':
                print("you have chosen {} and the computer have chosen {}. Computer wins!!".format(Player_choise, Comp_choise))
                C_result += 1                 
                print("> Player result is: {} \n> Computer result is: {} ".format(P_result, C_result))
                                                # Continue the Game
            cont = input("If you want to continue [Y], if not [N]: ")
            cont = cont.lower()
            if cont == 'y':
                pass
            elif cont == 'n':
                break
                         
players = Game()