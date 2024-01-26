# Dictionary to store country-capital pairs (case-insensitive)
country_capital_dict = {}

def get_country_capital(country):
    return country_capital_dict.get(country.lower(), "Unknown")

def main():
    while True:
        country = input("Enter the name of a country (or 'exit' to terminate): ").strip()

        if country.lower() == 'exit':
            print("Exiting the program.")
            break

        capital = get_country_capital(country)
        
        if capital != "Unknown":
            print(f"The capital of {country} is: {capital}")
        else:
            capital = input(f"We don't know the capital of {country}. Enter the capital: ").strip()
            country_capital_dict[country.lower()] = capital
            print(f"Thanks! The capital of {country} is now recorded as: {capital}")

if __name__ == "__main__":
    main()
