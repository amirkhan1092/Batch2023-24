import tkinter as tk


class CurrencyConverter:
    def __init__(self, exchange_rates):
        self.exchange_rates = exchange_rates

    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            return "Currency not supported"

        from_rate = self.exchange_rates[from_currency]
        to_rate = self.exchange_rates[to_currency]

        converted_amount = amount * (to_rate / from_rate)
        return converted_amount


class CurrencyConverterApp(tk.Tk):
    def __init__(self, exchange_rates):
        super().__init__()

        self.title("Currency Converter")

        self.converter = CurrencyConverter(exchange_rates)

        self.amount_label = tk.Label(self, text="Enter amount:")
        self.amount_label.grid(row=0, column=0, padx=5, pady=5)

        self.amount_entry = tk.Entry(self)
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5)

        self.from_currency_label = tk.Label(self, text="Convert from (currency code):")
        self.from_currency_label.grid(row=1, column=0, padx=5, pady=5)

        self.from_currency_entry = tk.Entry(self)
        self.from_currency_entry.grid(row=1, column=1, padx=5, pady=5)

        self.to_currency_label = tk.Label(self, text="Convert to (currency code):")
        self.to_currency_label.grid(row=2, column=0, padx=5, pady=5)

        self.to_currency_entry = tk.Entry(self)
        self.to_currency_entry.grid(row=2, column=1, padx=5, pady=5)

        self.convert_button = tk.Button(self, text="Convert", command=self.perform_conversion)
        self.convert_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.result_label = tk.Label(self, text="")
        self.result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def perform_conversion(self):
        amount = float(self.amount_entry.get())
        from_currency = self.from_currency_entry.get().upper()
        to_currency = self.to_currency_entry.get().upper()

        converted_amount = self.converter.convert(amount, from_currency, to_currency)
        self.result_label.config(text=f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")


if __name__ == "__main__":
    # Sample exchange rates (for demonstration purposes)
    exchange_rates = {
        'USD': 1.0,
        'EUR': 0.88,
        'GBP': 0.76,
        'JPY': 109.35,
        # Add more exchange rates as needed
    }

    app = CurrencyConverterApp(exchange_rates)
    app.mainloop()
