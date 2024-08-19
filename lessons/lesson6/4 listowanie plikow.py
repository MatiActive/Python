# Ścieżki plikow - podsumowujac ścieżka do pliku skryptu pythona, a katalog w ktorym jest on uruchomiony to dwie rozne rzeczy, dlatego trzeba miec to na uwadze
# Prosty kod pozwala na wylistowanie plikow w folderze w ktorym wykonywany jest domyslnie program;

import os 
# . to aktualny katalog czyli folder bieżący, gzie wykonuje sie program
# . to też scieżka realtywna/wzgledna

arr = os.listdir(".")
print("wylistowany folder glowny ",arr)

# Skrypt jest ścieżka relatywną aktualnego folderu czyli, wykonany na katalogu bieżacym pokazał liste plikow w tym katalogu jak wylistować zawartość folderu w scieżce relatywnej np. lessons
arr2 = os.listdir("./lessons")
print("wylistowany folder lesson",arr2)
arr3 = os.listdir("..")
print("wylistowany folder nadrzedny ",arr3)
arr3 = os.listdir("../Downloads")
print("wylistowany folder Downloads ",arr3)