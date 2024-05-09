str1=input("Enter string 1")
str2=input("Enter string 2")

if sorted(str1)==sorted(str2):
    print("Anagram")
else:
    print("Not an anagram")