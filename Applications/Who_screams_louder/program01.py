# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 13:53:09 2021

@author: Luigi D'annibale

In the game "who screams louder," two players A and B, generate
sequences of variable length values. Each value is represented by a
single character. The sequences can be of different lengths because
the values can be separated by one (or more) whitespaces
and tabs ('\t'). The number of non-space characters is, however, equal
for each sequence.

Each element of the sequence of A is compared with the corresponding
element of the B's sequence, and a point is assigned:
- to the player who generated the highest value (for example A), if
  the difference between the value of A and the value of B is less
  than or equal to a parameter k decided at the beginning of the
  challenge
- to the player who has generated the lowest value (for example B), if
  the difference between the value of A and the value of B is greater
  than k (i.e., A has failed)
- to none, in case of a tie.
At the end of the assignment, whoever scored the most points wins. In
the case of a tie, the player who generated the sequence with the
lower total sum of values wins. In the case of a further tie, the
player with the first sequence in lexicographic order wins. It cannot
happen that two players generate precisely the same sequence of
values.

It is necessary to create a function that evaluates the ranking of a
"who screams louder" tournament. The function takes as input a list of
strings and a k parameter, and returns the final ranking of the
tournament, as a list. The string in position "i" in the input list
corresponds to the player "i"'s sequence of values.  In the
tournament, each player challenges all the others with their own
sequence: thus, if there are n players, each player will make n-1
challenges. The number of winning challenges determines the position in
the ranking. In case of a tie, the players are ordered according to
their initial position.

Example of  "who screams louder" tournaments between three players.

    If k=2 and the list is ["aac", "ccc", "caa"], then
        the challenge 0, 1 is won by 1 by 2 points to 0, since the
            difference between "c" and "a" is less than or equal to 2
        the challenge 0, 2 is a 1 to 1 draw, the two sequences have
            equal sum, but 0 wins because "aac" < "caa"
        the challenge 1, 2 is won by 1 by 2 points to 0, since the
            difference between "c" and "a" is less than or equal to 2.

        In the end 0 has 1 challenge, 1 has 2 challenges and 2 has 0
            challenges, so the final ranking will be [1, 0, 2].

    If k=1 and the list is ["aac", "ccc", "caa"], then
        the challenge 0, 1 is won by 0 by 2 points to 0, since the
            difference between "c" and "a" is greater than 1
        the challenge 0, 2 is a 1 to 1 tie, the two sequences have
            equal sum equal, but 0 wins because "aac" < "caa".
        the challenge 1, 2 is won by 2 for 2 points to 0, since the
            difference between "c" and "a" is greater than 1.

        In the end 0 has 2 challenges, 1 has 0 challenges and 2 has 1
            challenge, so the final ranking will be [0, 2, 1].

    If k=10 and the list is [ "abc", "dba" , "eZo"], then
        the challenge 0, 1 is a tie, but 0 wins because its sequence
            has lower sum
        the challenge 0, 2 is won by 0 by 2 points to 1, because 2 is
            wrong with the letter 'o' against 'c'
        the challenge 1, 2 is won by 1 for 2 points to 1, because 2 is
            fails with the letter 'o' vs. 'a'.

        In the end 0 has 2 challenges, 1 has 1 challenge and 2 has 0
            challenges, so the final ranking will be [0, 1, 2].

    If k=50 and the list is [ "A ƐÈÜ", "BEAR" , "c Ʈ ´ ."]
        Challenge 0, 1 is won by 1 by 4 points to 0.
        Challenge 0, 2 is won by 2 for 3 points to 1.
        Challenge 1, 2 is won by 1 by 3 points to 1.
        In the end 0 has 0 challenges, 1 has 1 challenge and 2 has 2
        challenges, so the final ranking will be [1, 2, 0].

"""
def is_sorted(var):
    #Controls if the string is sorted
    if var == sorted (var):
        return True
    return False

def winner(p1_points, p2_points, player1_n,player2_n,p1_list,p2_list):
    #### Return of the winner number for the "challenge" function{
    #### If a player collected more points than the other he'll win, else there are two other possible scecnarios: 
    #### the winner is the one with the lower sum of char in his string, if the sum is equal the winner is the first with the ordinated string
    
    # Win per points
    if p1_points > p2_points:
        return player1_n
    elif p1_points < p2_points:
        return player2_n
    else:
      # Win for sum
      s1 = sum(p1_list) 
      s2 = sum(p2_list)
      if  s1 < s2 :
          return player1_n
      elif s2 < s1:
          return player2_n
      # Win per ordinate
      else:
         if is_sorted(p1_list):
            return player1_n
         elif is_sorted(p2_list):
            return player2_n
    ####}

def challenge (player1_n,player1_txt,player2_n,player2_txt,k):    
    # Given two players defined by a number and a text this function returns the number of the player that wins the challenge.  
    p1_list = [ord(char)  for char in player1_txt.replace("\t","").replace(" ","")]
    p2_list = [ord(char)  for char in player2_txt.replace("\t","").replace(" ","")]
    p1_points,p2_points = 0,0
    
    #### Cylce that executes the challenge between every char of the two strings (p1_list, p2_list){
    for n1,n2 in zip(p1_list,p2_list):
        
        #### Calculating the distance from the char of player1 and the char of player2 and calling it discriminating {
        discriminating = abs(n2 - n1)
        ####}
        
        #### Assignation of the point per turn{
        #### Switch on the discriminating, case it's zero there will be other controls, if it's greater than K the 
        #### distance is too big so the point goes to the lower char, else the distance is strictly lower than K so 
        #### the point goes to the higher char 
        if discriminating == 0:
            continue
        elif discriminating <= k:
            if n2 > n1:
                p2_points += 1
            else:
                p1_points += 1
        elif discriminating > k:
            if n2 < n1:
                p2_points += 1
            else:
               p1_points += 1 
        ####}
    ####}
    return winner(p1_points,p2_points, player1_n,player2_n,p1_list,p2_list)
    
      
                
def ex(matches, k):
    len_matches = len(matches)
    #### Calculating the winner for each challenge and storing it into a list
    winners = [challenge(n1, matches[n1], n2, matches[n2], k) for n1 in range(0,len_matches-1) for n2 in range(n1+1,len_matches)]
    #### Mapping the player to the number challenge won and returning the leaderboard
    results = {i: winners.count(i) for i in range(len_matches)}
    return sorted(list(results.keys()), key=lambda elem: -results[elem])
    
