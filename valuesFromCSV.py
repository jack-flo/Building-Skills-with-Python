with open('example_stock_purchases.csv', 'r') as portfolio:
    # Gets the titles and moves onto the actual quotes
    titles = next(portfolio).strip().split(',')
    for quote in portfolio:
        entry = quote.strip().split(',')
        # creates a dictionary of the data aligned with their values
        data = dict(zip(titles, entry))
        valueAtPurchase = float(data['shares']) * float(data['purchase_price'])
        print(data)
        print(
            f"The value of {data['stock']} at purchase was £{valueAtPurchase:.2f}")
