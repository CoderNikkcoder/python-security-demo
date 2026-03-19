import os
import hashlib

# A simple Python app
# (We'll add the security scanner in the next step)

def get_user(user_id):
    # Connects to a database and fetches a user
    print(f"Fetching user {user_id}")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def main():
    api_key = os.environ.get("API_KEY")
    print("App is running...")

if __name__ == "__main__":
    main()
