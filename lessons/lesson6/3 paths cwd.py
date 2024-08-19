import os 

print("ścieżka absolutna", __file__)
folder = os.path.dirname(__file__)
print("scieżka do katalogu glownego skryptu", os.getcwd())

fh= open(folder + "/3.1 newfile.txt", "w") # tworzy dokument tekstowy w folderze gdzie dokladnie jest skrypt
fh.write("comment")
fh.close()

filePath = (folder + "/3.2 secondfile.txt")
print("scieżka do pliku", filePath)
fw = open(filePath, "w")
fw.write("nastepny plik tworzony w tym samym katalogu")
fw.close()