emplopyee = {
    "name" : "mati",
    "email" : "mati@gmail.com",
    "rank" : "programmer",
    "salary" : 8000
}

for key, value in emplopyee.items():
    print(key,value)
def promoteToManager(user):

    if user["rank"] == "menager":
        print("Jestes juz menagerem")
        return 
    user["rank"] = "menager"
    user["salary"] = 8000 * 1.5
print("---------------")
promoteToManager(emplopyee)

for key, value in emplopyee.items():
    print(key,value)

print("---------------")
promoteToManager(emplopyee)
