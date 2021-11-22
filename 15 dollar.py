word=input("Enter the string ")
first_char=word[0]
new_word=first_char + word[1:].replace(first_char,"$")
print(new_word)
