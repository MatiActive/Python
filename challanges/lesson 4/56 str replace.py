print("pierwszy sposob".center(21,"*"))
def cleanText(cleaner="python"):
    cleaner = cleaner.replace("JavaScript", "*" * 10)
    cleaner = cleaner.replace("java", "*" * 4)
    cleaner = cleaner.replace("php", "*" * 3)
    cleaner = cleaner.replace("html", "*" * 4)
    cleaner = cleaner.replace("css", "*" * 3)
    return cleaner

print(cleanText("programowanie zaczalem z jezykiem php, nastepnie poznalem: html i css, ale obecnie skupiam sie na JavaScript"))
print("\n")
print("drugi sposob".center(18,"*"))
def cleanText2(cleaner2):
    cleaner2 = cleaner2.replace("JavaScript", "*" * 10)
    cleaner2 = cleaner2.replace("java", "*" * 4)
    cleaner2 = cleaner2.replace("php", "*" * 3)
    cleaner2 = cleaner2.replace("html", "*" * 4)
    cleaner2 = cleaner2.replace("css", "*" * 3)
    return cleaner2

content = "programowanie zaczalem z jezykiem php, nastepnie poznalem: html i css, ale obecnie skupiam sie na JavaScript"

newContent = cleanText2(content)
print(newContent)