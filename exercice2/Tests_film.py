
import unittest
from Film import Film


class TestFilm(unittest.TestCase):

     def setUp(self):
          
          self.film = Film("Le Parrain", "Francis Ford ", 1972, 9.2)

     # Test 1 : création d'un film
     def test_creation(self):
          self.assertEqual(self.film.titre, "Le Parrain")
          self.assertEqual(self.film.note, 9.2)

     # Test 2 : film classique
     def test_est_classique(self):
          self.assertTrue(self.film.est_classique())

     # Test 3 : film récent
     def test_film_recent(self):
          film = Film("Inception", "Christopher Nolan", 2010, 8.8)
          self.assertFalse(film.est_classique())

     # Test 4 : immutabilité
     def test_immutabilite(self):
          with self.assertRaises(AttributeError):
               self.film.note = 5.0

     # Test 5 : note négative
     def test_note_negative(self):
          with self.assertRaises(ValueError):
               Film("Film", "Auteur", 2000, -2)

     # Test 6 : note supérieure à 10
     def test_note_superieure(self):
          with self.assertRaises(ValueError):
               Film("Film", "Auteur", 2000, 12)

     # Test 7 : année invalide
     def test_annee_invalide(self):
          with self.assertRaises(TypeError):
               Film("Film", "Auteur", "2000", 8.0)

     # Test 8 : note non numérique
     def test_note_invalide(self):
          with self.assertRaises(TypeError):
               Film("Film", "Auteur", 2000, "Excellent")

     # Test 9 : titre vide
     def test_titre_vide(self):
          with self.assertRaises(ValueError):
               Film("", "Auteur", 2000, 8.0)

     # Test 10 : conversion JSON
     def test_json(self):
          chaine = self.film.to_json()
          film2 = Film.from_json(chaine)

          self.assertEqual(self.film, film2)

     # Test 11 : comparaison
     def test_comparaison(self):
          film2 = Film("Titanic", "James Cameron", 1997, 7.8)

          self.assertTrue(film2 < self.film)


if __name__ == "__main__":
    unittest.main()
