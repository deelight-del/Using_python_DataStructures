#writing function to sort list
def minimum_sort():
    
    '''It sorts a list(input list) by iterating through the 
    list(using while loop) and selects the
    minimum value in each iteration (using a for loop).
    It then appends each minimum value to a new list,
    that was empty initially'''
    
    n = int(input('Enter length of list: '))
    listed = []
    new_list = []
    for i in range(n):
        a = int(input(f'Enter element {i+1} for list'))
        listed.append(a)
    
    while listed:         #Loop continues as long as there  are values in listed
        mini = listed[0]
        for item in  listed:   #For loop that selects the(1) minimum value in listed as mini
        
            if item < mini:
                mini = item
        new_list.append(mini)   #Appends minimum value from for loop above to a new_list
        listed.remove(mini)    #Removes minimum value from listed list
    print(new_list) 