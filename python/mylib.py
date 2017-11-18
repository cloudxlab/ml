def interest(p, r, t):
    return (p*r*t)/100

def compoundinterest(p, r, t):
    c = p;
    for i in range(0, t):
        c = c + c*r/100
    return c - p

if __name__ == "__main__":
    print("I am in the main");
    compoundinterest(100, 5, 3)