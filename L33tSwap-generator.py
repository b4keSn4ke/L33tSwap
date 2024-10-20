# Date: 2024-10-14
# Name: L33tSwap-generator.py
# Description: L33tSwap Rules set generation script
# Author: b4keSn4ke
# Github: https://github.com/b4keSn4ke
# Project Repo: https://github.com/b4keSn4ke/L33tSwap
# Version: 1.0
# 
#!/usr/bin/python3 

# Lowercase and uppercase letters
# Uncomment the array below if you want to permutate lowercase and uppercase letters - comment the array below if using another sets of character.
#char = ['sa@','sa4','si1','si!','se#','se3',"se\\xC2 se\\xA3","se\\xC2 se\\x80",'suv','so0','ss$','ss5','sA@','sA4','sI1','sI!','sE#','sE3',"sE\\xC2 sE\\xA3","sE\\xC2 sE\\x80",'sUV','sO0','sS$','sS5']

# Only lowercase letters - comment the array below if using another sets of character.
char = ['sa@','sa4','si1','si!','se#','se3',"se\\xC2 se\\xA3","se\\xC2 se\\x80",'suv','so0','ss$','ss5']

# Only uppercase letters - comment the array below if using another sets of character.
#char = ['sA@','sA4','sI1','sI!','sE#','sE3',"sE\\xC2 sE\\xA3","sE\\xC2 sE\\x80",'sUV','sO0','sS$','sS5']


print ("# This set of rules will try to replace vowels from a word \n# for special characters or numbers that could be interpreted like the vowels")
print ("\n# It will also append up to 2 digits from 0 to 9 at the end of the word.\n")
print ("\n# Swap 1 vowel in a word\n# for a special character looking similar\n")

for c in char:
    print(c)

print ("\n# Swap 2 vowels in a word\n# for a special character looking similar\n")
# Permutate vowels only

for i in range(len(char)):
    for j in range (i+1, len(char)):
        if char[i][1] != char[j][1]:
            print (char[i] + " " + char[j])


print ("\n# Swap 3 vowels in a word\n# for a special character looking similar\n")

for i in range(len(char)):
    for j in range (i+1, len(char)):
        for k in range (j+1, len(char)):
            if (char[i][1] != char[j][1]) and (char[j][1] != char[k][1]):
                print (char[i] + " " + char[j] + " " + char[k])

print ("\n# Swap 4 vowels in a word\n# for a special character looking similar\n")

for i in range(len(char)):
    for j in range (i+1, len(char)):
        for k in range (j+1, len(char)):
            for l in range (k+1, len(char)):
                if (char[i][1] != char[j][1]) and (char[j][1] != char[k][1]) and (char[k][1] != char[l][1]):
                    print (char[i] + " " + char[j] + " " + char[k] + " " + char[l])

print ("\n# Swap all vowels in a word\n# for a special character looking similar\n")

for i in range(len(char)):
    for j in range (i+1, len(char)):
        for k in range (j+1, len(char)):
            for l in range (k+1, len(char)):
                for m in range (l+1, len(char)):
                    if (char[i][1] != char[j][1]) and (char[j][1] != char[k][1]) and (char[k][1] != char[l][1]) and (char[l][1] != char[m][1]):
                        print (char[i] + " " + char[j] + " " + char[k] + " " + char[l] + " " + char[m])

# Permutate vowels and add a single digit (0-9)

print ("\n# Swap 1 vowel in a word\n# for a special character looking similar\n# Appending 1 digit at the end of the word (0-9)\n")

for c in char:   
    for x in range (10):
        print(c + " $" + str(x))


print ("\n# Swap 2 vowels in a word\n# for a special character looking similar\n# Appending 1 digit at the end of the word (0-9)\n")

for i in range(len(char)):
    for j in range (i+1, len(char)):
        for x in range (10):
            if char[i][1] != char[j][1]:
                print (char[i] + " " + char[j] + " $" + str(x))

print ("\n# Swap 3 vowels in a word\n# for a special character looking similar\n# Appending 1 digit at the end of the word (0-9)\n")

