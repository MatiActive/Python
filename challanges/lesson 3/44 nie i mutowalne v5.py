def analyzeTemperatures(temperatures):
    avgTemp = sum(temperatures) / len(temperatures)
    minTemp = min(temperatures)
    maxTemp = max(temperatures)
    return (avgTemp, minTemp, maxTemp)
temperatures = []

while True:     
    temp = input("wprowadz kolejna temperature lub koniec aby zakonczyc : ")
    if temp.lower() == "koniec": break
    else:
        temperatures.append(int(temp))
print(temperatures)

data = analyzeTemperatures(temperatures)
avg = data[0]
min = data[1]
max = data[2]

print("avg", avg)
print("min", min)
print("max", max)

avgTemp, minTemp, maxTemp = data
print("avgTemp: ", avgTemp)
print("minTemp: ", minTemp)
print("maxTemp: ", maxTemp)