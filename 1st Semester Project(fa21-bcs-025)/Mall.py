import mysql.connector as mysql

database = mysql.connect(host="localhost",username="root",password="",database="mall_management_system")
print("\nConnected to the Database Successfully..")

command_handler = database.cursor(buffered=True)





#Admin Authentication
def authentication_admin():
    print("\nDirector Login.\n")
    username = input(str("Username : "))
    password = input(str("Password :"))
    
    if username == "admin_1" and password == "Admin_123!" : 
        admin_session()
        
    else:
        if username != "admin_1" and password != "Admin_123!" :
            print("\nIncorrect Credentials!\nTry again. ")
    
        else: 
            print("\nDetails do not Match\nTry again.")






#Admin Session
def admin_session():
    print("****************************************\n"
    "Login Successfull.\nWelcome to Main Server,Employee."
    "\n****************************************")

    while 1 :
        print("\nAdmin Menu:\n ")
        print("1.Register a new Employee.")
        print("2.Delete existing Emplyee's Data.")
        print("3.Access Departments' Data and functions")
        print("4.Access Employees' Data.")
        print("5.Icome.")
        print("6.Logout.")
        user_option = input(str("Option : "))
        
        if user_option == "1":
            create_user()


        elif user_option == "2":
            delete_user()

        elif user_option == "3":
            department_data_and_funtion()
        

        elif user_option == "4":
            employee_database()
        

        elif user_option == "5":
            access_income()
        
        elif user_option == "6":
            print("are you sure? ")
            user_option = input(str("Y/N : "))
     
            if user_option == "y" :
                break
            else: 
                user_option == "n"
                admin_session()
        else:
            print("\nNo Valid Option Selected.")





#Employee Authentication
def authentication_user():
    print("\nEmployee Login.\n")
    username = input(str("Username : "))
    password = input(str("Password :"))
    department = input(str("Department : "))
    query_values = [username,password,department]
    command_handler.execute("SELECT  * FROM employee WHERE username=%s AND password=%s AND department=%s",query_values)
    database.commit()

    if command_handler.rowcount <= 0 :
        print("Username Not Found.")
    else:
        if department == "C_S":
            customer_service()
        elif department == "S_E":
            security()
        elif department == "T_T":
            tenants()
        
         

#Create a new user
def create_user():
    print("\nRegister a new Employee.")
      
    username = input(str("New Employee Username : "))
    password = input(str("New Password : "))
    department = input(str("select the department : "))

            
    query_values = [username,password,department]
    command_handler.execute("INSERT INTO employee(username,password,department) VALUES (%s,%s,%s)",query_values)
    database.commit()
    print("\nUsername "+ username + " has been registered as an Employee of the department "+ department)





#Delete a user
def delete_user():
   
    print("\nDelete a registered Employee's Account.")
    username = input(str(" Employee Username : "))
    department = input(str("select the department : "))
    query_values = [department,username]
    command_handler.execute("DELETE FROM employee WHERE department = %s AND username = %s",query_values)
    
    database.commit()
    if command_handler.rowcount < 1 :
        print("User Not Found.")
    else :
        print(username + " has been deleted.")




#Department Data
def department_data_and_funtion():
   
   while 1:
    print("\nSelect your desired Department.\n")
    print("1.Security.")
    print("2.Customer Service.")
    print("3.Tenants.")
    print("4.Logout.")
     
    
    user_option = input(str("Option : "))

    if user_option == "1":
            security()


    elif user_option == "2":
        customer_service()
        

    elif user_option == "3":
        tenants()

    elif user_option == "4":
        
            print("are you sure? ")
            user_option = input(str("Y/N : "))
     
            if user_option == "y" :
                break
            else: 
                user_option == "n"
                department_data_and_funtion()
        
    else:
        print("Invalid option Selected.")





#Employee database
def employee_database():
   
   while 1:
    print("Select the desired department.\n")
    print("1.Security.")
    print("2.Customer Service.")
    print("3.Tenants.")
    print("4.Logout.")
    user_option = input(str("Option : "))
    if user_option == "1":
            command_handler.execute("SELECT  * FROM employee WHERE department='S_E'")
            records = command_handler.fetchall()
            print("Displaying Employees' data from the Security Department.\n")
            for record in records:
                print(record)


    elif user_option == "2":
            command_handler.execute("SELECT  * FROM employee WHERE department='C_S'")
            records = command_handler.fetchall()
            print("Displaying Employees' data from the Customer Service Department.\n")
            for record in records:
                print(record)
        

    elif user_option == "3":
            command_handler.execute("SELECT  * FROM employee WHERE department='T_T'")
            records = command_handler.fetchall()
            print("Displaying Employees' data from the Tenants Department.\n")
            for record in records:
                print(record)

    elif user_option == "4":
        
            print("are you sure? ")
            user_option = input(str("Y/N : "))
     
            if user_option == "y" :
                break
            else: 
                user_option == "n"
                employee_database

    else:
        print("Invalid option Selected.")




