from tabulate import tabulate   #------------> Mengimport Tabulate

def display_customer_table():   #------------> Menampilkan Daftar Customer
    headers = ["Id", "Username", "Password", "Name", "Age", "Phone Number", "Gender"]
    table_data = [[customer[key] for key in headers] for customer in Customer_List.values()]
    print('\nCustomer Data:')
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

def display_film_table():       #------------> Menampilkan Daftar Film
    headers = ["Film Id", "Title", "Genre", "Rating", "Duration (Minutes)", "IMDb Score"]
    table_data = [[film[key] for key in headers] for film in Film_List.values()]
    print('\nFILMS:')
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

# Membuat Daftar Awal Customer dan Film
Customer_List ={'CI1' : {"Id":"CI1", "Username":"Ajimassss", "Password":"123", "Name":"Ajimas Wahyu", "Age":"22", "Phone Number":"082257218351", "Gender":"Male"},
                'CI2' : {"Id":"CI2", "Username":"Lunar", "Password":"123", "Name":"Luna Rose", "Age":"20", "Phone Number":"081235664432", "Gender":"Female"},
                'CI3' : {"Id":"CI3", "Username":"Angelinanrl", "Password":"123", "Name":"Angelina", "Age":"21", "Phone Number":"082324252526", "Gender":"Female"},
                'CI4' : {"Id":"CI4", "Username":"Rez4", "Password":"123", "Name":"Muhammad Reza", "Age":"24", "Phone Number":"081556545852", "Gender":"Male"},
                'CI5' : {"Id":"CI5", "Username":"Fwaki", "Password":"123", "Name":"Daffa Rizaldi", "Age":"22", "Phone Number":"089615264885", "Gender":"Male"}}

Film_List = {'MO1' : {"Film Id": "MO1", "Title":"Inside Out", "Genre":"Family", "Rating":"PG", "Duration (Minutes)":"95", "IMDb Score":"8.1"},
             'MO2' : {"Film Id": "MO2", "Title":"John Wick", "Genre":"Action", "Rating":"R", "Duration (Minutes)":"101", "IMDb Score":"7.4"},
             'MO3' : {"Film Id": "MO3", "Title":"The Conjuring", "Genre":"Horror", "Rating":"R", "Duration (Minutes)":"112", "IMDb Score":"7.5"},
             'MO4' : {"Film Id": "MO4", "Title":"Twilight", "Genre":"Romance", "Rating":"PG-13", "Duration (Minutes)":"122", "IMDb Score":"5.3"},
             'MO5' : {"Film Id": "MO5", "Title":"Mr. Bean", "Genre":"Comedy", "Rating":"G", "Duration (Minutes)":"90", "IMDb Score":"6.4"}}

User_Tickets = {}

#================================================== 
# LOGIN MENU AWAL

def login():
    while True:
        login = (input(f'''
            ----------------------
            ||Welcome to Cinemax||
            ----------------------
            1. Login as Admin
            2. Login as Member
            3. Exit Program
            
            Choose One Menu: '''))
        if(login == "3"):
            exit_program()
            exit()
        elif(login == "1"):
            login_admin()
            break
        elif(login == "2"):
            login_member()
            break
        else:
            print('''
            Your menu is not valid''')

#================================================== 
# EXIT PROGRAM

def exit_program():
    while True:
        sure = input(f'''
            Exit Program?
            (Y/N): ''')  
        lower_sure = sure.lower() 
        if(lower_sure == "y"):
            print('''
            Thank you! :)''')
            return
        elif(lower_sure == "n"):
            login()
        else:
            print('''
            Invalid!''')

#================================================== 
# LOGIN MENU ADMIN

