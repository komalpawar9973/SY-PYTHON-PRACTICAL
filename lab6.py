expenses=0.0
while True:
    value= float(input("enter a value :")) 
    
    if value== -1:
        break
     
    expenses =expenses+value
    print("total expenses is:",expenses)