from pydantic import BaseModel

# On définit un modèle "User" avec 3 champs typés
class User(BaseModel):
    name: str          # doit être du texte
    email: str         # doit être du texte
    account_id: int    # doit être un nombre entier

# On crée un utilisateur valide
user = User(
    name="Salah",
    email="salah@gmail.com",
    account_id=12345
)

print(user.name)        # Salah
print(user.email)       # salah@gmail.com
print(user.account_id)  # 12345
# Créer un utilisateur depuis un dictionnaire
user_data = {
    'name': 'Salah',
    'email': 'salah@gmail.com',
    'account_id': 12345
}
user2 = User(**user_data)
print(user2)