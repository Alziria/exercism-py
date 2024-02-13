
def clean_input(s):
    return s.replace(",", "")

budget = float(clean_input(input("How much money do you have? >")))
exchange_rate = float(input("What is the exchange rate? >"))
print(f"Your wallet is worth {budget/exchange_rate:.2f}")
