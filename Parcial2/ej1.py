def filter_and_modify(list):
    results=[]
    for x in list:
        if x % 2 == 0:
            if x > 10:
                results.append(int(x/2))
            elif(x<=10):
                results.append(int(x*2))
    return results

#Ejemplo de lista
listInput = [3, 14, 6, 12, 7, 18]
print(listInput)
listInput = filter_and_modify(listInput)  
print(listInput)