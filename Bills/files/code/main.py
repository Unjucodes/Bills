from flat import Bill, Flatemate
from reports import Pdfreport

# input for the bill and the period of the bill
user_input_bill = float(input("Enter the bill amount: "))
user_bill_period = input("What is the bill period? E.g May 2024: ")

# user1 name and how many days spent in house
user1 = input("What is user name?: ")
days_in_house1 = int(input(f"How many days did {user1.title()} stay in the house during the bill period: "))

# user2 name and how many days spent in house
user2 = input("What is the name of the other user?: ")
days_in_house2 = int(input(f"How many days did {user2.title()} stay in the house during the bill period: "))

# storing the user input into a function
the_bill = Bill(amount=user_input_bill, period=user_bill_period)

# storing user names and days in house into function
flatmate1 = Flatemate(name=user1, days_in_house=days_in_house1)
flatmate2 = Flatemate(name=user2, days_in_house=days_in_house2)

# printing how much each user has to pay
print(f"{flatmate1.name} pays: ", flatmate1.pays(bill=the_bill, flatmate2=flatmate2))
print(f"{flatmate2.name} pays: ", flatmate2.pays(bill=the_bill, flatmate2=flatmate1))

# storing the filename in a function and storing the values
pdf_report = Pdfreport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)
