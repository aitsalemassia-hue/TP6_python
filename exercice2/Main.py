
from Film import Film


if __name__ == "__main__":

     film1 = Film("Le Seigneur des anneaux", "Peter Jackson", 2001, 8.9)

     film2 = Film("Interstellar", "Christopher Nolan", 2014, 8.7)

     film3 = Film("Inception", "Christopher Nolan", 2010, 8.8)

     # Affichage JSON
     print("Film en JSON :")
     print(film1.to_json())

     # Vérification classique
     print("\nEst-ce un classique ?")
     print(film1.est_classique())

     # Chargement JSON
     print("\nChargement JSON :")
     film_restaure = Film.from_json(film1.to_json())
     print(film_restaure)

     # Comparaison
     print("\nComparaison des notes :")
     print(film1 < film2)

     # Tri des films
     print("\nFilms triés par note croissante :")

     films = [film1, film2, film3]

     for film in sorted(films):
          print(film.titre, "-", film.note)