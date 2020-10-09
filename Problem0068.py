import itertools as iter

L1 = [0,5,6]
L2 = [1,6,7]
L3 = [2,7,8]
L4 = [3,8,9]
L5 = [4,9,5]
line_list = [L1,L2,L3,L4,L5]
my_array = [0] * 10

my_array[0] = 6

result_list = []
permutation_list_2 = list(iter.permutations(range(7,11)))
for u in range(len(permutation_list_2)-1,-1,-1):
    perm2 = permutation_list_2[u]
    for i in range(4):
        my_array[i+1] = perm2[i]

    permutation_list = list(iter.permutations(range(1,6)))
    for i in range(len(permutation_list)-1,-1,-1):
        perm = permutation_list[i]
        for j in range(5):
            my_array[j+5] = perm[j]
        sum_list = []
        for line in line_list:
            total = 0
            for point in line:
                total += my_array[point]
            sum_list.append(total)
        if sum_list.count(sum_list[0]) == 5:
            number_list = ["","","","",""]
            for j in range(len(line_list)):
                line = line_list[j]
                for point in line:
                    number_list[j] += str(my_array[point])
                number_list[j] = int(number_list[j])
            min_number = min(number_list)
            min_index = number_list.index(min_number)
            result = ""
            for k in range(len(line_list)):
                result += str(number_list[(min_index+k) % len(line_list)])
            result = int(result)
            if result not in result_list:
                result_list.append(result)
print(max(result_list))
