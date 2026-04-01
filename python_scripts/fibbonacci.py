import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Haec scripta computat numerum in locis lectis in seriem fibonacciem")
    
    parser.add_argument("pos", help = 'Positio in serie fibbonacie.', type=int)
    
    parser.add_argument("-v","--verbose", help = "Proventum verbosum (longus) imprimat.",action = 'store_true')
    
    return parser.parse_args()

def fib():
    global fibo
    a,b = 0,1
    for i in range(int(args.pos)):
        a,b = b,a+b
    fibo = a 
    
def fibout():
    if args.verbose:
        print(f"Numerum fibonaccem in positione {args.pos} est {fibo}.")
    else: 
        print(f"{fibo}")

def main():
    global args
    args = get_args()
    fib()
    fibout()
# Aedificatur mundum 

if __name__ == "__main__":
    main()