print("""
   _________     .__                  __________.__                         ________         .__  .__                   .__                
  /   _____/__ __|  |   ____ ___  ___ \______   \__|____________________    \______ \   ____ |  | |__|__  __ ___________|__| ____   ______ 
  \_____  \|  |  \  | _/ __ \\  \/  /  |     ___/  \___   /\___   /\__  \    |    |  \_/ __ \|  | |  \  \/ // __ \_  __ \  |/ __ \ /  ___/ 
  /        \  |  /  |_\  ___/ >    <   |    |   |  |/    /  /    /  / __ \_  |    `   \  ___/|  |_|  |\   /\  ___/|  | \/  \  ___/ \___ \  
 /_______  /____/|____/\___  >__/\_ \  |____|   |__/_____ \/_____ \(____  / /_______  /\___  >____/__| \_/  \___  >__|  |__|\___  >____  > 
         \/                \/      \/                    \/      \/     \/          \/     \/                   \/              \/     \/  

""")

size= input("what size of pizz do you want? S,M,L:")
pepperori=input("Do you want pepperori ? Y or N:")
extra_cheese=input("Do you want extra cheese? Y or N :")

bill=0
if size == 'S':
    bill=15
    print(f"small pizza(S) is ${bill}")
elif size == 'M':
    bill = 20
    print(f"Medium pizza(M) is ${bill}")
elif size == 'L':
    bill = 25
    print(f"Large pizza(L) is ${bill}")
else:
    print("you extry a wrong size")

if size == 'S':
    if pepperori == 'Y':
        bill +=2
    else:
        bill += 3
if extra_cheese == 'Y':
    bill += 1
print(f"your total bill is ${bill}")


