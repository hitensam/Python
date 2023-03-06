#!/usr/bin/python
# -*- coding: utf-8 -*-
compilecode.py
import random
import pymysql
import datetime
import funcn as link  # funcn is a user defined library
import requests  # Requests is a python library
import time
x = datetime.datetime.now()

# *************************SQL CONNECTION*************************************************************************************************************************************************

con = pymysql.connect(host='localhost', user='root', passwd='12345',
                      database='project')
cur = con.cursor()
k = \
    'create table Bank(account_number bigint primary key,name varchar(40),address varchar(100),telephone_number bigint,EMAIL varchar(100), AGE int,balance bigint,DOJ varchar(100),LAST_use varchar(100))'
cur.execute(k)
con.commit()
x = datetime.datetime.now()
y = x.strftime('%c')

n1 = 'insert into Bank values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'

p1 = [
    1126357891019,
    'Ram Nath Kovind',
    'Rashtrapati Bhavan Rajpath New Delhi',
    9843097509,
    'unspecified',
    73,
    1000000,
    y,
    '',
    ]
cur.execute(n1, p1)
con.commit()
p2 = []
p2 = [
    1126357865432,
    'Narendra Damodardas Modi',
    '7, Lok Kalyan Marg New Delhi',
    9848906750,
    'unspecified',
    68,
    100000,
    y,
    'TODAY',
    ]
cur.execute(n1, p2)
con.commit()
p3 = []
p3 = [
    1126357865007,
    'James bond',
    ' 007 SkyfallDelhi',
    9900886677,
    'unspecified',
    55,
    10000,
    y,
    'TODAY',
    ]
cur.execute(n1, p3)
con.commit()

# ******************************************FROM HERE SQL COMMANDS ENDS.*******************************************************************************

f = open('Bank.txt', 'a')  # userid,password,account number
f.write('u234 abc@1234 1126357891019\n ')
f.write('u567 pqr@5678 1126357865432\n')
f.write('u143 xyz@9045 1126357865007\n')  # not enter
f.close()


def choices(a):
    while True:
        print """1.Deposit
2.Transaction
3.Withdraw
4.Display
5.Update
6.Delete
7.Logout"""
        ch = input('Enter the number of choice')
        if ch == '1':
            link.deposit(a)
        elif ch == '2':
            link.transaction(a)
        elif ch == '3':
            link.withdraw(a)
        elif ch == '4':
            link.display(a)
        elif ch == '5':
            link.update(a)
        elif ch == '6':
            link.delete(a)
            start(
                r1=None,
                r2=None,
                r3=None,
                r5=None,
                r6=None,
                s1=None,
                s2=None,
                s3=None,
                s5=None,
                verific=None,
                c=None,
                )
        elif ch == '7':

            start(
                r1=None,
                r2=None,
                r3=None,
                r5=None,
                r6=None,
                s1=None,
                s2=None,
                s3=None,
                s5=None,
                verific=None,
                c=None,
                )
        else:

            print 'ENTER A VALID CHOICE'


def num_verific(
    c,
    r1,
    r2,
    r3,
    r4,
    r5,
    s1,
    mail,
    ):
    ran_no = random.randint(1000, 9999)
    print 'AN OTP has been sent to your mobile number'
    print ran_no
    d = '91' + c
    send_event(value3=ran_no, value1=d)
    otp = int(input('ENTER YOUR OTP'))
    if otp != ran_no:
        print 'PLEASE ENTER A VALID NUMBER/OTP.'
        time.sleep(0.5)
        number_field(
            r1,
            r2,
            r3,
            r5,
            s1,
            mail,
            )
    else:
        flush_data(
            r1,
            r2,
            r3,
            r4,
            r5,
            s1,
            mail,
            )


def check(
    verific,
    c,
    r1,
    r2,
    r3,
    r4,
    r5,
    s1,
    mail,
    ):
    if verific == 10:
        num_verific(
            c,
            r1,
            r2,
            r3,
            r4,
            r5,
            s1,
            mail,
            )
    else:
        print 'PLEASE ENTER A VALID NUMBER.'
        time.sleep(0.5)
        number_field(
            r1,
            r2,
            r3,
            r5,
            s1,
            mail,
            )


def number_field(
    r1,
    r2,
    r3,
    r5,
    s1,
    mail,
    ):
    r4 = int(input('Enter your mobile number'))
    c = str(r4)
    verific = len(c)
    check(
        verific,
        c,
        r1,
        r2,
        r3,
        r4,
        r5,
        s1,
        mail,
        )


