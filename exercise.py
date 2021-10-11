"""
Created on Thu Oct  7 11:40:42 2021

@author: luigi

"""
"""
# scarabeo.py

   Abbiamo quattro giocatori che si sfidano a Scarabeo+. In ogni mano
   di Scarabeo+, i giocatori, a turno, devono inserire una parola nel
   tabellone ed ottengono un punteggio, calcolato in base al valore
   delle lettere che compongono la parola inserita.
   Ogni giocatore crea la propria parola scegliendola a partire da una
   mano di 8 lettere, che vengono rimpiazzate una volta che la parola
   è stata giocata, finché non sono esaurite. Il numero totale di
   lettere è 130.  Il gioco finisce quando un giocatore riesce a
   finire tutte le lettere nella sua mano e non ci sono più lettere a
   disposizione per rimpiazzare quelle che ha appena giocato (ovvero,
   le 130 lettere sono esaurite, perché giocate oppure perché in mano
   agli altri giocatori).
   Alla fine delle giocate, vince il giocatore che ha accumulato più
   punti, considerando che per ogni lettera che rimane non giocata
   (ovvero rimane in mano ad un giocatore quando il gioco finisce)
   vengono sottratti 3 punti. 
   I punteggi sono così calcolati:
    1 punto:  E, A, I, O, N, R, T, L, S, U
    2 punti: D, G
    3 punti: B, C, M, P
    4 punti: F, H, V, W, Y
    5 punti: K
    8 punti: J, X
   10 punti: Q, Z
   Progettare una funzione ex1(g1, g2, g3, g4, dim_hand, num_letters) che calcola i
   punteggi di una partita di Scarabeo+ svolta fra i 4 giocatori, con
   la variante che il numero di lettere iniziali è num_letters, piuttosto che
   130 e il numero di lettere a disposizione di ogni giocatore è dim_hand.
   g1, g2, g3 e g4 sono liste di stringhe che rappresentano le
   giocate dei giocatori g1, g2, g3 e g4, rispettivamente, 
   in ciascun turno.
ES: dim_hand=5, num_letters=40
    g1 = ['seta','peeks','deter']
    g2 = ['reo','pumas']
    g3 = ['xx','xx']
    g4 = ['frs','bern']
    
    Notare che all’inizio della partita 5 lettere vengono date ad ognuno dei
    giocatori, dunque il contatore num_letters decresce conseguentemente.
dim_hand - num_letters - parola - punti
5 5 5 5    20            seta      4  0  0  0
5 5 5 5    16            reo       4  3  0  0
5 5 5 5    13            xx        4  3 16  0
5 5 5 5    11            frs       4  3 16  6
5 5 5 5     8            peeks    15  3 16  6
5 5 5 5     3            pumas    15 12 16  6
5 3 5 5     0            xx       15 12 32  6
5 3 3 5     0            bern     15 12 32 12
5 3 3 1     0            deter    21 12 32 12
0 3 3 1     0                       GAME OVER
---------------------------------------------
Finale                            21  3 23  9
Il TIMEOUT per ciascun test è di 0.5 secondi
ATTENZIONE: è proibito:
    - importare altre librerie
    - usare variabili globali
    - aprire file
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
