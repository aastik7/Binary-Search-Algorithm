

def binary_search(arr , target ):
    middle = 0
    start = 0 
    end = len(arr)
    steps = 0 

    while(start<=end):
        print("Step", steps, ":" , str(arr[start:end+1]))

        steps = steps+1
        middle = (start + end) //2

        if target == arr[middle]:
            return middle
        if target < arr[middle]:
            end = middle-1
        else:
            start = middle + 1
    return -1

# Example

my_arr = [ 1,2,3,4,5,6,7,8,9,10]
target = 2

binary_search(my_arr,target)
