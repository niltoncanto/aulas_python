from datetime import datetime

# Classe Contact
class Contact:
    def __init__(self, name: str, address: str, age: int, gender: str):
        self.name = name
        self.address = address
        self.age = age
        self.gender = gender

    @classmethod
    def createContact(cls, name: str, age: int):
        return cls(name, "", age, "")

# Subclasse Friend de Contact
class Friend(Contact):
    def __init__(self, name: str, address: str, age: int, gender: str, firstMet: datetime):
        super().__init__(name, address, age, gender)
        self.firstMet = firstMet

# Subclasse Relative de Contact
class Relative(Contact):
    def __init__(self, name: str, address: str, age: int, gender: str, relationship: str):
        super().__init__(name, address, age, gender)
        self.relationship = relationship

# Classe Category
class Category:
    def __init__(self, title: str, desc: str):
        self.title = title
        self.desc = desc
        self.contacts = []  # Composição: Category contém uma lista de contatos

    def add_contact(self, contact: Contact):
        self.contacts.append(contact)

# Classe PhoneBook
class PhoneBook:
    def __init__(self, owner: str):
        self.owner = owner
        self.createDate = datetime.now()
        self.categories = []  # Composição: PhoneBook contém várias categorias

    def createPhoneBook(self, owner: str):
        return PhoneBook(owner)

    def add_category(self, category: Category):
        self.categories.append(category)

# Exemplo de utilização
if __name__ == "__main__":
    # Criando um PhoneBook
    phonebook = PhoneBook("João Silva")

    # Criando uma categoria
    family_category = Category("Família", "Contatos da família")

    # Criando contatos
    contact1 = Relative("Maria Souza", "Rua A, 123", 30, "F", "Prima")
    contact2 = Friend("Carlos Oliveira", "Rua B, 456", 28, "M", datetime(2020, 5, 12))

    # Adicionando contatos à categoria
    family_category.add_contact(contact1)
    family_category.add_contact(contact2)

    # Adicionando a categoria ao PhoneBook
    phonebook.add_category(family_category)

    # Exibindo informações do PhoneBook
    print(f"PhoneBook de {phonebook.owner}, criado em {phonebook.createDate}")
    for category in phonebook.categories:
        print(f"Categoria: {category.title} - {category.desc}")
        for contact in category.contacts:
            print(f"Contato: {contact.name}, {contact.address}, {contact.age} anos")
