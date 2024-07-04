config = {
    "website" : "example.com",
    "dbType" : "mysql",
    "dbUser" : "admin",
    "dbPassword" : 1234
}
print("-----1----")
print(config)
print("------2---")
print(len(config))
print("---------")
print(config["dbType"])
print("------3---")
print("-----4----")
print(config.keys())
print(type(config))
print("------5---")
print(config.values())
print("----6-----")
for key, value in config.items():
    print("Klucz w config : ",key, " z wartoscia : ", value)