----------------------Eng version----------------------

The speedtester code is simple after all, but really helpful to track your network stats, I personally use it like this:
first I have wrote the start command, for windows in my case (start.cmd), then i wrote the visual basic code that starts it discreetly in background.
In the end I scheduled, on the windows "task scheduler", a custom activity that everytime I start my pc, opens the visual basic code which in turn opens 
the start command that starts the speedtest.py.
So I have a track of my internet speed in two files, one is .json mostly used like a database perfectly readable by another future program, the second is .txt more readable by a 
human than the json one is used to easily read datas whenever I want.

----------------------Ita version---------------------- 

Il codice dello speedtest è molto semplice nel complesso, ma molto comodo per tener traccia delle statistiche della mia connessione, personalmente lo uso in questo modo:
prima di tutto ho scritto un programma che lancia lo script python, per windows nel mio caso (start.cmd), poi ho scritto in visual basic un codice che lancia il comando discretamente in background. In fine ho pianificato su "attività di pianificazione" di windows, un'attività personalizzata che ogni volta che avvio il pc, avvia il codice visual basic che a sua volta avvia in modo discreto in background lo start.cmd che avvia speedtest.py.
Così tengo traccia delle statistiche della mia connessione su due file, uno .json usato come mini-database perfettamente leggibile da un altro futuro ed ipotetico proramma, il secondo è un .txt più leggibile da un utente umano, cosicche io possa leggere facilmente i dati quando voglio.