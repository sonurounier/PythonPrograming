def run_statistics(ball_face_result, total_ball):
    dot_count=0
    total_run=0
    boundaries=0
    sixes=0
    for i in range (total_ball):
        if ball_face_result[i] == ".":
            dot_count=dot_count+1
            continue
        total_run= total_run + int(ball_face_result[i])
        if ball_face_result[i]== "4":
            boundaries=boundaries+1
        elif ball_face_result[i]=="6":
            sixes=sixes+1
    return int(dot_count),int(total_run),int(boundaries),int(sixes)
                
            
        

'''
below codes take input and break till new line before enter key
'''
batsman_ball_faced = []
print("""Enter run scored for each ball faced by batsman seperated by space,
Enter '.' for no run & 'Enter' for out.""")
while True:
    ball_facing = input()
    if ball_facing:
        batsman_ball_faced.append(ball_facing)   #append the next line to previous line

    else:
        break
ball_faced_print = '\n'.join(batsman_ball_faced)
#text = lines.append(line)
print("Print the entered value of ball faced: ",ball_faced_print)

for i in batsman_ball_faced:
    run_plus_dot=i.split()
    ball_count=len(run_plus_dot)

total_dot_ball, total_run, total_boundaries, total_sixes=run_statistics(run_plus_dot,ball_count)
strike_rate=(total_run/ball_count)

print("total dot ball:",total_dot_ball)
print("total run:",total_run, "& strike rate is:","{:.2%}".format(strike_rate))
print("total boundaries:",total_boundaries)
print("total sixes:",total_sixes)


