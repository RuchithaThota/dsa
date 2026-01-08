# The given statement is describing a problem where you are provided with an array of integers
# (`nums`) and an integer (`target`). The task is to find two numbers in the array that add up to the
# target value. The solution should return the indices of these two numbers.

# List
arr = [2, 11, 7, 15]

# variable (dynamically typed)
target = 9

# Brut Force Solution time-O(n2),space-O(1)
def brut_force_two_sum():
    for i in range(len(arr)):
        num=target-arr[i]
        for j in range(i+1,len(arr)):
            if(arr[j]==num):
                return [i,j]

brut_force_output = brut_force_two_sum()

print(brut_force_output)

# Optimized Solution time-O(n),space-O(n)

def two_sum():
    two_sum_map={}
    for i, num in enumerate(arr):
        complement=target-num
        if complement in two_sum_map:
            return [two_sum_map[complement],i]
        two_sum_map[num]=i

output = two_sum()
print(output)