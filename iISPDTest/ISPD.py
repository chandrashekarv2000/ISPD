import policefacecapture as pfc
import keyBoardControl as kc
import mysql.connector
from mysql.connector.authentication import get_auth_plugin
mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",auth_plugin="mysql_native_password",database="ispd")
mycursor=mydb.cursor()
re="yes/no"
secret_key="alphaBetaGamma"
password=""
station_id=0
si_pass=""

def dontPush():
    selectSQL="select count(*) from policestation"
    mycursor.execute(selectSQL)
    myresult = mycursor.fetchall()
    return myresult

def login():
    print("==================================ISPD SERVICES=======================================")
    print("======================================================================================")
    print("\t\t 1) FACE LOCK\n \t\t 2) MANUAL LOGIN\n \t\t 3) Exit")
    choice=int(input("ENTER THE CHOICE "))
    if choice==1:
        x=pfc.choice1()
    if choice==2:
        police_id=input("POLICE ID ")
        password=input("PASSWORD ")
        selectSQL="select count(*) from ispd_management where police_id=%s and police_password=%s"
        val=(police_id,password)
        x=select2(selectSQL,val)
    if choice==3:
        x=[(0,)]
    return x
def display_login():
    while True:
        print("======================================================================================")
        print("\t\t 1) ADD NEW CRIMINAL\n \t\t 2) MODIFY CRIMINAL DETAILS\n \t\t 3) DELETE CRIMINAL DETAIL\n \t\t 4) VIEW CRIMINAL DETAIL\n \t\t 5) START PATROLLING\n \t\t 6) BACK")
        print("=====================================================================================")
        print("ENTER YOUR CHOICE\t", end="")
        x = int(input())
        choice(x)
        if x==6:
            return
def choice(x):
    if x==1:
        print("======================================================================================")
        print("\t\t ENTER CRIMINAL NAME\t", end="")
        name = input()
        print("\t\t ENTER CRIMINAL AGE\t", end="")
        age = int(input())
        print("\t\t ENTER CRIMINAL GENDER\t", end="")
        gender = input()
        print("\t\t ENTER NUMBER OF CRIMINAL CASES\t", end="")
        no_of_cases = int(input())
        print("\t\t ENTER CRIMINAL PHONE NUMBER(10 digit)\t", end="")
        phone = int(input())
        print("\t\t ENTER STATION NUMBER(10 digit)\t", end="")
        number = int(input())
        print("\t\t ENTER STATION ID\t", end="")
        id1 = int(input())
        print("\t\t ENTER CRIMINAL ID\t", end="")
        id2 = input()
        insertSQL = "insert into criminals(criminal_name,criminal_age,criminal_gender,number_of_criminal_cases,criminal_number,station_number,station_id,criminal_id) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (name,age,gender,no_of_cases,phone,number,id1,id2)
        insert(insertSQL, val)
    if x==2:
        while True:
            x22 = update_criminal_details()
            if x22 == 1:
                old = input("ENTER OLD CRIMINAL NAME ")
                new = input("ENTER NEW CRIMINAL NAME ")
                val = (new, old,)
                updateSQL = "update criminals set criminal_name=%s where criminal_name=%s"
                update(updateSQL, val)
            elif x22 == 2:
                old = int(input("ENTER OLD CRIMINAL AGE "))
                new = int(input("ENTER NEW CRIMINAL AGE "))
                val = (new, old,)
                updateSQL = "update criminals set criminal_age=%s where criminal_age=%s"
                update(updateSQL, val)
            elif x22 == 3:
                old = input("ENTER OLD CRIMINAL GENDER ")
                new = input("ENTER NEW CRIMINAL GENDER ")
                val = (new, old,)
                updateSQL = "update criminals set criminal_gender=%s where criminal_gender=%s"
                update(updateSQL, val)
            elif x22 == 4:
                old = int(input("ENTER OLD NUMBER OF CRIMINAL CASES "))
                new = int(input("ENTER NEW NUMBER OF CRIMINAL CASES "))
                val = (new, old,)
                updateSQL = "update criminals set number_of_criminal_cases=%s where number_of_criminal_cases=%s"
                update(updateSQL, val)
            elif x22 == 5:
                old = int(input("ENTER OLD CRIMINAL NUMBER "))
                new = int(input("ENTER NEW CRIMINAL NUMBER "))
                val = (new, old,)
                updateSQL = "update criminals set criminal_number=%s where criminal_number=%s"
                update(updateSQL, val)
            elif x22 == 6:
                old = int(input("ENTER OLD CRIMINAL ID "))
                new = int(input("ENTER NEW CRIMINAL ID "))
                val = (new, old,)
                updateSQL = "update criminals set criminal_id=%s where criminal_id=%s"
                update(updateSQL, val)
            elif x22 == 7:
                break
            else:
                print("Ofcourse I love you enter the correct choice :)")
    if x==3:
        while True:
            x23 = delete_things()
            if x23 == 1:
                deleteSQL = "delete from criminals"
                delete(deleteSQL, '')
            elif x23 == 2:
                id = int(input("ENTER CRIMINAL ID "))
                deleteSQL = "delete from criminals where criminal_id=%s"
                add = (id,)
                delete(deleteSQL, add)
            elif x23 == 3:
                break
            else:
                print("Ofcourse I love you enter the correct choice :)")
    if x==4:
        while True:
            x24 = view_things()
            if x24 == 1:
                selectSQL1 = "select * from criminals"
                select4(selectSQL1, "")
            elif x24 == 2:
                id = int(input("ENTER CRIMINAL ID "))
                selectSQL2 = "select * from criminals where criminal_id=%s"
                add = (id,)
                select4(selectSQL2, add)
            elif x24 == 3:
                break
            else:
                print("Ofcourse I love you enter the correct choice :)")
    if x==5:
        kc.ispd()
    elif x>6:
        print("Ofcourse I love you enter the correct choice")
