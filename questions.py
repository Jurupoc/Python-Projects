def verify_number_in_a_list(number, array):
    return number in array


def find_duplicate_number(array):
    duplicate, seen = set(), set()
    for element in array:
        if element in seen:
            duplicate.add(element)
        seen.add(element)
    return duplicate


def check_anagram(string_a, string_b):
    return set(string_a) == set(string_b)


def remove_duplicate(array):
    return list(set(array))


def find_pair_element_with_sum_x(array, x):
    pair = []
    for (i, el_1) in enumerate(array):
        for (j, el_2) in enumerate(array[i + 1]):
            if el_1 + el_2 == x:
                pair.append((el_2, el_1))
    return pair


def check_palindrome(string):
    return string == string[::-1]


def get_missing_number(array):
    return set(range(array[len(array) - 1])[1:]) - set(array)


def get_intersection(array1, array2):
    res, array2_copy = [], array2[:]
    for element in array1:
        if element in array2_copy:
            res.append(element)
            array2_copy.remove(element)
    return res


def reverse_string(string):
    if len(string) <= 1: return string
    return reverse_string(string[1:]) + string[0]


def quick_sort(array):
    if not array:
        return []
    return quick_sort([x for x in array[1:] if x < array[0]]) + array[0:1] + \
        quick_sort([x for x in array[1:] if x >= array[0]])


def get_permutations(string):
    if len(string) <= 1:
        return set(string)
    smaller = get_permutations(string[1:])
    perms = set()
    for x in smaller:
        for pos in range(0, len(x)+1):
            perm = x[:pos] + string[0] + x[pos:]
            perms.add(perm)
    return perms


def main():
    pass


if __name__ == '__main__':
    main()
