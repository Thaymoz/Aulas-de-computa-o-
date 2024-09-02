# Use um loop for e range para somar todos os números ímpares de 1 a 300 e exiba a soma

# list = range(1,300)
# rlist= sum(list)
# list2 = range(1,300,2)
# rlist2=sum(list2)

# print(rlist-rlist2)


# for i in range(1,301,2):
#     list=range(i)
# print(sum(list))

list = 0
for i in range(1,301,2):
    list += i
print(list)