def create_ispd_management():
    print("======================================================================================")
    print("\t\t ENTER STATION ID\t", end="")
    id = int(input())
    print("\t\t ENTER STATION NUMBER\t", end="")
    number = int(input())
    print("\t\t ENTER STATION NAME\t", end="")
    name = input()
    print("\t\t ENTER NEW POLICE ID\t", end="")
    police_id = input()
    print("\t\t ENTER NEW PASSWORD\t", end="")
    psswd = input()
    print("\t\t CREATING FACE LOCK PLEASE LOOK AT THE CAMERA IT COULD TAKE A WHILE\t")
    pfc.findFace1(police_id)
    return [id, number, name, police_id, psswd]
def display_create_things():
    print("==================================ISPD SERVICES=======================================")
    print("\t\t 1) LOGIN\n \t\t 2) BACK")
    print("======================================================================================")
    print("ENTER YOUR CHOICE\t", end="")
    x = int(input())
    return x
def display_title():
    print("====================INTELLIGENCE SURVEILLANCE PATROLLING DRONE=========================")
def display_ispd_title():
    print("================================POLICE MANAGEMENT=======================================")
def display_unlisted_things():
    display_title()
    print("\t\t 1) Police Station\n \t\t 2) Exit")
    print("=====================================================================================\n")
    print("ENTER YOUR CHOICE\t",end="")
    x=int(input())
    return x
def display_unlisted_things1():
    display_title()
    print("\t\t 1) Police Station\n \t\t 2) ISPD MANAGEMENT\n \t\t 3) Exit")
    print("=====================================================================================\n")
    print("ENTER YOUR CHOICE\t",end="")
    x=int(input())
    return x
def display_ispd_list():
    print("\t\t 1) ADD NEW STATION\n \t\t 2) MODIFY STATION DETAILS\n \t\t 3) DELETE STATION DETAIL\n \t\t 4) VIEW STATION DETAIL\n "
          "\t\t 5) CREATE ISPD\n \t\t 6) DELETE ISPD\n \t\t 7) BACK")
    print("=====================================================================================")
    print("ENTER YOUR CHOICE\t", end="")
    x = int(input())
    return x
def view_things():
    print("=====================================================================================\n")
    print("\t\t 1) VIEW ALL\n \t\t 2) SEARCH\n \t\t 3) BACK")
    print("=======================================================================================")
    print("ENTER YOUR CHOICE\t",end="")
    x=int(input())
    return x
