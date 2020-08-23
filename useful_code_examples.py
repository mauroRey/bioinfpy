


'''''''''''''''''''''''''''''''''''''
'''        INTERVAL MERGER        '''
'''''''''''''''''''''''''''''''''''''

# Python3 program to merge overlapping Intervals  
# in O(n Log n) time and O(1) extra space 
def mergeIntervals(arr): 
          
        # Sorting based on the increasing order  
        # of the start intervals 
        arr.sort(key = lambda x: x[0])  
          
        # array to hold the merged intervals 
        m = [] 
        s = -10000
        max = -100000
        for i in range(len(arr)): 
            a = arr[i] 
            if a[0] > max: 
                if i != 0: 
                    m.append([s,max]) 
                max = a[1] 
                s = a[0] 
            else: 
                if a[1] >= max: 
                    max = a[1] 
          
        #'max' value gives the last point of  
        # that particular interval 
        # 's' gives the starting point of that interval 
        # 'm' array contains the list of all merged intervals 
  
        if max != -100000 and [s, max] not in m: 
            m.append([s, max]) 
        print("The Merged Intervals are :", end = " ") 
        for i in range(len(m)): 
            print(m[i], end = " ") 
  
# Driver code 
arr = [[6, 8], [1, 9], [2, 4], [4, 7]] 
mergeIntervals(arr) 


#%%

''''''''''''''''''''''''''''''''''''
'''         DICTIONARIES         '''
''''''''''''''''''''''''''''''''''''
def get_week_day(argument):
    switcher = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday"
    }
    return switcher.get(argument, "Invalid day")
# Driver program

print (get_week_day(6))
print (get_week_day(8))
print (get_week_day(0))


#------------------------------------------------------------------------------


def get_week_day(argument):
    def zero():
        return "Sunday"
    def one():
        return "Monday"
    def two():
        return "Tuesday"
    def three():
        return "Wednesday"
    def four():
        return "Thursday"
    def five():
        return "Friday"
    def six():
        return "Saturday"
    switcher = {
        0: zero(),
        1: one(),
        2: two(),
        3: three(),
        4: four(),
        5: five(),
        6: six()
    }
    return switcher.get(argument, "Invalid day")
# Driver program

print (get_week_day(6))
print (get_week_day(8))
print (get_week_day(0))




#%%

''''''''''''''''''''''''''''''''''''
'''            LAMBDA            '''
''''''''''''''''''''''''''''''''''''

def pene(a,b):
    return lambda c : a*b*c

p=pene(2,3) #defino p con un lambda adentro con los valores a y b
print(p(4)) #llamo a p y le paso el valor C


#------------------------------------------------------------------------------


my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)


#------------------------------------------------------------------------------


x = lambda a, b : a * b
print(x(5, 6)) 


#------------------------------------------------------------------------------

mylist = [[7, 8], [1, 2, 3], [2, 5, 6]]
mysortedlist = sorted(mylist, key = lambda x: x[0])
print(mysortedlist) 


#------------------------------------------------------------------------------


mylist = [[7, 8], [1, 2, 3], [2, 5, 6]]
mylist.sort(key = lambda x: x[0])
print(mylist) 


#%%

'''''''''''''''''''''''''''''''''''''
'''           ENUMERATE           '''
'''''''''''''''''''''''''''''''''''''

numbers = [1,4,7,10,15]
for i, num in enumerate(numbers):
    print(i, num)
    
    
    
    