#income database
def access_income():
    while 1:
        print("Select the desired option.\n")
        print("1.Enter a new income source.")
        print("2.Display Monthly income.")
        print ("3.Return to main menu.")
        user_option = input(str("Option: "))
        if user_option == "1":
            source = input(str("Source Name: "))
            monthly_revenue = input(str("Monthly revenue generation: "))
            month = month = input(str("Enter month: "))
            query_values = [source,monthly_revenue,month]
            command_handler.execute("INSERT INTO income(source,monthly_revenue,month) VALUES (%s,%s,%s)",query_values)
            database.commit()
            print("A new source of income has been registered.")

        elif user_option == "2":
            month = input(str("Select the month: "))
            query_values =[month]
            command_handler.execute("SELECT * FROM income WHERE month =%s ",query_values)
            records = command_handler.fetchall()
            print("Displaying monthly revenue generated for the month of "+ month)
            for record in records:
                print(record)
        

        elif user_option == "3":
        
            print("are you sure? ")
            user_option = input(str("Y/N : "))
     
            if user_option == "y" :
                break
            else: 
                user_option == "n"
                access_income()
        else:
            print("\nNo Valid Option Selected.")





#Security Database
def security() :
    print("****************************************\n"
   "Login Successfull.\nWelcome to Main Server,Employee."
   "\n****************************************")
    while 1:
     
     print("Select your desired option")
     print("1.Theft cases and suspects.")
     print("2.Staff monitoring")
     print("3.Logout.")
     user_option = input(str("Option : "))
    
    if user_option == "1":
        print("Select your desired option")
        print("1.Report a Theft.")
        print("2.Report a suspect")
        print("3.Show report")

        user_option = input(str("Option : "))
        if user_option =="1":
            theif_name = input(str("Enter name: "))
            age = input(str("age: "))
            item_stolen =input(str("item stolen: "))
            shop_id = input(str("Stolen from shop: "))
            time_stolen = input(str("Time Stolen "))
            query_values =[theif_name,age,item_stolen,shop_id,time_stolen]
            command_handler.execute("INSERT INTO security_theft(theif_name,age,item_stolen,shop_id,time_stolen) VALUES (%s,%s,%s,%s,%s)",query_values)
            database.commit()
            print("Theft has been reported.")


        elif  user_option =="2":
            suspect_name = input(str("Enter name: "))
            age = input(str("age: "))
            shop_id = input(str("Seen at : "))
            time_of_activity = input(str("Time of suspicious activiy: "))
            query_values =[suspect_name,age,shop_id,time_of_activity]
            command_handler.execute("INSERT INTO security_suspect([suspect_name,age,shop_id,time_of_activity) VALUES (%s,%s,%s,%s)",query_values)
            database.commit()
            print("Suspect has been reported.")


        elif user_option =="3":
            print("Select your desired option")
            print("1.Show theft reports.")
            print("2.Show suspect reports.")
            user_option = input(str("Option : "))
            if user_option =="1":
                command_handler.execute("SELECT * FROM security_theft")
                records = command_handler.fetchall()
                print("Displaying all theft reports.\n")
                for record in records:
                    print(record)
            elif user_option == "2":
                command_handler.execute("SELECT * FROM security_suspect")
                records = command_handler.fetchall()
                print("Displaying all suspect reports.\n")
                for record in records:
                    print(record)
            else :
                print("Invalid option.")



    elif user_option == "2":
        employee_database()


    
    elif user_option == "3":
            print("are you sure? ")
            user_option = input(str("Y/N : "))
     
            if user_option == "y" :
                main()
            else: 
                user_option == "n"
                security()


    else:
        print("Invalid Option Selected.")




