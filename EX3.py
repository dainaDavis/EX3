Array2D = eval(input())
integer = 0
sum = 0
for number in Array2D:
    for i in number:
        integer += i
        sum +=1
integer = integer/sum
print(int(integer))