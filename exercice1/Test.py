from Livre import Livre
# Fonction principale de test
if __name__ == "__main__":

     livre1 = Livre("Al-Ayyam", "Taha Hussein", 1929, 9.90)

     livre2 = Livre("Saison de la migration vers le Nord", "Tayeb Salih", 1966, 12.50)

     livre3 = Livre("Des hommes dans le soleil", "Ghassan Kanafani", 1963, 8.50)

     #  Affichage JSON
     print("JSON :")
     print(livre1.to_json())

     #  Tester l'immutabilité
     print("\nTest immutabilité :")
     try:
          livre1.prix = 15.0
     except AttributeError as e:
          print("Modification impossible :", e)

     # Tester la promotion
     print("\nPromotion :")
     nouveau_livre = livre1.promo(7.90)

     print("Ancien prix :", livre1.prix)
     print("Nouveau prix :", nouveau_livre.prix)

     #  Chargement depuis JSON
     print("\nChargement JSON :")
     livre_restaure = Livre.from_json(livre1.to_json())
     print(livre_restaure)

     #  Comparaison des livres
     print("\nComparaison :")
     print("Livre 1 moins cher que livre 2 :", livre1 < livre2)

     #  Trier les livres selon leur prix
     print("\nLivres triés par prix croissant :")
     livres = [livre1, livre2, livre3]

     for livre in sorted(livres):
          print(livre.titre, "-", livre.prix, "DH")