#Italian Verb Bot
#Taylor Thackaberry (tthacks)
#07.04.2019
#Untested version - if errors in grammar or code are found, please contact
#tthacks@vt.edu. 
#Note: tenses that require adding -gh or -ch are not supported. Request a fork
#if you think of a smart solution, and we will celebrate you with a feast of
#many breakfast cereals.

import random

presentAre = ["o", "i", "a", "iamo", "ate", "ano"]
presentEre = ["o", "i", "e", "iamo", "ete", "ono"]
presentIre = ["o", "i", "e", "iamo", "ite", "ono"]
pastAre = ["avo", "avi", "ava", "avamo", "avate", "avano"]
pastEre = ["evo", "evi", "eva", "evamo", "evate", "evano"]
pastIre = ["ivo", "ivi", "iva", "ivamo", "ivate", "ivano"]
avere = ["ho", "hai", "ha", "abbiamo", "avete", "hanno"]
essere = ["sono", "sai", "sa", "siamo", "siete", "sono"]
essereImpPast = ["ero", "eri", "era", "eravamo", "eravamo", "eravate", "erano"]
futureAreEre = ["ero\'", "erai", "era\'", "eremo", "erete", "eranno"]
futureIre = ["iro\'", "irai", "ira\'", "iremo", "irete", "iranno"]
irregPresBase = ["apire", "apr"]
irregImperfectPastBase = ["fare", "dire", "bere"]
irregFutureDoubleLetterBase = ["bere", "berr", "tenere", "terr", "venire", "verr", "volere", "vorr"]
irregFutureTrunc = ["avere", "avr", "andare", "andr", "potere", "potr", "dovere", "dovr", "vedere", "vedr"]
keepAFuture = ["fare", "far", "stare", "star", "dare", "dar"]

nouns = ["io", "tu", "lui/lei", "noi", "voi", "loro"]
verbBases = ["accompagnare", "apire", "apprezzare", "arrivare", "avere", "ballare", "bere", "cadere", "camminare", "chiudere", "communicare", "consigliare", "dare", "dire", "dovere", "entrare", "entrare", "essere", "fare", "giocare", "guidare", "imparare", "indosare", "insegnare", "lasciare", "leggere", "mangiare", "mettere", "mostare", "nascere", "nuotare", "offrire", "partire", "piacere", "potere", "prendere", "prestare, to lend", "provare, to try", "regalare", "restare", "rimanere", "rispondere", "riuscire", "salire", "scegliere", "scendere", "sciare", "scrivere", "sentire", "spiegare", "stare", "tenere", "tornare", "trovare", "uscire", "vedere", "vendere", "venire", "vivere", "volere"]
verbTenses = ["present", "past imperfect", "future", "past perfect"]
ppEssere = ["andare", "venire", "tornare", "salire", "scendere", "entrare", "uscire", "partire", "arrivare", "cadere", "essere", "stare", "restare", "rimanere", "piacere"]
irregPP = ["prendere", "preso", "leggere", "letto", "vedere", "visto", "mettere", "messo", "fare", "fatto", "rispondere", "risposto", "vivere", "vissuto", "apire", "aperto", "chiudere", "chiuso", "venire", "venuto", "rimanere", "rimasto", "partire", "partiti", "bere", "bevuto", "dire", "detto", "nascere", "nato", "scrivere", "scritto"]

cont = "y"
#Debug Mode: Internal use only. Do not touch. 
#bug = input("WOULD MASTER CARE FOR DEBUGGING MODE, FOR MASTER IS A LOUSY PROGRAMMER?")
#if bug == "y":
#    debugMode = True
#else:
debugMode = False

while(cont == "y"):
    if(not debugMode):
        rand1 = random.randint(0, 2)
        rand2 = random.randint(0, 3)
        rand3 = random.randint(0, 5)
    else:
        requestedVerb = input("verb? Type: ")
        while(requestedVerb not in verbBases):
            requestedVerb = input("not an option. Try again: ")
        rand1 = verbBases.index(requestedVerb)
        rand2 = int(input("tense? 0-3: "))
        rand3 = int(input("subject? 0-5: "))
    
    infinit = verbBases[rand1]
    
    print(nouns[rand3], infinit, "in the", verbTenses[rand2], "tense")
    userInput = input()
    
    #computer does the conjugation
    
    if rand2 == 0: #present tense
        if infinit in irregPresBase:
            base = irregPresBase[irregPresBase.index(infinit) + 1]
        else:
            base = infinit[:-3]
        if infinit[-3] == 'a':
            if infinit[-4] == "i" and (rand3 == 1 or rand3 == 3): #fix for mangiare
                ans = base + presentAre[rand3]
            else:
                ans = base + presentAre[rand3]
        elif(infinit[-3] == 'e'):
            ans = base + presentEre[rand3]
        else:
            ans = base + presentIre[rand3]
    elif(rand2 == 1): #past imperfect
        if infinit == "essere":
            ans = essereImpPast[rand3]
        elif infinit in irregImperfectPastBase: #fare, dire, bere
            ans = infinit + pastEre[rand3]
        elif(infinit[-3] == 'a'):
            ans = infinit[:-3] + pastAre[rand3]
        elif(infinit[-3] == 'e'):
            ans = infinit[:-3] + pastEre[rand3]
        else:
            ans = infinit[:-3] + pastIre[rand3]
    elif rand2 == 2: #future
        if infinit == "essere":
            ans = "sar" + futureAreEre[rand3]
        elif infinit in keepAFuture:
            ans = keepAFuture[keepAFuture.index(infinit) + 1] + futureAreEre[rand3]
        elif infinit in irregFutureDoubleLetterBase:
            ans = irregFutureDoubleLetterBase[irregFutureDoubleLetterBase.index(infinit) + 1] + futureAreEre[rand3]
        elif infinit in irregFutureTrunc:
            ans = irregFutureTrunc[irregFutureTrunc.index(infinit) + 1] + futureAreEre[rand3]
        elif(infinit[-3] == 'a' or infinit[-3] == 'e'):
            ans = infinit[:-3] + futureAreEre[rand3]
        else:
            ans = infinit[:-3] + futureIre[rand3]
    else: #passato prossimo
        if infinit in irregPP:
            pp = irregPP[irregPP.index(infinit) + 1]
        else:
            pp = infinit[:-2] + "to"
        if infinit in ppEssere:
            av = essere[rand3]
        else:
            av = avere[rand3]
        ans = av + " " + pp
    
    
    print("You said", userInput)
    print("Valentina said", ans)
    if userInput == ans:
        print("Va bene!")
    else:
        print("L'americano stupido!")
    
    cont = input("Conjugate another? y/n: ")


        
        
    