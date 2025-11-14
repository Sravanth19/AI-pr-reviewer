def login(user):
    # naive login - should be improved
    if not user:
        return False
    if user.get("name") == "admin":
        return True
    return False