def login_admin():
    while True:
        input_admin = input(f'''
            Username: ''')
        if (input_admin == 'Admin01'):
            while True:
                password_admin = input(f'''
            Password: ''')
                if (password_admin == '123'):
                    print(f'''
            _________________________

            Welcome, {input_admin} :)
            _________________________''')
                    menu_admin()
                    return
                else:
                    print('''
            Incorrect Password
            Try Again''')
        else:
            print('''
            Username doesn't exist
            Try Again''')

def menu_admin():                   #------------> Menu Utama Admin
    while True:
        daftar_menu_admin = input(f'''                                
            1. Customer List
            2. Edit Customer List
            3. Films
            4. Edit Film
            5. Logout
            Please choose one menu: ''')
        if (daftar_menu_admin == "5"):
            checker = input('''
            Back to menu? (Y/N) : ''')
            if checker.lower() == 'y':
                login()
                break
            elif checker.lower() == 'n':
                break
            else: 
                print('''
            Invalid!
            select (Y/N)''')
        elif (daftar_menu_admin == "1"):
            menu1_admin()
        elif (daftar_menu_admin == "2"):
            menu2_admin()
        elif (daftar_menu_admin == "3"):
            menu3_admin()
        elif (daftar_menu_admin == "4"):
            menu4_admin()
        else: 
            print('''
            Invalid!
            Data does not exist''')

#================================================== 
# LOGIN MENU MEMBER

def login_member():
    global current_user
    while True:
        input_member = input('''
            Username: ''')
        for unique_id, customer_data in Customer_List.items():    
            if input_member == customer_data['Username']:
                while True:
                    password_member = input('''
            Password: ''')
                    if password_member == customer_data['Password']:
                        current_user = input_member
                        print(f'''
            _________________________

            Welcome, {customer_data['Name']} :)
            _________________________''')
                        menu_member()
                        return
                    else:
                        print('''
            Incorrect Password
            Try Again''')
                    break
        else:
            print('''
            Username doesn't exist
            Try Again''')

def menu_member():                  #------------> Menu Utama Member
    while True:
        daftar_menu_member = input(f'''         
            1. All Films
            2. Search Film
            3. Buy Ticket
            4. My Tickets
            5. Logout
            Please choose one menu: ''')
        if (daftar_menu_member == "5"):
            checker = input('''
            Back to menu? (Y/N) : ''')
            if checker.lower() == 'y':
                login()
                break
            elif checker.lower() == 'n':
                break
            else: 
                print('''
            Invalid!
            select (Y/N)''')
        elif (daftar_menu_member == "1"):
            display_film_table()
            menu_member()
        elif (daftar_menu_member == "2"):
            menu2_member()
        elif (daftar_menu_member == "3"):
            menu3_member()
            menu_member()
        elif (daftar_menu_member == "4"):
            display_user_tickets()
        else: 
            print('''
            Invalid!
            Data does not exist''')

#================================================== 
# READ MENU ADMIN
       
def menu1_admin():
    while True:
        listcustomer = input('''
            1. View All Customer
            2. Search Customer
            3. Back
                         
            Choose One Menu: ''')
        if (listcustomer == '3'):
            while True:
                    checker = input('''
            Back to menu? (Y/N) : ''')
                    if checker.lower() == 'y':
                        menu_admin()
                        break
                    elif checker.lower() == 'n':
                        break
                    else: 
                        print('''
            Invalid!
            select (Y/N)''')
        elif (listcustomer == '1'): #----> Melihat Semua Customer
            display_customer_table()

        elif (listcustomer == '2'): #----> Mencari Customer Berdasarkan Keyword
            keyword = input('''
            Enter keyword to search : ''')
            results = []
            for unique_id, customer_info in Customer_List.items():
                if (keyword.lower() in customer_info['Username'].lower() or 
                    keyword.lower() in customer_info['Password'].lower() or 
                    keyword.lower() in customer_info['Name'].lower() or 
                    keyword.lower() in customer_info['Age'].lower() or 
                    keyword.lower() in customer_info['Phone Number'].lower() or 
                    keyword.lower() in customer_info['Gender'].lower()):
                    results.append({'Id': unique_id, **customer_info})
            if results:
                print(f"Found {len(results)} result(s):")
                table = []
                headers = ["Id", "Username", "Password", "Name", "Age", "Phone Number", "Gender"]
                for result in results:
                    table.append([result['Id'], result['Username'], result['Password'], 
                          result['Name'], result['Age'], result['Phone Number'], result['Gender']])

                print(tabulate(table, headers, tablefmt="grid"))

            else:
                print("No customer found with that keyword.")

