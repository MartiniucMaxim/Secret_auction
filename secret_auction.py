
auction_list = {}


def add_data():
    while(True):
        name_input = input('What\'s your name ? :')
        if name_input == 'quit':
            break
        else: 
            money_input = input('How much you spend for auction? :') 
        
            if money_input.isdigit(): 
                money_input = int(money_input)
                input_data = {'name':name_input,"money":money_input}
                auction_list[name_input] = input_data
            else:
                print('Money input should be positive integer.')


def print_data():
    print('Collected data:')
    for name,input_data in auction_list.items():
        print(f" {input_data['name']}:{input_data['money']}")  

add_data()
print_data()
