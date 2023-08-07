from datetime import datetime, timedelta
from jose import jwt
from settings import JWT_EXPIRE_TIME, SECRET_KEY, ALGORITHM
import random


def generate_nickname():
    words = ["Lion", "Star", "Fire", "Ice", "Shadow", "Storm", "Dream", "Silver", "Ruby", "Crimson",
             "Phoenix", "Dragon", "Whisper", "Midnight", "Mystic", "Aurora", "Willow", "Velvet",
             "Sapphire", "Ember"]
    word = random.choice(words)
    numbers = random.randint(10, 999)  # Генерируем двух-трехзначное число
    nickname = f"{word}{numbers}"
    return nickname


def create_jwt(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=JWT_EXPIRE_TIME)
    to_encode.update(
        {
            'exp': expire
        }
    )
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
