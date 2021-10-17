import mysql.connector
con = mysql.connector.connect(host="localhost",
                              port = "3307",
                              user="root",
                              passwd="",
                              database="dummydb")
mycursor1 = con.cursor()

#--------------------CREATE------------------------
def mycreate():
    tablename = input("enter table name=> ")
    mycursor1.execute("CREATE  TABLE {}(`membership_number` INT   ,`full_names` VARCHAR(150) NOT NULL ,`gender` VARCHAR(6))".format(tablename))
#---------------------------------------------------

#--------------------INSERT-------------------------
def myinsert():
    membership_number=input("enter membership number")
    fullname=input("enter full name")
    gender=input("enter gender")
    x="INSERT INTO mytab_1 (`membership_number`, `full_names`, `gender`) VALUES ({},'"'{}'"','"'{}'"')".format(membership_number,fullname,gender)
    print(x)
    mycursor1.execute(x)
    con.commit()
    print(mycursor1.rowcount, "record inserted.")
#---------------------------------------------------


#--------------------RETRIVE------------------------
def myretrive():
    x="SELECT * FROM `mytab_1` WHERE 1"
    print(x)
    mycursor1.execute(x)
   #------------DISPLAY TABLE DATA------------------
    myresult = mycursor1.fetchall()

    for x in myresult:
        print(x)
   #-------------------------------------------------
    con.commit()
#---------------------------------------------------


#--------------------UPDATE-------------------------
def myupdate():
    fullname=input("enter full name")
    membership_number=input("enter membership number")

    x="UPDATE  mytab_1 SET full_names = '"'{}'"' WHERE membership_number =  {}".format(fullname,membership_number)
    mycursor1.execute(x)
    print(x)
    con.commit()
#---------------------------------------------------

#--------------------DELETE-------------------------
def mydelete():
    membership_number=input("enter membership_number")
    x = "DELETE FROM `mytab_1` WHERE membership_number= {}".format(membership_number)
    mycursor1.execute(x)
    print(x)
    con.commit()
#---------------------------------------------------

#------------------EXECUTE--------------------------
#------------------DISPLAY LOOP---------------------
while True:
    print("\nOperations used, ")
    print("\n1.CREATE DB\n"
          "2.INSERT\n"
          "3.RETRIVE" "\n"
          "4.UPDATE\n"
          "5.DELETE\n"
          "6.EXIT")

    ch = int(input("Enter choice:"))
    if (ch == 1):
        mycreate()
    elif(ch == 2):
        myinsert()
    elif(ch == 3):
        myretrive()
    elif(ch == 4):
        myupdate()
    elif(ch == 5):
        mydelete()
    else:
        print("Thank you!!!")
        break

#----------------------------------------------------------


