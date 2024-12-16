# Day 1 solution

def calculate_sorted_list(input_list):
    return sorted(input_list)

def main():
    left_list, right_list = [], []

    try:
        with open("inputs/day1.txt") as file:
            for line in file:
                data = line.split()

                num_1, num_2 = data[0], data[1]

                left_list.append(int(num_1))
                right_list.append(int(num_2))

    except FileNotFoundError:
        print("File not found")

    new_left = calculate_sorted_list(left_list)
    new_right = calculate_sorted_list(right_list)
    sum = 0

    for i in range(len(new_left)):
        sum += abs(new_right[i] - new_left[i])

    print(sum)

if __name__ == "__main__":
    main()