def menu2_admin():
    while True: 
        edit_customer = input(f'''
            1. Add New Customer
            2. Delete Customer 
            3. Update Customer
            4. Back
            Please choose one menu: ''')
        if (edit_customer == "4"):
            while True:
                    checker = input('''
            Back to menu? (Y/N) : ''')
                    if checker.lower() == 'y':
                        menu_admin()
                        break
                    elif checker.lower() == 'n':
                        break
                    else: 
                        print('''
            Invalid!
            select (Y/N)''')
        elif (edit_customer == "1"):
            Add_Customer()
        elif (edit_customer == "2"):
            Delete_Customer()
        elif (edit_customer == "3"):
            Update_Customer()
        else: 
            print('''
            Invalid!
            Data does not exist''')

def menu3_admin():
    while True:
        listfilm = input('''
            1. All Films
            2. Search Film
            3. Back
                         
            Choose One Menu: ''')
        if (listfilm == '3'):
            while True:
                    checker = input('''
            Back to menu? (Y/N) : ''')
                    if checker.lower() == 'y':
                        menu_admin()
                        break
                    elif checker.lower() == 'n':
                        break
                    else: 
                        print('''
            Invalid!
            select (Y/N)''')
        elif (listfilm == '1'):
            display_film_table()
        elif (listfilm == '2'): #-----> Mencari Film Berdasarkan Keyword
            keyword = input('''
            Enter keyword to search : ''')
            results = []
            for film_id, film_info in Film_List.items():
                if (keyword.lower() in film_info['Film Id'].lower() or 
                    keyword.lower() in film_info['Title'].lower() or 
                    keyword.lower() in film_info['Genre'].lower() or 
                    keyword.lower() in film_info['Rating'].lower() or 
                    keyword.lower() in film_info['Duration (Minutes)'].lower() or 
                    keyword.lower() in film_info['IMDb Score'].lower()):
                    results.append({'Film Id': film_id, **film_info})
            if results:
                print(f"Found {len(results)} result(s):")
                table = []
                headers = ["Film Id", "Title", "Genre", "Rating", "Duration (Minutes)", "IMDb Score"]
                for result in results:
                    table.append([result['Film Id'], result['Title'], result['Genre'], 
                          result['Rating'], result['Duration (Minutes)'], result['IMDb Score']])

                print(tabulate(table, headers, tablefmt="grid"))

            else:
                print("No Film found with that keyword.")
        else: 
            print('''
            Invalid!''')

def menu4_admin():
    while True:
        edit_film = input(f'''
            1. Add New Film
            2. Delete Film
            3. Update Film
            4. Back
            Please choose one menu: ''')
        if (edit_film == "4"):
            while True:
                    checker = input('''
            Back to menu? (Y/N) : ''')
                    if checker.lower() == 'y':
                        menu_admin()
                        break
                    elif checker.lower() == 'n':
                        break
                    else: 
                        print('''
            Invalid!
            select (Y/N)''')
        elif (edit_film == "1"):
            Add_Film()
        elif (edit_film == "2"):
            Delete_Film()
        elif (edit_film == '3'):
            Update_Film()
        else: 
            print('''
            Invalid!
            Data does not exist''')

#================================================== 
# READ MENU MEMBER

