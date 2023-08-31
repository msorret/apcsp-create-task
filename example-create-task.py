restaurant_list = ["Millie's Cafe", "True Food Kitchen", "HomeState", "Panda Express" ]

def rank_restaurant(new_res):

    for i in range(len(restaurant_list)):
        input_str = "Do you prefer A) " + new_res + " or B) " + restaurant_list[i] + " "
        question = input(input_str)

        if question == "A":
            restaurant_list.insert(i, new_res)
            break
        else: 
            continue

keep_adding = True
while keep_adding == True:
   
    add_question = input("Would you like to add and rank a new restaurant? Y/N ")
    
    if add_question == "Y":
        new_res = input("What restaurant would you like to add? ")
        rank_restaurant(new_res)
        print("Your current ranking is ", restaurant_list)

    else: 
        keep_adding = False




