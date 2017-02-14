import pickle

def print_menu():
    print "\n"
    print "Electronic Phone Book"
    print "====================="
    print "1. Look up an entry"
    print "2. Set an entry"
    print "3. Delete an entry"
    print "4. List all entries"
    print "5. Save entries"
    print "6. Restore saved entries"
    print "7. Quit"
    print "\n"

def look_up():

    global phonebook_dict

    counter = 0

    while True:

        print "\n"

        name = raw_input("Name: ")

        counter += 1

        if phonebook_dict.get(name) == None:
            print "Name does not exist."
            if counter > 2:
                print "Too many trials."
                break
            continue
        else:
            break

    if counter <=2:
        print "Found entry for %s: %s, %s, %s" % (name, phonebook_dict[name]["phone_number"], phonebook_dict[name]["email"], phonebook_dict[name]["website_url"])


def set_entry():

    global phonebook_dict

    print "\n"

    phonebook_dict_entry = {}

    name = raw_input("Name: ")

    phone_number = raw_input("Phone Number: ")

    email = raw_input("Email: ")

    website_url = raw_input("Website: ")

    phonebook_dict_entry = {"name": name, "phone_number": phone_number, "email": email, "website_url": website_url}

    phonebook_dict[name] = phonebook_dict_entry

    print "Entry stored for %s." % name

def delete_entry():

    global phonebook_dict

    counter = 0

    while True:

        print "\n"

        name = raw_input("Name: ")

        counter += 1

        if phonebook_dict.get(name) == None:
            print "Name does not exist."
            if counter > 2:
                print "Too many trials."
                break
            continue
        else:
            break

    if counter <=2:
        del phonebook_dict[name]
        print "Deleted entry for %s." % name


def list_all_entry():
    global phonebook_dict

    print "\n"

    for name, value in phonebook_dict.items():
        print "Found entry for %s: \n\tPhone_number: %s, \n\tEmail: %s,  \n\tWebsite: %s" % (name, value["phone_number"], value["email"], value["website_url"])

def save_database():

    myfile = open("phonebook.pickle", "w")

    pickle.dump(phonebook_dict, myfile)

    myfile.close()

    print "\n"

    print "Entries saved to phonebook.pickle"

def restore_saved():
    global phonebook_dict

    myfile = open('phonebook.pickle', 'r')

    while True:
        try:
            phonebook_dict.update(pickle.load(myfile))
        except EOFError:
            break

    print "\n"

    print "Restored save entries."


def quit():
    global runner
    runner = False

runner = True
phonebook_dict = {}

while runner == True:
    print_menu()
    while True:
        try:
            input_number = int(raw_input("What do you want to do (1-7)?"))
            if input_number == 1:
                look_up()
            elif input_number == 2:
                set_entry()
            elif input_number == 3:
                delete_entry()
            elif input_number == 4:
                list_all_entry()
            elif input_number == 5:
                save_database()
            elif input_number == 6:
                restore_saved()
            elif input_number == 7:
                quit()
                break
            print_menu()
        except ValueError:
            print "Not an number. Try again."
            continue
else:
    print "Bye"
