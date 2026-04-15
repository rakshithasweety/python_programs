s=input("Enter a string:")
for ch in s:
    if ch.lower() in "aeiou":
        continue
    print(ch,end=" ")
