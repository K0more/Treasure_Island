print('''' 
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|                                                                
                                                                     

 ''')
print("Welcome to the Treasure Island")
print("Your mission is to find the treasure burried by the great pirate Gold D Roger")
Decision1 = input("You have arrived at the treasure island and you see 3 paths in front of you, Path 1 has some footprints that fade away in the middle, path 2 has no footprints and path 3 has sign pointing towards it. Choose which path you would want to take. ").lower()
if Decision1 == "path 2":
    print("As you follow those footrints you notice something")
    Decision2 = input("You see a stone sword and a iron sword in front of you, would you like to pick one up, if yes which one. ").lower()
    if Decision2 == "Stone":
        print("you encounter a monster in front of you and you defeat it after a feirce battle but your stone sword is now broken into half")
        print("You arrive at a castle, and you witness-")
        Decision4 = input("You see a 2 chests in front of you, a platinum one and a gold one, both of them are embedded with jewels and are sparkling, which one would you like to pick up, or you choose to explore more of the island instead? ").lower()
        if Decision4 == "gold" and "platnium":
            print("A venemous spider came out of the chest and poisoned you. Game over")
        elif Decision4 == "explore":
            print("As you walk past those chests, you see a man in some distance, he approaches you")
            Decision5 = input("Would you take out your sword and fight or offer some alcohol ").lower()
            if Decision5 == "sword":
                print('Gold D Roger: "Everyone in this world has offered me some alcohol but you showed me the guts to resist with a broken sword, Thats all I wanted to see from the person that would take the treasure which I hold more dear to than my own life."')
                print("You have obtained the treasure. You win!!")
            elif Decision5 == "alcohol":
                print('Gold D Roger: " I would love some"')
                print("As you extend your hand to offer some alcohol to him he stabs you with a knife he has been hiding under his left arm")
                print('Gold D Roger: "Anyone can be smart in this world but you need to have to prove yourself to em if you want the treasure i hold more dear to than my own life. Game Over"')
    elif Decision2 == "iron":
        print("The iron sword was a part of a monster itself, you get dragged by the sword to the monster and he eats you alive")
        print("Game Over")
elif Decision1 == "path 1":
    print("You hear some grunts, and you rush to the place where they are coming from")
    Decision3 = input("You see another person on the ground asking for water, would you like to offer him some water or you happen to have some alcohol left over with you from your journey to arrive here, would you like to offer him some alcohol instead. name which one or no for none. ").lower()
    if Decision3 == "water":
        print('strange man:"you really saved me! as a thanks I offer you this treasure map that I found earlier"')
        print("you follow the map and it brings you back to the start")
        print("you get angry and head back home empty handed. Game Over")
    elif Decision3 == "alcohol":
        print("The man drinks the alcohol and becomes tipsy")
        print("He accidentally pushes you back and you hit your head hard on a tree, you died due to concussion. Game Over")
    elif Decision3 == "no":
        print("He pulls out his gun and shoots you in the head")
        print('strange man:"Kids these days are so selfish"')
        print("Game Over")
elif Decision1 == "path 3":
    print("The path led you to a cave in which you found a women lying on the ground")
    print("As you go near the women, she attacks you")
    print('strange woman:"Its been a long time since i have eaten a virgin man"')
    print("Game Over")
else:
    print("invalid option")

