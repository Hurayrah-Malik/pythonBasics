"""
input is a list of values

make a dictionary counting how many times values appear

make a set of which values have been seen

make a list of unique values

make a list of the duplicates 
"""

from collections.abc import Hashable


values = [True, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, True]


def main() -> None:
    print("Program started")

    combined_function(values)



  
   


#coutns the stores the duplicates, unique values, and occurances
def combined_function(items: list[Hashable]) -> dict[str, object]:
    duplicates: list[Hashable] = []
    seen: set[Hashable] = set()
    unique_values: list[Hashable] = []
    counts: dict[Hashable, int] = {}
    for item in items:
        # the 0 means that if the item spefcied is not in the dictionary, then 0 will be set default value
        counts[item] = counts.get(item, 0) + 1
        if item not in seen:
            seen.add(item)
            unique_values.append(item)
       
        else:
            duplicates.append(item)
           
    print ("duplicates " , duplicates)
    print("unique values ", unique_values)
    print("counts dict ", counts)
    return {"duplicates list": duplicates, "unique values": unique_values, "counts": counts}








if __name__ == "__main__":
    main()
