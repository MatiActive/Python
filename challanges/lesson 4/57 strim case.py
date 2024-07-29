def getUserInformation(name,surname,job):
    name = name.strip().upper()
    surname = surname.strip().upper()
    job = job.strip().lower()

    info = "imie: " + name + " ,nazwisko: " + surname + " praca: " + job
    return info

print(getUserInformation("\tAnia\t", "\nKowalska", "\tProgramistka"))
print(getUserInformation("Daniel\t\t", "\n\tLis", "\t\tAdministrator"))