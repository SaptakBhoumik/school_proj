import csv
def add_customer_record(customer_db,room_db):
    id=input("Enter id: ")
    name=input("Enter name: ")
    room_no=input("Enter room no: ")
    data=[id,name,room_no]
    #Check for duplicate and then add
    with open(customer_db, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0]==id:
                print("Duplicate id found")
                return
    record=[]
    found=False
    with open(room_db, 'r') as f:
        record = list(csv.reader(f))
    for i in range(len(record)):
        if record[i][0]==room_no:
            if record[i][1]=='y':
                print("Room already occupied")
                return
            record[i][1]='y'
            found=True
            break     
    if found==False:
        print("Room not found")
        return   
    with open(room_db, 'w') as f:
        writer = csv.writer(f)
        for row in record:
            writer.writerow(row)
    with open(customer_db, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def add_room_record(room_db):
    room_no=input("Enter room no: ")
    data=[room_no,'n']
    with open(room_db, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0]==room_no:
                print("Duplicate room no found")
                return
    with open(room_db, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def delete_custormer(customer_db,room_db):
    id=input("Enter id: ")
    idx1=-1
    record1=[]
    record2=[]
    data=[]
    with open(customer_db, 'r') as f:
        record1 = list(csv.reader(f))
        for i in range(len(record1)):
            if record1[i][0]==id:
                idx1=i
                data=record1[i]
                break
    if idx1==-1:
        print("Record not found")
        return
    with open(room_db, 'r') as f:
        record2 = list(csv.reader(f))
        for i in range(len(record2)):
            if record2[i][0]==data[2]:
                record2[i][1]='n'
                break   
    with open(room_db, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(record2)
    del record1[idx1]
    with open(customer_db, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(record1)
    
def add_transaction_info(customer_db):
    id=input("Enter id: ")
    record=[]
    idx=-1
    with open(customer_db, 'r') as f:
        record = list(csv.reader(f))
        for i in range(len(record)):
            if record[i][0]==id:
                idx=i
                break
    if idx==-1:
        print("Record not found")
        return
    paid=input("Paid? (y/n): ")
    if len(record[idx])==3:
        amt=float(input("Enter amount: "))
        record[idx].append(amt)
        record[idx].append(paid)
    else:
        record[idx][4]=paid
    with open(customer_db, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(record)

def show_billing_info(customer_db):
    id=input("Enter id: ")
    found=False
    data=[]
    with open(customer_db, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0]==id:
                found=True
                data=row
                break
    if found==False:
        print("Record not found")
        return
    print("Id: ",data[0])
    print("Name: ",data[1])
    print("Room no: ",data[2])
    if len(data)!=3:
        print("Amount: ",data[3])
        print("Paid: ",data[4])

def room_info(room_db):
    room_no=input("Enter room no: ")
    found=False
    data=[]
    with open(room_db, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0]==room_no:
                found=True
                data=row
                break
    if found==False:
        print("Record not found")
        return
    print("Room no: ",data[0])
    print("Occupied: ",data[1])
def delete_room(room_db):
    room_no=input("Enter room no: ")
    idx=-1
    record=[]
    with open(room_db, 'r') as f:
        record = list(csv.reader(f))
        for i in range(len(record)):
            if record[i][0]==room_no:
                idx=i
                break
    if idx==-1:
        print("Record not found")
        return
    if record[idx][1]=='y':
        print("Room is occupied")
        return
    del record[idx]
    with open(room_db, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(record)
def show_menu():
    print("Hotel Management System")
    print("1. Show customer records")
    print("2. Add customer record")
    print("3. Add room record")
    print("4. Delete customer record")
    print("5. Add/Modify transaction info")
    print("6. Show room info")
    print("7. Delete room")
    print("8. Exit")
    customer_db="customer_db.csv"
    room_db="room_db.csv"
    while True:
        i=int(input("Enter choice: "))
        if i==1:
            show_billing_info(customer_db)
        elif i==2:
            add_customer_record(customer_db,room_db)
        elif i==3:
            add_room_record(room_db)
        elif i==4:
            delete_custormer(customer_db,room_db)
        elif i==5:
            add_transaction_info(customer_db)
        elif i==6:
            room_info(room_db)
        elif i==7:
            delete_room(room_db)
        elif i==8:
            return
        else: 
            print("Invalid choice\nTry again")

show_menu()