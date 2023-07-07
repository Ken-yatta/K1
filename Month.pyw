# this is a program to print the abbreviation of a month

def main():
    # months is a list used as a loookup table
    
    months="JanFebMarAprMayJunJulAugSepOctNovDec"
    
    n = int(input("Enter a month number 1-12: "))
    
    # compute starting position of month n in months
    
    pos =  (n-1) * 3
    
    # rab the appropriate slice from months
    
    monthAbbrev= months[pos:pos+3]
    
    # print the result
    
    print("The abbreviation for the month ", n, "is", monthAbbrev + ".")
    
main()