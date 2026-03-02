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
# ── PARTIE 2 : Validation ───────────────────────────────────

# Test 1 : account_id n'est pas un int → erreur
try:
    u = User(name='Ali', email='ali@gmail.com', account_id='hello')
except Exception as e:
    print("❌ Erreur type account_id :", e)

# Test 2 : email invalide → erreur
try:
    u = User(name='Ali', email='ali', account_id=1234)
except Exception as e:
    print("❌ Erreur email invalide :", e)