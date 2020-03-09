from flask import Flask
import hashlib
app = Flask(__name__)

#************Caeser Cypher
def Caeser(txt, n=3):
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
def Railfence(text, key=2):
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

#***************SHA224
def SHA224(str):
    result = hashlib.sha224(str.encode())
    return(result.hexdigest())

@app.route('/<int:l>/<int:e1>/<int:e2>/<int:e3>/<int:e4>/<int:e5>/<ct>')
def main(l,e1,e2,e3,e4,e5,ct):
    ChEn=[]
    ChEn.append(e1)
    ChEn.append(e2)
    ChEn.append(e3)
    ChEn.append(e4)
    ChEn.append(e5)
    #Layering Begins here
    cypherText=ct
    for i in range(l):
        if ChEn[i]==0:
            cypherText=cypherText
        elif ChEn[i]==1:
            cypherText=Caeser(cypherText)
            print("Encryption after Caeser Cypher:")
            print(cypherText)
        elif ChEn[i]==2:
            cypherText=Railfence(cypherText)
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
    return cypherText