def menu2_member():
    keyword = input('''
            Enter keyword to search : ''')
    results = []
    for film_id, film_info in Film_List.items():
        if (keyword.lower() in film_info['Film Id'].lower() or 
            keyword.lower() in film_info['Title'].lower() or 
            keyword.lower() in film_info['Genre'].lower() or 
            keyword.lower() in film_info['Rating'].lower() or 
            keyword.lower() in film_info['Duration (Minutes)'].lower() or 
            keyword.lower() in film_info['IMDb Score'].lower()):
            results.append({'Film Id': film_id, **film_info})
            if results:
                print(f"Found {len(results)} result(s):")
                table = []
                headers = ["Film Id", "Title", "Genre", "Rating", "Duration (Minutes)", "IMDb Score"]
                for result in results:
                    table.append([result['Film Id'], result['Title'], result['Genre'], 
                                  result['Rating'], result['Duration (Minutes)'], result['IMDb Score']])

                print(tabulate(table, headers, tablefmt="grid"))
            else:
                print("No Film found with that keyword.")
        else: 
            print('''
            Invalid!''')

def display_user_tickets():
    global current_user
    if current_user not in User_Tickets or not User_Tickets[current_user]:
        print('''
            You have no tickets.''')
        return
    
    print('''
            Your Tickets:''')
    headers = ["Film", "Amount"]
    table_data = [[ticket["Film"], ticket["Amount"]] for ticket in User_Tickets[current_user]]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

#================================================== 
#CREATE MENU
def Add_Customer():         #------------> Menu Menambah Customer
    while True:
        Add_choices = input('''
            1. Add Customer
            2. Back
            Choose one menu: ''')
        if Add_choices == '1':
            Menu1_Add_Customer()
        elif Add_choices == '2':
            while True:
                    checker = input('''
            Back to menu? (Y/N) : ''')
                    if checker.lower() == 'y':
                        menu_admin()
                        break
                    elif checker.lower() == 'n':
                        break
                    else: 
                        print('''
            Invalid!
            select (Y/N)''')
        else : print('''
            Invalid menu!''')
def Menu1_Add_Customer():
    while True:
        ID_exist = False
        try:
            ID = int(input('''
            Input Id : ''')) 
            if ID > 0:
                ID = ID
                break
            else:
                print('''
            Input Number more than zero!''') 
        except:
            print('''
            Input Number Only!''')
        
    for unique_id, customer_data in Customer_List.items():    
        if "CI"+str(ID) == customer_data['Id']:
            print('''
            Id is already exist''')
            ID_exist = True
            Menu1_Add_Customer()
            return
        elif len(str(ID)) == 0:
                print('''
            Invalid input''')
                ID_exist = True
                Menu1_Add_Customer()
        if ID_exist: 
            continue
    while True:
        username_exist = False
        Username = input('''
            Username : ''')
        for unique_id, customer_data in Customer_List.items():    
            if Username == customer_data['Username']:
                print('''
            Username is already exist''')
                username_exist = True
                break
            elif len(Username) == 0:
                    print('''
            Invalid input''')
                    username_exist = True
                    break
        if username_exist:
            continue
        while True:
            Password = (input(f'''
            Password : '''))
            if len(Password) ==0:
                continue
            while True:
                Name = (input('''
            Name : ''').title())
                name_exist = False
                for unique_id, customer_data in Customer_List.items():    
                    if Name == customer_data['Name']:
                        print('''
            Name is already exist''')
                        name_exist = True
                        break
                    elif len(Name) == 0:
                        print('''
            Invalid input''')
                        name_exist = True
                        break
                if name_exist:
                    continue
                while True:
                    try:   
                        Age = int(input('''
            Age : '''))
                        if Age > 0:
                            break
                        elif len(Age) == 0:
                            print('''
            Invalid input''')
                            name_exist = True
                            break
                        else:
                            print('''
            Invalid Input. Please enter a valid number of age.''')
                    except:
                        print('''
            Invalid input. Please enter a number.''')
                while True:
                    try:
                        Phone_Number = int(input('''
            Phone number : '''))
                        if Phone_Number > 0:
                            break
                        else:
                            print('''
            Invalid Input. Please enter a valid number phone number.''')
                    except:
                        print('''
            Invalid input. Please enter format with number.''')
                while True:
                    Gender = input('''
            Gender (Male/Female) : ''')
                    if Gender.capitalize() == 'Male' or Gender.capitalize() == 'Female':
                        break
                    else:
                        print('''
            Invalid Input. Choose Male or Female.''')
                unique_id = ID

                new_member = {'Id':"CI"+str(unique_id), 
                        'Username':Username,
                        'Password':Password,
                        'Name':Name,
                        'Age':Age,
                        'Phone Number':Phone_Number,
                        'Gender':Gender}

                headers = ["Id", "Username", "Password", "Name", "Age", "Phone Number", "Gender"]
                new_table_data = [[new_member[key] for key in headers]]
                print(tabulate(new_table_data, headers=headers, tablefmt="grid"))

                while True :
                    checker = input('''
            Is your data correct? (Y/N) : ''')
                    if checker.lower() == 'y':
                        Customer_List[unique_id] = new_member
                        display_customer_table()
                        print ('''
            Your data is saved''')
                        return
                    elif checker.lower() == 'n':
                        display_customer_table()
                        print ('''
            Your data is not saved''')
                        return
                    else :
                        print('''
            Invalid code, choose Y/N''')

