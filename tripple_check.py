

def tripple_check(input_list):
    non_tripples = ''
    for item in input_list:
        item_count = input_list.count(item)
        if item_count == 3:
            input_list = [items for items in input_list if items != item]
    if input_list:
        return ",".join(map(str,input_list))
    else:
        return "List Contains all tripples"



