#LIM ZI HONG
#TP064970
import datetime

def gen_new_cusid(): #auto generate new customer id
    i=1
    default_no = "00000"
    with open('user.txt','r') as cus_no:
        lines = cus_no.readlines()

    for line in lines:
        if line[:3]== "CUS":
            i = i+1

    no =str(i)
    nextid = "CUS" + default_no[:len(default_no)-len(no)]+no
    return nextid

def gen_new_staffid(): #auto generate new customer id
    i=1
    default_no = "00000"
    with open('user.txt','r') as staff_no:
        lines = staff_no.readlines()

    for line in lines:
        if line[:5]== "STAFF":
            i = i+1
        
    no =str(i)
    nextid = "STAFF" + default_no[:len(default_no)-len(str(i))]+str(i)
    return nextid

def change_password():
    edit_list=[]
    with open ("user.txt","r") as read:
        userdetails = read.readlines()
    for userdetail in userdetails:
        rec = userdetail.split(":")
        if username == rec[0]:
            rec[1] = input("NEW PASSWORD:")
        edit_list.append(rec)#append rec in list every loop

    with open("user.txt","w") as edit:
        for recs in edit_list:#a line of rec in all lines of rec
            frec = ''
            for field in recs:
                frec +=field + ":"
            edit.write(frec.strip(":"))
        print("Successfully change password")

def customer_detail():
    with open ("user.txt","r") as customeread:
        customerdetails = customeread.readlines()
        for customerdetail in customerdetails:
            rec = customerdetail.split(":")
            if username == rec[0]:
                print("=====================")
                print("ACCOUNT DETAILS")
                print("=====================")
                print("ACCOUNT TYPE    :" + rec[2])
                print("ACCOUNT BALANCE :" + rec[3])
                print("ACCOUNT NO      :" + rec[0])
                print("NAME            :" + rec[4])
                print("IDENTITY CARD   :" + rec[5])
                print("PHONE NO        :" + rec[6])
                print("EMAIL           :" + rec[7])

def customer_deposit():
    edit_list=[]
    now = datetime.datetime.now()
    local_time = (str(now.year) + "-" + str(now.month) + "-" + str(now.day))
    while True:#validation for only integer input
        try:
            deposit = int(input("DEPOSIT:"))
            break

        except ValueError:
            print("YOU CAN ONLY INPUT INTEGERS")
            continue
        
        
    with open ("user.txt","r") as customeread:
        customerdetails = customeread.readlines()
    for customerdetail in customerdetails:
        rec = customerdetail.split(":")
        if username == rec[0]:
            rec[3] = str(int(rec[3]) + deposit)
            with open ("customerstatement.txt","a") as writetrans:
                newtrans = [local_time,"DEPOSIT",username,str(deposit),rec[3]]
                newtrans = ":".join(newtrans)
                writetrans.write(newtrans + "\n")#append newtrans to txt file

        edit_list.append(rec)

    with open("user.txt","w") as edit:
        for recs in edit_list:
            frec = ''
            for field in recs:
                frec +=field + ":"
            edit.write(frec.strip(":"))
    print("DEPOSIT SUCCESSFULLY")

def customer_withdrawal():
    flag =1
    edit_list=[]
    now = datetime.datetime.now()
    local_time = (str(now.year) + "-" + str(now.month) + "-" + str(now.day))
    while True:
        try:
            withdrawal = int(input("WITHDRAWAL:"))
            break

        except ValueError:
            print("YOU CAN ONLY INPUT INTEGERS")
            continue
            
    with open ("user.txt","r") as customeread:
        customerdetails = customeread.readlines()
    for customerdetail in customerdetails:
        rec = customerdetail.split(":")
        if username == rec[0]:
            if rec[2] == "SAVING ACCOUNT":
                if (int (rec[3]) - withdrawal)<100:
                    print("THIS WITHDRAWAL AMOUNT HAS AFFECT MINIMUM BALANCE")
                    flag = 0
                else:
                    rec[3] = str(int(rec[3]) - withdrawal)
                    with open ("customerstatement.txt","a") as writetrans:
                        newtrans = [local_time,"WITHDRAWAL",username,str(withdrawal),rec[3]]
                        newtrans = ":".join(newtrans)
                        writetrans.write(newtrans + "\n")

            elif rec[2] == "CURRENT ACCOUNT":
                if (int (rec[3]) - withdrawal)<500:
                    print("THIS WITHDRAWAL AMOUNT HAS AFFECT MINIMUM BALANCE")
                    flag = 0
                else:
                    rec[3] = str(int(rec[3]) - withdrawal)
                    with open ("customerstatement.txt","a") as writetrans:
                        newtrans = [local_time,"WITHDRAWAL",username,str(withdrawal),rec[3]]
                        newtrans = ":".join(newtrans)
                        writetrans.write(newtrans + "\n")

                
        edit_list.append(rec)

    if flag == 1:
        with open("user.txt","w") as edit:
            for recs in edit_list:
                frec = ''
                for field in recs:
                    frec +=field + ":"
                edit.write(frec.strip(":"))
        print("WITHDRAWAL SUCCESSFULLY")
    

