__auteur__ = "François Gauthier-Drouin"
__NI__ = "111075877"
__date__ = "2020-05-31"

# On importe la fonction integrate de la librairie scipy pour intégrer la fonction f(x).
import scipy.integrate as integrale


def trouver_A(n):
    """Détermine la valeur de A de manière itérative en additionnant les valeurs de ar pour chaque itération.

       Args:
        n (int) : le nombre de rectangles utilisés pour calculer l'aire sous la courbe de façon approximative.

       Returns:
         float : Valeur calculée de A (aire sous la courbe).
    """

    A = 0  # Soit A l'aire du rectangle
    L = 1 / n  # Étape 5a / Soit L la largeur de chaque rectangle et n le nombre de rectangles
    for i in range(0, n):  # Étape 5bi
        xg = i * L # Soit xg la limite gauche du rectangle
        xd = i * L + L # Soit xd la limite droite du rectangle
        yg = xg ** 3 + 1  # Étape 5bii / Soit yg la hauteur à gauche du rectangle
        yd = xd ** 3 + 1 # Soit yd la hauteur à droite du rectangle
        h = (yg + yd) / 2 # Soit h la hauteur du rectangle
        ar = h * L  # Étape 5biii / Soit ar l'aire du rectangle pour une itération donnée de i
        A += ar
    print("A (méthode itérative) = " + str(A))  # Étape 5c


f = lambda x: (x ** 3 + 1)

"""Calcule l'intégrale de la fonction f(x) = x ** 3 + 1.

    Args:
    x (int) : variable représentant la coordonnée horizontale sur la courbe f(x)

    """


def verifier_extremes():
    """Vérifie la validité du nombre n saisi et calcule l'aire sous la courbe de manière itérative et analytique si
       le nombre n est valide.

    """

    # On définit d'abord la valeur de n.
    n = int(input("Entrez un nombre (0 pour quitter) : "))  # Étape 1

    # On valide que n est différent de 0. Si ce n'est pas le cas, le programme est arrêté.
    while n != 0:  # Étape 4

        # On valide que n est supérieur à 0. Si ce n'est pas le cas, on obtient un message d'erreur et on recommence.
        if n > 0:  # Étape 2

            # On valide que n est inférieur ou égal à 10000. Si ce n'est pas le cas, on obtient un message d'erreur et
            # on recommence.
            if n < 10001:  # Étape 3

                # Si toutes les conditions sont respectées, on calcule A avec les deux méthodes précédemment spécifiées.
                trouver_A(n)
                A_analytique = integrale.quad(f, 0, 1)[0]
                print("A (méthode analytique) = " + str(A_analytique))
            else:
                print(
                    "Le nombre {} est supérieur à 10 000. Veuillez entrer un nombre positif inférieur ou égal à 10 000."
                    .format(n))
        else:
            print("Le nombre {} est négatif. Veuillez entrer un nombre positif inférieur ou égal à 10 000.".format(n))

        # On demande à nouveau à l'utilisateur, puis la condition de la boucle décidera si on continue ou non.
        n = int(input("\nEntrez un nombre (0 pour quitter) : "))


# On appelle la fonction verifier_extremes() qui exécute le code ci-dessus.
verifier_extremes()

