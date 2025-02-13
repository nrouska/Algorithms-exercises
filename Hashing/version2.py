import random
import string 
import math
import time
random.seed(1092581)
def get_key(val,mydict):
   
    for key, value in mydict.items():
        if val == value:
            return key
 
    return "key doesn't exist"

class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size
        self.count_values=0
        self.count_keys=0
    def hash(self, key):
        return hash(key) % self.size
    def put(self, key, value): 
        self.count_values += 1
        ld_fact = self.count_keys / self.size
        if ld_fact > 0.7:
            self.rehashing()  
        index = self.hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                # Key already exists, update the value
                self.values[index].append(value)
                return
            # Linear probing to find the next available slot
            index = (index + 1) % self.size 
        # Found an empty slot, insert the key and value
        self.keys[index] = key
        self.values[index] = [value]
        self.count_keys += 1
    def get(self, key):
        index = self.hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            # Linear probing to search for the key
            index = (index + 1) % self.size

        # Key not found
        return None
    def rehashing(self):
        n = self.size * 2
        next_num = n
        
        new_keys = [None] * next_num
        new_values = [None] * next_num
        
        for i in range(self.size):
            if self.keys[i] is not None:  
                index = self.hash(self.keys[i])
                while new_keys[index] is not None:
                    index = (index + 1) % next_num
                new_keys[index] = self.keys[i]
                new_values[index] = self.values[i]
        
        self.size = next_num
        self.keys = new_keys
        self.values = new_values

hash_table = HashTable(101)
cards=[]
charges=[]
days=["Mon", "Tue","Wed", "Thu","Fri","Sat"] 
for i in range(20000):
    id= ''.join(random.choice(string.digits) for j in range(4))+"-" + ''.join(random.choice(string.digits) for j in range(4))+"-" +''.join(random.choice(string.digits) for j in range(4))+"-"+''.join(random.choice(string.digits) for j in range(4))
    cards.append(id)
start_time = time.time()
for j in range(1000000):
    charge=random.randrange(5,500)
    charge_day=[random.choice(days),charge]
    hash_table.put(random.choice(cards),charge_day)

min_count=math.inf
max_count=-math.inf
max_count_synallages=-math.inf
mon,tue,wed,thu,fri,sat=0,0,0,0,0,0
for key in hash_table.keys:   
    if key!=None:
        count=0
        count_synallages=0
        values_list=hash_table.get(key)
        if hash_table.get(key)!=None:
            # print(values_list)
            for i in values_list:
                count_synallages+=1
             
                for j in range(len(i)):
                
                    if i[j]==i[1]:
                        count+=i[j]
                    if i[j]=="Mon" : mon+=1
                    if i[j]=="Tue" : tue+=1
                    if i[j]=="Wed" : wed+=1
                    if i[j]=="Thu" : thu+=1
                    if i[j]=="Fri" : fri+=1
                    if i[j]=="Sat" : sat+=1
        if count_synallages>max_count_synallages:
            max_count_synallages=count_synallages  
            card_max_synallages=key                  
        if count<min_count:
            min_count=count
            card_min_charges=key
        if count>max_count:
            max_count=count   
            card_max_charges=key



d={'Mon':mon,'Tue':tue,'Wed':wed,'Thu':thu,'Fri':fri,'Sat':sat}
min_day=min(d.values())
print("--- %s seconds ---" % (time.time() - start_time))    
print("Η κάρτα με τον μέγιστο αριθμό (%i) συναλλαγών: %s"%(max_count_synallages,card_max_synallages))
print("Η κάρτα με τον μέγιστο αριθμό (%i) χρεώσεων: %s"%(max_count,card_max_charges)) 
print("Η κάρτα με τον ελάχιστο αριθμό (%i) χρεώσεων: %s"%(min_count,card_min_charges))      
print("Η ημέρα με τον ελάχιστο αριθμό (%i) χρεώσεων: %s"%(min_day,get_key(min_day,d)   ) )
print(d)