def Add_Film():             #------------> Menu Menambah Film
    while True:
        Add_choices = input('''
            1. Add Film
            2. Back
            Choose one menu: ''')
        if Add_choices == '1':
            Menu1_Add_Film()
        elif Add_choices == '2':
            while True:
                    checker = input('''
            Back to menu? (Y/N) : ''')
                    if checker.lower() == 'y':
                        menu_admin()
                        break
                    elif checker.lower() == 'n':
                        break
                    else: 
                        print('''
            Invalid!
            select (Y/N)''')
        else : print('''
            Invalid menu!''')    

def Menu1_Add_Film():    
    while True:
        Film_ID_exist = False
        try:
            ID = int(input('''
            Input Id : ''')) 
            if ID > 0:
                ID = ID
                break
            else:
                print('''
            Input Number more than zero!''') 
        except:
            print('''
            Input Number Only!''')
        
    for film_id, film_data in Film_List.items():    
        if "MO"+str(ID) == film_data['Film Id']:
            print('''
            Id is already exist''')
            Film_ID_exist = True
            Menu1_Add_Film()
            return
        elif len(str(ID)) == 0:
                print('''
            Invalid input''')
                Film_ID_exist = True
                Menu1_Add_Film()
        if Film_ID_exist: 
            continue
    while True :
        Title_exist = False
        Title = input('''
            Title : ''').title()
    
        for film_id, film_data in Film_List.items():    
            if Title == film_data['Title']:
                print('''
            Title is already exist''')
                Title_exist = True
                break
            elif len(Title) == 0:
                    print('''
            Invalid input''')
                    Title_exist = True
                    break

        if Title_exist:
            continue    

        Genre = input('''
            Genre : ''').title()
        Rating = input('''
            Rating : ''').upper()
        while True:
            try:   
                Duration = int(input('''
            Duration (in minutes) : '''))
                if 1 <= Duration <= 1000:
                    break
                else:
                    print('''
            Invalid Input. Please enter a number between 1 and 1000 minutes.''')
            except:
                print('''
            Invalid input. Please enter a valid number of duration.''')
        while True:
            try:
                IMDb_Score = float(input('''
            IMDb Score (1-10) : '''))
                if 1 <= IMDb_Score <= 10:
                    break
                else:
                    print('''
            Invalid Input. Please enter a number between 1 and 10.''')    
            except:
                print('''
            Invalid Input. Please enter a format number.''')
        
        ID = film_id

        new_film = {'Film Id':str(film_id),  
                    'Title':Title,
                    'Genre':Genre,
                    'Rating':Rating,
                    'Duration (Minutes)':Duration,
                    'IMDb Score':IMDb_Score}

        headers = ["Film Id", "Title", "Genre", "Rating", "Duration (Minutes)", "IMDb Score"]
        new_table_data = [[new_film[key] for key in headers]]
        print(tabulate(new_table_data, headers=headers, tablefmt="grid"))

        while True :
            checker = input('''
            Is your data correct? (Y/N) : ''')
            if checker.lower() == 'y':
                Film_List[film_id] = new_film
                display_film_table()
                print ('''
            Your data is saved, Please check''')
                return
            elif checker.lower() == 'n':
                print ('''
            Your data is not saved, please try again''')
                return
            else :
                print('''
            Invalid code, choose Y/N''')

