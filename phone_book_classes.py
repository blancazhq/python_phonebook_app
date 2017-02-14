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

class Phonebook(object):

    phone_book_dict = {}

    def __init__(self, name, email, phone_number, website_url):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.website_url = website_url

    def look_up(self):
        print "Found entry for %s: %s, %s, %s" % (self.name, self.phone_number, self.email, self.website_url)

    def set_entry(self):

        phonebook_dict_entry = {"name": self.name, "phone_number": self.phone_number, "email": self.email, "website_url": self.website_url}
        phonebook_dict[self.name] = phonebook_dict_entry
        print "Entry stored for %s." % self.name

    def delete_entry(self):

        del phonebook_dict[self.name]
        print "Deleted entry for %s." % self.name


    def list_all_entry(self):
        print "\n"
        for name, value in phonebook_dict.items():
            print "Found entry for %s: \n\tphone_number: %s, \n\temail: %s,  \n\tWebsite: %s" % (name, value["phone_number"], value["email"], value["website_url"])

    def save_database(self):
        myfile = open("phonebook.pickle", "w")
        pickle.dump(phonebook_dict, myfile)
        myfile.close()
        print "\n"
        print "Entries saved to phonebook.pickle"

    def restore_saved(self):
        myfile = open('phonebook.pickle', 'r')
        while True:
            try:
                phonebook_dict.update(pickle.load(myfile))
            except EOFError:
                break
        print "\n"
        print "Restored save entries."


    def quit(self):
        global runner
        runner = False

runner = True
my_data = {}
phonebook_dict = {}

while runner == True:
    print_menu()
    while True:
        try:
            input_number = int(raw_input("What do you want to do (1-7)?"))

            if input_number == 1:
                name = raw_input("name: ")
                my_data[name].look_up()

            elif input_number == 2:
                print "\n"
                name = raw_input("Name: ")
                phone_number = raw_input("Phone Number: ")
                email = raw_input("Email: ")
                website_url = raw_input("Website: ")
                my_data[name] = Phonebook(name, phone_number, email, website_url)
                my_data[name].set_entry()

            elif input_number == 3:
                name = raw_input("name: ")
                my_data[name].delete_entry()

            elif input_number == 4:
                my_data[name].list_all_entry()

            elif input_number == 5:
                my_data[name].save_database()
            elif input_number == 6:
                my_data[name].restore_saved()
            elif input_number == 7:
                my_data[name].quit()
                break
            print_menu()
        except ValueError:
            print "Not an number. Try again."
            continue
else:
    print "Bye"
