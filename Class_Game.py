# Damage calculator project
# Get base damage
# Get increase damage
# Calculate the combat scenario
# figure out how to loop the combat until death
# Fernando Galvan 3/22/2021


#added contact to the story fg 3/19/2021
story=open("C:\\Users\\sonom\Documents\\Game start message.txt")
#wrote story for the new intro to game fg 3/19/2021


print(story.read())
#added some opening text for the game fg 3/19/2021

t=open("C:\\Users\\sonom\Documents\\Game File.txt", "w")
# story rewrote some sections to give the player start a little more creative thinking fg 3/22/2021

t.write("You wake up in an forest full of trees as high up as far as you can see. You hear noises coming from a bush to the left of you.")
99
t.close()


print("A Creature appears snarling at you as it approaches to attack,") 

print("you use your grandfathers sword to strike the creature down  ")

import sys


#created the fight sequence to the game fg 3/18/2021
# had to make sure each section checks for player and creature health fg 3/22/2021

def main():
    global cDefense,pDefense,iCombat
    init()
    while iCombat == "yes":
        combat()
    else:
        if iCombat == "no":
            coward()
    
    closing()


def init():
    global cDefense,pDefense,pAttack,cAttack,pDamage,pHeal,iCombat
    cDefense = 20
    pDefense = 15
    pAttack = 8
    pDefense = 15
    cDefense = 20
    cAttack = 4

    pDamage = 2
    pHeal = 2

    iCombat = "yes"
    

    print("Player Defense is; ", pDefense)
    print("Player Attack is; ", pAttack)
    print("Creature Attack is; ", cAttack)
    print("Creature Defense is; ", cDefense)
    #added contact to the story fg 3/19/2021
    

   
def combat():
    global cDefense,pDefense,pAttack,cAttack
    iCombat = "yes" 
    while iCombat == "yes":
    
        import random

        Hit_Chance = ["Hit","Miss"]

        HitChance = random.choice(Hit_Chance)

        print(HitChance)

        if HitChance == "Hit":
            HitDamage = 4
            print("You have delt damage equal to : ", HitDamage)
            cDefense = cDefense - HitDamage
            print("Creature has remaining defense; ", cDefense)
        
            if cDefense <= 0:
                closing()
            else: 
               if pDefense <= 0:
                    closing()
            iCombat = input("Do you wish to try again? ")
            if iCombat == "yes":
                potion()
            else:
                if iCombat == "no":
                    coward()
        else:
           if HitChance == "Miss":
            print("Creature is about to attack ")
            dodge()
def dodge():
    global cDefense,pDefense
    iChoice = input("Do you wish to block incoming damage or take your chance and dodge the attack? ")
    if iChoice == "block":
        import random
        Block_Chance = [0,1,2,3,4,5]
        BlockChance = random.choice(Block_Chance)
        print(" You have blocked damage equal to : ", BlockChance)
        pDefense = pDefense - BlockChance
        print("Player has remaining defense; ", pDefense)
        if pDefense >0:
            combat()
        else:
            if pDefense <= 0:
                closing()
                
    elif "dodge":
            pDefense = pDefense -2
            print("Player has remaining defense; ", pDefense)
            if pDefense >0:
                combat()
            else:
                if pDefense <= 0:
                    closing()

            
                        #potion portion to this section for some reason does a killer potion damage need more investigating fg 3/22/2021
                        #fixed fg 5/10/2021
def coward():
     print("You have chosen the cowards way out! ")
     print("Begone you sorry excuse of an adventurer! ")
     ending()


def potion():       
    global pDefense
    iPotion = input("Do you wish to use a potion adventurer? ")
    if iPotion == "yes":
        print("Your potion has healed you for 2 ")
        pDefense = pDefense + 2
        print("Your player defense now has; ", pDefense)
        print("Careful adventurer, this creature is strong ")
        combat()
    else:
         if iPotion =="no":
             combat()

     #survey part works as intended had to modify output messages fg 3/22/2021   
def closing():
    global cDefense,pDefense
    if cDefense <= 0:
        print("You've done it you have killed the creature ")
        iSurvey = input("Did you have fun killing the creature? ")
        if iSurvey == "yes":
            print("Great to hear!")
            print("I hope to bring you more and exciting adventures in the future! ")
            sys.exit(0)
        else:
            if iSurvey == "no":
                print("We feel sorry for wasting your time!")
                print("Don't worry adventurer, these are not tears but the glistening sweat from watching your fight! ")
                sys.exit(0)
    else:
        if pDefense <= 0:
            print("You have endured a great battle")
            iSurvey = input("Did you have fun getting murdered? ")
            if iSurvey == "yes":
                print("You have a very dark sense of humor ")
                sys.exit(0)
            else:
                if iSurvey =="no":
                    print("We apologize for your terrible time, Gain more equipment and try again ")   
                    sys.exit(0)
                    
def ending():
    
    iAnswer = input("Did you have a great time running away from the battle only to see your village slaughter?")
    if iAnswer == "yes":
        print("You have forsaken your soul into the darkest depths of evil. Congratulations, you are now banished.")
        sys.exit(0)
    else:
        if iAnswer == "no":
            print("We see great fight and honor in you, come back once you've regained your spirits.")
            sys.exit(0)

# Cannot seem to get the game over piece to trigger unless hitting no to the 2nd loop of combat and then creater and player has negative defense which shouldn't be the case fg 3/21/2021
         #fixed and done fg 5/10/21
# game over scenario of the game

# Managed to get the combat phase to loop and break cycle by adding a while loop fg 3/22/2021
# Worked on calculations to make it flow better 3/22/2021

main()

