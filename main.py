# Enter your code here. Read input from STDIN. Print output to STDOUT
def checkcombinations(array,check):
    combinations = []
    for i in array:
        r+=1
        if(item == check):
            combinations.append(array[r-1] + "," + check)
        else:
            continue
    return combinations

array = [1,2,3,2,4,2,5,6,7,8,9,2]
print(checkcombinations(array, 2))

        
        
