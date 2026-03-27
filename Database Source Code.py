def add():
    import pickle
    f=open('mob.dat','wb')
    s={}
    ans='y'
    while ans=='y':

        s['Model']=input("Enter the Model: \n")
        s['Brand Name']=input("Enter the Brand Name: \n")
        s['Price']=input("Enter the Price: \n")
        s['Screen Size']=input("Enter the Screen Size: \n")
        s['Display Technology']=input("Enter the Display Technology: \n")
        s['Resolution']=input("Enter the Resolution: \n")
        s['Warranty Period']=input("Enter the Warranty Period: \n")
        s['OS']=input("Enter the Operating System: \n")
        s['Country of Origin']=input("Enter the Country of Origin: \n")
        s['Item Weight']=input("Enter the Item Weight: \n")
        print(s)
        pickle.dump(s,f)
        ans=input("Want to Enter more Records [y/n]:") 
    f.close()


def display():
    import pickle
    f=open('mob.dat','rb')
    try:
        while True:
            s=pickle.load(f)
            print(s)
    except EOFError:
        f.close()

def search():
    import pickle
    f=open('mob.dat','rb')
    found='f'
    m=input("Enter the Model you are searching for:")
    try:
        while True:
            s=pickle.load(f)
            if s['Model']==m:
                print("Record found")
                print(s)
                found='t'           
                
    except EOFError:
        if found=='f':
            print("Record not found")
        f.close()


def update():
    import pickle
    s={}
    f=open('mob.dat','rb+')
    found='f'
    m=input("Enter the Model you need to Update:")
    try:
        while True:
            pos=f.tell()
            s=pickle.load(f)
            if s['Model']==m:
                found='t'
                print("Record found")
                print("Enter the new Rcord")
                s['Model']=input("Enter the Model: \n")
                s['Brand Name']=input("Enter the Brand Name: \n")
                s['Price']=input("Enter the Price: \n")
                s['Screen Size']=input("Enter the Screen Size: \n")
                s['Display Technology']=input("Enter the Display Technology: \n")
                s['Resolution']=input("Enter the Resolution: \n")
                s['Warranty Period']=input("Enter the Warranty Period: \n")
                s['OS']=input("Enter the Operating System: \n")
                s['Country of Origin']=input("Enter the Country of Origin: \n")
                s['Item Weight']=input("Enter the Item Weight: \n")
                f.seek(pos)
                pickle.dump(s,f)
                break
                
            
    except EOFError:
        if found=='t':
            print("Record Updated")
        else:
            print("Record not found")
        f.close()

def delete():
    import pickle
    import os
    found='f'
    s={}
    f=open('mob.dat','rb+')
    f1=open('mob1.dat','wb+')
    m=input("Enter the Model number you want to delete:")
    try:
        while True:
            s=pickle.load(f)
            if s['Model']!=m:
                pickle.dump(s,f1)
            else:
                found='t'
    except EOFError:
        if found=='t':
            print("Record found and deleted")
        else:
            print("Record does not exist in the file.")
        f.close()
        f1.close()
        os.remove('mob.dat')
        os.rename('mob1.dat','mob.dat')

###############################################################################

ch=1
while ch<=6:
    print("\t\t## Main Menu ##")
    print(" \n1.To Add a new record of Television:")
    print(" \n2.To Display all the records of Televisions :")
    print(" \n3.To Search a record of Television:")
    print(" \n4.To Update a record of Television:")
    print(" \n5.To Delete a record of Television:")
    print(" \n6.To Exit the Menu \n ")
    ch=int(input("Enter your choice [1-6]:"))
    if ch==1:
        print("Add Record")
        add()
    elif ch==2:
        print("Display all Records")
        display()
    elif ch==3:
        print("Search a Record")
        search()
    elif ch==4:
        print("Update a Record")
        update()
    elif ch==5:
        print("Delete a Record")
        delete()
    elif ch==6:
        print("Thank You for your visit to our Television showroom Database.")
        print("Exit Program")
        break
    else:
        print("Invalid Choice")


   
            
