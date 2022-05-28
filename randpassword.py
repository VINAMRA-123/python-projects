import random

wordlist = []
special_char= ['@','$','&','!']

with open("timepass.txt",'r' ) as file:
    data = file.readlines()
    
    for line in data:
        words = line.split()
        
        for items in words:
            if len(items)>5:
                wordlist.append(items.capitalize())
word = random.choice(wordlist) 
schar = random.choice(special_char)
integer = str(random.randint(10,99))
password=word + schar + integer
print(password)                              

    