def print_bank_state():
    now = datetime.datetime.now()
    totalwith = 0
    totaldep = 0
    month = str(now.month)
    months = str(now.month - 1)
    if len(months)==1:
        months = "0" + months
    # determine days of month
    if month == "03" or month == "05" or month == "07" or month == "08" or month == "10" or month == "12":
        day ="31"

    elif month == "02" or month == "04" or month == "06" or month == "09" or month == "11":
        day ="30"

    print("==============================")
    print("BANK STATMENT")
    print("==============================")

    with open ("user.txt","r") as detailread:
        details = detailread.readlines()
    for detail in details:
        rec = detail.split(":")
        if username == rec[0]:
            print(rec[4])
            print ("ACCOUNT NO:" + rec[0])
    #print this month and last month bank statement
    if month =="01":
        print("STATEMENT PERIOD:" + str(now.year - 1) + "/" + "12" + "/" + "01" + "-" + str(now.year) + "/" + month + "/" + "31")
    else:
        print("STATEMENT PERIOD:" + str(now.year) + "/" + months + "/" + "01" + "-" + str(now.year) + "/" + month + "/" + day)


    print("-------------------------------------------------------------")
    print("DATE".center(20),"DEPOSIT".center(20),"WITHDRAWAL".center(20),"BALANCE".center(20))
    print("-------------------------------------------------------------")

                
    with open("customerstatement.txt","r") as transread:
       trans = transread.readlines()
    for tran in trans:
        rect = tran.split(":")
        if rect[2] == username:
            if month == "01":
                if (rect[0])[:7] ==(str(now.year) + "-" + str(now.month)) or (rec[0])[:7] == (str(now.year - 1) + "-" + "12"):
                    if rect[1] == "DEPOSIT":
                        print(rect[0].center(20),rect[3].center(20),"".center(20),rect[4].center(20))
                        totaldep = totaldep + int(rect[3])

                    elif rect[1] == "WITHDRAWAL":
                        print(rect[0].center(20),"".center(20),rect[3].center(20),rect[4].center(20))
                        totalwith = totalwith + int(rect[3])

            else:
                if (rect[0])[:7] ==(str(now.year) + "-" + str(now.month)) or (rec[0])[:7] == (str(now.year) + "-" + months):
                    if rect[1] == "DEPOSIT":
                        print(rect[0].center(20),rect[3].center(20),"".center(20),rect[4].center(20))
                        totaldep = totaldep + int(rect[3])

                    elif rect[1] == "WITHDRAWAL":
                        print(rect[0].center(20),"".center(20),rect[3].center(20),rect[4].center(20))
                        totalwith = totalwith + int(rect[3])

            

   

    print("TOTAL WITHDRAWAL:" + str(totalwith))
    print("TOTAL DEPOSIT   :" + str(totaldep))

