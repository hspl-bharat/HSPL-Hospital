data = [(1, 45), (2, 3), (3, 10), (4, 20), (5, 30)]
cases = [42, 31, 51, 5, 45, 16, 14]


def select_location(data, need):
    sorted_data = sorted(data, key=lambda x: x[1], reverse=True)
    selected_locations = []
    remaining_need = need
    
    for location in sorted_data:
        if remaining_need <= 0:
            break
        
        if location[1] <= remaining_need:
            
            selected_locations = min()
    











    return selected_locations

# data = [(1, 45), (2, 3), (3, 10), (4, 20), (5, 30)]

# Test cases
# cases = [42, 31, 51, 5, 45, 16, 14]
for case in cases:
    selected_locations = select_location(data, case)
    print(f"If need is {case}, fetch the product from: {selected_locations}")