for i in range(len(char)):
    for j in range (i+1, len(char)):
        for k in range (j+1, len(char)):
            for x in range (10):
                if (char[i][1] != char[j][1]) and (char[j][1] != char[k][1]):
                    print (char[i] + " " + char[j] + " " + char[k]+ " $" + str(x))

print ("\n# Swap 4 vowels in a word\n# for a special character looking similar\n# Appending 1 digit at the end of the word (0-9)\n")

for i in range(len(char)):
    for j in range (i+1, len(char)):
        for k in range (j+1, len(char)):
            for l in range (k+1, len(char)):
                for x in range (10):
                    if (char[i][1] != char[j][1]) and (char[j][1] != char[k][1]) and (char[k][1] != char[l][1]):
                        print (char[i] + " " + char[j] + " " + char[k] + " " + char[l]+ " $" + str(x))

print ("\n# Swap all vowels in a word\n# for a special character looking similar\n# Appending 1 digit at the end of the word (0-9)\n")

for i in range(len(char)):
    for j in range (i+1, len(char)):
        for k in range (j+1, len(char)):
            for l in range (k+1, len(char)):
                for m in range (l+1, len(char)):
                    for x in range (10):
                        if (char[i][1] != char[j][1]) and (char[j][1] != char[k][1]) and (char[k][1] != char[l][1]) and (char[l][1] != char[m][1]):
                            print (char[i] + " " + char[j] + " " + char[k] + " " + char[l] + " " + char[m]+ " $" + str(x))


# Permutate vowels and add two digits ( 0-9)
print ("\n# Swap 1 vowel in a word\n# for a special character looking similar\n# Appending 2 digit at the end of the word (0-9)\n")

for c in char:   
    for x in range (10):
        for y in range (10):
            print(c + " $" + str(x) + " $" + str(y))


print ("\n# Swap 2 vowels in a word\n# for a special character looking similar\n# Appending 2 digit at the end of the word (0-9)\n")

for i in range(len(char)):
    for j in range (i+1, len(char)):
        for x in range (10):
            for y in range (10):
                if char[i][1] != char[j][1]:
                    print (char[i] + " " + char[j] + " $" + str(x) + " $" + str(y))

print ("\n# Swap 3 vowels in a word\n# for a special character looking similar\n# Appending 2 digit at the end of the word (0-9)\n")

for i in range(len(char)):
    for j in range (i+1, len(char)):
        for k in range (j+1, len(char)):
            for x in range (10):
                for y in range (10):
                    if (char[i][1] != char[j][1]) and (char[j][1] != char[k][1]):
                        print (char[i] + " " + char[j] + " " + char[k]+ " $" + str(x)+ " $" + str(y))

print ("\n# Swap 4 vowels in a word\n# for a special character looking similar\n# Appending 2 digit at the end of the word (0-9)\n")

for i in range(len(char)):
    for j in range (i+1, len(char)):
        for k in range (j+1, len(char)):
            for l in range (k+1, len(char)):
                for x in range (10):
                    for y in range (10):
                        if (char[i][1] != char[j][1]) and (char[j][1] != char[k][1]) and (char[k][1] != char[l][1]):
                            print (char[i] + " " + char[j] + " " + char[k] + " " + char[l]+ " $" + str(x)+ " $" + str(y))

print ("\n# Swap all vowels in a word\n# for a special character looking similar\n# Appending 2 digit at the end of the word (0-9)\n")

for i in range(len(char)):
    for j in range (i+1, len(char)):
        for k in range (j+1, len(char)):
            for l in range (k+1, len(char)):
                for m in range (l+1, len(char)):
                    for x in range (10):
                        for y in range (10):
                            if (char[i][1] != char[j][1]) and (char[j][1] != char[k][1]) and (char[k][1] != char[l][1]) and (char[l][1] != char[m][1]):
                                print(char[i] + " " + char[j] + " " + char[k] + " " + char[l] + " " + char[m]+ " $" + str(x)+ " $" + str(y))
