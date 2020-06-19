#Various unit conversion functions with a basic user menu to select between them.

#Distance conversion functions

def in_cm():
    inches = float(input("Enter distance in inches: "))
    cm = inches * 2.54
    m = cm / 100
    print('{0} inches is equal to: {1} centimeters and {2} meters.'.format(inches, cm, m))
    in_cm = [cm, m]
    return in_cm

def ft_m():
    feet = float(input("Enter distance in feet: "))
    m = feet * 0.3048
    cm = m * 100
    print('{0} feet is equal to: {1} centimeters and {2} meters.'.format(feet, cm, m))
    ft_m = [cm, m] 
    return ft_m

def mile_km():
    miles = float(input("Enter a distance in miles: "))
    km = miles * 1.609
    m = km * 1000
    print('{0} miles is equal to: {1} meters and {2} kilometers.'.format(miles, m, km))
    mile_km = [m, km]
    return mile_km

def ly_km():
    ly = float(input("Enter a distance in light-years: "))
    km = ly * (9.4607304725808*(10**12))
    print('{0} light-years is equal to {1:4f} kilometers. '.format(ly, km))

#Weight conversion functions

def lbs_kg():
    lbs = float(input("Enter weight in lbs: "))
    g = lbs * 453.5924
    kg = g / 1000
    print('{0} lbs is equal to {1} gram, which is {2} kilogram.'.format(lbs, g, kg))
    lbs_kg = [g, kg]
    return lbs_kg

def oz_g():
    oz = float(input("Enter weight in ounces: "))
    g = oz * 28.34952
    print('{0} ounces is equal to {1} gram. '.format(oz, g))
    oz_g = [oz, g]
    return oz_g

#Temperature conversion functions

def fah_cel():
    fah = float(input("Enter a temperature value in degrees Fahrenheit: "))
    cel = (fah - 32)*5/9
    print("{0} degrees Fahrenheit is equal to {1} degrees Celsius. ".format(fah, cel))
    fah_cel = [fah, cel]
    return fah_cel

def cel_k():
    cel = float(input("Enter a temperature value in degrees Celsius: "))
    k = cel + 273.13
    print("{0} degrees Celsius is equal to {1} Kelvin. ".format(cel, k))
    cel_k = [cel, k]
    return cel_k


#If unit_conversion_py is run directly, rather than being imported as a module, run the below
if __name__ == '__main__':

    selection = 0

    while selection != 9:
        print('\n')
        print('1 - Distance - in to cm')
        print('2 - Distance - ft to m')
        print('3 - Distance - miles to km')
        print('4 - Distance - light-years to km')
        print('5 - Weight - lbs to kg')
        print('6 - Weight - oz to g')
        print('7 - Temperature - deg F to deg C')
        print('8 - Temperature - deg C to K')
        print('9 -Exit')
        print('\n')

        selection = int(input("Select the conversion to perform: "))
        if selection == 1:
            in_cm()
        elif selection == 2:
            ft_m()
        elif selection == 3:
            mile_km()
        elif selection == 4:
            ly_km()
        elif selection == 5:
            lbs_kg()
        elif selection == 6:
            oz_g()
        elif selection == 7:
            fah_cel()
        elif selection == 8:
            cel_k()
        else:
            break
