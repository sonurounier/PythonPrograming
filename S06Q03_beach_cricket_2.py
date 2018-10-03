
#Main Starts from here:
wicket = 0
ball_count = 30             #Match is for 30 ball
runsPerBatter   = [0] * 2   #*2 for two batter
dot_PerBatter   = [0] * 2   # track both player for dot ball
four_perBatter  = [0] * 2   #track boundries for both player
six_perBatter   = [0] * 2   #track sixes for both player
ball_faced      = [0] * 2   #track ball faced by both player, also required for calculating strike rate
strike_rate     = [0] * 2   #Calculate strike rate after run scored by player 

 

batsman = input("Enter two players name sperated by comma. 1st Name for striking end & 2nd name for non-striking end:\n").split(', ')

'''
Loop begin for output of each ball
'''

for ball in range (ball_count):
    print("Ball", ball+1, end=', ')
    dot_count = 0
    six_count = 0
    four_count = 0
    run = str(input("Enter Run> "))
    if wicket == 0:
        ball_faced[0]+=1
    else:
        ball_faced[1]+=1
            
    if run == '':       #Break loop on empty line (condition for wicket out)
        print(batsman[wicket], "Out")
        break
    
    if run == '.':
        dot_count += 1
        dot_PerBatter[wicket] += dot_count
        #for player in range(2):
        #    print(f"{batsman[player]:<7}: ball faced-{ball_faced[player]:2} runs-{runsPerBatter[player]:2} dot ball-{dot_PerBatter[player]:2} 4s-{four_perBatter[player]:2} 6s-{six_perBatter[player]:2}")
        #continue

    if run == '4':
        four_count += 1
        four_perBatter[wicket] += four_count

    if run == '6':
        six_count += 1
        six_perBatter[wicket] += six_count
    if run == '.':
        runsPerBatter[wicket] += 0
    else:
        runsPerBatter[wicket] += int(run)

    if runsPerBatter[wicket] > 60:      #Break loop after scoring more than 60 runs by either of the players
        print("Match end as player scores more than 60 runs")
        break        
    
    if run == '1' or run == '3' or run == '5' :
        if wicket == 0:
            wicket = 1
            #print("wicket value after odd run", wicket)
        else:
            wicket = 0
            #print("wicket value if not odd run", wicket)
    
    if (ball+1)%6 == 0:
        if wicket == 1:
            wicket = 0
        else:
            wicket = 1
            #print("wicket value after over", wicket)
    for player in range(2):
        print(f"{batsman[player]:<7}: ball faced-{ball_faced[player]:2} runs-{runsPerBatter[player]:2} dot ball-{dot_PerBatter[player]:2} 4s-{four_perBatter[player]:2} 6s-{six_perBatter[player]:2}")
    print()    

for player in range(2):
    print(f"{batsman[player]:<7}: strike rate-{(runsPerBatter[player]/ball_faced[player]):.2%}")



'''
        if run == '.' or run == '2' or run == '4' or run == '6':
            if wicket == 0:
                wicket = 1
            else:
                wicket = 0
        #elif wicket == 1 and (run == '.' or run == '2' or run == '4' or run == '6'):
         #   wicket = 0
'''
    

