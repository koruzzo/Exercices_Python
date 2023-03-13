import math #Bibliothèque pour utilsation sqrt
import json
import random

#from geometry1 import *
#from geometry2 import *

# Plan TD
#

#####################################################################################
#################  Exercice 1 : entrée/sortie (input/output) ########################
#####################################################################################

def affichage(r):
    print(f"le rayon du disque est {r}")
    p=2*math.pi*r
    print(f"le disque de rayon {r} a comme perimètre: {p:.2f}")
    a=math.pi*r*r
    print(f"L'aire du cercle de rayon {r} est {math.pi*r*r} mais avec 3 chiffres après la virgule {math.pi*r*r:.3f}")


def saisieEntier():
    text=input("Entrer un entier  x= ")   
    print(f"la longueur de la chaine de caractères text est {len(text)}")
    x=int(text)
    return x
    #cette fonction est assez ridicule... on pourrait écrire simplement x=int(input("blablabla x="))

def saisieDecimal():
    text=input("Entrer un nombre décimal, de préférence à virgule y= ")
    x=float(text)
    #à noter qu'on peut prendre la partie entière de x en faisant (cette fonction coupe les chiffres après la virgule)
    entier=int(x)
    print(f"On a saisi le nombre décimal {x} et sa partie entière est {entier}")
    return x

def exercice1():
    print("start exercice1")
    rayon=saisieEntier() 
    affichage(rayon) 
    rayon=saisieDecimal() 
    affichage(rayon)                      
    print("end exercice1")
    
#exercice1()





    
##########################################################################################
#################  Exercice 2 : les chaines de caractère (string) ########################   
##########################################################################################
    
# 3) on va créer une nouvelle chaine... en ajoutant au début et à la fin les valeurs de variables...
# 4) D'après vous que va afficher print(autretexte) en fonction de la ligne saisie au clavier ? faites l'essai pour vérifier que vous avez compris...

def exercice2():
    print("start exercice2")
    #s est une chaine de caractères... qu'on saisit au clavier:
    s=input("saisir une chaine de caractères (mot ou texte d'au moins 4 caractères...):")
    print(f"la longueur de la chaine {s} qu'on manipule est {len(s)}")
    
    print(f"le premier caractère de s est {s[0]}")
    print(f"le second caractère de s est {s[1]}")
    print(f"le troisième caractère de s est {s[2]}")
    print(f"le quatrième caractère de s est {s[3]}")
       
    x=5
    y=6.2
    z=19
    nouveautexte=f"{x}-bla {y} bla {z}"
    print(f"le nouveau texte est : {nouveautexte}")
    autretexte=f"{x}_{s}-truc-{y}"
    print(autretexte)
    print("end exercice2")
    
#exercice2()


##############################################################################
#################  Exercice 3 : chaines de caractères ########################
##############################################################################

#  afficher à l'écran quelque chose qui ressemble à:
    # (0,0) (0,1) (0,2) (0,3)    (0,9)
    # (1,0) (1,1) (1,2) (1,3)    (1,9)
    # ...
    # (9,0) (9,1) (9,2) (9,3)    (9,9)

def exercice3():
    print("start exercice3")
    #remarquez bien que les indices vont de 0 à 9
    for i in range (0,10):
        s=f"({i},0)"
        for j in range (1,10):
            s=f"{s} ({i},{j})"
        print(s)
    print("end exercice3")
    
#exercice3()

    
#################################################################################
#################  Exercice 4 : écriture dans un fichier ########################
#################################################################################

def exercice4():
    print("start exercice4")
    entier=input("entrer un entier de 1 à 1000 ->  n=")
    trucmuche=70000
    filename=f"nombres_{entier}.txt"
    print(f"mon nom de fichier est {filename}")
    file = open(filename, "w")
    n=int(entier) #à vérifier: on voudrait que n soit la valeur de "entier" et pour l'instant , "entier" est la chaîne de caractères entrée au clavier (piège classique)
    for i in range(0,n+1):
        file.write(f"{i}\n")
    #A la fin, il ne faut pas oublier de fermer le fichier
    file.close()
    print("end exercice4")
    
