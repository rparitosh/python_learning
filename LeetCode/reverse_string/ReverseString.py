x=-5002834892
y=0
negative=False
if x<0 :
    negative=True
    x=abs(x)
while x!=0:
    y=y*10+x%10
    x=x//10
if negative:
    y=-y

print(f"Y={y}")