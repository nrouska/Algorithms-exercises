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

def add_values_in_dict(sample_dict, key, list_of_values):
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict

card_charges= dict()
cards=[]
charges=[]
days=["Mon", "Tue","Wed", "Thu","Fri","Sat"] 


for i in range(20000):
    id= ''.join(random.choice(string.digits) for j in range(4))+"-" + ''.join(random.choice(string.digits) for j in range(4))+"-" +''.join(random.choice(string.digits) for j in range(4))+"-"+''.join(random.choice(string.digits) for j in range(4))
    cards.append(id)

# print(cards,'\n')
start_time = time.time()
for j in range(1000000):
    charge=random.randrange(5,500)
    charge_day=[random.choice(days),charge]
    card_charges.setdefault(random.choice(cards), []).append(charge_day)
    # charges.append(charge_day)
    # add_values_in_dict(card_charges,random.choice(cards),charges)
    # charges.clear()

# print(card_charges,"\n")

min_count=math.inf
max_count=-math.inf
max_count_synallages=-math.inf
mon,tue,wed,thu,fri,sat=0,0,0,0,0,0
for values in card_charges.values():   
    count=0
    count_synallages=0
    for i in values:
        # print(i)
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
            card_max_synallages=get_key(values,card_charges)                  
    if count<min_count:
        min_count=count
        card_min_charges=get_key(values,card_charges)
    if count>max_count:
        max_count=count   
        card_max_charges=get_key(values,card_charges) 

        
d={'Mon':mon,'Tue':tue,'Wed':wed,'Thu':thu,'Fri':fri,'Sat':sat}
min_day=min(d.values())

print("--- %s seconds ---" % (time.time() - start_time))
print("Η κάρτα με τον μέγιστο αριθμό (%i) συναλλαγών: %s"%(max_count_synallages,card_max_synallages)   ) 
print("Η κάρτα με τον μέγιστο αριθμό (%i) χρεώσεων: %s"%(max_count,card_max_charges)   ) 
print("Η κάρτα με τον ελάχιστο αριθμό (%i) χρεώσεων: %s"%(min_count,card_min_charges)   ) 
print("Η ημέρα με τον ελάχιστο αριθμό (%i) χρεώσεων: %s"%(min_day,get_key(min_day,d)   ) )
print(d)
