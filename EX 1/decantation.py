frontier = { }  
possible={ }

goal_states = []
states = []
sequence_states = [(8,0,0)]

jar_volume = (8,5,3)   
initial_state = (8,0,0)

x = jar_volume[0]
y = jar_volume[1]
z = jar_volume[2]

def next_states(s):
  jar1 = s[0]
  jar2 = s[1]
  jar3 = s[2]
  
  states = []


  if(jar1>0):
      
      if(jar1+jar2<=y):
        states.append((0,jar1+jar2,jar3))
          
          
      else:
        states.append((jar1-(y-jar2), y, jar3))
      
      
      if(jar1+jar3<=z):
        states.append((0,jar2,jar1+jar3))

      else:
        states.append((jar1-(z-jar3),jar2,z))


  
  if(jar2>0):
      
      if(jar1+jar2<=x):
        states.append((jar1+jar2, 0, jar3))

      else:
        states.append((x, jar2-(x-jar1), jar3))
        

      
      if(jar2+jar3<=z):
        states.append((jar1, 0, jar2+jar3))


      else:
        states.append((jar1,jar2-(z-jar3),z))


  
  if(jar3>0):
      
      if(jar1+jar3<=x):
        states.append((jar1+jar3,jar2,0))

      else:
        states.append((x,jar2,jar3-(x-jar1)))

      
      if(jar2+jar3<=y):
        states.append((jar1,jar2+jar3,0))

      else:
        states.append((jar1,y,jar3-(y-jar2)))

def goal_checker(s):
    if( s[0] == 4 or s[1] == 4 or s[2] == 4):
        return 1
    return 0

def check_helper(s):
    if(s in [ (4,4,0) , (4, 0 ,4) ] ):
        return 0
    return 1



while(len(sequence_states) != 0):
    s = sequence_states.pop(0)
    explored[s] = 1
    for i in (next_states(s)):
        if i not in explored :
            sequence_states.append(i)
            if (check_helper(s) != 0) and (check_helper(i) !=0 ):
                possible[i] = s
                if (goal_checker(i)):
                    goal_states.append(i)

print("STARTING...")
print("INITIAL STATE :",initial_state)
print("GOAL STATES :" ,goal_states)
print("\n")
print("THE POSSIBLE WAYS ARE:\n")
for i in goal_states:
    temp = i
    result=[]
    while(t not in [(8,0,0)]):
        result.append(temp)
        temp =  possible[temp]
    result.append((8,0,0))
    result.reverse()
    print(result)

'''OUTPUT:
STARTING...
INITIAL STATE : (8, 0, 0)
GOAL STATES : [(1, 4, 3), (4, 1, 3)]

THE POSSIBLE WAYS ARE :

[(8, 0, 0), (3, 5, 0), (3, 2, 3), (6, 2, 0), (6, 0, 2), (1, 5, 2), (1, 4, 3)]
[(8, 0, 0), (5, 0, 3), (5, 3, 0), (2, 3, 3), (2, 5, 1), (7, 0, 1), (7, 1, 0), (4, 1, 3)]

Process finished with exit code 0 '''