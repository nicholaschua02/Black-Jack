def flatten_list_of_lists(input_list):
    flattened_list = []
    for item in input_list:
        if isinstance(item[0], list):
            flattened_list.extend(flatten_list_of_lists(item))
        else:
            flattened_list.append(item)
    return flattened_list

# Provided list
nested_list = [['8', '5', 'J'], [['8', 'Q'], ['8', '10']]]

# Check if the list is already in the desired shape
if any(isinstance(item, list) for item in nested_list):
    flattened_list = flatten_list_of_lists(nested_list)
    print(flattened_list)
else:
    print("List is already in the correct shape:", nested_list)