#exercice4()

#####################################################################################
#################  Exercice 5 : test "if" et boucle "while"  ########################    
#####################################################################################

def multipleDe13(x):
    reste=x%13
    if reste==0:
        return 1
    return 0

def exercice5():
    print("start exercice5")
    x=int(input("entrer un entier non nul:"))
    while (multipleDe13(x)==0):
        if multipleDe13(x)==1:
            print(f"Le nombre {x} est divisible par 13")
        else:
            print(f"Le nombre {x} n'est pas divisible par 13")
        x=int(input("entrer un multiple de 13 pour sortir:"))
    print("end exercice5")

#exercice5()

   
#################################################################################
#################  Exercice 6 : boucle "for" et comptage ########################    
#################################################################################

def distance(x,y,z):
    return math.sqrt(x*x+y*y+z*z)

def enumerate(R):
    Rentier=int(R)
    count=0
    for x in range(-Rentier,Rentier+1):
        for y in range(-Rentier,Rentier+1):
            for z in range(-Rentier,Rentier+1):
                if distance(x,y,z)<=R:
                    print(f"({x},{y},{z})")
                    count=count+1
    
    return count

def exercice6():
    print("end exercice6")
    R=float(input("On va énumérer les points à coordonnées entières à un rayon R de l'origine. Entrer R (0 pour sortir):"))
    while (R!=0):
        count=enumerate(R)
        print(f"Il y a {count} points entiers à distance <={R} de l'origine")
        R=float(input("On va énumérer les points à coordonnées entières à un rayon R de l'origine. Entrer R (0 pour sortir):"))
    print("end exercice6")
    
#exercice6()

###################################################################
#################  Exercice 7 : les listes ########################    
###################################################################

def distanceToOrigin(P):
    return math.sqrt(P[0]*P[0]+P[1]*P[1]+P[2]*P[2])

def ball(R):
    S=[]
    r=int(R)
    for x in range(-r,r+1):
        for y in range (-r,r+1):
            for z in range (-r,r+1):
                P=(x,y,z)
                if distanceToOrigin(P)<=R:
                    S.append(P)
    S.sort(key=distanceToOrigin, reverse=True) 
    return S

def maximizeCoordinatesSum(S):
    P=S[0]
    maxi=P[0]+P[1]+P[2] #On initialise la valeur maximale toujours avec le premier point de la liste
    Pmaxi=S[0] #On initialise le point qui donne le maximum avec le premier point de la liste
    for Q in S:  #Le point Q parcourt tous les éléments de la liste de points S
        if Q[0]+Q[1]+Q[2]>maxi: #Là, ces trois lignes, c'est pas bon du tout, mais tout n'est peut-être pas à jeter... A vous de voir
            maxi=Q[0]+Q[1]+Q[2]
            Pmaxi=Q
    return Pmaxi 

def exercice7():
    print("end exercice7")
    R=float(input("On crée la liste des points à coordonnées entières à un rayon <=R de l'origine. Entrer R (0 pour sortir):"))
    while (R!=0):
        S=ball(R)
        print(f"Il y a {len(S)} points entiers à distance <={R} de l'origine:")
        print(S)
        if len(S)>0:
            P=maximizeCoordinatesSum(S)
            print("Dans le 4), votre fonction maximizeCoordinatesSum fournit comme point entier de la boule qui a la plus grande somme de coordonnées :")
            print(P)
            print("On peut aussi calculer un minimum ou un maximum d'une liste en une ligne -de la même façon que l'on trie. Cela donne le point (vérifiez que votre résultat est correct):")
            Q=max(S,key=lambda p:p[0]+p[1]+p[2])
            print(Q)
        R=float(input("On crée la liste des points à coordonnées entières à un rayon <=R de l'origine. Entrer R (0 pour sortir):"))
    print("end exercice7")


