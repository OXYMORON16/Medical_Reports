import mysql.connector
import mod
mydb=mysql.connector.connect(host="localhost",password="123456",username="root",port=3307,database="project")
if mydb.is_connected():
    print("Connected successfully")
    mycur=mydb.cursor()
    query="SELECT * FROM login"
    query2="SELECT * FROM register"
    mycur.execute(query)
    data=mycur.fetchall()
    mycur.execute(query2)
    data2=mycur.fetchall()
    if data==[]:
        print("Press 1 to register")
    else:
        print("Press 1 to register")
        print("Press 2 to login")
    option=input("Enter your option: ")
    if option=='1':
        register_id=int(input("Enter your id: "))
        lent=len(data)
        if lent==0:
            print(mod.insert_register(register_id))
        else:
            for i in range(lent):
                if register_id == data[i][0]:
                    print("The given id already exists")
                    break
                else:
                    print(mod.insert_register(register_id))
                    break
    elif option=='2':
        login_id=int(input("Enter your id: "))
        lst_login_id=[]
        for i in range(len(data)):
            lst_login_id.append(data[i][0])
        if login_id not in lst_login_id:
            print("Invalid User ID")
        else:
            password=input("Enter your password: ")
            tup=(login_id,password)
            if tup in data:
                print("Login Successful")
                program_loop = 'y'
                while program_loop == 'y':
                    if mod.see_all_patient_details()==[]:
                        print("Press 1 to create prescription form")
                        print("Press 0 to exit")
                    else:
                        print("Press 1 to create prescription form")
                        print("Press 2 to see all patients details")
                        print("Press 3 to see 1 patient detail according to name")
                        print("Press 4 to see all patients details in MS Word")
                        print("Press 5 to see one patient details in MS Word")
                        print("Press 6 to delete all patients records")
                        print("Press 7 to delete one patient record")
                        print("Press 0 to exit ")
                    option=input("Enter your option: ")
                    if option == '1':
                        condition = 'y'
                        while condition.lower()=='y':
                            print(mod.insert_reception())
                            print("Do you want to add another patient's details(y/n)")
                            cond=input("y/n: ")
                            if cond=='y':
                                condition='y'
                            else:
                                condition='n'
                    elif option== '2':
                        print("\n")
                        mod.output_all()
                        print("\n")
                    elif option == '3':
                        mod.output_one()
                        print("\n")
                    elif option =='4':
                        print(mod.output_all_word())
                    elif option =='5':
                        print(mod.output_one_word())
                    elif option == '6':
                        print(mod.delete_all_patients())
                    elif option =='7':
                        print(mod.delete_one_patient())
                        print("New records are:-")
                        print("\n")
                        mod.output_all()
                    elif option == '0':
                        program_loop='n'
                        print("GoodBye!")
            else:
                    print("The password you entered is incorrect!")
else:
    print("couldn't connect to the database you fool!")
