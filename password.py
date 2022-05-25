import string
import random

s1=list(string.ascii_lowercase)
s2=list(string.ascii_uppercase)
s3=list(string.digits)
s4=list(string.punctuation)

charcters_name=input("please enter number of charcters for the password?")
while True:
    try:
        charcters_name=int(charcters_name)
        if charcters_name < 6:
            print("you should enter at least 6 charcters")
            charcters_name=input("please enter number again")

        else:
            break

    except:
        print('please enter numbers only')
        charcters_name=input("please enter number of charcters for the password?")

random.shuffle(s1)
random.shuffle(s2)   
random.shuffle(s3)   
random.shuffle(s4)      

part1=round(charcters_name*(30/100))
part2=round(charcters_name*(20/100))

password=[]
for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])

for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])


random.shuffle(password)

password_st="".join(password[0:])
print(password_st)
