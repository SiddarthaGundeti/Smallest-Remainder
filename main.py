a=int(input())
b=int(input())
a_b=a%b
b_a=b%a
if (a_b) < (b_a):
    print(a_b)
else:
    print(b_a)
