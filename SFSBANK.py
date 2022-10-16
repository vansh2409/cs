#<==========================IMPORTS========================>
#FOR CONNECTING SQL 
import mysql.connector as a
#<======================CONNECTING SQL=====================>
db2 = a.connect(host="localhost",user="root",password="1234",database="bank", auth_plugin = 'mysql_native_password')
cursor = db2.cursor()
#<===========================FUNCTIONS=====================>
#DEFINING A FUNCTION TO OPEN A NEW ACCOUNT 
def openAcc():
    #ACQUIRING USER
     n= input("Enter Name :")
     ac= input ("Enter Account No:")
     db= input ("Enter D.O.B:")
     p= input ("Enter Phone:")
     ad= input("Enter Address:")
     ob= int(input("Enter Opening Balance:"))
     data1 =(n,ac,db,ad,p,ob)
     data2 =(n,ac,ob)
     sql1="insert into account values(%s,%s,%s,%s,%s,%s)"
     sql2="insert into amount values(%s,%s,%s)"
     c=db2.cursor()
     c.execute(sql1,data1)
     db2.commit()
     c.execute(sql2,data2)
     db2.commit()
     print("Data Entered Succesfully")

#DEFINING A FUNCTION TO DEPOSIT AMOUNT
def depoAmo():
     am= int(input ("Enter Amount:"))
     ac= input ("Enter Account No:")
     #ACQUIRING THE CURRENT AMOUNT FROM THE DATABASE
     a="Select balance from amount where acno=%s"
     data=(ac,)
     c=db2.cursor()
     c.execute(a,data)
     myresult=c.fetchone()
     #ADDING THE NEW AMOUNT ENTERED BY THE USER TO THE CURRENT AMOUNT
     tam=myresult[0]+am
     sql="update amount set balance =%s where acno =%s"
     d=(tam,ac)
     c.execute(sql,d)
     db2.commit()
     print("amount deposited successfully")
     
#DEFINING A FUNCTION TO WITHDRAW AMOUNT
def witham():
    am= int(input ("Enter Amount:"))
    ac= input ("Enter Account No:")
    #ACQUIRING THE CURRENT AMOUNT FROM THE DATABASE
    a="Select balance from amount where acno=%s"
    data=(ac,)
    c=db2.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    #SUBTRACTING THE NEW AMOUNT ENTERED BY THE USER FROM THE CURRENT AMOUNT
    tam=myresult[0]-am
    sql="update amount set balance =%s where acno =%s"
    d=(tam,ac)
    c.execute(sql,d)
    db2.commit()
    print("amount deposited successfully")
    
#DEFINING A FUNCTION TO CHECK USER BALANCE
def balance():
    ac= input ("Enter Account No:")
    a="Select balance from amount where acno=%s"
    data=(ac,)
    c=db2.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    print("balance for account :",ac,"is",myresult[0])
    
#DEFINING A FUNCTION TO DISPLAY ACCOUNT DETAILS 
def dispacc():
    ac= input ("Enter Account No:")
    a="Select *from account where acno=%s"
    data=(ac,)
    c=db2.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    for i in myresult:
        print(i,end=" ")
    
#DEFINING A FUNCTION TO CLOSE ACCOUNT
def closeac():
    ac= input ("Enter Account No:")
    sql1="delete from account where acno=%s"
    sql2="delete from amount where acno=%s"
    data=(ac,)
    c=db2.cursor()
    c.execute(sql1,data)
    c.execute(sql2,data)
    db2.commit()
    print("account closed succesfully")

def main():
    print("""
 
 
░██████╗███████╗░██████╗  ██████╗░░█████╗░███╗░░██╗██╗░░██╗
██╔════╝██╔════╝██╔════╝  ██╔══██╗██╔══██╗████╗░██║██║░██╔╝
╚█████╗░█████╗░░╚█████╗░  ██████╦╝███████║██╔██╗██║█████═╝░
░╚═══██╗██╔══╝░░░╚═══██╗  ██╔══██╗██╔══██║██║╚████║██╔═██╗░
██████╔╝██║░░░░░██████╔╝  ██████╦╝██║░░██║██║░╚███║██║░╚██╗
╚═════╝░╚═╝░░░░░╚═════╝░  ╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝


 > 1 | OPEN NEW ACCOUNT
 > 2 | DEPOSIT AMOUNT
 > 3 | WITHDRAW AMOUNT
 > 4 | BALANCE ENQUIRY
 > 5 | DISPLAY CUSTOMER DETAILS
 > 6 | CLOSE EXISTING ACCOUNT
""")
main()    
choice =input("Enter task No:")
print (">------------------------------------------------------<")
if (choice =='1'):
    openAcc()
elif(choice=='2'):
    depoAmo()
elif(choice=='3'):
    witham()
elif(choice=='4'):
    balance()
elif(choice=='5'):
    dispacc()
elif(choice=='6'):
    closeac()
else:
    print ("Wrong Choice! Try Again!")
    main()