def delete_things():
    print("=====================================================================================\n")
    print("\t\t 1) DELETE ALL\n \t\t 2) SEARCH TO DELETE\n \t\t 3) BACK")
    print("=======================================================================================")
    print("ENTER YOUR CHOICE\t",end="")
    x=int(input())
    return x
def delete_things1():
    print("=====================================================================================\n")
    print("\t\t 1) DELETE ALL\n \t\t 2) SEARCH TO DELETE\n \t\t 3) BACK")
    print("=======================================================================================")
    print("ENTER YOUR CHOICE\t",end="")
    x=int(input())
    return x
def insert_police_details():
    print("\t\t ENTER NEW STATION ID\t",end="")
    id=int(input())
    print("\t\t ENTER NEW STATION PASSWORD\t", end="")
    ps =input()
    print("\t\t ENTER STATION NUMBER\t", end="")
    number = int(input())
    print("\t\t ENTER STATION NAME\t", end="")
    name = input()
    print("\t\t ENTER STATION ADDRESS\t", end="")
    address = input()
    print("\t\t ENTER STATION SI\t", end="")
    si = input()
    return [id,number,name,address,si,ps]
def update_police_details():
    selectSQL1 = "select * from policestation"
    select(selectSQL1, "")
    print("=======================================================================================")
    print("\t\t 1) STATION ID\n \t\t 2) STATION NUMBER\n \t\t 3) STATION NAME\n \t\t 4) STATION ADDRESS\n \t\t 5) STATION SI\n \t\t 6) BACK")
    print("=======================================================================================")
    print("ENTER YOUR CHOICE\t", end="")
    x = int(input())
    return x
def update_criminal_details():
    selectSQL1 = "select * from criminals"
    select4(selectSQL1, "")
    print("=======================================================================================")
    print("\t\t 1) CRIMINAL NAME\n \t\t 2) CRIMINAL AGE\n \t\t 3) CRIMINAL GENDER\n \t\t 4) NUMBER OF CRIMINAL CASES\n \t\t 5) CRIMINAL NUMBER\n \t\t 6) CRIMINAL ID\n \t\t 7) BACK")
    print("=======================================================================================")
    print("ENTER YOUR CHOICE\t", end="")
    x = int(input())
    return x
def insert(sql,val):
    mycursor.execute(sql,val)
    mydb.commit()
    print("1 record inserted successfully")
def select(sql,id):
    mycursor.execute(sql,id)
    myresult = mycursor.fetchall()
    print("STATION ID,STATION NUMBER,STATION NAME,STATION ADDRESS,STATION SI,N0.OF POLICE,NO.OF CRIMINALS")
    for x in myresult:
        print(x)
def select4(sql,id):
    mycursor.execute(sql,id)
    myresult = mycursor.fetchall()
    print("CRIMINAL NAME,CRIMINAL AGE,CRIMINAL GENDER,NO OF CRIMINAL CASES,CRIMINAL NUMBER,STATION NUMBER,STATION ID,CRIMINAL ID")
    for x in myresult:
        print(x)
def select1(sql):
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult
def select2(sql,val):
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    return myresult
def delete(sql,val):
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")
def update(sql,val):
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
def ispd_management():
    display_ispd_title()
    x2=display_ispd_list()
    return x2
