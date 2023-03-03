figure = int(input("Kindly enter your figure: "))

def figureToRomans(figure):
    figureToRomanNumeral = {1000: 'M', 900 : 'CM', 500 : 'D', 400 : 'CD',
    100 : 'C', 90 : 'XC', 50 : 'L', 40 : 'XL', 10 : 'X', 9 : 'IX',
    5 : 'V', 4 : 'IV', 1 : 'I'}

    romanNumeral = ' '
    for value, numeral in figureToRomanNumeral.items():
        while figure >= value:
            romanNumeral += numeral
            figure -= value     
    return "The equivalent value of {} is: {}".format(figure, romanNumeral)

print (figureToRomans(figure))