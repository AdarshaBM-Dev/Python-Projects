#LCM of two numbers
#LCM - Least common Multiple 
#in Mathematics , Lcm of any two number its
#the value which is evenly divsible
# by the two  gen number    


x = int(input("enter number >> "))
y = int(input("enter number >> "))

if x>y:
    greater = x
else:
    greater = y 
while(True):
    if ((greater%x==0) & (greater%y==0)):
        lcm = greater
        break
    greater += 1


print(f"LCM of {x} and {y} is {lcm}")

