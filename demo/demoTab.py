# toto = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# toto.insert(3, 2.5)
# toto.insert(3, "Quentin")

# # toto.reverse()

# # tab.append("test")

# print(toto)

# # -----------------

tab = ["e1", "e2", "e3"] # 3
#       0     1     2 

i = 0

while i <= len(tab) - 1:
    #       3
    print("Element :", tab[i])
    i += 1

# # -----------------

toto = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#         [                ]     

# print(toto[4]) # 4
# print(toto[4:6]) # [4, 5] ou [4, 5, 6]
# print(toto[:6]) # [0, 1, 2, 3, 4, 5]
# print(toto[0:6]) # [0, 1, 2, 3, 4, 5]
# print(toto[4:]) # [4, 5, 6, 7, 8, 9]
# print(toto[:]) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(toto[]) # PAS OK
# print(toto[1:8:2]) # [1, 3, 5, 7]
totoJ = toto[1:8] # 
print(totoJ[::-1])
# print(toto[::-1])

# 04/10/2021
array = [5, 750, 110, 6, 2, 1] # 6
#        0   1    2   3  4  5  array[6] => out of range exception
#        0  1  2  3  4  5  array[-1] => 1
#        0  1  2  3  4  5  array[4:5] => [2] 
#        0  1  2  3  4  5  array[2:5] => [1, 6, 2] 
#        0  1  2  3  4  5  array[:5] => [5, 750, 110, 6, 2]
#        0  1  2  3  4  5  array[2:] => [110, 6, 2, 1]
#        0  1  2  3  4  5  array[2::2] => [110, 2]
#                               [départ:arrivé:pas]
#        0  1  2  3  4  5  array[-2] => [1, 6, 750]

# print(array[::-2])