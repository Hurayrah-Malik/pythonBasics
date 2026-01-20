"""
input is a list of values

make a dictionary counting how many times values appear

make a set of which values have been seen

make a list of unique values

make a list of the duplicates 
"""

values = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5]


def main() -> None:
    print("Program started")

    #print the occurances of each int 
    store_occurances(values)

    #print the unique ints
    unique_values(values)

    #print duplicates 
    duplicates(values)

  
   

#input list of ints, print the occurences
def store_occurances(items: list[int]) -> None:
    occurance_dictionary = {}
    for item in items:
        if item in occurance_dictionary:
            occurance_dictionary[item] = occurance_dictionary[item] + 1
        else:
            occurance_dictionary[item] = 1


    print ("occurance dict  ",occurance_dictionary)
    


#input list of ints, print the unique values
def unique_values(items: list[int]) -> None:
    unique_ints = set()
    for item in items: 
        unique_ints.add(item)
    print("unique ints " , unique_ints)


def duplicates(items: list[int]) -> None:
    duplicates_list = []
    seen = set()
    for item in items:
        if item in seen:
            duplicates_list.append(item)
        else:
            seen.add(item)

    print ("duplicates list " ,duplicates_list)







if __name__ == "__main__":
    main()
