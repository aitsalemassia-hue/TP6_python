
from dataclasses import dataclass, asdict, replace
import json


@dataclass(frozen=True, slots=True)
class Livre:
     titre: str
     auteur: str
     annee: int
     prix: float

    # Convertir le livre en JSON
     def to_json(self):
          return json.dumps(asdict(self), ensure_ascii=False)

     # Créer un nouveau livre avec un prix réduit
     def promo(self, prix_reduit):
          if prix_reduit <= 0 or prix_reduit >= self.prix:
               raise ValueError("Le prix réduit doit être positif et inférieur au prix initial.")

          return replace(self, prix=prix_reduit)

     # Créer un livre à partir d'une chaîne JSON
     @classmethod
     def from_json(cls, chaine_json):
          donnees = json.loads(chaine_json)
          return cls(**donnees)

     # Comparer deux livres selon leur prix
     def __lt__(self, autre):
          if not isinstance(autre, Livre):
               return NotImplemented

          return self.prix < autre.prix



