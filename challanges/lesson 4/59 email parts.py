def getEmailParts(email):
    monkeyExists = email.find("@")
    if monkeyExists == -1: return None

    dot = email.rfind(".")
    if dot == -1: return None

    user = email[0:monkeyExists]
    domaineName = email[monkeyExists+1:dot]
    domainExt = email[dot+1:]

    return {
        "user " : user,
        "domena " : domaineName,
        "zakonczenie domeny " : domainExt
    }
email= "ola@gmail.com"
print(getEmailParts(email))