from auth import login
from utils import process

def main():
    user = {"name": "alice"}
    if login(user):
        print("Welcome")
    else:
        print("Login failed")
