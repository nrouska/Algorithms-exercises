import random, time 
def MaxSubArray(array,n):
    maximum_sum=0
    global start_index,end_index
    for j in range(0,n):
        current_sum=0
        for k in range(j,n):
            current_sum+=array[k]
            if current_sum > maximum_sum:
                maximum_sum=current_sum
                end_index=k
                start_index=j
    return maximum_sum     

randomlist =[ ]
for i in range(0,11000):
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
       
            

             

