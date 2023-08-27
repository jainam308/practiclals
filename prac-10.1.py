def palindrome(s):
    s1=s[::-1]
    print(s,"=",s1)
    if(s==s1):
        print("palindrome")
    else:
        print("not palindrome")
palindrome("naman")