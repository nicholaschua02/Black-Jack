import random

hard_strategy = {8: {2:"H", 3:"H", 4:"H", 5:"H", 6:"H", 7:"H", 8:"H", 9:"H", 10:"H", 11:"H"}, 
                 9: {2:"H", 3:"Dh", 4:"Dh", 5:"Dh", 6:"Dh", 7:"H", 8:"H", 9:"H", 10:"H", 11:"H"},
                 10: {2:"Dh", 3:"Dh", 4:"Dh", 5:"Dh", 6:"Dh", 7:"Dh", 8:"Dh", 9:"Dh", 10:"H", 11:"H"},
                 11: {2:"Dh", 3:"Dh", 4:"Dh", 5:"Dh", 6:"Dh", 7:"Dh", 8:"Dh", 9:"Dh", 10:"Dh", 11:"H"},
                 12: {2:"H", 3:"H", 4:"S", 5:"S", 6:"S", 7:"H", 8:"H", 9:"H", 10:"H", 11:"H"},
                 13: {2:"S", 3:"S", 4:"S", 5:"S", 6:"S", 7:"H", 8:"H", 9:"H", 10:"H", 11:"H"},
                 14: {2:"S", 3:"S", 4:"S", 5:"S", 6:"S", 7:"H", 8:"H", 9:"H", 10:"H", 11:"H"},
                 15: {2:"S", 3:"S", 4:"S", 5:"S", 6:"S", 7:"H", 8:"H", 9:"H", 10:"H", 11:"H"},
                 16: {2:"S", 3:"S", 4:"S", 5:"S", 6:"S", 7:"H", 8:"H", 9:"H", 10:"H", 11:"H"},
                 17: {2:"S", 3:"S", 4:"S", 5:"S", 6:"S", 7:"S", 8:"S", 9:"S", 10:"S", 11:"S"}}

soft_strategy = {12: {2:"H", 3:"H", 4:"H", 5:"H", 6:"H", 7:"H", 8:"H", 9:"H", 10:"H", 11:"H"},
                 13: {2:"H", 3:"H", 4:"H", 5:"Dh", 6:"Dh", 7:"H", 8:"H", 9:"H", 10:"H", 11:"H"},
                 14: {2:"H", 3:"H", 4:"H", 5:"Dh", 6:"Dh", 7:"H", 8:"H", 9:"H", 10:"H", 11:"H"},
                 15: {2:"H", 3:"H", 4:"Dh", 5:"Dh", 6:"Dh", 7:"H", 8:"H", 9:"H", 10:"H", 11:"H"},
                 16: {2:"H", 3:"H", 4:"Dh", 5:"Dh", 6:"Dh", 7:"H", 8:"H", 9:"H", 10:"H", 11:"H"},
                 17: {2:"H", 3:"Dh", 4:"Dh", 5:"Dh", 6:"Dh", 7:"H", 8:"H", 9:"H", 10:"H", 11:"H"},
                 18: {2:"S", 3:"Ds", 4:"Ds", 5:"Ds", 6:"Ds", 7:"S", 8:"S", 9:"H", 10:"H", 11:"H"},
                 19: {2:"S", 3:"S", 4:"S", 5:"S", 6:"S", 7:"S", 8:"S", 9:"S", 10:"S", 11:"S"},
                 20: {2:"S", 3:"S", 4:"S", 5:"S", 6:"S", 7:"S", 8:"S", 9:"S", 10:"S", 11:"S"}}

split_strategy = {"2": {2:"Ph", 3:"Ph", 4:"P", 5:"P", 6:"P", 7:"P", 8:"H", 9:"H", 10:"H", 11:"H"},
                  "3": {2:"Ph", 3:"Ph", 4:"P", 5:"P", 6:"P", 7:"P", 8:"H", 9:"H", 10:"H", 11:"H"},
                  "4": {2:"H", 3:"H", 4:"H", 5:"Ph", 6:"Ph", 7:"H", 8:"H", 9:"H", 10:"H", 11:"H"},
                  "6": {2:"Ph", 3:"P", 4:"P", 5:"P", 6:"P", 7:"H", 8:"H", 9:"H", 10:"H", 11:"H"},
                  "7": {2:"P", 3:"P", 4:"P", 5:"P", 6:"P", 7:"P", 8:"H", 9:"H", 10:"H", 11:"H"},
                  "8": {2:"P", 3:"P", 4:"P", 5:"P", 6:"P", 7:"P", 8:"P", 9:"P", 10:"P", 11:"P"},
                  "9": {2:"P", 3:"P", 4:"P", 5:"P", 6:"P", 7:"S", 8:"P", 9:"P", 10:"S", 11:"S"},
                  "A": {2:"P", 3:"P", 4:"P", 5:"P", 6:"P", 7:"P", 8:"P", 9:"P", 10:"P", 11:"P"}}

practice = [hard_strategy, soft_strategy, split_strategy]
scores = [0,0,0]
i = 0

while True:
    i += 1
    print("\n========================= Question" , str(i) , "==========================")
    
    strategy = random.randint(0,0)
    player_value = random.choice(list(practice[strategy].keys()))
    dealer_card = random.choice(list(practice[strategy][player_value].keys()))
    answer = practice[strategy][player_value][dealer_card]    
    
    if dealer_card == 11:
        dealer_show = "A"
    else:
        dealer_show = str(dealer_card)
                
    if strategy == 0:
        print("hard", player_value, "against", dealer_show)
    elif strategy == 1:
        print("soft", player_value, "against", dealer_show)
    else:
        print("pair", player_value, "against", dealer_show)
    
    print()
    response = input("action: ")

    while response == "":
        response = input("action: ")
    
    if response.lower() in answer.lower():
        print("correct ✔", answer)
        print()
        scores[strategy] += 1
        print("Hard score: " + str(scores[0]) + "/100")
        print("Soft score: " + str(scores[1]) + "/90")
        print("Split score: " + str(scores[2]) + "/80")
        del practice[strategy][player_value][dealer_card]
        if len(practice[strategy][player_value]) < 1:
            del practice[strategy][player_value]
    else:
        print("wrong ✘", answer)
        print()
        print("Hard score: " + str(scores[0]) + "/100")
        print("Soft score: " + str(scores[1]) + "/90")
        print("Split score: " + str(scores[2]) + "/80")