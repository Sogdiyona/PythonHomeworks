def invest(years,amount, rate):
    rate=rate/100
    for year in range(1,years):
        amount+=rate*amount
        print(f"year {year}: ${amount:.2f}")
    return amount
years=int(input("Enter years: "))
amount=float(input("Enter the initial amount: "))
rate=float(input("Enter the annual rate in per cents: "))
print(f"year {years}: ${invest(years,amount, rate)}")