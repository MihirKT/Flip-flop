LOGIC GATES
def AND():
print('******AND GATE TRUTH TABLE******')
a=[1,1,0,0]
b=[1,0,1,0]
print('................')
for i in range(0,4):
if a[i]==1 and b[i]==1:
ans = 1
else:
ans = 0
print(a[i],'AND',b[i],'=',ans)
print('................')
def OR():
print('******OR GATE TRUTH TABLE******')
a=[1,1,0,0]
b=[1,0,1,0]
print('................')
for i in range(0,4):
if a[i]==0 and b[i]==0:
ans = 0
else:
ans = 1
print(a[i],'OR',b[i],'=',ans)
print('................')
def NOT():
print('******NOT GATE TRUTH TABLE******')
a=[1,0]
print('................')
for i in range(0,2):
if a[i]==0:
ans = 1
else:
ans = 0
print(a[i],'NOT=',ans)
print('................')
def NAND():
print('******NAND GATE TRUTH TABLE******')
a=[1,1,0,0]
b=[1,0,1,0]
print('................')
for i in range(0,4):
if a[i]==1 and b[i]==1:
ans = 0
else:
ans = 1
print(a[i],'NAND',b[i],'=',ans)
print('................')
def NOR():
print('******NOR GATE TRUTH TABLE******')
a=[1,1,0,0]
b=[1,0,1,0]
print('................')
for i in range(0,4):
if a[i]==0 and b[i]==0:
ans = 1
else:
ans = 0
print(a[i],'NOR',b[i],'=',ans)
print('................')
def XOR():
print('******XOR GATE TRUTH TABLE******')
a=[1,1,0,0]
b=[1,0,1,0]
print('................')
for i in range(0,4):
if (a[i]==0 and b[i]==0) or (a[i]==1 and b[i]==1):
ans = 0
else:
ans = 1
print(a[i],'XOR',b[i],'=',ans)
print('................')
def XNOR():
print('******XNOR GATE TRUTH TABLE******')
a=[1,1,0,0]
b=[1,0,1,0]
print('................')
for i in range(0,4):
if (a[i]==0 and b[i]==0) or (a[i]==1 and b[i]==1):
ans = 1
else:
ans = 0
print(a[i],'XNOR',b[i],'=',ans)
print('................')
print('\n 1.AND \n 2.OR \n 3.NOT \n 4.NAND \n 5.NOR \n 6.XOR \n 7.XNOR')
opt=input('Enter your choice(1,2,3,4,5,6,7) :')
if opt=='1':
AND()
elif opt=='2':
OR()
elif opt=='3':
NOT()
elif opt=='4':
NAND()
elif opt=='5':
NOR()
elif opt=='6':
XOR()
elif opt=='7':
XNOR()
else:
print('Please select correct option !')
