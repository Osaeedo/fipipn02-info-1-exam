from argparse import ArgumentError, ArgumentTypeError
from enum import Enum

class TailleType(Enum):
    small = 0
    Medium = 0.5
    Large = 1

class Taille():
    _type = TailleType.small

    def __init__(self, type):
        self._type = type

    @property
    def type(self):
        return self._type

class Boissoin():
    _nom = ""
    _ingrédients  = ""
    _prix = int

    def __init__(self, nom, ingrédients, prix):
        self._nom = nom
        self._ingrédients = ingrédients
        self._prix = prix

    @property
    def nom(self):
        return self._nom

    @property
    def ingrédients(self):
        return self._ingrédients

    @property
    def prix(self):
        return self._prix


class Barmaid():
    _MenusBoissoin = list()
    _BoissoinSelectionnee = None
    _BoissoinChoisie  = list()
    _estPayee = False
    _estValidee = False

    @property
    def addition(self):
        total = 0
        for Taille in self._BoissoinChoisie:
            if Taille.type == TailleType.small:
                total += 0
            elif Taille.type == TailleType.Medium:
                total += 0.5
            elif Taille.type == TailleType.Large:
                total += 1
            else:
                raise ArgumentTypeError("TypeBillet unknown!")

        return total


    @property
    def estValide(self):
        return self._BoissoinSelectionnee!= None and len(self._BoissoinChoisie) > 0

    @property
    def estPayee(self):
        return self._estPayee

    @property
    def estValidee(self):
        return self._estValidee

    def __init__(self, listeBoissoin):
        if isinstance(listeBoissoin, list):
            if not all(isinstance(elem, Boissoin) for elem in listeBoissoin):
                raise ArgumentTypeError("must be a list of Boissoin!")
        else:
            raise ArgumentTypeError("must be a list!")

        self._MenusBoissoin = listeBoissoin

    def consulterMenu(self):
        return self._MenusBoissoin

    def SelectionnerMenu(self, boissoin):
        if not isinstance(boissoin, Boissoin):
            raise ArgumentTypeError("boissoin must be a Boissoin!")


        self._BoissoinSelectionnee = (boissoin)
        return True

    def SelectionnerTaille(self, type):
        if isinstance(type, list):
            if not all(isinstance(elem, type) for elem in type):
                raise ArgumentTypeError("must be a list of type!")
        else:
            raise ArgumentTypeError("must be a list!")

        self._BoissoinChoisie = type
        return True

    def valider(self):
        if self.estValide:
            self._estValidee = True
        else:
            self._estValidee = False
        return self._estValidee


    def payer(self, somme):
        if not self.estValidee:
            raise BaseException("command must be confirmed!")

        reste = somme - self.addition
        if reste < 0:
            self._estPayee = False
        else:
            self._estPayee = True
        return (self._estPayee, reste)



if __name__ == '__main__':
    initSeance = [
        Boissoin("1 The Bosst"," : 1/2 Mango , 2 Orange, 1u of guajana", ", prix = "+str(5)+"$"),
        Boissoin("2 The Fresh"," : 3 Apples, 1u of ginger, 1 Lemon", ", prix = "+str(4)+"$"),
        Boissoin("3 The Fusion",": 1 Guava, 1/4 pineapple, 1/2 banana", ", prix = "+str(5)+"$"),
        Boissoin("4 The Detox"," : 3 Carrots, 1 Celery Stick, 1 Beetroot", ", prix = "+str(3.5)+"$")
    ]
    # init barmaid
    barmaid = Barmaid(initSeance)
    print("barmaid initialisee!")

    # consultation
    menus = barmaid.consulterMenu()
    print("consultation séances:")
    for boissoin in menus:
        print(boissoin.nom,boissoin.ingrédients,boissoin.prix)

    # selection boissoin
    # osama
    boissoin = menus.pop(0)
    selectionnee = barmaid.SelectionnerMenu(boissoin)
    print("boissoin selectionne ? %s" % selectionnee)

    # selection Taille
    # osama
    type = list()
    type.append(Taille(TailleType.small))
    type.append(Taille(TailleType.Medium))
    typeSelectionne = barmaid.SelectionnerTaille(type)
    print("type(s) selectionne(s) ? %s" % typeSelectionne)

    # validation
    # osama
    estValidee = barmaid.valider()
    print("commande validee ? %s" % estValidee)

    # payer
    # osama
    (estPayee, reste) = barmaid.payer(26)
    print("commande payee (%d euros) ? %s" % (reste, estPayee))

    # choix=input("veuillez choisir votre boissoin  ")
    # taille = input("veuillez choisir la taille boissoin  S, M, L")
    #
    # if choix == 1 and taille=="S":
    #     print("vous venez de choisir la boissoin : The Bosst")
    # if choix == 2 :
    #     print("vous venez de choisir la boissoin : The Fresh")
    # if choix == 3 :
    #     print("vous venez de choisir la boissoin : The Fusion")
    # if choix == 4 :
    #     print("vous venez de choisir la boissoin : The Detox")
    # taille=input("veuillez choisir la taille boissoin  S, M, L")
    #
    # if taille == 1 :
    #     print("vous venez de choisir la boissoin : The Bosst")
    # if taille == 2 :
    #     print("vous venez de choisir la boissoin : The Fresh")
    # if choix == 3 :
    #     print("vous venez de choisir la boissoin : The Fusion")
    # if choix == 4 :
    #     print("vous venez de choisir la boissoin : The Detox")



