----------------------Ita version---------------------- 
È stato creato un programma che simula una partita del gioco "Chi la spara più grossa". Ci sono n giocatori (ognuno di questi è una stringa) ogni giocatore, partendo dal primo, si batte con tutti gli altri eseguendo tutte le possibili sfide, una volta effettuate tutte le sfide vengono effettuati dei controlli sui punteggi e si stila la classifica.

Il codice è diviso in 3 funzioni,

La funzione principale ex :

mappa i player tramite il loro testo e il loro numero
calcola il vincitore di ogni sfida (richiamndo la funzione challenge)
mappa ogni giocatore al numero di partite che quest'ultimo ha vinto e crea la classifica, stilandola secondo i criteri di orinamento
ritorna la classifica salvata in una lista
La funzione challenge calcola i punti di ogni giocatore per sfida e ritorna il vincitore tra i due sfidanti richiamando "winner" a cui passa i punti dei giocatori

La funzione winner viene richiamata da "challenge" e ritorna il vincitore tra due sfidanti studiando tutti i possibili casi di vittoria

----------------------Eng version---------------------- 
It's been created a program that simulates a game of "Chi la spara più grossa". There are n players (each rapresented by a string) each player, starting from the first, challenges every other in order to execute every possible combination, once every challenge is over, points are checked and a leaderboard is listed.

The code has been splitted in 3 functions:

Function ex : Maps the text of the pleyr to the number using a dictionary, Calculates the winner for each challenge and stores it into a list Maps the player to the challenge won and returns the leaderboard sorted by the sorting parameters

Function challenge: Given two players defined by a number and a text returns the number of the player that wins the challenge This function calculates the points of each player and calls "winner" function to calculate the winner

Function winner: Return of the winner number for the "challenge" function: If a player collected more points than the other he'll win, else there are two other possible scecnarios: the winner is the one with the lower sum of char in his string, if the sum is equal the winner is the first with the ordinated string
