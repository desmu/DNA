import csv#bibliothèque pour l'édition de documents csv
from sys import argv#bibliothèque de gestion d'arguments en ligne de commande
import time#pour avoir le temps de voir défiler les infos

arr = []#on initialise le tableau qui va stocker le nombre concécutif maximal de chaque nucléotide pour la séquence argv[2] entrée

db = open(argv[1],"r")
data = list(csv.reader(db))#ouverture de la base de donnée et stockage dans un tableau à 2 dimensions découpé au niveau des virgules par reader()
x = data[0]#première ligne correspondante aux séquences

s = open(argv[2],"r")
seq = s.read()#ouverture et stockage de la base de donnée de la base de donnée lecture

def look(b,c,j):#fonction qui retourne la position du premier caractère de la prochaine série type de nucléotide recherchée x[i]
    while j <= len(b):#(while car j est mis à jour dans des cas particuliers) on parcours toute la séquence en partant de a (ici j vaut a)
        if b[j] == c[0]:#si le caractère j de la séquence correspond au premier caractère de la série type de nucléotides x[i]
            k = 0#on réintitialise la boucle suivante à 0
            while k <= len(c):#while car j est mis à jour dans des cas particuliers)on parcours la séquence sur la longeure de x[i] pour déterminer si il s'agit bien d'un occurence de la série type x[i]
                if b[j+k] != c[k]:#si le caractère j+k de la série est != du caractère x[i] à la position k
                    j += 1#on passe au caractère suivant dans laboucle j
                    k += len(c)#on quitte k
                elif k == len(c)-1:#si k arrive au dernier caractère de x[i] et que celui-ci est égal à celui de la grande séquence
                    print("Trouvé à position P = ",j)
                    return j#"a" prend la valeur de j dans l'appel de la fonction, j correspondant à la position du premier caractère de l'occurence de x[i] trouvée
                k += 1#on passe au caractère de x[i] suivant
        elif j < (len(b) - len(c)):#début de x[i] non trouvé et position testée inférieure à la longueur de la grande séquence moins celle de la série de nucléotide type x[i]
            j += 1#passer au caractère suivant
        else:#supérieur ou égal à len(séquence) - len(x[i]) et caractère j de séquence != x[i] de 0
            return -1#signifier qu'il n'y a plus d'occurence de x[i]

for i in range(1,len(x)):#on passe une fois dans la boucle pour chaque groupe de nucléotide
    nbm = 0#nombre d'itération consécutive maximale d'une séquence type dans la séquence analysée
    nb = 0#nombre d'itération consécutive d'une séquence type dans la séquence analysée
    prec = 0#indice de la séquence précédente
    a = 0#indice de la position de la boucle dans l'analyse de la grande séquence
    #ici while est chisi car for in range avance de 1 en 1 sans tenir compte des modifications de a dans l'action de la boucle
    #avec for arr retournerait [2,2,2,2,2,2,2,2]
    print("")
    print("")
    print("On recherche plus longue série de : ",x[i])
    print("")
    print("")
    while a <= len(seq):#on scanne toute la séquence à la recherche du nombre maximal consécutif de la séquence type "i" que l'on est entrain de chercher
        a = look(seq,x[i], a)#on retourne la position de l'itération suivante de la séquence type "i" recherchée en partant de "a"
        if a == -1: #retourne -1 si non trouvé/si aucune itération de la séquence cherchée à partir de "a" n'est trouvée
            nb = 0#réinitialisation
            print("FIN recherche de ", x[i])
            break#fin de l'analyse pour la séquence "i"
        else:#itération trouvée aprés "a"
            if ((a - len(x[i])) == prec):#si la séquence type trouvée est consécutive à la précédente
                nb += 1#on ajoute 1 au nombre d'itérations consécutives
                prec = a#on sauvegarde la position de cette trouvaille dans "prec"
                if nbm < nb:#si la chaîne de séquence type consécutives en cours de dénombrement se trouve être plus longue que la suite précédente
                    nbm = nb#nb d'itération est assigné au max à retourner dans le tableau arr
            else:#si la séquence type trouvée n'est pas consécutive à la précédente
                time.sleep(0.2)#on attend pour voir défiler les infos
                print("Série de : ",nb)
                print("")
                print("Nouvelle série commence à : ",a)
                nb = 1#nb repasse à une seule séquence trouvée
                prec = a#nb d'itération est assigné au max à retourner dans le tableau arr
                if nbm < nb:#si la chaîne de séquence type consécutives en cours de dénombrement se trouve être plus longue que la suite précédente
                    nbm = nb
        a += 1#on passe au rang suivant dans la séquence analysée
    arr.append(nbm)#on inserre le nombre de la plus longue chaîne consécutive de la séquence analysée
    print("")
    print("")
    print("plus longue série de ",x[i]," = ", nbm)
    print("")
    print("Signature génétique de ",argv[2]," : ",arr)
    print("")
    print("")
arr = list(map(str, arr))#change le tableau de valeurs int en string pour que celui-ci puisse être comparé aux montants inscrits dans la base de donnée pour chaque personne
i=1
while i < len(data):#pour chaque ligne de la base de données
    if data[i][1:] == arr:#si toute la ligne de valeurs max vaut celle de "arr"
        print("")
        print("")
        print("C'est : ",data[i][0])#c'est lui
        print("")
        print("")
    else:
        print("Ce n'est pas : ",data[i][0])#sinon : ce n'est pas lui
    i+=1#on passe au suspect suivant

