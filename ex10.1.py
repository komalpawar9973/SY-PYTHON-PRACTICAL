def price_engine(asset_costs):
    asset_costs.sort(reverse=True)

    print("Top 3 priciest assets:")
    for price in asset_costs[:3]:
        print(price)


assets = [1230.50, 5500.75, 3500.25, 7500.00, 2700.40, 4500.60]

price_engine(assets)