#exercice7()


##############################################################################
#################  Exercice 8 : for, range et listes  ########################    
##############################################################################

def combinaison3Lettres(alphabet):
    combinaisons=[]
    for lettre1 in alphabet:
        for lettre2 in alphabet:
            for lettre3 in alphabet:
                mot=f"{lettre1}{lettre2}{lettre3}"
                combinaisons.append(mot)
    print(f"la fonction combinaison3Lettres a créé une liste de {len(combinaisons)} mots")
    return combinaisons

# 2) On écrit une fonction qui supprimme tous les mots qui ont un "a" en seconde
#    position ou un "c" en troisième position.
#    et qui supprime aussi les mots qui qui ont un "a" en première position et
#    un "e" en troisième position"
#    Le "et" et le "ou" logique s'écrivent simplement "and" et "or"

def supprimeMots(listeDeMots):
    listeDesMotsAsupprimmer=[]
    for mot in listeDeMots:         
        if mot[1]=="a" or mot[2]=="c":
            listeDesMotsAsupprimmer.append(mot)
        else:
            if mot[0]=="a" and mot[2]=="e":
                listeDesMotsAsupprimmer.append(mot)
    print(f"liste des mots à supprimmer a comme longueur {len(listeDesMotsAsupprimmer)}")
    print(listeDesMotsAsupprimmer)
    for mot in listeDesMotsAsupprimmer:
        listeDeMots.remove(mot)
        
 
# 3) On veut afficher les 10 premiers mots de la liste!
#    Plusieurs façons de faire sont possibles.
#    On explore les différentes options pour "range"...
#    Corriger la fonction "supprimeMots" pour qu'elle affiche
#    les 10 premiers mots, ni plus ni moins,
#    avec trois utilisations différentes de range!


def afficheLes10premiersMotsDeLaListe(listeDeMots):
    print("première façon d'afficher les 10 premiers mots")
    for i in range(10): 
        print(listeDeMots[i])
    print("seconde façon de faire")
    for i in range(0,10):
        print(listeDeMots[i])
    print("troisième façon de faire")
    for i in range(0,10,1): 
        print(listeDeMots[i])

def exercice8():
    print("end exercice8")
    alphabet=["a","b","c","d","e"]
    listeDeMots=combinaison3Lettres(alphabet)
    print(listeDeMots)
    print(f"Avant suppression, la liste a {len(listeDeMots)} mots")
    supprimeMots(listeDeMots)
    print(f"Après suppression, il reste {len(listeDeMots)} mots")
    afficheLes10premiersMotsDeLaListe(listeDeMots)
    print("end exercice8")
    
#exercice8()

#####################################################################################
#################  Exercice 9 : retourner plusieurs valeurs  ########################    
#####################################################################################

# Modifiez la fonction débile pour qu'elle retourne les puissances du nombre a
# (a au carré, a au cube,
# a à la puissance 4, a à la puissance 5

def fonctionDebile(a):
    return a,a*a,a*a*a,a*a*a*a,a*a*a*a*a


def exercice9():
    #On peut récupérer les résultats de la fonction débile de façon indépendante,
    # avec des variables
    u,v,w,x,y=fonctionDebile(5)
    print(f"u={u}, v={v}, w={w}, x={x}, y={y}")

    #Ou bien, on peut récupérer le résultat de la fonction débile dans une liste...
    h=fonctionDebile(6)
    print(h)
    print(h[2])
    
#exercice9()
    








############################################################################################
############################################################################################
####################################  exercices ############################################
############################################################################################
############################################################################################

def norm(v):
    return math.sqrt(v[0]*v[0]+v[1]*v[1])

def distance(a,b):
    return math.sqrt((b[0]-a[0])*(b[0]-a[0])+(b[1]-a[1])*(b[1]-a[1]))

#------------------------------ début partie à modifier -----------------------------------