def create_customer_acc():
    print("=====================")
    print("CREATE CUSTOMER ACCOUNT")
    print("=====================")
    while True:
        user_account_key = input("1)CURRENT ACCOUNT 2)SAVING ACOUNT ,3)EXIT PLEASE SELECT (1,2,3):")
        if user_account_key == "1":
            user_account = "CURRENT ACCOUNT"
            while True:
                try:
                    user_balance = int(input("MIN BALANCE IS RM500,PLEASE ENTER AMOUNT:"))
                    break
                
                except ValueError:
                    print("YOU CAN ONLY INPUT INTEGERS")
                    continue
                
            if user_balance < 500:
                print("INSUFFICIENT AMOUNT")
                continue
            elif user_balance >= 500:
                user_name = input("CUSTOMER NAME:")
                user_IC = input("IDENTITY NUMBER:")
                user_phoneno = input("PHONE NUMBER:")
                user_email = input("EMAIL:")
                user_password = (user_name + "@" + user_IC[:5] + user_email[:5])#default password
                with open ("user.txt","a") as cusdetail:
                    nextid = gen_new_cusid()
                    newcus = [nextid,user_password,user_account,str(user_balance),user_name,user_IC,user_phoneno,user_email]
                    newcus = ':'.join(newcus)
                    cusdetail.write(newcus + "\n")
                print("Customer Username:" + nextid)
                print("Customer Password:" + user_password)
                print("CUSTOMER ACCOUNT CREATED")
                break

        elif user_account_key == "2":
            user_account = "SAVING ACCOUNT"
            while True:
                try:
                    user_balance = int(input("MIN BALANCE IS RM100,PLEASE ENTER AMOUNT:"))
                    break

                except ValueError:
                    print("YOU CAN ONLY INPUT INTEGERS")
                    continue

            if user_balance < 100:
                print("INSUFFICIENT AMOUNT")
                continue

            elif user_balance >= 100:
                user_name = input("CUSTOMER NAME:")
                user_IC = input("IDENTITY NUMBER:")
                user_phoneno = input("PHONE NUMBER:")
                user_email = input("EMAIL:")
                user_password = (user_name + "@" + user_IC[:5] + user_email[:5])
                with open ("user.txt","a") as cusdetail:
                    nextid = gen_new_cusid()
                    newcus = [nextid,user_password,user_account,str(user_balance),user_name,user_IC,user_phoneno,user_email]
                    newcus = ':'.join(newcus)
                    cusdetail.write(newcus + "\n")
                print("Customer Username:" + nextid)
                print("Customer Password:" + user_password)
                print("CUSTOMER ACCOUNT CREATED")
                break

                

        elif user_account_key == "3":
            break

        else:
            print("INVALID ACTION")
            continue


def edit_customer_detail():
    flag=0
    edit_list=[]
    user_name = input("Customer Account No:")
    with open ("user.txt","r") as read:
        cusdetails = read.readlines()
        for cusdetail in cusdetails:
            rec = cusdetail.split(":")
            if user_name == rec[0] and user_name[:3] == "CUS":
                print ("1)PHONE NO:" + rec[6])
                print ("2)EMAIL   :" + rec[7])
                flag =1
                while True:
                    action = input("PLEASE SELECT(1)PHONE NO,(2)EMAIL TO EDIT:")
                    if action == "1":
                        rec[6] = input("NEW PHONE NO:")
                        print("Successfully updated!")
                        break
                    if action == "2":
                        rec[7] = input("NEW EMAIL:")
                        print("Successfully updated!")
                        break
                    else:
                        print("INVALID ACTION")
                
            edit_list.append(rec)

    if flag == 1:#run this only customer account username exist
        with open("user.txt","w") as edit:
            for recs in edit_list:
                frec = ''
                for field in recs:
                    frec +=field + ":"
                edit.write(frec.strip(":"))

    if flag == 0:
        print("THIS ACCOUNT IS NOT AVAILABLE")

def staff_print_bank_state():
    account = input("CUSTOMER ACC NO:")
    now = datetime.datetime.now()
    flag = 0
    totalwith = 0
    totaldep = 0
    month = str(now.month)
    months = str(now.month - 1)
    if len(months)==1:
        months = "0" + months

    if month == "03" or month == "05" or month == "07" or month == "08" or month == "10" or month == "12":
        day ="31"

    elif month == "02" or month == "04" or month == "06" or month == "09" or month == "11":
        day ="30"

    

    with open ("user.txt","r") as detailread:
        details = detailread.readlines()
    for detail in details:
        rec = detail.split(":")
        if account == rec[0]:
            print("==============================")
            print("BANK STATMENT")
            print("==============================")
            print(rec[4])
            print ("ACCOUNT NO:" + rec[0])
            if month =="01":
                print("STATEMENT PERIOD:" + str(now.year - 1) + "/" + "12" + "/" + "01" + "-" + str(now.year) + "/" + month + "/" + "31")
            else:
                print("STATEMENT PERIOD:" + str(now.year) + "/" + months + "/" + "01" + "-" + str(now.year) + "/" + month + "/" + day)
            print("-------------------------------------------------------------")
            print("DATE".center(20),"DEPOSIT".center(20),"WITHDRAWAL".center(20),"BALANCE".center(20))
            print("-------------------------------------------------------------")
            break

    if account!=rec[0]:
        print("THIS ACCOUNT IS NOT AVAILABLE")
        flag = 1

    with open("customerstatement.txt","r") as transread:
       trans = transread.readlines()
    for tran in trans:
        rect = tran.split(":")
        if rect[2] == account:
            if month == "01":
                if (rect[0])[:7] ==(str(now.year) + "-" + str(now.month)) or (rect[0])[:7] == (str(now.year - 1) + "-" + "12"):
                    if rect[1] == "DEPOSIT":
                        print(rect[0].center(20),rect[3].center(20),"".center(20),rect[4].center(20))
                        totaldep = totaldep + int(rect[3])

                    elif rect[1] == "WITHDRAWAL":
                        print(rect[0].center(20),"".center(20),rect[3].center(20),rect[4].center(20))
                        totalwith = totalwith + int(rect[3])

            else:
                if (rect[0])[:7] ==(str(now.year) + "-" + str(now.month)) or (rect[0])[:7] == (str(now.year) + "-" + months):
                    if rect[1] == "DEPOSIT":
                        print(rec[0].center(20),rect[3].center(20),"".center(20),rect[4].center(20))
                        totaldep = totaldep + int(rect[3])

                    elif rect[1] == "WITHDRAWAL":
                        print(rect[0].center(20),"".center(20),rect[3].center(20),rect[4].center(20))
                        totalwith = totalwith + int(rect[3])

   
    if flag == 0:
        print("TOTAL WITHDRAWAL:" + str(totalwith))
        print("TOTAL DEPOSIT   :" + str(totaldep))

    

