"""
Created on Thu Oct  7 11:40:42 2021

@author: luigi

"""

def ex1 (g1, g2, g3, g4, dim_hand, num_letters) :
    
    hand_players = [dim_hand,dim_hand,dim_hand,dim_hand]
    points_counter = [0,0,0,0]
    game_status = "PLAYING"
    game_round = 0
    print ("Players hand\tLetters\tWord\tPoints score\n")
    
    while game_status == "PLAYING" :
        
        #round starts
        current_player = 0
        while current_player < 4 :
            #to control if there are players that won during the round 
            for each in hand_players:
                if each == 0 :
                    game_status = "OVER"
                    
            if game_status == "OVER" : break
        
            #controls who's playing
            if current_player == 0 : play = g1
            elif current_player == 1 : play = g2
            elif current_player == 2 : play = g3
            elif current_player == 3 : play = g4
            
            word = play[game_round]
            
            #points per word calculation
            word_points = 0
            for char in word:
                char = char.lower()
                if char == "e" or char == "a" or char == "i" or char == "o" or char == "n" or char == "r" or char == "t" or char == "l" or char == "s" or char == "u":
                    word_points +=1
                elif char == "d" or char == "g":
                    word_points +=2
                elif char == "b" or char == "c" or char == "m" or char == "p":
                    word_points +=3
                elif char == "f" or char == "h" or char == "v" or char == "w" or char == "y":
                    word_points +=4
                elif char == "k":
                    word_points +=5
                elif char == "j" or char == "x":
                    word_points +=8    
                elif char == "q" or char == "z":
                    word_points +=10
            
            
            #assigns the player his points
            points_counter[current_player] += word_points
            
            #updates letter numbers situation
            hand_players[current_player] -= len(word)
            new_num_letters = num_letters - len(word)
            if new_num_letters >= 0:
                hand_players[current_player] += len(word)
                num_letters = new_num_letters
                
            elif new_num_letters < 0:
                hand_players[current_player] += num_letters
                num_letters = 0
            
            print (f"{hand_players}\t{num_letters}\t{word}\t{points_counter}")
            
            #passes the turn to another player till round's end
            current_player += 1
        
        print("\n"f"Round number {game_round} finished""\n")
        if game_status == "OVER": print("GAME OVER")
        #round finishes
        game_round += 1
        
        
        
    #cutting points
    for pointer ,player in enumerate(hand_players) :
        points_counter[pointer] -= 3 * hand_players[pointer]
        
    print(f"Final score : ---------------------\t {points_counter}")
    
    
dim_hand = 5
num_letters = 20
g1 = ['seta','peeks','deter']
g2 = ['reo','pumas']
g3 = ['xx','xx']
g4 = ['frs','bern']
ex1(g1, g2, g3, g4, dim_hand, num_letters)
