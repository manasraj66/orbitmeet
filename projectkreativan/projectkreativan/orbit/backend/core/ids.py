import secrets, string
def token(n=32): return secrets.token_urlsafe(n)
def meeting_code(n=6): return ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(n))
