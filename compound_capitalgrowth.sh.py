# This script calculates halal capital growth based on real yearly profits.
# Interest-free (no riba), profit-and-loss based.
# Sample purpose only.

# Input:
# c = initial capital
# profits = list of yearly profits (can be negative)
# s = investor profit share percentage

def halal_capital_growth(c, profits, s):
    capital = c
    investor_total_profit = 0

    for year, profit in enumerate(profits, start=1):
        investor_share = profit * (s / 100)
        investor_total_profit += investor_share
        capital += investor_share

        print(f"Year {year}:")
        print(f"  Total Profit: {profit}")
        print(f"  Investor Share: {investor_share}")
        print(f"  Capital After Year {year}: {capital}")
        print("-" * 30)

    return capital, investor_total_profit


if __name__ == "__main__":
    c = float(input("Enter the initial capital: "))
    years = int(input("Enter number of years: "))
    s = float(input("Enter investor profit share (%): "))

    profits = []
    for i in range(years):
        p = float(input(f"Enter actual profit for year {i + 1}: "))
        profits.append(p)

    final_capital, total_profit = halal_capital_growth(c, profits, s)

    print("\n====== HALAL SUMMARY ======")
    print(f"Initial Capital: {c}")
    print(f"Total Investor Profit: {total_profit}")
    print(f"Final Capital Value: {final_capital}")
