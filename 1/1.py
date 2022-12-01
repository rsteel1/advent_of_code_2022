
def get_input_list():
    with open("1/input.txt", "r") as infile:
        return infile.read().splitlines()

def calculate_answer():        
    max_calories = [0, 0, 0]
    current_sum = 0

    for cals in get_input_list():
        if cals != "":
            current_sum += int(cals)
        else:
            max_calories[max_calories.index(min(max_calories))] = max(min(max_calories), current_sum)
            current_sum = 0

    return sum(max_calories)

if __name__ == "__main__":
    print(calculate_answer())