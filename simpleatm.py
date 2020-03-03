# databse connectivity
import mysql.connector as mysql
db = mysql.connect(host="localhost",user="root",passwd="root123",database="atm_system")
c = db.cursor()
c.execute("use atm_system")
c.execute("select accname from details")
accname =c.fetchall()
accountHoldersName = accname[0]
c.execute("select accno from details")
accno=c.fetchall()
accountNumber = accno[0]
c.execute("select pincode from details")
pincode =c.fetchall()
pinCode = pincode[0][0]
c.execute("select balance from details")
balance1 =c.fetchall()
balance = balance1[0][0]
db.commit()
db.close()


def main():
    
    flag = False
    for i in range (0,999999999): #so the loop runs almost infinite many times
        print("""
    \t\t Welcome To ATM system
""")
        inputName = input("Enter Your Name: ")

        inputPin = 0000 #if pin is wrong it will be use as this is assigned before referance.
        index = 0 #if pin is wrong it will be use as this is assigned before referance.
        for name in accountHoldersName:
            count = 0
            if name == inputName:
                index = count #index of name is stored and if the pin of that index is same user will be given access to the account.
                inputPin = input("\nEnter Pin Number: ")
            count += 1

        if inputPin == pinCode:
            flag = True
        else:
            print("Invalid data.")
            flag = False
            continue
        if flag == True:
            print("\nYour account number is: ",accountNumber[index])
            print("Your account balance is: Rs.", balance)
            drawOrDeposite = input("\nDo you want to draw or deposit cash (draw/deposite/no): ")
            if drawOrDeposite == "draw":
                amount = input("\nEnter the amount you want to draw: ")
                try: #Exception handling
                    amount = int(amount)
                    if amount > balance[index]:
                        raise
                except:
                    print("invalid amount.")
                    continue
                remainingBalalnce = balance[index] - amount #subtracting the drawed amount.
                balance.remove(balance[index]) #removing the old ammount from the list and adding the new list after draw.
                balance.insert(index,remainingBalalnce)
                availableBalance = print("\nYour available balance is: ",remainingBalalnce)
            elif drawOrDeposite == "deposite":
                amount = input("Enter the amount you want to deposite: ")
                try:
                    amount = int(amount)
                    if amount > balance[index]:
                        raise
                except:
                    print("invalid amount.")
                    continue
                remainingBalalnce = balance[index] + amount #adding the deposited amount.
                balance.remove(balance[index])#removing the old ammount from the list and adding the new list after draw.
                balance.insert(index,remainingBalalnce)
                availableBalance = print("Your available balance is: ",remainingBalalnce)
            

main()




