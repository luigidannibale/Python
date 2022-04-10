# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 13:53:09 2021

@author: Luigi D'annibale
"""
   
def ordinate(l1,l2,n1,n2):
    #### This functions returns the number of the first ordinated string
    for i in range (len(l1)):
        if l1[i] < l2[i] :
            return n1
        elif l2[i] < l1[i] : 
            return n2
        
def winner(p1,p2):
    #### Return of the winner number{
    #### If a player collected more points than the other he'll win, else there are two other possible scecnarios: 
    #### the winner is the one with the lower sum of char in his string, if the sum is equal the winner is the first with the ordinated string
    # Win per points
    if p1["points"] > p2["points"]:
        return p1["number"]
    elif p1["points"] < p2["points"]:
        return p2["number"]
    elif p1["points"] == p2["points"]:
      # Win for sum
      if sum(p1["string"]) < sum(p2["string"]):
          return p1["number"]
      elif sum(p2["string"]) < sum(p1["string"]):
          return p2["number"]
      # Win per ordinate
      else:
          return ordinate(p1["string"], p2["string"], p1["number"], p2["number"])
    ####}

def challenge (n1,player1_txt,n2,player2_txt,k):
    
    # Given two players defined by a number and a text this function returns the number of the player that wins the challenge.
    p1 = {"number":n1,"points":0,"string":map(ord, player1_txt.replace("\t","").replace(" ",""))}
    p2 = {"number":n2,"points":0,"string":map(ord, player2_txt.replace("\t","").replace(" ",""))}
  
    
    #### Cylce that executes the challenge between every char of the two strings (p1["string"], p2["string"]){
    for i in range (len(p1["string"])):
        
        #### Calculating the distance from the char of player1 and the char of player2 and calling it discriminating {
        discriminating = abs(p2["string"][i] - p1["string"][i])
        ####}
        
        #### Assignation of the point per turn{
        #### Switch on the discriminating, case it's zero there will be other controls, if it's greater than K the 
        #### distance is too big so the point goes to the lower char, else the distance is strictly lower than K so 
        #### the point goes to the higher char 
        if discriminating == 0:
            continue
        elif discriminating <= k:
            if p2["string"][i] > p1["string"][i]:
                p2["points"] += 1
            else:
                p1["points"] += 1
        elif discriminating > k:
            if p2["string"][i] < p1["string"][i]:
                p2["points"] += 1
            else:
                p1["points"] += 1 
        ####}
    ####}
    return winner(p1,p2)
    
      
                
def ex(matches, k):
    
    diz={matches[i]:i for i in range(len(matches))}
    result_points = [challenge(n1, player1, diz[player2], player2, k) for n1,player1 in enumerate(matches[:len(matches)-1]) for n2,player2 in enumerate(matches[n1+1:])]
    results = {i: result_points.count(i) for i in range(len(matches))}
    
    return sorted(list(results.keys()), key=lambda elem: -results[elem])
    
    
if __name__ == "__main__":
    pass
