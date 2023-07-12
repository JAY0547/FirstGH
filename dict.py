arr = [5,4,10,1,6,2]

for i in range (1,len(arr)):
    j = i -1
    tmp = arr[i]
    while (j>=0 and tmp < arr[j]):
     arr[j+1] = arr[j]
     j = j-1

    arr[j+1] = tmp

print(arr)




    