#================================================== 
# UPDATE MENU ADMIN

def Update_Customer():      #------------> Menu Mengupdate Customer  
    display_customer_table()
    customer = input('''
            Input Customer Id (ex: CI0001): ''').upper()
    if customer not in Customer_List:
        print('''
            Customer Doesn't Exist.''')
        return
    
    print(f'''
            Customer Data: 
            {Customer_List[customer]}''')
    while True :
            checker = input('''
            Continue Update? (Y/N) : ''')
            if checker.lower() == 'y':
                break
            elif checker.lower() == 'n':
                print ('''
            Action canceled''')
                return
            else :
                print('''
            Invalid code, choose Y/N''')

    field = input('''
            Insert menu you want to update : ''').capitalize()
    if field not in Customer_List[customer]:
        print('''
            Menu invalid.''')
        return
    
    new_value = input(f'''
            Insert new value of {field}: ''')

    while True :
            checker = input('''
            Update data? (Y/N) : ''')
            if checker.lower() == 'y':
                break
            elif checker.lower() == 'n':
                print ('''
            Action canceled''')
                return
            else :
                print('''
            Invalid code, choose Y/N''')
                
    Customer_List[customer][field] = new_value
    display_film_table()
    print('''
            Data succesfully updated.''')
    return

def Update_Film():          #------------> Menu Mengupdate Film
    display_film_table()
    film = input('''
            Input Film Id (ex: MO0001): ''').upper()
    if film not in Film_List:
        print('''
            Film Doesn't Exist.''')
        return
    
    print(f'''
            Film Data: 
            {Film_List[film]}''')
    while True :
            checker = input('''
            Continue Update? (Y/N) : ''')
            if checker.lower() == 'y':
                break
            elif checker.lower() == 'n':
                print ('''
            Action canceled''')
                return
            else :
                print('''
            Invalid code, choose Y/N''')

    field = input('''
            Insert menu you want to update : ''').capitalize()
    if field not in Film_List[film]:
        print('''
            Menu invalid.''')
        return
    
    new_value = input(f'''
            Insert new value of {field}: ''')

    while True :
            checker = input('''
            Update data? (Y/N) : ''')
            if checker.lower() == 'y':
                break
            elif checker.lower() == 'n':
                print ('''
            Action canceled''')
                return
            else :
                print('''
            Invalid code, choose Y/N''')
                
    Film_List[film][field] = new_value
    display_film_table()
    print('''
            Data succesfully updated.''')
    return

#================================================== 
# UPDATE MENU MEMBER

