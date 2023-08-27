def anagrom(s1,s2):
    if(sorted(s1)==sorted(s2)):
        print("Both are anagrom")
    else:
        print("not anagrom")
s1=input("enter word")
s2=input("enter another word")
anagrom(s1,s2)