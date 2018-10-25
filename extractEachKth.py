def extractEachKth(inputArray, k):
    
    ### create empty array to hold values that aren't multiples of k
    newArray = []
    
    ### iterate through inputArray
    for i in range(len(inputArray)):
    
        ### add 1 to i so index matches, check if divisible by k
        ### if it isn't, add value to newArray
        if (i + 1) % k != 0:
            newArray.append(inputArray[i])
        
        ### if it is, don't do that.
        else:
            continue
            
    return newArray
