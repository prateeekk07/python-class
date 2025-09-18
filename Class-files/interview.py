arr = [1,0,2,3,0,0,0,4,5,6,0,0,0,0,9,8,7]  # [1,2,0,3,0,0,0,4,5,6,0,0,0,0,9,8,7]
for i in range(len(arr)-1):
    for j in range(len(arr)-1):
        if arr[j] == 0:
            arr[j+1], arr[j] = arr[j], arr[j+1] #arr[2], arr[1] = 
print(arr)
        
# print(arr)