import math 

number = input('Enter Numbers:> ')
lst = number.split(' ')
tot = 0
lst_1 = []
for i in lst:
    i = float(i)
    # print(f'Vlaue of delta lamda {i / 3200}')
    # print(f"diffraction angle {i} ==> {i - 326.010}")

    # sin_value = math.sin(math.radians(i))
    # cos_vlaue = math.cos(math.radians(i))
    # cot_value = cos_vlaue/sin_value
    # print(f'delta d with respct theta {cot_value * 0.0001903 }')
    # print(f"lamdas k=1 indirect measurements {i} ==> {(sin_value / (80)) * 1000000}")
    # print(f"lamdas k=2 indirect measurements {i} ==> {(sin_value / (2* 80)) * 1000000}")

    # tot = tot + i
# print(f'Avergae height {tot / 10}')
    value = ((0.004418- i) ** 2)
    lst_1.append(value)
    # print(value)
    
# print(lst_1)
total_sum = 0
for j in lst_1:
    j = float(j)
    total_sum = total_sum + j
print(math.sqrt(total_sum) / math.sqrt(20))
# # print(total_sum)