def menu3_member():         #------------> Menu Membeli Tiket
    global current_user
    while True:
        display_film_table()
        film = input('''
            Input Film Id you want to watch: ''').upper()
    
        if film in Film_List:
            break
        else:
            print('''
            Invalid Film Id.''')
    while True:
        amount = int(input('''
            Enter number of ticket: '''))
        price = 50000
        total = price*amount
        confirm = input(f'''
            Confirm to order {Film_List[film]['Title']}
            Total : IDR {total}
        
            Is your order correct?(Y/N) : ''').lower()
        if confirm == 'y':
            while True:
                money = int(input(f'''
            Total of your purchase is IDR {total}
            Please insert your money: '''))
                if money >= total:
                    if current_user not in User_Tickets:
                        User_Tickets[current_user] = []
                    User_Tickets[current_user].append({
                        "Film": Film_List[film]['Title'],
                        "Amount":amount
                    })
                    headers = ["Film", "Amount"]
                    new_table_data = [[Film_List[film]['Title'], amount]]
                    print(tabulate(new_table_data, headers=headers, tablefmt='grid'))
                    if money > total:
                        print(f'''
            Purchase Successful. Your change is IDR {money-total}''')    
                    else:
                        print('''
            Purchase Successful. Thank you :)''')
                    return
                else:
                    print(f'''
            Your order canceled. you need more IDR {total-money} to purchase.''')      
        elif confirm == 'n':
            print('''
            Order Canceled.''')
            return
        else : 
            print('''
            Invalid Menu! 
            Choose Y/N.''')


#================================================== 
# DELETE MENU
def Delete_Customer():      #------------> Menu Menghapus Customer
    if not Customer_List:
        display_customer_table()
        print('''
            No customer ID or name to delete.''')
        return
    display_customer_table()
    while True:
        delete_by = input('''
            Delete customer by (ID/Name): ''').capitalize()
        if delete_by in ['Id', 'Name']:
            break
        else : 
            print('''
            Invalid option. Please choose ID or Name.''')
    while True:    
        if delete_by == 'Id':
            identifier = input(f'''
            Enter the {delete_by} of the customer to delete: ''').upper()
        elif delete_by == 'Name':
            identifier = input(f'''
            Enter the {delete_by} of the customer to delete: ''').title()
        for unique_id, customer_data in Customer_List.items():    
            if customer_data[delete_by] == identifier:
                print(customer_data)
                while True:
                    checker = input('''
            Are you sure want to delete this customer? (Y/N) : ''')
                    if checker.lower() == 'y':
                        break
                    elif checker.lower() == 'n':
                        print('''   
            Action canceled.''')
                        menu2_admin()
                    else:
                        print('''
            Invalid option. Please choose Y or N.''')
                del Customer_List[unique_id]
                print(f'''
            Customer with {delete_by} '{identifier}' has been deleted.''')
                display_customer_table()
                return
            else:
                print(f'''
            Customer with {delete_by} '{identifier}' cant be found.''')
            return

def Delete_Film():          #------------> Menu Menghapus Film
    if not Film_List:
        display_film_table()
        print('''
            No Film ID or Title to delete.''')
        return
    display_film_table()
    while True:
        delete_by = input('''
            Delete film by (Film Id/Title): ''').title()
        if delete_by in ['Film Id', 'Title']:
            break
        else : 
            print('''
            Invalid option. Please choose Film Id or Title.''')
    while True:    
        if delete_by == 'Film Id':
            identifier = input(f'''
            Enter the Id of the film to delete: ''').upper()
        elif delete_by == 'Title':
            identifier = input(f'''
            Enter the {delete_by} of the film to delete: ''').title()
        for film_id, film_data in Film_List.items():    
            if film_data[delete_by] == identifier:
                while True:
                    checker = input('''
            Are you sure want to delete this film? (Y/N) : ''')
                    if checker.lower() == 'y':
                        break
                    elif checker.lower() == 'n':
                        print('''   
            Action canceled.''')
                        menu4_admin()
                    else:
                        print('''
            Invalid option. Please choose Y or N.''')
                del Film_List[film_id]
                print(f'''
            Film with {delete_by} '{identifier}' has been deleted.''')
                display_film_table()
                return
            else:
                print(f'''
            Film with {delete_by} '{identifier}' cant be found.''')

login()



