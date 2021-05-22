print("\t\t\t\t\t\t***Stone paper scissor*** ")
print("Rules : 1. Stone smack scissor\n2.paper cover Stone\n3.Scissor cut paper\n4. you will get 10 chances to win\n")
chances = 1
total_chances = 11
print(": Game start :  \n")
sum1 = 0
sum2 = 0 
while(chances<total_chances):
    # flag = 0
    
    import random 
    player = input("Player turn : stone[s] , paper[p] , scissor[sc] \n")
    if(player == ""):
        print("Wrong input take valid input\n")
        continue 
    if((player!='s' and player!='sc' and player!='p')):
        print("Wrong input take valid input\n")
        continue 

    print("Computer turn : stone , paper , scissor")

    computer = random.randint(1,3)

    if(computer==1):
        print("stone")
    elif(computer==2):
        print("paper")
    elif(computer==3):
        print("scissor")

    flag = 0
        
    if((player=="stone" or player=="s") and computer==3):
        print("Player won")
        sum1=sum1+1
        chances = chances + 1
        print("player score {}".format(sum1))
        print("chances left {} \n".format(total_chances-chances)) 

    if((player=="paper" or player=="p") and computer==3):
        print("computer won")
        sum2=sum2+1
        chances = chances + 1
        print("computer score {}".format(sum2))
        print("chances left {}\n".format(total_chances-chances))

    if((player=="scissor" or player=="sc") and computer==2 ):
        print("player won")
        sum1 = sum1+1
        chances = chances + 1
        print("player score {}".format(sum1))
        print("chances left {}\n".format(total_chances-chances))

    if((player=="stone" or player=="s") and computer==2):
        print("computer won")
        sum2 = sum2+1
        chances = chances + 1
        print("computer score {}".format(sum2))
        print("chances left {}\n".format(total_chances-chances))

    if((player=="scissor" or player=="sc") and computer==1):
        print("computer won ")
        sum2 = sum2+1
        chances = chances +1 
        print("computer score {}".format(sum2))
        print("chances left {}\n".format(total_chances-chances))

    if((player=="paper" or player=="p") and computer==1):
        print("player won")
        sum1 = sum1+1
        chances = chances + 1 
        print("player score {}".format(sum1))
        print("chances left {}\n".format(total_chances-chances))


    flag = 1
    
    if(player=="stone" or player=="s" and computer==1):
        print("Tie")

    elif((player=="paper" or player=="p") and computer==2):
        print("Tie")

    elif((player=="scissor" or player=="sc") and computer==3):
        print("Tie")
    

if(sum1>sum2): 
    print("\t\t\t **player won the match**\n")
    print("Total score of player {}".format(sum1))
    print("Total score of computer {}".format(sum2))

elif(sum2>sum1):
    print("\t\t\t**computer won the match**\n")
    print("Total score of computer {}".format(sum2))
    print("Total score of player {}".format(sum1))

else:
    print("\t\t\t**match is tie**\n")
    print("Total score of player {}".format(sum1))
    print("Total score of computer {}".format(sum2))

print("\t\t\t\t\t\t\t**Game finish**")

k = int(input("How was my game give rating from 10 : "))
if(k==10):
    print("You rated {} = brillant game ".format(k))
if((k ==9 or k==8 or k==7)):
    print("you rated {} = excellent ".format(k))
if(k>10):
    print("you rated more than {} = you love it".format(k))
elif((k==6 or k==5 or k==4)):
    print("you rating {} = good,it can be more better".format(k))
elif((k==3 or k==2 or k==1 or k==0)):
    print("you rated {} = bad game , what should i improve in game".format(k))