while True:
    val=()
    sql="select count(*) from policestation"
    ans=select1(sql)
    if ans[0][0]==0:
        x1 = display_unlisted_things()
        x11=0
    elif ans[0][0]>0:
        x11=display_unlisted_things1()
        x1=0
    if x1==1 or x11==1:
        while True:
            password = input("\t\t Enter the Secret Key ")
            if password==secret_key:
                x2=ispd_management()
                if x2==1:
                    x21=insert_police_details()
                    insertSQL="insert into policestation(station_id,station_number,station_name,station_address,station_SI,SI_password) values(%s,%s,%s,%s,%s,%s)"
                    val=(int(x21[0]),int(x21[1]),x21[2],x21[3],x21[4],x21[5])
                    insert(insertSQL,val)
                elif x2==2:
                    while True:
                        x22=update_police_details()
                        if x22==1:
                            old=int(input("ENTER OLD STATION ID "))
                            new=int(input("ENTER NEW STATION ID "))
                            val=(new,old,)
                            updateSQL="update policestation set station_id=%s where station_id=%s"
                            update(updateSQL,val)
                        elif x22==2:
                            old = int(input("ENTER OLD STATION NUMBER "))
                            new = int(input("ENTER NEW STATION NUMBER "))
                            val = (new, old,)
                            updateSQL = "update policestation set station_number=%s where station_number=%s"
                            update(updateSQL, val)
                        elif x22==3:
                            old = input("ENTER OLD STATION NAME ")
                            new = input("ENTER NEW STATION NAME ")
                            val = (new, old,)
                            updateSQL = "update policestation set station_name=%s where station_name=%s"
                            update(updateSQL, val)
                        elif x22==4:
                            old = input("ENTER OLD STATION ADDRESS ")
                            new = input("ENTER NEW STATION ADDRESS ")
                            val = (new, old,)
                            updateSQL = "update policestation set station_address=%s where station_address=%s"
                            update(updateSQL, val)
                        elif x22==5:
                            old = input("ENTER OLD STATION SI ")
                            new = input("ENTER NEW STATION SI ")
                            val = (new, old,)
                            updateSQL = "update policestation set station_si=%s where station_si=%s"
                            update(updateSQL, val)
                        elif x22==6:
                            break
                        else:
                            print("Ofcourse I love you enter the correct choice :)")
                elif x2==3:
                    while True:
                        x23=delete_things()
                        if x23==1:
                            deleteSQL="delete from policestation"
                            delete(deleteSQL,'')
                        elif x23==2:
                            id=input("ENTER STATION ID ")
                            deleteSQL="delete from policestation where station_id=%s"
                            add=(id,)
                            delete(deleteSQL,add)
                        elif x23==3:
                            break
                        else:
                            print("Ofcourse I love you enter the correct choice :)")
                elif x2==4:
                    while True:
                        x24=view_things()
                        if x24==1:
                            selectSQL1="select * from policestation"
                            select(selectSQL1,"")
                        elif x24==2:
                            id=int(input("ENTER STATION ID "))
                            selectSQL2 = "select * from policestation where station_id=%s"
                            add=(id,)
                            select(selectSQL2,add)
                        elif x24==3:
                            break
                        else:
                            print("Ofcourse I love you enter the correct choice :)")
                elif x2==5:
                    if dontPush()[0][0]>0:
                        print("=======================================================================================")
                        station_id = int(input("ENTER STATION ID "))
                        si_pass = input("ENTER PASSWORD ")
                        SEL = "select count(*) from policestation where station_id=%s and SI_password=%s"
                        val = (station_id, si_pass)
                        x = select2(SEL, val)
                        if x[0][0] > 0:
                            print("=======================================================================================")
                            x1111 = create_ispd_management()
                            insertSQL = "insert into ispd_management(station_id,station_number,station_name,police_id,police_password) values(%s,%s,%s,%s,%s)"
                            val = (int(x1111[0]), int(x1111[1]), x1111[2], x1111[3], x1111[4])
                            insert(insertSQL, val)
                    else:
                        print("ENTER THE STATION DETAILS FIRST")
                elif x2==6:
                    if dontPush()[0][0] > 0:
                        while True:
                            x1112 = delete_things1()
                            if x1112 == 1:
                                deleteSQL = "delete from ispd_management"
                                delete(deleteSQL, '')
                            elif x1112 == 2:
                                id = int(input("ENTER POLICE ID "))
                                deleteSQL = "delete from ispd_management where police_id=%s"
                                add = (id,)
                                delete(deleteSQL, add)
                            elif x1112 == 3:
                                break
                            else:
                                print("Ofcourse I love you enter the correct choice :)")
                    else:
                        print("ENTER THE STATION DETAILS FIRST")
                elif x2==7:
                    break
                else:
                    print("Ofcourse I love you enter the correct choice :)")
            else:
                print("\t\t INVALID SECRET KEY")
    elif x1==2:
        break
    elif x11==2:
        while True:
            print("=======================================================================================")
            x111=display_create_things()
            if x111==1:
                x=login()
                if x[0][0]>0:
                    display_login()
            elif x111==2:
                display_title()
                break
            else:
                print("Ofcourse I love you enter the correct choice :)")
    elif x11==3:
        break
    else:
        print("Ofcourse I love you enter the correct choice :)")