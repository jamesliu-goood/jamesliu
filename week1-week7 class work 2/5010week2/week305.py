def fucntion3(word):
    first = word[0]
    last = word [len(word)-1]
    combined = last + first
    return combined.upper()


word = input("Enter  word>>") 
print(fucntion3(word))   