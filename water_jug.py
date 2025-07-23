a = int(input("Enter jug A capacity : "))
b = int(input("Enter jug B capacity : "))
c = int(input("Enter starting water in jug A : "))
d = int(input("Enter starting water in jug B : "))
e = int(input("Enter target water in jug A : "))
f = int(input("Enter target water in jug B : "))
print("Operations")
print("1. Fill jug A")
print("2. Fill jug B")
print("3. Empty jug A")
print("4. Empty jug B")
print("5. Pour from A to B")
print("6. Pour from B to A")
while(c != e or d != f):
    op = int(input("Enter operation : "))
    if op == 1:
        c = a
    elif op == 2:
        d = b
    elif op == 3:
        c = 0
    elif op == 4:
        d = 0
    elif op == 5:
        if b-d >= c:
            d += c
            c = 0
        else:
            c -= (b-d)
            d = b
    elif op == 6:
        if a-c >= d:
            c += d
            d = 0
        else:
            d -= (a-c)
            c = a
    print(f"Jug A : {c}  ;  Jug B : {d}\n")
print("Target reached")