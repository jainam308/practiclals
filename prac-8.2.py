def rem_dup(l):
    f_l=[]
    for num in l:
        if num not in f_l:
            f_l.append(num)
    return f_l
l=[2,2,1,1,3,4]
print(rem_dup(l))