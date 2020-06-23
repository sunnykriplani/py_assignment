# LAB 1 Assignment CS6505
# Author:- Sunny Kriplani
# Student Id:- 119220438


# CreditCard class to store the details of customers who purchased creditcard
# and payment related details
class CreditCard:
    Customers = []

    def __init__(self, name, bank, accnt, limit, balance):
        self.__name = name
        self.__bank = bank
        self.__accnt = accnt
        # Need to verify is limit set is negative as logic works on negative
        if(limit > 0):
            limit = 0 - limit
        self.__limit = limit
        self.__balance = balance
        CreditCard.Customers.append(self)

    # Getters for all the instance variables
    def get_name(self):
        return self.__name

    def get_bank(self):
        return self.__bank

    def get_accnt(self):
        return self.__accnt

    def get_limit(self):
        return self.__limit

    def get_balance(self):
        return self.__balance

    # Whenever a charge is made, limit of card has to be checked before hand
    def charge(self, price):
        if self.__balance - price >= self.__limit:
            self.__balance = self.__balance - price
            return True
        return False

    # Payment received by customers against the outstanding balance
    def make_payment(self, amount):
        self.__balance = self.__balance + amount

    # Per Class function to list all the creditcard assigned to the customers
    def show_summary():
        if len(CreditCard.Customers) > 0:
            accounts = sorted(CreditCard.Customers, key=lambda x: x.__name,
                              reverse=False)
            for acc in accounts:
                print(acc.__name, acc.__accnt, acc.__balance)


# Priority queue class to store list of key and value pair and return based on
# priorities assigned in key
class PriorityQueue:

    def __init__(self):
        self.__queue = []

    def len(self):
        return len(self.__queue)

# Returns true if PriorityQueue is empty
    def is_empty(self):
        if len(self.__queue) == 0:
            return True
        return False

# Adds data to the priority queue in the form of a list
    def add(self, k, v):
        lst = [k, v]
        self.__queue.append(lst)

# Returns the pair of Key value based on the prioirities, lowest priority is
# sent out first
    def min(self):
        lst = sorted(self.__queue, key=lambda x: x[0], reverse=False)
        return lst[0]

# Remove the lowest pair and returns the value to the user
    def remove_min(self):
        lst = self.min()
        self.__queue.remove(lst)
        return lst