def create_staff_acc():
    print("=====================")
    print("CREATE STAFF ACCOUNT")
    print("=====================")
    user_name = input("STAFF NAME:")
    user_IC = input("IDENTITY NUMBER:")
    user_phoneno = input("PHONE NUMBER:")
    user_email = input("EMAIL:")
    user_password = (user_name + "@" + user_IC[:5] + user_email[:5])
    with open ("user.txt","a") as staffdetail:
        nextid = gen_new_staffid()
        newstaff = [nextid,user_password,user_name,user_phoneno,user_IC,user_email]
        newstaff = ":".join(newstaff)
        staffdetail.write(newstaff + "\n")
    print("Staff Username:" + nextid)
    print("Staff Password:" + user_password)
    print("STAFF ACCOUNT CREATED")


def customer_acc_menu():
    print("=====================")
    print ("WELCOME")
    while True:
        print("=====================")
        print("1.DETAIL")
        print("2.PRINT BANK STATEMENT")
        print("3.DEPOSIT")
        print("4.WITHDRAWAL")
        print("5.CHANGE PASSWORD")
        print("6.QUIT")
        action = input("PLEASE SELECT (1,2,3,4,5,6):")
        if action == "1":
            customer_detail()

        elif action == "2":
            print_bank_state()

        elif action == "3":
            customer_deposit()

        elif action == "4":
            customer_withdrawal()

        elif action == "5":
            change_password()

        elif action == "6":
            print("Goodbye")
            print("=====================")
            break

        else:
            print("invalid action")
            continue

def staff_acc_menu():
    print("=====================")
    print ("WELCOME")
    while True:
        print("=====================")
        print("1.CREATE CUSTOMER ACCOUNT")
        print("2.PRINT CUSTOMER BANK STATEMENT")
        print("3.EDIT CUSTOMER DETAILS")
        print("4.CHANGE PASSWORD")
        print("5.QUIT")
        action = input("PLEASE SELECT (1,2,3,4,5):")
        if action == "1":
            create_customer_acc()

        elif action == "2":
            staff_print_bank_state()

        elif action == "3":
            edit_customer_detail()

        elif action == "4":
            change_password()

        elif action == "5":
            print("Goodbye")
            print("=====================")
            break

        else:
            print("invalid action")
            continue


def super_acc_menu():
    print("=====================")
    print ("WELCOME")
    while True:
        print("=====================")
        print("1.CREATE STAFF ACCOUNT")
        print("2.QUIT")
        action = input("PLEASE SELECT (1,2):")
        if action == "1":
            create_staff_acc()

        elif action == "2":
            print("GOODBYE")
            print("=====================")
            break

        else:
            print("invalid action")
            continue

def login():# a function to determine account exist
    with open ("user.txt","r")as login_read:
        user_reads = login_read.readlines()
    for user_read in user_reads:
        usr = user_read.split(":")
        if username == usr[0] and password == usr[1]:
            if username[:5] == "SUPER":
                super_acc_menu()

            elif username[:5] == "STAFF":
                staff_acc_menu()

            elif username[:3] == "CUS":
                customer_acc_menu()
            break

    if username != usr[0] or (password) != usr[1]:
        print("INVALID USERNAME OR PASSWORD")
        
    
while True:
    print("=====================")
    print("*********************")
    print("BANKING SERVICE LOGIN")
    print("*********************")
    print("=====================")
    username = input("USERNAME:")
    password = input("PASSWORD:")
    login()