def flush_data(
    r1,
    r2,
    r3,
    r4,
    r5,
    s1,
    mail,
    ):
    int(r4)
    s2 = input('Enter password must have 8 Characters')
    s3 = input('Confirm Password')
    r6 = int(input('Enter amount you want to deposit in your account'))
    s4 = str(r1)
    s5 = s1 + ' ' + s2 + ' ' + s4 + '\n'
    new(
        s2,
        s3,
        s5,
        r1,
        r2,
        r3,
        r4,
        r5,
        r6,
        s1,
        mail,
        )


def send_event(
    api_key='eBeURBw5Jr_kggWqLnsBFLEX2OGlHdKUwvOKSuvcwkW',
    event='message',
    value1=None,
    value2=None,
    value3=None,
    ):
    url = \
        'https://maker.ifttt.com/trigger/{e}/with/key/{k}/'.format(e=event,
            k=api_key)
    payload = {'value1': value1, 'value2': value2, 'value3': value3}
    return requests.post(url, data=payload)


def new(
    s2,
    s3,
    s5,
    r1,
    r2,
    r3,
    r4,
    r5,
    r6,
    s1,
    mail,
    ):
    if len(s2) >= 8:
        if s2 == s3:
            con = pymysql.connect(host='localhost', user='root',
                                  passwd='12345', database='project')
            cur = con.cursor()
            f = open('Bank.txt', 'a')
            f.write(s5)
            f.close()
            x1 = datetime.datetime.now()
            y1 = x.strftime('%c')
            L = [
                r1,
                r2,
                r3,
                r4,
                mail,
                r5,
                r6,
                y1,
                y1,
                ]
            n1 = 'insert into Bank values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cur.execute(n1, L)
            con.commit()
            con.close()
            print 'Account created Successfully'
            print ('Your Account Number is', r1, 'Your User id', s1)
            print r1
            choices(r1)
        else:

            print 'Password not matched'
            s2 = input('Enter password must have 8 Characters')
            s3 = input('Confirm Password')
            new(
                s2,
                s3,
                s5,
                r1,
                r2,
                r3,
                r4,
                r5,
                r6,
                s1,
                mail,
                )
    else:

        print 'password less than 8 characters'
        s2 = input('Enter password must have 8 Characters')
        s3 = input('Confirm Password')
        new(
            s2,
            s3,
            s5,
            r1,
            r2,
            r3,
            r4,
            r5,
            r6,
            s1,
            mail,
            )


def log(l1, s):
    c = input('User id')
    b = input('Enter your Password')
    for i in range(0, s):
        if c == l1[i]:
            if b == l1[i + 1]:
                a = int(l1[i + 2])
                print 'Login successful'
                print ('Your Account Number', a)
                return a

                break
            else:
                print 'Password Invalid'
                break
            log()
        elif i == s - 1:
            print 'Account does not exist'
            log()


def acc_open():
    age_ver = int(input('ENTER YOUR AGE'))
    if age_ver >= 18 and age_ver <= 110:
        f = open('Bank.txt', 'a')
        q = random.randint(10000, 99999)
        r1 = 11263578 * 10000 + q
        a = r1
        s1 = 'u' + str(random.randint(100, 999))
        r2 = input('Enter your name')
        r3 = input('Enter your Address')
        r5 = age_ver
        mail = input('ENTER YOU EMAIL')
        number_field(
            r1,
            r2,
            r3,
            r5,
            s1,
            mail,
            )
    else:

        print 'VISIT NEAREST BRANCH WITH YOUR GUARDIAN'
        start()


def start(
    r1=None,
    r2=None,
    r3=None,
    r5=None,
    r6=None,
    s1=None,
    s2=None,
    s3=None,
    s5=None,
    verific=None,
    c=None,
    ):

    while True:
        print 'WELCOME TO BBPS BANK E-LOBBY'
        print '1.Existing User'
        print '2.New User'
        n = input('enter your choice')
        if n == '1':
            f = open('Bank.txt', 'r')
            l = f.readlines()
            l1 = []
            r = len(l)
            for i in range(0, r):

                x = l[i].split()
                for j in x:
                    l1.append(j)
            f.close()
            s = len(l1)
            a = log(l1, s)
            choices(a)
            break
        elif n == '2':

            acc_open()
        else:

            print 'ENTER A VALID CHOICE'


start(
    r1=None,
    r2=None,
    r3=None,
    r5=None,
    r6=None,
    s1=None,
    s2=None,
    s3=None,
    s5=None,
    verific=None,
    c=None,
    )
