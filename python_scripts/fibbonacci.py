import argparse


parser =argparse.ArgumentParser(description="Haec scripta computat numerum in locis lectis in seriem fibonacciem")

parser.add_argument("pos", help = 'Positio in serie fibbonacie.', type=int)

parser.add_argument("-v","--verbose", help = "Proventum verbosum (longus) imprimat.",action = 'store_true')

args = parser.parse_args()

#pos input('enter position in the fibonacci sequence: ')

a,b = 0,1

for i in range(int(args.pos)):
    a,b = b,a+b
    
    fibo = a 
if args.verbose:
    print(f"Numerum fibonaccem in positione {args.pos} est {fibo}.")
else: 
    print(f"{fibo}")
    