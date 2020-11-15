#Bill Calculator Program

print("Welcome To Bill Calculator.")

#Ask for the required information
total_bill = input('\nWhat was the total bill?: GHC ')
number_of_people = input('How many people are to split the bill? ')
tip_percentage = input('What percentage tip would you like to give? (10,12 or 15) ')

#Calculate the tip
tip = int(total_bill) * (int(tip_percentage)/100)
total_amount = int(total_bill) + tip
amount_per_person = total_amount / int(number_of_people)

#Display the amount each person has to pay
print('\nEach person has to pay : GHC ' + str(amount_per_person))