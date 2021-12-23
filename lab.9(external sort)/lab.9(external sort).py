def merge(left, right):
    """
    A function, that sorts array of numbers using merge sort.
    :param left: list, the left(first) array of numbers..
    :param right: list, right(extreme) array of numbers.
    :return: Sorted array.
    """
    sorted_array = []
    left_index = right_index = 0
    left_len = len(left)
    right_len = len(right)
    for i in range(left_len + right_len):
        if left_index < left_len and right_index < right_len:
            if left[left_index] <= right[right_index]:
                sorted_array.append(left[left_index])
                left_index += 1
            elif right[right_index] < left[left_index]:
                sorted_array.append(right[right_index])
                right_index += 1
        elif left_index == len(left):
            sorted_array.append(right[right_index])
            right_index += 1
        elif right_index == len(right):
            sorted_array.append(left[left_index])
            left_index += 1
    return sorted_array


def merge_sort(array):
    """
    A function, that divides array(subarray) in half and sorts them recursively.
    :param array: list, array of numbers.
    :return: Sorted array.
    """
    if len(array) == 1:
        return array
    else:
        mid = len(array) // 2
        left = merge_sort(array[:mid])
        right = merge_sort(array[mid:])
        return merge(left, right)


def read_file():
    """
    A function, that reads data from file. Data is red with chunks, that are sorted after.
    :return: None.
    """
    f1 = open('file1.txt', 'r')
    for i in range(5):
        if i & 1 == 0:
            num_list = list(map(int, f1.readline().split()))
            array = merge_sort(num_list)
            f_add = open('file2.txt', 'a')
            for k in array:
                f_add.write(str(k) + ' ')
            f_add.write('\n')
            f_add.close()
        else:
            num_list = list(map(int, f1.readline().split()))
            array = merge_sort(num_list)
            f_add = open('file3.txt', 'a')
            for k in array:
                f_add.write(str(k) + ' ')
            f_add.write('\n')
            f_add.close()
    f1.close()


def merge_file_1():
    """
    A function, that merges sorted arrays and adds data to another file.
    :return: None.
    """
    f_add = open('file2.txt', 'r')
    array_1 = list(map(int, f_add.readline().split()))
    f_add.close()
    f_add = open('file3.txt', 'r')
    array_2 = list(map(int, f_add.readline().split()))
    f_add.close()
    add_array = merge(array_1, array_2)
    f_add = open('file4.txt', 'a')
    for i in add_array:
        f_add.write(str(i) + ' ')
    f_add.write('\n')
    f_add.close()

    f_add = open('file2.txt', 'r')
    array_1 = list(map(int, f_add.readline().split()))
    f_add.close()
    f_add = open('file3.txt', 'r')
    array_2 = list(map(int, f_add.readline().split()))
    f_add.close()
    add_array = merge(array_1, array_2)
    f_add = open('file5.txt', 'a')
    for i in add_array:
        f_add.write(str(i) + ' ')
    f_add.write('\n')
    f_add.close()

    f_add = open('file2.txt', 'r')
    array = list(map(int, f_add.readline().split()))
    f_add.close()
    f_add = open('file4.txt', 'a')
    for i in array:
        f_add.write(str(i) + ' ')
    f_add.write('\n')
    f_add.close()


def final_file():
    """
    A function, that merges last arrays and adds in the final file.
    :return: None.
    """
    f = open('file4.txt', 'r')
    array_1 = list(map(int, f.readline().split()))
    f.close()
    f = open('file5.txt', 'r')
    array_2 = list(map(int, f.readline().split()))
    f.close()
    final_array = merge(array_1, array_2)
    f = open('file4.txt', 'r')
    array_1 = list(map(int, f.readline().split()))
    f.close()
    end_array = merge(array_1, final_array)
    f = open('file6.txt', 'a')
    for i in end_array:
        f.write(str(i) + ' ')
    f.close()


#  The main program.
read_file()
merge_file_1()
final_file()
