def removeDups(arr, n): 
       
    # dict to store every element 
    # one time 
    mp = {i : 0 for i in arr} 
      
    for i in range(n): 
          
        if mp[arr[i]] == 0: 
            print(arr[i], end = " ") 
            mp[arr[i]] = 1
  
# Driver code 
arr = [1,2,3,4,4,2,1,5,1,4,5] 
  
# len of array 
n = len(arr) 
  
removeDups(arr,n) 