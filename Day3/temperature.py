def calculateTemperature():
    lst = []
    n = int(input("How many day's temperature: "))
    sum = 0
    for i in range(n):
        tmp = float(input("Day's " + str(i+1)+ " high temp: "))
        lst.append(tmp)
        sum += tmp
    avgTemp = sum/len(lst)
    count = 0
    for temp in lst:
        if temp > avgTemp:
            count += 1
    
    print("Average =", avgTemp)
    print(str(count)+" day(s) above average", end ='')
    
calculateTemperature()
