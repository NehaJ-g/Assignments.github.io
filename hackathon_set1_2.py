inp=list(map(int,input().split()))
no_of_students=inp[0]
grades=inp[1:]
final_grades=[]
for num in grades:
    if num>=38:
        next_multiple=(num//5)+1
        difference=(next_multiple*5)-num
        if difference<3:
            final_grades.append(next_multiple*5)
        else:
            final_grades.append(num)
    else:
        final_grades.append(num)
for num in final_grades:
    print(num,end=" ")