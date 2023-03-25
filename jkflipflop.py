JK FLIP FLOP:-
j = 0
k = 0
q = 0
q_bar = 0
def jk_flip_flop(j, k):
global q, q_bar
if j == 1 and k == 0:
q = 1
q_bar = 0
print("Q is Set to 1 and Q_bar is reset to 0")
elif j == 0 and k == 1:
q = 0
q_bar = 1
print("Q_bar is Set to 1 and Q is reset to 0")
elif j == 0 and k == 0:
pass # no change
print("No change hold condi􀆟on")
else:
print("Toggle Condi􀆟on")
J=int(input("Enter the value of J: "))
K=int(input("Enter the value of K: "))
jk_flip_flop(J, K)
if(J==0 and K==0):
print("q =", q, "q_bar =", q_bar)
elif(J==1 and K==0):
print("q =", q, "q_bar =", q_bar)
elif(J==0 and K==1):
print("q =", q, "q_bar =", q_bar)
elif(J==1 and K==1):
print("")
