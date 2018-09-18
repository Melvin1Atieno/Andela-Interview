

def tripple_check(input_list):
    for item in input_list:
        item_count = input_list.count(item)
        if item_count == 3:
            input_list = [items for items in input_list if items != item]
    if input_list:
        return input_list[0]



print(tripple_check([5, 3, 4, 3, 5, 5, 3]))