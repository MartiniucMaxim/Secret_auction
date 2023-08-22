# import os module
import os 
# initialize empty auction_list dictionary
auction_list = {}

# make method add_data 
def add_data():
    #put main logic in while loop
    while True:
        name_input = input('What\'s your name ? :') # asks name input
        if name_input == 'quit': # if user input quit - program is finished
            break
        money_input = input('How much you spend for auction? :') # asks user input money
# check if money  is digit and greater then 0
        if money_input.isdigit() and int(money_input) > 0:
            money_input = int(money_input)  # make money value to int 
            input_data = {'name': name_input, "money": money_input} # store my user input into  input_data dictionary
            auction_list[name_input] = input_data # store keys and values in auction_list dictionary through assignment to input_data
        else:
            print('Money input should be positive integer.') 

        question_input = input('Is there any users who want to bid?(yes/no)') # asks users to input a question prompt        
        if question_input == 'no': # if user input no, show who have the most high bid and finish program
            most_high_bid()
            break
            
def print_data():  # method that print data from input_data
    print('Collected data:')
    for name,input_data in auction_list.items():  # access for loop which iterates each items and values from auction_list
        print(f"{input_data['name']}:{input_data['money']}")  # print data 

def most_high_bid(): # method that calculate the most high bid from users
    if auction_list:
        high_bid = max(auction_list.values(), key=lambda input:input['money']) # find the most high bid from users
        name_input = high_bid['name'] # store username
        money_input = high_bid['money'] # store money amount
        print(f"{name_input} has the highest money: {money_input}")
    else:
        print('No data')
        



