try:
    total_runs=0
    total_balls=0
    fours=0
    sixes=0
    dot_balls=0
    boundries=0
    ball1= int(input('score batao first ball par :'))
    ball2= int(input('score batao second ball par :'))
    ball3= int(input('score batao third ball par :'))
    ball4= int(input('score batao fourth ball par :'))
    ball5= int(input('score batao fifth ball par :'))
    ball6= int(input('score batao sixth ball par :'))
    score=(ball1,ball2, ball3,ball4,ball5,ball6)
    for runs in score:
     total_runs=total_runs+runs
     total_balls=total_balls+1
     if runs==4:
        fours+=1
        boundries+=1  
     elif runs==6:
        boundries+=1  
        sixes+=1
     elif runs ==0:
      dot_balls+=1
    strike_rate=(total_runs/total_balls)*100
    print('total runs :',total_runs)
    print('total balls :',total_balls)
    print('total fours :',fours)
    print('total sixes :',sixes)
    print('strike rate :',strike_rate)
    print('total boundries :',boundries)
    print('total dot balls are :',dot_balls)
except:
    print('try again only numbers are allowed')


    
