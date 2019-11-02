class ContactList(list):
    def __init__(self,*all):
        self.all = all


    def search_by_name(self, search_name):
        l = [print(x) for x in self.all if x == search_name]

name = input("Enter your name: ")
contacts = ContactList('Azamat', 'Bek', 'Maksat')
contacts.search_by_name(name)


  

