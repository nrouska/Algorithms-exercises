import random, time
#Divide and Conquer method
def MaxCrossingSubArray(array,low,middle,high):
    sum=0
    left_sum=0
    right_sum=0   
    global start_index
    global end_index
    for i in range(middle,high+1):
        sum+=array[i]
        if sum>right_sum:
            right_sum=sum            
            end_index=i
    sum=0
    for j in range(middle,low-1,-1):
        sum=array[j]
        if sum>left_sum:
            left_sum=sum
            start_index=j

    return max(left_sum,right_sum,left_sum+right_sum-array[middle])      

def MaxSubArray(array,low,high):
    if low>high: return -10000
    if low==high: return array[low]
    middle=(low+high)//2
    return max(MaxSubArray(array,low,middle-1),
               MaxSubArray(array,middle+1,high),
               MaxCrossingSubArray(array,low,middle,high))
  

randomlist =[] 
for i in range(0,2100000):
    num = random.randint(-100,101)
    randomlist.append(num)
# print('The random array is',randomlist,'\n')

n=len(randomlist)
start = time.time()
m=MaxSubArray(randomlist,0,n-1)
end=time.time()
elapsed=end-start
print('The maximum sum is',m,'\n')
print('The indexes of SubArray are [{}] [{}]'.format(start_index,end_index),'\n')
print('Time elapsed is {:.6f}'.format(elapsed),'seconds')
