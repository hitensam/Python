funcn.py
#a is the account number inputted while logging in
#COND ADDED TO SOME LAST USE 1,2
import datetime
import time
import pymysql
import random
import requests
con=pymysql.connect(host="localhost",user="root",passwd="12345",database="project")
cur=con.cursor()
def send_event(api_key="eBeURBw5Jr_kggWqLnsBFLEX2OGlHdKUwvOKSuvcwkW", event="message", value1=None, value2=None, value3=None):
        url = 'https://maker.ifttt.com/trigger/{e}/with/key/{k}/'.format(e=event,k=api_key)
        payload = {'value1': value1, 'value2': value2, 'value3': value3}
        return requests.post(url, data=payload)
def num_verific(c,a):
        ran_no=random.randint(1000,9999)
        print("AN OTP has been sent to your mobile number")
        print(ran_no)
        d="91"+c
        send_event(value3=ran_no,value1=d)
        otp=int(input("ENTER YOUR OTP"))
        if otp!=ran_no:
                print("PLEASE ENTER A VALID NUMBER/OTP.")
                time.sleep(0.5)
                number_field(a)
        else:
                u=str(c)
                v="update bank set telephone_number=%s where account_number=%s"
                flushdata(u,v,a)
                        
def check(verific,c,a):
        if verific==10:
                num_verific(c,a)
        else:
                print("PLEASE ENTER A VALID NUMBER.")
                time.sleep(0.5)
                number_field(a)
                                            
def number_field(a):
        u=int(input("enter updated telephone_number"))        
        c=str(u)
        verific=len(c)
        check(verific,c,a)
def flushdata(u,v,a):
        d="update bank set LAST_use=%s where account_number=%s"
        x= datetime.datetime.now()
        y=x.strftime("%c")
        l=[]
        l=[u,a]
        l1=[]
        l1=[y,a]
        cur.execute(v,l)
        con.commit()
        cur.execute(d,l1)
        con.commit()
        print("Value Updated")
def deposit(a):
    b=int(input("enter amount to be deposited"))
    c="update bank set balance=balance+%s where account_number=%s"
    d="update bank set LAST_use=%s where account_number=%s"
    x= datetime.datetime.now()
    y=x.strftime("%c")
    l=[]
    l1=[]
    l1=[y,a]
    l=[b,a]
    cur.execute(c,l)
    con.commit()
    cur.execute(d,l1)
    con.commit()
    
    print("amount deposited")
def transaction(a):
    tr=int(input("enter amount to be transfered"))
    ac=int(input("enter account number "))
    check_ac="SELECT * from bank where account_number=%s"
    l_check=[ac]
    cur.execute(check_ac,l_check)
    final_check=cur.fetchone()
    if final_check==None:
            print("THE ENTERED ACCOUNT NUMBER DOES NOT EXIST. PLEASE TRY AGAIN")
            transaction(a)
            
            
    else:
            check="select balance from bank where account_number=%s"
            l=[a]
            cur.execute(check,l)
            balance=cur.fetchone()
            data=balance[0]
            if (data>=tr):
                q="update bank set balance=balance-%s where account_number=%s"
                d="update bank set LAST_use=%s where account_number=%s"
                x=datetime.datetime.now()
                y=x.strftime("%c")
                l=[]
                l=[tr,a]
                cur.execute(q,l)
                con.commit()
                c="update bank set balance=balance+%s where account_number=%s"
                l1=[]
                l1=[tr,ac]
                l2=[]
                l2=[y,a]
                cur.execute(c,l1)
                con.commit()
                cur.execute(d,l2)
                con.commit()
                print("AMOUNT TRANSFER SUCCESSFULL.")
            else:
                d="update bank set LAST_use=%s where account_number=%s"
                x=datetime.datetime.now()
                y=x.strftime("%c")
                l2=[]
                l2=[y,a]
                cur.execute(d,l2)
                print("YOU HAVE INSUFFICIENT BALANCE FOR THE TRANSACTION. DEPOSIT MONEY AND TRY AGAIN")
    

def withdraw(a):
    p=int(input("enter amount to be withdrawn"))
    check="select balance from bank where account_number=%s"
    l=[a]
    cur.execute(check,l)
    balance=cur.fetchone()
    data=balance[0]
    if (data>=p):
        q="update bank set balance=balance-%s where account_number=%s"
        d="update bank set LAST_use=%s where account_number=%s"
        x= datetime.datetime.now()
        y=x.strftime("%c")
        l=[]
        l=[p,a]
        l1=[]
        l1=[y,a]
        cur.execute(q,l)
        con.commit()
        cur.execute(d,l1)
        con.commit()
        print("amount withdrawn")
    else:
        d="update bank set LAST_use=%s where account_number=%s"
        x=datetime.datetime.now()
        y=x.strftime("%c")
        l2=[]
        l2=[y,a]
        cur.execute(d,l2)
        print("YOU HAVE INSUFFICIENT BALANCE FOR THE TRANSACTION. DEPOSIT MONEY AND TRY AGAIN")
        

def display(a):
     s="select * from bank where account_number=%s"
     d="update bank set LAST_use=%s where account_number=%s"
     x= datetime.datetime.now()
     y=x.strftime("%c")
     l=[]
     l=[a]
     l1=[]
     l1=[y,a]
     cur.execute(s,l)
     data=cur.fetchall()
     print("Account Number, Address, Telephone Number, Age, Balance, DOJ ,LAST USE")
     for i in data :
          print(i)
     cur.execute(d,l1)
     con.commit()
     con.commit()

def update(a):
    print("MENU\n1)ENTER (A/a) FOR ADDRESS.\n2)ENTER (T/t) FOR TELEPHONE NUMBER\n3)ENTER (E/e) FOR EMAIL.")
    up=input("which field do you want to change ?")
    if(up=="A" or up=="a"):
        u=input("enter the updated address")
        v="update bank set address=%s where account_number=%s"
        print("BANK WILL VERIFY YOUR ADDRESSS in 3-5 WORKING DAYS")
        flushdata(u,v,a)
    elif(up=="t"or up=="T"):
            number_field(a)     
    elif(up=="E" or up=="e"):
        u=input("Enter New Email")
        v="update bank set EMAIL=%s where account_number=%s"
        flushdata(u,v,a)
    else:
        print("ENTER A VALID CHOICE")
        update(a)
        
    
   

def delete(a):
    sure=input("ENTER (Y/y) IF YOU WANT TO DELETE YOUR ACCOUNT.")
    if sure=="Y" or sure=="y":
         w="delete from bank where account_number=%s"
         d="update bank set LAST_use=%s where account_number=%s"
         x= datetime.datetime.now()
         y=x.strftime("%c")
         l=[]
         l=[a]
         l1=[]
         l1=[y,a]
         cur.execute(w,l)
         con.commit()
         cur.execute(d,l1)
         con.commit()
         print("Your Account will be deleted in 3 to 5 working days")
         con.close()
         
def logout():
    print("logged out")
    con.close()
    exit()



