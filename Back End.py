import mysql.connector as mq

password = input("Enter mysql password: ")

Capletters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',' ','.',"'"]
Capencr_letters = ['Q', 'A', 'Z', 'W', 'S', 'X', 'E', 'D', 'C', 'R', 'F', 'V', 'T', 'G', 'B', 'Y', 'H', 'N', 'U', 'J', 'M', 'I', 'K', 'O', 'L', 'P',' ',"'",'.']

Numbers = ['1','2','3','4','5','6','7','8','9','0']
Numbersenc = ['4','5','6','7','3','2','9','1','0','8']

Smallletters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Smallencr_letters = ['q', 'a', 'z', 'w', 's', 'x', 'e', 'd', 'c', 'r', 'f', 'v', 't', 'g', 'b', 'y', 'h', 'n', 'u', 'j', 'm', 'i', 'k', 'o', 'l', 'p']

try:
    con = mq.connect(host = 'Localhost',user = 'root', password = password, database = 'BankDet')
    cur = con.cursor()
    print("Connection Successful\n")
    l = True
except:
    l = False
    print("Invalid Password Exiting...")

def Encrypt(encr,path):
    encr_sentence = ''
    encr_list = []

    if path == "Encr":
        data = CardNumber()
        encr.append(data)
    
    encryptCapDict = dict(zip((Capletters),(Capencr_letters)))
    encryptSmallDict = dict(zip((Smallletters),(Smallencr_letters)))
    encryptNumbers = dict(zip((Numbers),(Numbersenc)))

    for j in range(len(encr)):
        for i in encr[j]:
            if i in Capletters:
                encr_sentence = encr_sentence + encryptCapDict[i]
            elif i in Smallletters:
                encr_sentence = encr_sentence + encryptSmallDict[i]
            elif i in Numbers:
                encr_sentence = encr_sentence + encryptNumbers[i]
        encr_list.append(encr_sentence)
        encr_sentence = ''
    if path == "Encr":
        SQLEncr(encr_list)
    elif path == "Decr":
        a = SQLDecr(encr_list)
        return a
    elif path == "Balance":
        Balance(encr_list)

def Decrypt(dencr):
    dencr_sentence = ''
    dencr_list = []
    newdencr_list = []
    for i in dencr:
        dencr_list.append(str(i))
    
    encryptCapDict = dict(zip((Capencr_letters),(Capletters)))
    encryptSmallDict = dict(zip((Smallencr_letters),(Smallletters)))
    encryptNumbers = dict(zip((Numbersenc),(Numbers)))

    for j in range(len(dencr_list)):
        for i in dencr_list[j]:
            if i in Capletters:
                dencr_sentence = dencr_sentence + encryptCapDict[i]
            elif i in Smallletters:
                dencr_sentence = dencr_sentence + encryptSmallDict[i]
            elif i in Numbers:
                dencr_sentence = dencr_sentence + encryptNumbers[i]
        newdencr_list.append(dencr_sentence)
        dencr_sentence = ''
               
    return newdencr_list

def SQLEncr(encrlist):

    cur.execute("insert into UserInfo values('{}','{}',{},{},{})".format(encrlist[0],encrlist[1],int(encrlist[2]),int(encrlist[3]),int(encrlist[4])))
    con.commit()
    
def SQLDecr(encrlist):

    cur.execute("Select * from UserInfo where Username = '{}'".format(encrlist[0]))

    data = cur.fetchone()
    a = Decrypt(data)
    return a 

def CardNumber():

    cur.execute("Select count(Username) from UserInfo")
    data = cur.fetchone()
    cardnumber = 100000000000 + data[0] + 1
    return str(cardnumber)

def Balance(encrlist):

    cur.execute("Update UserInfo set Balance = '{}' where username = '{}'".format(encrlist[0],encrlist[1]))
    con.commit()
