import hashlib
import subprocess

# Issue 1 — Hardcoded password (scanner should catch this)
DATABASE_PASSWORD = "admin123"

# Issue 2 — Weak MD5 hash (scanner should catch this)
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# Issue 3 — Shell injection risk (scanner should catch this)
def run_command(user_input):
    subprocess.call("ls " + user_input, shell=True)
