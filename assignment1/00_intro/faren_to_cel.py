def main():
    farenheit = float(input("Enter The temperatur in farenheit: "))
    celcius = (farenheit - 32) * 5.0 / 9.0
    celcius = round(celcius, 3)
    return print(f"The temperature is {celcius}C")

if __name__ == '__main__':
    main()