# Tenants Database
def tenants():
    print("****************************************\n"
   "Login Successfull.\nWelcome to Main Server,Employee."
   "\n****************************************")
    while 1:
         
        print("Select the desired option.\n")
        print("1.Register a New Lease.")
        print("2.Show Existing Leases.") 
        print("3.Resolve or delete an existing Lease")
        print("4.Logout.")
        user_option = input(str("Option : "))

    if user_option == "1":
        print("Enter the data for the new lease.\n")
        shop_id = input(str("Shop Name: "))
        tenant_id =  input(str("Tenant ID: "))
        rent =  input(str("Rent: "))
        lease_start = input(str("Leasing date: "))
        lease_end = input(str("Lease Expiry date: "))
        query_values = [shop_id,tenant_id,rent,lease_start,lease_end]
        command_handler.execute("INSERT INTO tenants(shop_id,tenant_id,rent,lease_start,lease_end) VALUES (%s,%s,%s,%s,%s)",query_values)
        database.commit()
        print("A new Lease has been registered.")
        

    elif user_option == "2":
            print("1.show all leases")
            print("2.show a spcific lease\n") 
    
            user_option = input(str("Option : "))

            if user_option == "1":
                command_handler.execute("SELECT  * FROM tenants")
                records = command_handler.fetchall()
                print("Displaying all existing leases\n")
                for record in records:
                    print(record)
            
                


            elif user_option == "2":
                shop_id = input(str("Shop Name: "))
                tenant_id =  input(str("Tenant ID: "))
                query_values = [shop_id,tenant_id]
                command_handler.execute("SELECT  * FROM tenants WHERE shop_id=%s AND tenant_id=%s",query_values)
                records = command_handler.fetchall()
                print("Displaying The lease\n")
                for record in records:
                    print(record)
            
            else:
                print("Invalid Option.")
        

    elif user_option == "3":
            print("Select the desired option.\n")
            print("1.Resolve a lease")
            print("2.Delete a lease.")
            user_option = input(str("Option : "))
            if user_option =="1":
                shop_id = input(str("Shop Name: "))
                tenant_id =  input(str("Tenant ID: "))
                query_values = [shop_id,tenant_id]
                
                command_handler.execute("UPDATE tenants SET lease_end = 'Expired' WHERE shop_id =%s AND tenant_id =%s ",query_values)
                database.commit()
                print("Lease has been resolved")
            elif user_option =="2":
                print("\nDelete  a Lease Data.")
                shop_id = input(str("Shop Name: "))
                tenant_id =  input(str("Tenant ID: "))
                query_values = [shop_id,tenant_id]
                command_handler.execute(" DELETE FROM tenants WHERE  WHERE shop_id =%s AND tenant_id =%s",query_values)
    
                database.commit()
                if command_handler.rowcount < 1 :
                    print("Lease Not Found.")
                else :
                    print(shop_id + " lease's data has been deleted.")


    elif user_option == "4":
            print("are you sure? ")
            user_option = input(str("Y/N : "))
     
            if user_option == "y" :
                main()

                
            else: 
                user_option == "n"
                tenants()
    

   
    else:
            print("\nNo Valid Option Selected.")


    



#Customer Services Database
def customer_service():


   print("****************************************\n"
   "Login Successfull.\nWelcome to Main Server,Employee."
   "\n****************************************")

   while 1:
    print("Select the desired option.\n")
    print("1.Enter a new complaint.")
    print("2.Show unresolved complaints.")
    print("3.Resolve or delete a complaint.")
    print("4.Logout.")
    user_option = input(str("Option : "))

    if user_option == "1":
        print("Enter the complaint.\n")
        customer_id = input(str("Customer Name: "))
        complaint =  input(str("Complaint: "))
        complaint_status =  input(str("Complaint status: "))
        query_values = [customer_id,complaint,complaint_status]
        command_handler.execute("INSERT INTO customer_service(customer_id,complaint,complaint_status) VALUES (%s,%s,%s)",query_values)
        database.commit()
        print("complaint has been registered.")
        

    elif user_option == "2":
            command_handler.execute("SELECT  * FROM customer_service WHERE complaint_status='U'")
            records = command_handler.fetchall()
            print("Displaying complaints that are unresolved\n")
            for record in records:
                print(record)
        

    elif user_option == "3":
            print("Select the desired option.\n")
            print("1.Change complaint status.")
            print("2.Delete a complaint.")
            user_option = input(str("Option : "))
            if user_option =="1":
                id = input(str("ID: "))
                customer_id = input(str("Customer Name: "))
                query_values =[id,customer_id]
                command_handler.execute("UPDATE customer_service SET complaint_status = 'R' WHERE id =%s AND customer_id =%s ",query_values)
                database.commit()
                print("Complaint has been resolved")
            elif user_option =="2":
                print("\nDelete  a Compliant.")
                id = input(str("ID: "))
                customer_id = input(str("Customer Name: "))
                query_values =[id,customer_id]
                command_handler.execute(" DELETE FROM customer_service WHERE id =%s AND customer_id =%s",query_values)
    
                database.commit()
                if command_handler.rowcount < 1 :
                    print("Complaint Not Found.")
                else :
                    print(customer_id + "'s complaint has been deleted.")

    elif user_option == "4":
        print("are you sure? ")
        user_option = input(str("Y/N : "))
     
        if user_option == "y" :
                break
        else: 
                user_option == "n"
                customer_service()
    else:
            print("\nNo Valid Option Selected.")






# Main Loop
def main():
        while 1:   
            main_loop = 0
            print("\n**************************************\n"
            "Welcome to The Mall Management Server\n"
            "**************************************\n"
            "Press enter to continue:\n")
            input()
            print("1.Login as Director.")
            print("2.Login as an Employee.")
            print("3.Exit.")
            user_option = input(str("Option : "))

            if user_option == "1":
                authentication_admin()

            elif user_option == "2" :
                  authentication_user()

            elif user_option == "3":
                break

            else:
                print("No valid option was selected\nTry again.")
         


main()