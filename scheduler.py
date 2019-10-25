import schedule
import time
import tweet_a_schwurbel

i = 0
Zeit = "15:00"

#tweetet einen schwurbel tweet und schreibt ihn auch nochmal in die shell
def schwurbeln():
    print("Tweet this:\n")
    print("-------------------------------------")
    tweet_a_schwurbel.tweet()
    print("-------------------------------------")


#Jeden Tag um 15:00 Uhr wird 'schwurbeln' ausgeführt
schedule.every().day.at(Zeit).do(schwurbeln)

#Hat das Twitter-API-Gedöns geklappt?
print("Twitter Api Kram:")
print(tweet_a_schwurbel.api.VerifyCredentials())
print("---------------------------------------------\n")

#Am Anfang was ausgeben
print("Jeden Tag um "+ Zeit +" Uhr gibt's Geschwurbel!")
print("Starting Geschwurbel...")
print("Es ist: "+ time.strftime("%d.%m.%Y %H:%M:%S"))

#Dauerschleife
while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
    #Immer mal schreiben, dass das skript noch lebt
    i += 1
    if i == 10:
	   #um die Connection zur twitter API aufrecht zu erhalten
        tweet_a_schwurbel.api.VerifyCredentials()
        print("Es ist: "+ time.strftime("%d.%m.%Y %H:%M:%S"))
        i = 0
