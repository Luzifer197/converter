
def binär_to_decimal(binär: str) -> int:
    try:
        dec: int = int(binär, 2)
        return dec
    except ValueError:
        print (f"ValueError, The Value {binär} is uncorrecly in decimal!!")
        exit()    

def decimal_to_binär(decimal: str) -> int:
    try:
        binär: int = bin(decimal).replace("0b", "")
        return int(binär)
    except ValueError:
        print (f"ValueError, The Value {decimal} is uncorrecly in binär!!")
        exit()

def binär_to_hexa(binär: str) -> str:
    try:
        hexa: str= int(binär, 16)
        return hexa

    except ValueError:
        print (f"ValueError, The Value {binär} is uncorrecly in Hexa!!")
        exit()
    
def hexa_to_binär(hexa: str) -> int:
    try:
        binär: int = bin(hexa).replace("0b", "")
        return int(binär)
    except ValueError:
        print (f"ValueError, The Value {hexa} is uncorrecly in binär!!")
        exit()

def decimal_to_hexa(decimal: int) -> str:      #convert Decimalnumber to Hexanumber
    conversion_table_16_to_10: dict[str, int] = {0: "0", 1: "1", 2: "2" ,3:"3" ,4:"4" ,5:"5" ,6:"6" ,7:"7" ,8:"8" ,9 :"9" ,10:"A" ,11:"B" ,12:"C" ,13:"D" ,14:"E" ,15:"F"}
    hexadecimal= ""

    if decimal < 0:
        decimal: int = decimal*(-1) 
        while(decimal > 0):
            remainder: int = decimal % 16
            hexadecimal: int = conversion_table_16_to_10[remainder] + hexadecimal
            decimal: int = decimal // 16
            return f"{hexadecimal}"
    else:
        while(decimal > 0):
            remainder: int = decimal % 16
            hexadecimal: int = conversion_table_16_to_10[remainder] + hexadecimal
            decimal: int = decimal // 16
        return f"{hexadecimal}"


def hexa_to_decimal(hexa: str) -> int:              #convert Hexanumber to Decimalnumber    
    try:
        dec = int(hexa, 16)
        return dec

    except ValueError:
        print (f"ValueError, The Value {hexa} is uncorrecly in Hexa!!")
        exit()

def decimalsystem(input_dt: str, decimal_input: int ):
    if input_dt == "hexa":
        print("\nThe hexadecimalform from ", decimal_input, "is ", decimal_to_hexa(decimal_input))
    elif input_dt == "binär":
        print("\nThe binärform from ", decimal_input, "is ", decimal_to_binär(decimal_input))
    else:
        print("Sorry, we can\'t read your number")

    input_yn: str = input("\n\nDo you want convert another Number? yes, no   ").lower()
      
    if input_yn == "yes":
        main()
    elif input_yn == "no":
        print("See you later!!")
    else:
        print("sorry can\'t read your input")

def hexasystem(input_dt: str, hexa_input: str):
    if input_dt == "decimal":
        print("\nThe decimalform from ", hexa_input, "is ", hexa_to_decimal(hexa_input))
    elif input_dt == "binär":
        print(f"the binärform from {hexa_input} is {hexa_to_binär(hexa_input)}")
    else:
        print("Sorry, we can\'t read your number")

    input_yn: str = input("\n\nDo you want convert another Number? yes, no   ").lower()
      
    if input_yn == "yes":
        main()
    elif input_yn == "no":
        print("See you later!!")
    else:
        print("sorry can\'t read your input")


def binärsystem(input_dt: str, binär_input: str):
    if input_dt == "decimal":
       print(f"the decimalform from {binär_input} is {binär_to_decimal(binär_input)}")
    
    elif input_dt == "binär":
        print(f"the hexaform from {binär_input} is {binär_to_hexa(binär_input)}")
    else:
        print("Sorry, we can\'t read your number")
    
    input_yn: str = input("\n\nDo you want convert another Number? yes, no   ").lower()
      
    if input_yn == "yes":
        main()
    elif input_yn == "no":
        print("See you later!!")
    else:
        print("sorry can\'t read your input")

def main():

    print("\nNumbersystems = decimal, hexa, binär\n")
    input_ask:str = input("Witch numbersysetm to would chance?  ").lower()        #ask a Numbersystem like Hexa or Decimal

    if input_ask == "decimal":

        print("system to chance: hexa, binär")

        input_dt: str = input("To witch system you would chance?:     ")
        decimal_input: int = int(input("\nPlease type a Decimal number:   "))

        decimalsystem(input_dt, decimal_input)

    elif input_ask == "hexa":
        
        input_dt: str = input("To witch system you would chance?:     ")
        hexa_input: str= input("\nPlease type a hexadecimal number:  ")
        
        hexasystem(input_dt, hexa_input)

    elif input_ask == "binär":
        
        input_dt: str = input("To witch system you would chance?:     ")
        binär: str = input("Please type a Binär number:     ")
        
        binärsystem(input_dt, binär)
            
    else:
        print("\nSorry, we didn\'t have this numbersystem")
        exit()


main()