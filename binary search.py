

def binary_search(arr , target ):
    middle = 0
    start = 0 
    end = len(list)
    steps = 0 

    while(start<=end):
        print("Step", steps, ":" , str(arr[start:end+1]))

        steps = steps+1
        middle = (start + end) //2

        if target == list[middle]:
            return middle
        if target < list[middle]:
            end = middle-1
        else:
            start = middle + 1

