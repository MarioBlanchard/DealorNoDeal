#deal or no deal game
#26 cases with different values.
from random import shuffle


def givecase():
    '''no prama. takes 26 cases and 26 values and makes them a dict. the cases
    are given values randomly
    '''
    case=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']
    money=[1,5,10,15,25,50,75,100,200,300,400,500,750,1000,5000,10000,25000,50000,75000,100000,200000,300000,400000,500000,750000,1000000]
    
    shuffle(money)
    
    done={}
    count=0
    done= done.fromkeys(case)

    for key in done:
        done[key]=money[count]
        count+=1
        
    return done
    
    
    
#print(givecase())


def value(casedict):
    '''takes in a dict with all values being ints.
    all values are added up then divided by the number of keys
    '''
    total=0
    count=0
    
    for i in casedict:
        total+=casedict[i]
        count+=1
        
        
    ans = total//(count+2)
    return ans


#print(value(cases))

def playdond(inputcase):
    '''takes in a dict of cases then plays deal or no deal with user input
    '''
    case=inputcase
    truecount=6
    guesses=truecount
    game=False
    deal=False
    finish=0
    called=[]
    values=[]
    
    
    
    #Users Picked case is not part of the board and banker math is not including users case
    
    print('WELCOME TO DEAL OR NO DEAL! There are 26 cases with different values of money in them. One of them is worth 1 Million Dollars! It\'s time to pick your case. ')
    usercase=input('what case would you like?(1-26)')
    called.append(usercase)
    playercasevalue=case[usercase]
    case['Your Case']= case[usercase]
    del case[usercase]
    
    while game == False:
        while guesses !=0:
            print('the remaining cases are',case.keys())
            print('                                        ')
            print('You have',guesses,'cases to remove')
            print('                                        ')
            userguess=input('what case would you like to get rid of? (type board to see what money is on the board)')
            print('                                        ')
            
            if userguess=='Your Case':
                print('You cant remove your case from the game. try again')
            
            
            elif userguess == 'board':
                values=[]
                for i in case:
                    values.append(case[i])
                shuffle(values)
                print(values)
                
            elif userguess not in called:
                called.append(userguess)
                print('case',userguess,'had $',case[userguess],'in it!')
                del case[userguess]
                guesses-=1
                    
                
            else:
                print('not a valid guess')
                
        dealervalue=value(case)
        print('RING! RING! RING! That\'s the banker calling. He want\'s to buy your case.')        
        print(dealervalue,'is the bankers offer')
        choice=input('Deal or No Deal?(use capitals)')
        
        if choice == 'Deal':
            game=True
            deal=True
            finish=dealervalue
            
        elif choice == 'No Deal':
            if len(case) == 2:
                values=[]
                for i in case:
                    values.append(case[i])
                shuffle(values)
                print(values)
                
                del case['Your Case']
                lastchoice=input('would you like to switch cases?(yes or no)')
                
                if lastchoice == 'yes':
                    for i in case:
                        usercase=i
                    game=True
                    break
                
                elif lastchoice=='no':
                    game = True
                    break
                    
                    
                    
                else:
                    print('not valid input')
            print('ok then. lets keep playing!')
            if truecount !=1:
                truecount-=1
                guesses=truecount
            else:
                guesses=truecount
                
        else:
            print('Not a valid input. try again and remeber to use capitals!')
            
    if deal == True:
        print('You go home with $',finish)
        print('Your case was worth $',playercasevalue)
        
    else:
        print('your case is worth $',playercasevalue)
        
            
            
        
        
        
cases=givecase()

print(playdond(cases))
        
        
    



    
    
    
    
