import random, time 
#Kadane's Algorithm
def MaxSubArray(array,n):
    current_max=array[0]
    maximum_sum=0
    pointer_index=0
    global start_index,end_index
    for i in range(0,n):
        current_max=max(array[i],current_max+array[i])
        if current_max>maximum_sum:
            maximum_sum=current_max
            start_index=pointer_index
            end_index=i
        if current_max<0:    
            pointer_index+=1
    return maximum_sum        


randomlist =[  ] 
for i in range(0,20500000):
    num = random.randint(-100,101)
    randomlist.append(num)
# print('The random array is',randomlist,'\n')

n=len(randomlist)
start = time.time()
m=MaxSubArray(randomlist,n)
end=time.time()
elapsed=end-start
print('The maximum sum is',m,'\n')
print('The indexes of SubArray are [{}] [{}]'.format(start_index,end_index),'\n')
print('Time elapsed is {:.6f}'.format(elapsed),'seconds')
