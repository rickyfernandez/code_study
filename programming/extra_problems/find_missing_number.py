def find_missing_number(input_list):
    sum = 0
    for i in range(len(input_list)):
        sum = sum + input_list[i]
        return (55-sum)

def find_missing_number2(input_list):
    return sum(range(1,11)) - sum(input_list)
