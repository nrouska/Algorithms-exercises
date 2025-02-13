import random
import time
class MinHeap():
    def __init__(self, arr):
        self.array = []         # tuple (key, value)
        self.pos = {}           # position of key in array
        self.size = len(arr)    # number of elements in min heap

        for i, item in enumerate(arr):
            self.array.append((item[0], item[1]))
            self.pos[item[0]] = i

        for i in range(self.size // 2, -1, -1):
            self.heapify(i)


    # display items of heap
    def display(self):
        print('array =', end=' ')
        for i in range(self.size):
            print(f'({self.array[i][0]} : {self.array[i][1]})', end=' ')
        print()


    # is heap empty ?
    def isEmpty(self):
        return self.size == 0


    # i is the array index
    # modify array so that i roots a heap, down-heap
    def heapify(self, i):

        smallest = i
        le = 2 * i + 1
        ri = 2 * i + 2

        if le < self.size and self.array[le][1] < self.array[smallest][1]:
            smallest = le
        if ri < self.size and self.array[ri][1] < self.array[smallest][1]:
            smallest = ri

        if smallest != i:
            # update pos
            self.pos[self.array[smallest][0]] = i
            self.pos[self.array[i][0]] = smallest

            # swap
            self.array[smallest], self.array[i] = \
                self.array[i], self.array[smallest]

            self.heapify(smallest)


    # return the min element of the heap
    def getMin(self):
        if self.size == 0:
            return None

        return self.array[0]


    # return and remove the min element of the heap
    def extractMin(self):
        if self.size == 0:
            return None

        root = self.array[0]
        lastNode = self.array[self.size - 1]

        self.array[0] = lastNode

        # update pos
        self.pos[lastNode[0]] = 0
        del self.pos[root[0]]

        self.size -= 1
        self.heapify(0)

        return root


    # item (key, value) to insert
    # modify array to include item
    def insert(self, item):
        # insert an item at the end with big value
        if self.size < len(self.array):
            self.array[self.size] = (item[0], 10**80)
        else:
            self.array.append((item[0], 10**80))

        self.pos[item[0]] = self.size
        self.size += 1
        self.decreaseKey(item)


    # decrease value of item (key, value)
    # with value smaller than current
    def decreaseKey(self, item):
        i = self.pos[item[0]]
        val = item[1]

        # new value must be smaller than current
        if self.array[i][1] <= val:
            return

        self.array[i] = item

        # check if is smaller than parent
        p = (i - 1) // 2
        while p >= 0 and self.array[i][1] < self.array[p][1]:
            # update pos
            self.pos[self.array[i][0]] = p
            self.pos[self.array[p][0]] = i

            # swap
            self.array[p], self.array[i] = self.array[i], self.array[p]

            i = p
            p = (i - 1) // 2

    # ---
    # increase value of item (key, value),
    # with value greater than current
    def increaseKey(self, item):
        i = self.pos[item[0]]
        val = item[1]

        # new value must be greater than current
        if self.array[i][1] >= val:
            return

        self.array[i] = item

        # check children
        self.heapify(i)


    # change value of item (key, value),
    # call decreaseKey or increaseKey
    def changeKey(self, item):
        i = self.pos[item[0]]
        val = item[1]

        if val < self.array[i][1]:
            self.decreaseKey(item)

        if val > self.array[i][1]:
            self.increaseKey(item)


    # check if exists an item with key = v
    def isInMinHeap(self, v):
        if self.pos.get(v) == None:
            return False
        if self.pos[v] < self.size:
            return True
        return False


    # get the value of item with key = key
    def getValueMinHeap(self, key):
        if self.pos.get(key) == None:
            return None
        if self.pos[key] < self.size:
            return self.array[self.pos[key]][1]
        return None


    # delete item 
    # reduce value of item to minus infinite 
    # and call extractMin() 
    def deleteKey(self, item): 
        self.decreaseKey((item[0], float('-inf'))) 
        self.extractMin()

class Metallikh_Plaka():
    def __init__(self):
        self.array=[]
        for i in range(100000):
            x = random.randint(0, 999)
            y = random.randint(0, 999)
            self.array.append((x,y))
        
    def rMedian(self,N):
        minHeap, maxHeap = MinHeap([]),  MinHeap([])
        curMedian=0
        for i in range(N):
            
            thermokrasia=round(random.uniform(-10.00, 90.00), 2)            
            key=random.choice(self.array)   
             
            if  not minHeap.isInMinHeap(key) and not maxHeap.isInMinHeap(key):
                minHeap.insert((key,thermokrasia))
            else:
                if thermokrasia < curMedian and minHeap.isInMinHeap(key) : 
                    minHeap.deleteKey((key,minHeap.getValueMinHeap(key)))
                    maxHeap.insert((key,-thermokrasia)) 
                    
                elif thermokrasia > curMedian and maxHeap.isInMinHeap(key) :
                    maxHeap.deleteKey((key,maxHeap.getValueMinHeap(key)))
                    minHeap.insert((key,thermokrasia))
                elif thermokrasia < curMedian and maxHeap.isInMinHeap(key) and not minHeap.isInMinHeap(key): 
                    maxHeap.changeKey((key,-thermokrasia)) 
                    
                elif thermokrasia > curMedian and minHeap.isInMinHeap(key) and not maxHeap.isInMinHeap(key):
                    minHeap.changeKey((key,thermokrasia))
                    
                    
            if abs(maxHeap.size - minHeap.size) > 1:
                if maxHeap.size > minHeap.size:
                    t = maxHeap.extractMin()
                    minHeap.insert((t[0],-t[1]))
                else: 
                    t = minHeap.extractMin()
                    maxHeap.insert((t[0],-t[1]))  
            if minHeap.size:
                t_min = minHeap.getMin()[1]
            if maxHeap.size: 
                t_max = -maxHeap.getMin()[1]
            if maxHeap.size == minHeap.size:
                curMedian = (t_min + t_max) / 2 
            elif maxHeap.size > minHeap.size: 
                curMedian = t_max
            else:
                curMedian = t_min
          
            
        return curMedian ,maxHeap, minHeap            
            
if __name__== '__main__' :
    random.seed(1092581) 
    N=500000
    points = Metallikh_Plaka ()
    start=time.time()
    median, maxh,minh= points.rMedian(int(N/2))
    end=time.time()
    print("Running median for Ν/2 : %.2f " %median,"in %.2f sec " %(end-start))
    print("MaxHeap size",maxh.size)
    print("MinHeap size",minh.size)
    
    start=time.time()
    median, maxh,minh= points.rMedian(N)
    end=time.time()
    print("Running median for Ν : %.2f " %median,"in %.2f sec" %(end-start))
    print("MaxHeap size ",maxh.size)
    print("MinHeap size ",minh.size)