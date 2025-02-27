contacts = {}

while True:
    print('\nContact Book App')
    print('1.Create contact')
    print('2.View Contact')
    print('3.Update Contact')
    print('4.Delete Contact')
    print('5.search Contact')
    print('6.Count Contacts')
    print('7.Exit')

    choise= input('Enter your choise= ')

    if choise == '1':
        name=input('Enter Your name= ')
        if name in contacts:
            print('Contact name {name} already exsists...!')
        else:
            age= input('Enter age= ')
            email= input('Enter E-mail= ')
            mobile= input('Enter mobile Number= ')
            contacts[name]={'age':int(age),'email':email,'mobile':mobile}
            print(f'contact name{name} has been created successfully....!')
    elif choise== '2':
        name=input('Enter Contact name to View= ')
        if name in contacts:
           contact=contacts[name]
           print(f'Name:{name}, age:{age},Mobile number:{mobile}')
        else:
            print('Contact not Found....!')
    elif choise == '3':
        name= input('Enter name to Update Contact = ')
        if name in contacts:
            age=input('Enter Updating age = ')
            email=input('Enter the updating email= ')
            mobile=input('enter the updating mobile mumber= ')
            contacts[name]={'age':int(age),'email':email,'mobile':mobile}
        else:
            print('Cntact not Found...!')
    elif choise == '4':
        name=input('Enter Contact name to delete= ')
        if name in contacts:
            del contacts[name]
            print(f'the contact {name} has been deleted successfuly..!')
        else:
            print('contact not found....!')
    
    elif choise== "5":
        search_name=input('eter the name of the Contact you need to search= ')
        found=False
        for name,contacts in contacts.items():
            if search_name.lowe() in name.lower():
                print("found-name: {name}, age:{age},mobile number:{mobile}, email:{email}")
                found=True
        if not found:
            print('No Contact found With that name...!')
    elif choise=="6":
        print(f'The Total Contacts in the book are: {len(contacts)}')

    elif choise=='7':
        print('Have a great day ........')
        break
    else:
        print('invalid nimber Entered')