#Calculer le produit scalaire des vecteurs u et v
def dotprod(u,v):
    return u[0]*v[0]+u[1]*v[1]


#Calculer l’angle (non orienté, donc angle entre 0 et π entre les deux vecteurs du plan u et v)
def angle(u,v):
    nu=norm(u)
    nv=norm(v)
    if nu==0 or nv==0:
        return 0
    d=dotprod(u,v)
    q=d/(nu*nv)
    if q<-1:
        return math.pi
    if q>1:
        return 0
    return math.acos(dotprod(u,v)/(norm(u)*norm(v)))


# Déterminant des vecteurs u et v :
def det(u,v):
    # Ux*Vy-Uy*Vx
    return u[0]*v[1]-u[1]*v[0]


# Angle entre les vecteurs AB et CB
def angleTriangle(A,B,C):
    AB=[B[0]-A[0],B[1]-A[1]]
    CB=[B[0]-C[0],B[1]-C[1]]
    return angle(AB,CB)


# Aire du triangle de sommets A,B,C
def area(A,B,C):
    AB=(B[0]-A[0],B[1]-A[1])
    AC=(C[0]-A[0],C[1]-A[1])
    return det(AB,AC)/2


# Fonction qui retourne 1 si C est dans le segment [AB] et 0 sinon...
def insegment(A,B,C):
    if C[0]==A[0] and C[1]==A[1]:
        return 1
    if C[0]==B[0] and C[1]==B[1]:
        return 1
    if area(A,B,C)!=0:
        #C n'est pas sur le segment [AB]
        return 0
    if angleTriangle(A,C,B)>0.999*math.pi:
        return 1
    return 0


def testIntersect():
    print("exercice 2: testIntersect")
    for r in range(20):
        #on tire 4 points de façon aléatoire dans une petite grille
        A=[random.randint(0,2),random.randint(0,2)]
        B=[random.randint(0,2),random.randint(0,2)]
        C=[random.randint(0,2),random.randint(0,2)]
        D=[random.randint(0,2),random.randint(0,2)]
    
        print(f"Premier segment AB: ({A[0]},{A[1]})->({B[0]},{B[1]})")
        print(f"Second segment CD: ({C[0]},{C[1]})->({D[0]},{D[1]})")
        print("se coupent-ils ?")
        if intersect(A,B,C,D)==1:
            print("OUI")
        else:
            print("NON")
            
#testIntersect()



# Fonction qui retourne 1 si P est dans le triangle et 0 sinon...
def inTriangle(A,B,C,P):
    if area(A,B,C)==0:#triangle dégénéré
        if insegment(A,B,P)==1:
            return 1
        if insegment(A,C,P)==1:
            return 1
        if insegment(B,C,P)==1:
            return 1
        return 0
    #On teste si P et C sont du même côté de (AB) (ont la même orientation)
    if area(A,B,C)*area(A,B,P)<0:
        return 0
    #On teste si P et B sont du même côté de (AC) (ont la même orientation)
    if area(A,C,B)*area(A,C,P)<0:
        return 0
    #On teste si P et A sont du même côté de (BC) (ont la même orientation)
    if area(B,C,A)*area(B,C,P)<0:
        return 0
    return 1   

      
def testInTriangle():
    print("exercice 2: testInTriangle")
    #D'abord une série de tests aléatoires
    print("tests aléatoires")
    for r in range(20):
        #on tire 4 points de façon aléatoire dans une petite grille
        A=[random.randint(0,2),random.randint(0,2)]
        B=[random.randint(0,2),random.randint(0,2)]
        C=[random.randint(0,2),random.randint(0,2)]
        P=[random.randint(0,2),random.randint(0,2)]
    
        print(f"A({A[0]},{A[1]}) , B({B[0]},{B[1]}), C({C[0]},{C[1]})")
        print(f"P({P[0]},{P[1]}) est-il dans ABC ?")
        if inTriangle(A,B,C,P)==1:
            print("OUI")
        else:
            print("NON")

#testInTriangle()
