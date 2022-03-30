import copy
import math
#generate all possible paths for the clerk
def generate_clerk_paths(rooms, nights):
    #Base case
    if(nights <= 1):
        return [[e] for e in range(1, rooms + 1)]
    #Recursive call
    base_list = generate_clerk_paths(rooms, nights-1)
    return clerk_paths_add_night(base_list, rooms)

#This function takes a list of clerk paths and adds a night
#Separating it out makes some stuff later more efficient
def clerk_paths_add_night(base_list, rooms):
    output_list = []
    #This uses copy to create new elements
    #I do not fully understand how copies and references work
    #But it's not broken yet
    for e in base_list:
        for i in range(1, rooms+1):
            new_element = copy.copy(e)
            new_element.append(i)
            output_list.append(new_element)
    return output_list
    

#generate all possible paths for the guest
def generate_guest_paths(rooms, nights):
    #Base case
    if(nights <= 1):
        return [[e] for e in range(1, rooms + 1)]
    #Recursive call
    base_list = generate_guest_paths(rooms, nights-1)
    return guest_paths_add_night(base_list, rooms)

#This function takes a list of guest paths and adds a night
#Separating it out makes some stuff later more efficient
def guest_paths_add_night(base_list, rooms):
    output_list = []
    for e in base_list:
        #The next element is based on the last element of the path
        last = e[-1]
        if(last == 1):
            new_element = copy.copy(e)
            new_element.append(last + 1)
            output_list.append(new_element)
        elif(last == rooms):
            new_element = copy.copy(e)
            new_element.append(last - 1)
            output_list.append(new_element)
        else:
            new_element = copy.copy(e)
            new_element.append(last - 1)
            output_list.append(new_element)
            new_element2 = copy.copy(e)
            new_element2.append(last + 1)
            output_list.append(new_element2)
    return output_list
    
                
#check two arrays for overlap
#precondition: the arrays are the same size
def check_paths(clerk_path, guest_path, verbose = False):
    for i in range(0, len(guest_path)):
        if(verbose):
            print(i)
            print(guest_path)
            print(clerk_path)
        if(guest_path[i] == clerk_path[i]):
            return True
    return False

#compares two 2D arrays
#precodition: the elements of each 2D array are the same length
def check_path_lists(clerk_path_list, guest_path_list, verbose = False):
    for i in range(0, len(clerk_path_list)):
        found_them = True #haven't failed yet
        e = clerk_path_list[i]
        for f in guest_path_list:
            if(not check_paths(e, f, verbose)):
                found_them = False
                break
        if(found_them):
            return i
    return -1

#input an integer number of rooms greater than 1 to get the smallest number
#of nights it takes to find the guest
def find_min_night(rooms):
    curr_nights = math.floor(rooms/2)
    clerk_paths = generate_clerk_paths(rooms, curr_nights)
    guest_paths = generate_guest_paths(rooms, curr_nights)
    path_index = check_path_lists(clerk_paths, guest_paths)
    while(path_index < 0):
        clerk_paths = clerk_paths_add_night(clerk_paths, rooms)
        guest_paths = guest_paths_add_night(guest_paths, rooms)
        path_index = check_path_lists(clerk_paths, guest_paths)
    return clerk_paths[path_index]

print(find_min_night(7))
