from pydantic import BaseModel, EmailStr, field_validator
from dataclasses import dataclass

# ── PARTIE 1 & 3 : Modèle avec validation custom ────────────
class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int

    @field_validator("account_id")
    def validate_account_id(cls, value):
        if value <= 0:
            raise ValueError(f"account_id must be positive: {value}")
        return value

# ── PARTIE 2 : Tests de validation ──────────────────────────
try:
    u = User(name='Ali', email='ali@gmail.com', account_id='hello')
except Exception as e:
    print("❌ Erreur type account_id :", e)

try:
    u = User(name='Ali', email='ali', account_id=1234)
except Exception as e:
    print("❌ Erreur email invalide :", e)

# Test account_id négatif
try:
    u = User(name='Ali', email='ali@gmail.com', account_id=-12)
except Exception as e:
    print("❌ Erreur account_id négatif :", e)
# ── PARTIE 4 : JSON Serialization ───────────────────────────
user_valid = User(name="Ali", email="ali@gmail.com", account_id=1234)

# Convertir en JSON string
user_json_str = user_valid.model_dump_json()
print("📄 JSON string :", user_json_str)

# Convertir en dictionnaire Python
user_dict = user_valid.model_dump()
print("📦 Dictionnaire :", user_dict)