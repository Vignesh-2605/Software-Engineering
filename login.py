def login(username, password):
    # For simplicity, check hardcoded username and password
    if username == "admin" and password == "password":
        return "Login successful"
    else:
        return "Invalid credentials"
