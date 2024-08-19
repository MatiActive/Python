fh= open("/home/matiactive/python_lessons/test.txt", "r")
lines = fh.readlines()
fh.close()

for line in lines:
    print(line)