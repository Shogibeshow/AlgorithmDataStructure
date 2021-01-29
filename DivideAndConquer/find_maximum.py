import math


def find_maximum(num_list, start, end):
    # divide
    mid = math.floor((start + end) / 2)

    # solve
    if start == end - 1:
        return num_list[start]
    left_maximum = find_maximum(num_list, start, mid)
    right_maximum = find_maximum(num_list, mid, end)

    # conquer
    return max(left_maximum, right_maximum)


def main():
    num_list = [1, 35, 354, 15, 32, 154, 3354, 21, 54, 64, 21458, 12]
    print(find_maximum(num_list, 0, len(num_list)))

if __name__ == '__main__':
    main()
