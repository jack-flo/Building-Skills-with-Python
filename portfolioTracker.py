with open('example_stock_purchases_100.csv') as orderBook:
    titles = next(orderBook).strip().split(',')
    portfolio = {}
    for quote in orderBook:
        values = quote.strip().split(',')
        mergedRow = dict(zip(titles, values))
        shares = int(mergedRow['shares'])
        purchasePrice = float(mergedRow['purchase_price'])
        # perform calculation
        valueAtPurchase = round(shares * purchasePrice, 2)

        # decide if stock is already purchased
        if mergedRow['stock'] not in portfolio:
            portfolio[mergedRow['stock']] = {
                'shares': shares,
                'value': valueAtPurchase
            }
        else:
            portfolio[mergedRow['stock']
                      ]['shares'] += shares
            portfolio[mergedRow['stock']
                      ]['value'] += valueAtPurchase

portfolioValue = 0
print('Ticker | Shares | Value')
for stock, info in portfolio.items():
    # print nice table
    print(f"{stock} | {info['shares']} | £{info['value']:.2f}")
    # add value to total
    portfolioValue += info['value']

print(f"Your portfolio has a total value of £{portfolioValue:.2f}")
