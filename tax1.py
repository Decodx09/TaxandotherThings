import math

def salary():

	income = int(input("Enter your salary"))

	if(income >= 100000):
		return((income*(1%100))*30)

	elif (income >= 500000):
		return((income*(1%100))*10)

	else:
		(income >= 250000)
		return "There's nothing you can contribute to the Goverment"


def month():

	Month = str(input("Which Month is it ?"))

	if (Month == "January" or Month == "March" or Month == "May" or Month == "July" or Month == "August" or Month == "October" or Month == "December"):
		return(31)

	elif (Month == "Febuary"):
		return(28)

	else:
		(Month == "April" or Month == "June"  or Month == "September" or Month == "November")
		return(31)


def labour():

		daysinthismonth = (input(month()))
		n = int(input("Enter the number of Workers"))

		while True:


			for i in range(1, n):


				Name = (input("Enter the name"))
				Salary = int(input("Enter the Salary"))

print(labour())

		
