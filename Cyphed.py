#Importing necessary libraries
import hashlib

#************Caeser Cypher
def Caeser(txt, n):
    result=''
    for i in txt:
        if i==' ':
            result = result+i
        elif ord(i)>=65 and ord(i)<=90:
            result = result+chr((ord(i) + n-65) % 26 + 65)
        elif ord(i)>=97 and ord(i)<=122:
            result = result+chr((ord(i) + n-97) % 26 + 97)
        elif ord(i)>=48 and ord(i)<=57:
        		result = result+chr((ord(i) + n-48) % 10 + 48)
    return result

#***********Railfence
def Railfence(text, key):
    # create the matrix to cipher
    # plain text key = rows ,
    # length(text) = columns
    # filling the rail matrix
    # to distinguish filled
    # spaces from blank ones
    rail = [['\n' for i in range(len(text))]
            for j in range(key)]

    # to find the direction
    dir_down = False
    row, col = 0, 0

    for i in range(len(text)):

        # check the direction of flow
        # reverse the direction if we've just
        # filled the top or bottom rail
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down

        # fill the corresponding alphabet
        rail[row][col] = text[i]
        col += 1

        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    # now we can construct the cipher
    # using the rail matrix
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return ("".join(result))


#**************SHA512
# encoding GeeksforGeeks using encode()
# then sending to SHA512()
def SHA512(str):
    result = hashlib.sha512(str.encode())
    return (result.hexdigest())


#***************SHA256
def SHA256(str):
    result = hashlib.sha256(str.encode())
    return(result.hexdigest())

#***************SHA1
def SHA1(str):
    result = hashlib.sha1(str.encode())
    return(result.hexdigest())

#***************SHA2
def SHA224(str):
    result = hashlib.sha224(str.encode())
    return(result.hexdigest())


#***********MD5
"""def MD5(txt):
    result = hashlib.md5()

    result.update(txt.encode())

    result = result.digest()
    return result"""

#%%%%%%%MAIN DRIVER FUNCTION
print("WELCOME TO CYPHED")
#Taking necessary inputs
print("How many layers do you want in your encryption? Please enter atmost 5 types")
l=int(input())
ChEn=[]
print("We offer the following types of encryption:\n1. Caesar Cypher\n2.Railfence Cypher\n3.SHA1\n4.SHA224\n5.SHA256\n6.SHA2512\n7.MD5\n8.")
print("Choose",l,"items from the list")
for i in range(l):
    a=int(input())
    ChEn.append(a)
print("Enter text to be Encrypted")
plainText=input()
cypherText=plainText
#Layering Begins here
for i in range(l):
    if ChEn[i]==1:
        print("For Caeser Cypher, enter the KEY value ")
        s=int(input())
        cypherText=Caeser(cypherText,s)
        print("Encryption after Caeser Cypher:")
        print(cypherText)
    elif ChEn[i]==2:
        print("For Railfence, enter number of RAILS ")
        s=int(input())
        cypherText=Railfence(cypherText,s)
        print("Encryption after Railfence: ")
        print(cypherText)
    elif ChEn[i] == 3:
        print("The hexadecimal equivalent of SHA1 is : ")
        cypherText = SHA1(cypherText)
        print(cypherText)
    elif ChEn[i]==4:
        print("The hexadecimal equivalent of SHA224 is : ")
        cypherText = SHA224(cypherText)
        print(cypherText)
    elif ChEn[i]==5:
        print("The hexadecimal equivalent of SHA256 is : ")
        cypherText = SHA256(cypherText)
        print(cypherText)
    elif ChEn[i]==6:
        print("The hexadecimal equivalent of SHA512 is : ")
        cypherText=SHA512(cypherText)
        print(cypherText)
    elif ChEn[i]==7:
        cypherText=BlowFish(cypherText)
    elif ChEn[i]==8:
        cypherText=AES(cypherText)






