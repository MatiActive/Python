setList = {-3,-2,-1,0,1,2,3}


set = {-1}

for i in setList:
    if i % 2 != 0:
        set.add(i)
for i in set:
    print(i)
print("lista po dodaniu liczb nieparzystych : ",set)