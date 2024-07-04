raining = True

haveUmbrella = True

temperature = 9

if temperature >= 40 or temperature <= 0:
    print("zostan w domu")
elif temperature > 0 and temperature < 10 and raining and haveUmbrella:
    print("mozesz wyjsc z parasolka")
elif not raining and temperature >= 10:
    print("mozesz wyjsc bez parasolki")
else:
    print("zostan w domu")