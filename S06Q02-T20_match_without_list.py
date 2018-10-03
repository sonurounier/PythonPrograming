def run_statistics(ball_face_result , total_ball):
    dot_count = 0
    total_run = 0
    boundaries = 0
    sixes = 0
    for i in range (total_ball):
        if ball_face_result[i] == ".":
            dot_count = dot_count+1
            continue
        total_run = total_run + int(ball_face_result[i])
        if ball_face_result[i] == "4":
            boundaries = boundaries+1
        elif ball_face_result[i] == "6":
            sixes = sixes+1
    return int(dot_count),int(total_run),int(boundaries),int(sixes)

#Main Starts from here
total_dot_ball = 0
total_run = 0
strike_rate = 0
total_boundaries = 0
total_sixes = 0
ball_count = 1

while True:
    run = str(input("""Enter run scored for each ball faced by batsman seperated by space,
Enter '.' for no run & 'Enter' for out.\n"""))
    if run == '':
        break

    run_list = run.split()
    ball_count = ball_count + len(run_list)
    total_dot_ball, total_run, total_boundaries, total_sixes = run_statistics(run_list , ball_count-1)
    #if total_run != 0:
    strike_rate = (total_run/ball_count)
    #else:
        #strike_rate = 0
        
print("total ball faced", ball_count)
print("total dot ball:", total_dot_ball)
print("total run:", total_run, "& strike rate is:","{:.2%}".format(strike_rate))
print("total boundaries:", total_boundaries)
print("total sixes:", total_sixes)
