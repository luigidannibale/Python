# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 21:15:17 2021

@author: luigi
"""

def is_sorted(var):
    if var == sorted (var):
        return 0
    else :
        return 1

def winner_sorter(array): 
    print(array)
    return -array[0],array[1],array[2],array[3]

    

def challenge (player1_n,player1_txt,player2_n,player2_txt,k):    
    # Given two players defined by a number and a text this function returns the number of the player that wins the challenge.
    p1_list = map(ord, player1_txt.replace("\t","").replace(" ",""))
    p2_list = map(ord, player2_txt.replace("\t","").replace(" ",""))
    p1_points,p2_points = 0,0
    
    #### Cylce that executes the challenge between every char of the two strings (p1_list, p2_list){
    for i in range (len(p1_list)):
        
        #### Calculating the distance from the char of player1 and the char of player2 and calling it discriminating {
        discriminating = abs(p2_list[i] - p1_list[i])
        ####}
        
        #### Assignation of the point per turn{
        #### Switch on the discriminating, case it's zero there will be other controls, if it's greater than K the 
        #### distance is too big so the point goes to the lower char, else the distance is strictly lower than K so 
        #### the point goes to the higher char 
        if discriminating == 0:
            continue
        elif discriminating <= k:
            if p2_list[i] > p1_list[i]:
                p2_points += 1
            else:
                p1_points += 1
        elif discriminating > k:
            if p2_list[i] < p1_list[i]:
                p2_points += 1
            else:
                p1_points += 1 
        ####}
    ####}
    
    
    
    p1 =[p1_points,sum(p1_list),is_sorted(p1_list),player1_n]
    p2 =[p2_points,sum(p2_list),is_sorted(p2_list),player2_n]
    
    lista = sorted([p1,p2],key=winner_sorter)

    return lista[0][3]
    
    # return winner(p1_points, p2_points, player1_n,player2_n,p1_list,p2_list)
    
      
                
def ex(matches, k): 
    diz={matches[i]:i for i in range(len(matches))}
    result_points = [challenge(n1, player1, diz[player2], player2, k) for n1,player1 in enumerate(matches[:len(matches)-1]) for n2,player2 in enumerate(matches[n1+1:])]
    results = {i: result_points.count(i) for i in range(len(matches))}
    print (result_points)
    return sorted(list(results.keys()), key=lambda elem:-results[elem])
    
    
if __name__ == "__main__":
    pass
