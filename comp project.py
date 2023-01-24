import random
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='amaatra',database='bank')
if con.is_connected():
    print("Connected Successfully")
else:
    print("Connection not established!!!")
cursor=con.cursor()
print("WELCOME TO THE D.A. BANK")
print("1. Login")
print("2. Create Bank Account")
v=int(input("Enter your choice :"))
def menu():
    print("Welcome !")
    print("What would you like to do today.")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Transaction")
    print("4. View Transaction history")
    print("5. Delete your Bank Account")
    ch=int(input("Enter your Choice :"))
    if ch==1:
        withdraw=int(input("Enter the amount you want to withdraw:"))
        cursor.execute("select balance from account_holders where account_number = {}".format(acc_no,))
        data_w= cursor.fetchone()
        withdraw_new = data_w[0] - withdraw
        cursor.execute("update account_holders set balance={} where account_number={}".format(withdraw_new,acc_no))
        con.commit()
        print("Amount withdrawn successfully!")
        terminator()
    elif ch==2:
        deposit=int(input("Enter the amount you want to deposit:"))
        cursor.execute("select balance from account_holders where account_number = {}".format(acc_no,))
        data_d = cursor.fetchone()
        deposit_new = data_d[0] + deposit
        cursor.execute("update account_holders set balance={} where account_number={}".format(deposit_new,acc_no))
        con.commit() 
        print("Amount depositied successfully!")
        terminator()
    elif ch==3:
        to_acc=int(input("Enter the Account Number to which you want to transfer money :"))
        cursor.execute("select account_number from account_holders where account_number = {}".format(to_acc,))
        data_to = cursor.fetchone()
        if data_to[0]==to_acc:
            amt=int(input("Enter the amount to be transferred:"))
            cursor.execute("select balance from account_holders where account_number = {}".format(to_acc,))
            data_dt=cursor.fetchone()
            cursor.execute("select balance from account_holders where account_number = {}".format(acc_no,))
            data_wt=cursor.fetchone()
            data_new_wt= data_wt[0]-amt
            data_new_dt= data_dt[0]+amt
            cursor.execute("update account_holders set balance={} where account_number={}".format(data_new_wt,acc_no))
            con.commit()
            cursor.execute("update account_holders set balance={} where account_number={}".format(data_new_dt,to_acc))
            con.commit()
            statement="From:"+str(acc_no)+" To:"+str(to_acc)+" Amount:"+str(amt)
            cursor.execute("update account_holders set transaction='{}' where account_number={}".format(statement,acc_no))
            con.commit()
            print("Transaction Successful!")
            terminator()
    elif ch==4:
        cursor.execute("select trancsaction from account_holders where account_number={}".format(acc_no,))
        data_trans=cursor.fetchone()
        print("Your Transaction History is:")
        print(data_trans[0])
        terminator()
    elif ch==5:
        check_name=input(print("Please enter your last name to confirm:"))
        check_add=input(print("Please enter your address to confirm:"))
        check_ph=input(print("Enter your Phone number to confirm:"))
        cursor.execute("select last_name,address,phone from account_holders where account_number={}".format(acc_no,))
        data_del=cursor.fetchone()
        if (check_name==data_del[0] and check_add==data_del[1] and check_ph==data_del[2]):
            cursor.execute("delete from account_holders where account_number={}".format(acc_no,))
            cursor.commit()
            print("Deleted successfully!")
            terminator()
        else:
            print("Entered Details are wrong!!")
            terminator()
    elif ch>5:
        print("Invalid option!! Please enter a valid number.")
        terminator()
def terminator():
    exit()
if v==1:
    acc_no=int(input("Enter your Account Number :"))
    PIN=int(input("Enter your PIN :"))
    cursor.execute("select account_number from account_holders where account_number = %s" %acc_no)
    data_acc = cursor.fetchone()
    cursor.execute("select pin from account_holders where pin = %s" %PIN)
    data_pin = cursor.fetchone()
    if (data_acc[0]==acc_no and data_pin[0]==PIN):
        print("Login Successful!")
        menu()
    else:
        print("Account Number or PIN enetered is invalid!!!")
        terminator()
elif v==2:
    phone_no=int(input("Enter your Phone Number :"))
    address=input("Enter your Permanent Address:") 
    amt_to_credit=int(input("Enter the amount to be credited :"))
    first_nam=input("Enter your First Name:") 
    last_nam=input("Enter your Last Name:")
    pin=random.randint(100000,999999)
    cursor.execute("select count(*) from account_holders")
    x=cursor.fetchone()
    ass_acc_no= 194730400000+x[0]
    cursor.execute("insert into account_holders values({},{},'{}','{}','{}',{},{},'{}')".format(ass_acc_no,pin,first_nam,last_nam,address,phone_no,amt_to_credit,"Trans: "))
    con.commit()
    print(first_nam," your Account Number is ",ass_acc_no,"and your assigned PIN is ",pin)
    print("Account Information Stored Successfully!")
else:
    print("Invalid Option!!! Please try again with a valid number.")
    terminator()
#end of code