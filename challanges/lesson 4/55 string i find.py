def validateEmail(email):
    mokneyIndex = email.find("@")
    if mokneyIndex < 0 : return False

    dotIndex = email.rfind(".")
    if dotIndex == -1: return False 
    if dotIndex < mokneyIndex: return False
    return True

email = "asia@example.com"
print(email, validateEmail(email))
email = "karol@domena"
print(email, validateEmail(email))
email = "user.com"
print(email, validateEmail(email))
email = "ostatni@prawidlowy.pl"
print(email, validateEmail(email))
