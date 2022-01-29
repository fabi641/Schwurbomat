#!/usr/bin/env python3

import time
import tweet_a_schwurbel


#tweetet einen schwurbel tweet und schreibt ihn auch nochmal in die shell
def schwurbeln():
    print("Tweet this:\n")
    print("-------------------------------------")
    tweet_a_schwurbel.tweet()
    print("-------------------------------------")

#Hat das Twitter-API-Gedöns geklappt?
print("Twitter Api Kram:")
print(tweet_a_schwurbel.api.VerifyCredentials())
print("---------------------------------------------\n")

#Am Anfang was ausgeben
print("Starting Geschwurbel...")
print("Es ist: "+ time.strftime("%d.%m.%Y %H:%M:%S"))

schwurbeln()
