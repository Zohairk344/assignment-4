def main():
    C = 299792458
    Mass = float(input("Enter mass in kilos: "))
    E = Mass * C**2
    return print(f"{E} joules of energy")

if __name__ == '__main__':
    main()