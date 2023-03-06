
import os

BASE_PATH = os.path.dirname(
    os.path.dirname(__file__))
print(BASE_PATH)

BD_PATH = os.path.join(BASE_PATH, 'db')