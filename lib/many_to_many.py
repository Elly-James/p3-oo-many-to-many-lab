from datetime import datetime

class Author:
    all = []  

    def __init__(self, name):
        self.name = name
        self._contracts = []  
        Author.all.append(self)

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("The book must be an instance of the Book class.")
        if not isinstance(date, str):
            raise Exception("The date must be a string.")
        if not isinstance(royalties, (int, float)) or royalties < 0:
            raise Exception("Royalties must be a positive number.")

        contract = Contract(author=self, book=book, date=date, royalties=royalties)
        self._contracts.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


class Book:
    all = []  

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return list({contract.author for contract in self.contracts()})


class Contract:
    all = []  

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("The author must be an instance of the Author class.")
        if not isinstance(book, Book):
            raise Exception("The book must be an instance of the Book class.")
        if not isinstance(date, str):
            raise Exception("The date must be a string.")
        if not isinstance(royalties, (int, float)) or royalties < 0:
            raise Exception("Royalties must be a positive number.")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

       
        if self not in author._contracts:
            author._contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Return a list of contracts that match the given date, sorted by royalties."""
        matching_contracts = [contract for contract in cls.all if contract.date == date]
       
        return sorted(matching_contracts, key=lambda contract: contract.royalties)



def test_contract_contracts_by_date():
    """Test Contract class has method contracts_by_date() that sorts all contracts by date"""
    Contract.all = []  
    author1 = Author("Name 1")
    book1 = Book("Title 1")
    book2 = Book("Title 2")
    book3 = Book("Title 3")
    author2 = Author("Name 2")
    book4 = Book("Title 4")
    contract1 = Contract(author1, book1, "02/01/2001", 10)
    contract2 = Contract(author1, book2, "01/01/2001", 20)
    contract3 = Contract(author1, book3, "03/01/2001", 30)
    contract4 = Contract(author2, book4, "01/01/2001", 40)

 
    assert Contract.contracts_by_date("01/01/2001") == [contract2, contract4]



if __name__ == "__main__":
    author1 = Author("Author One")
    book1 = Book("Book One")
    book2 = Book("Book Two")

    contract1 = author1.sign_contract(book1, "20/02/2025", 10)
    contract2 = author1.sign_contract(book2, "21/02/2025", 15)

    print(author1.contracts())  
    print(author1.books())  
    print(author1.total_royalties())  
    print(Contract.contracts_by_date("20/02/2025"))  


    test_contract_contracts_by_date()