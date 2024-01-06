import BackEnd

global userdetails

def Login():
  log = input("\nEnter Username:  ")
  psw = input("\nEnter your Password:  ")
  pin = (input("\nEnter your PIN: "))
  b = [log, psw, pin]
  checkInfo(b)

def User():
  l = input('''1. Login
2. Sign up

''')
  if l == "1":
    Login()
  elif l == "2":
    Signup()

def Signup():
  si = input("\nEnter Username: ")
  passw = input("\nEnter Password: ")
  pi = input("\nEnter PIN: ")
  X = [si, passw, pi, "0"]
  InputValue(X)
  print("\nProcessing......")
  for s in range(1, 1000000):
    pass
  print("\nYour Account has been registered \nWelcome to Srujeeth and Aaditya Unlimited Bank where your money is 'Very Safe'")
  for i in range(1, 10000000):
    pass
  User()

def Start():
  print("\nPlease Insert your ATM Card")
  choice = input("Card Inserted? (Y/N): ")

  if (choice == "Y" or choice == "y"):

    print("\nProcessing........")
    for i in range(0, 10000000):
      pass
      Login()
      break
  else:
    print("Card not inserted, please insert your ATM card\n")
    Start()

def checkInfo(details):
  UserDetails(details[0])
  if userdetails[1] == details[1] and userdetails[2] == details[2] and userdetails[0] == details[0]:
    Menu()
  else:
    print("\nInvalid Details")
    User()

def Menu():
  global userdetails
  
  balance = int(userdetails[3])

  print("\n")
  print("₹-BANKING MENU-₹".center(65, "-"))
  print("""

  1. Deposit
  2. Withdraw
  3. Check Balance
  4. Exit
  """)
  print("-".center(65, "-"))

  choice = input("\nSelect a banking option: ")

  if choice == "1":
    print("\nDirecting to Deposit Page....")

    for i in range(0, 10000000):
      pass

    deposit = int(input("\nPlease enter the deposit amount: ₹"))
    balance = deposit + balance

    Balance([str(balance), userdetails[0]])

    print("\n\nProcessing Transaction....\n")

    for i in range(0, 10000000):
      pass
    print("\nYour final balance is: ₹", balance)
    userdetails[3] = str(balance)
    Receipt(balance, deposit,"Deposit", "   ")

  elif choice == "2":
    print("\nDirecting to Withdrawl Page....")
    for i in range(0, 10000000):
      pass

    withdraw = int(input("\nEnter withdrawl amount: ₹"))
    balance = balance - withdraw
    Balance([str(balance), userdetails[0]])
    userdetails[3] = str(balance)

    print("\nProcessing Transaction....\n")

    for i in range(0, 10000000):
      pass
    if (balance <= 0):
      print("Insufficient Balance, Cannot Process Transaction!\n")
      Menu()
    else:
      print("Your final balance is: ₹", balance)
      Receipt(balance, withdraw, "Withdraw", "  ")

  elif choice == "3":
    print("\nYour Account Balance: ", "₹" + userdetails[3])
    i = input("\nPress 1 to go to Exit or 0 to Menu: ")
    if (i == "0"):
      Menu()
    elif (i == "1"):
      Exit()
  elif choice == "4":
    Exit()

def Receipt(balance,amt,Str,Space):
  CardNum = userdetails[4]

  a = input("\n\nWould you like a receipt: (Y/N): ")

  if a == "Y" or a == "y":
    print("\n\nPrinting Receipt.......")
    for i in range(0, 10000000):
      pass

    print("""
      \t\tTransaction Receipt:\n
      \t\tCard Number:       XXXX-XXXX-'{}'
      \t\t'{}' Amount:'{}'""".format(CardNum[8:12:1],Str,Space).replace("'",""),
             "₹"+ str(amt),
            end=" ")
    print("""
      \t\tBalance:          """, "₹" + str(balance))
    SubMenu()

  elif a == "N" or a == "n":
    SubMenu()

def SubMenu():
  b = int(input("\nPress 1 to exit or 0 to go to Menu: "))
  if b == 1:
    print("\nExiting.......")
    for i in range(0, 10000000):
      pass
    print("\nPlease collect your ATM Card\n")
    print("₹-Thank You For Banking With Srujeeth and Aaditya Unlimited Bank-₹".center(65, "-"))
  elif b == 0:
    Menu()

def Exit():
  print("\nExiting.......")
  for i in range(0, 10000000):
    pass
  print("\nPlease collect your ATM Card\n")
  print("₹-Thank You For Banking With Srujeeth and Aaditya Unlimited Bank-₹".center(65, "-"))

def InputValue(UserInfo):

  BackEnd.Encrypt(UserInfo, "Encr")

def UserDetails(username):
  global userdetails
  userdetails = BackEnd.Encrypt([username], "Decr")

def Balance(balance):
  BackEnd.Encrypt(balance, "Balance")

if BackEnd.l == True:
  x = "₹-WELCOME TO BANK OF SRUJEETH AND AADITYA UNLIMITED-₹"
  print(x.center(65, "-"))
  User()
