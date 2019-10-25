# -*- coding: iso-8859-15 -*-

#Twitter Kram
import twitter
import keys
api = twitter.Api(consumer_key=keys.consumer_key,
                  consumer_secret=keys.consumer_secret,
                  access_token_key=keys.access_token_key,
                  access_token_secret=keys.access_token_secret)
##
##  Gibt 3 Hashtags zurück.
##  Diese 3 sind random aus den 50 aktuell in DE trendenden
##
def get_random_hashtags():
    #Liste an Trends bekommen
    trends = api.GetTrendsWoeid(woeid=23424829,exclude=None)

    #Drei random Zahlen bekommen, um drei Hashtags aus der Liste zu holen
    r1 = r2 = r3 = random.randint(0,len(trends)-1)
    while r1 == r2:
        r2 = random.randint(0,len(trends)-1)   
    while r1 == r3 or r2 == r3:
        r3 = random.randint(0,len(trends)-1)

    #Wenn der Name eines trends nciht mit einem Hashtag beginnt, dieses hinzufügen
    if trends[r1].name[0] != "#":
        trends[r1].name = "#" + trends[r1].name
    if trends[r2].name[0] != "#":
        trends[r2].name = "#" + trends[r2].name
    if trends[r3].name[0] != "#":
        trends[r3].name = "#" + trends[r3].name

    hashtags = trends[r1].name.replace(" ", "") + " " + trends[r2].name.replace(" ", "") + " " + trends[r3].name.replace(" ", "")

    return hashtags
	  
#print(api.VerifyCredentials())

#Schwurbel Kram

import random
import sys
import codecs

class Noun:
    nominative = ""
    genitiv = ""
    gender = ""

class Verb:
    v = ""
    case = ""
    
#Artikel
articles ={
    "nominative" : {"m" : "der", "f": "die", "n": "das"},
    "genitive" : {"m": "des", "f": "der", "n": "des"},
    "dative" : {"m": "dem", "f": "der", "n": "dem"},
    "accusative" : {"m": "den", "f": "die", "n": "das"}
    }

#Adjektiv Enden
ends ={
    "nominative" : {"m": "e", "f": "e", "n": "e"},
    "genitive" : {"m": "en", "f": "en", "n": "en"},
    "dative" : {"m": "en", "f": "en", "n": "en"},
    "accusative" : {"m": "en", "f": "e", "n": "e"}
    }

#Zeilen in Dateien zählen
with open("Daten/noun.csv", "r") as z:
    zeilen_noun = sum(1 for line in z)
with open("Daten/verb.csv", "r") as z:
    zeilen_verb = sum(1 for line in z)
with open("Daten/modifier.csv", "r") as z:
    zeilen_modifier = sum(1 for line in z)
with open("Daten/adjective.csv", "r") as z:
    zeilen_adjective = sum(1 for line in z )


#gibt ein Objekt der Klasse Noun zurück.
#Der Inhalt ist random aus der datei noun.csv
def get_noun():
    with codecs.open("Daten/noun.csv", "r","utf-8") as dat_noun:
        zeile = ""
        noun = Noun()
        
        ri = random.randint(1,zeilen_noun)
        i = 1
        for line in dat_noun:
            if i == ri:
                zeile = line.rstrip()
            i = i+1
        noun.nominative, noun.genitiv, noun.gender = zeile.split(';')
        return noun

#gibt ein Objekt der Klasse Verb zurück.
#Der Inhalt ist random aus der datei verb.csv
def get_verb():
    with codecs.open("Daten/verb.csv", "r","utf-8") as dat_verb:
        zeile = ""
        verb = Verb()
        
        ri = random.randint(1,zeilen_verb)
        i = 1
        for line in dat_verb:
            if i == ri:
                zeile = line.rstrip()
            i = i+1
        verb.v, verb.case = zeile.split(';')
        return verb

#gibt random einen Modifier aus modifier.csv zurück
def get_mod():
    with codecs.open("Daten/modifier.csv", "r","utf-8") as dat_modifier:
        ri = random.randint(1,zeilen_modifier)
        i = 1
        for line in dat_modifier:
            if i == ri:
                return(line.rstrip())
            i = i+1

#gibt random ein Adjektiv aus adjective.csv zurück
def get_adj():
    with codecs.open("Daten/adjective.csv", "r","utf-8") as dat_adjective:
        ri = random.randint(1,zeilen_adjective)
        i = 1
        for line in dat_adjective:
            if i == ri:
                return(line.rstrip())
            i = i+1
        
#Gibt Geschwurbel zurück
def schwurbo():
    woo = ""
    
    #Drei verschiedene Nomen bekommen
    noun0 = noun1 = noun2 = get_noun()
    while noun0.nominative == noun1.nominative:
        noun1 = get_noun()

    while noun0.nominative == noun2.nominative or noun1.nominative == noun2.nominative:
        noun2 = get_noun()
    
    #Drei verschiedene modifier bekommen
    mod0 = mod1 = mod2 = get_mod()
    while mod0 == mod1:
        mod1 = get_mod()
        
    while mod2 == mod0 or mod2 == mod1:
        mod2 = get_mod()
        
    
    #Drei verschiedene adjektive bekommen
    adj0 = adj1 = adj2 = get_adj()
    while adj0 == adj1:
        adj1 = get_adj()
        
    while adj0 == adj2 or adj1 == adj2:
        adj2 = get_adj()

    #Verb bekommen
    verb = get_verb()

    #Setzte das Geschwurbel zusammen
    woo += articles["nominative"][noun0.gender].capitalize() + " "
    woo += adj0
    woo += ends["nominative"][noun0.gender] + " "
    woo += mod0
    woo += noun0.nominative + " "
    woo += verb.v + " "
    woo += articles[verb.case][noun1.gender] + " "
    woo += adj1
    woo += ends[verb.case][noun1.gender] + " "
    woo += mod1
    if verb.case == "genitive":
        woo += noun1.genitive + " "
    else:
        woo += noun1.nominative + " "
    woo += articles["genitive"][noun2.gender] + " "
    woo +=  adj2
    woo += ends["genitive"][noun2.gender] + " "
    woo += mod2
    woo += noun2.genitiv + "."
    

    return(woo)


#twittert geschwurbel
def tweet():    
    schwurbeltweet = schwurbo() + "\n" + "#dailyschwurbel #Schwurbel #Geschwurbel #Eso #Spinner #Schwurbomat\n" + get_random_hashtags()
    api.PostUpdate(schwurbeltweet)
    #debug
    print(schwurbeltweet)

#Zum testen
def tweettest():
    schwurbeltweet = schwurbo() + "\n" + "#dailyschwurbel #Schwurbel #Geschwurbel #Eso #Spinner #Schwurbomat\n" + get_random_hashtags()
    print(schwurbeltweet)

