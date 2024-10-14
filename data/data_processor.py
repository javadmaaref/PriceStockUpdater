class DataProcessor:
    @staticmethod
    def find_least_price_with_stock(prices, stocks):
        least_price = None
        least_stock = None
        for price, stock in zip(prices, stocks):
            if stock > 0:
                if least_price is None or price < least_price:
                    least_price = price
                    least_stock = stock
        if least_stock is None:
            if prices[1] == 0 and stocks[1] == 0:  # If Price2 is 0 and Stock2 is 0
                least_price = prices[0]
                least_stock = stocks[0]
            else:
                least_price = min(prices)  # Select the minimum price among available options
                least_stock = max(stocks)  # Select the maximum stock among available options
        return least_price, least_stock

    def process(self, data):
        processed_data = []
        for row in data:
            prices = [int(row['Price']), int(row['Lion_Price'])]
            stocks = [int(row['Stock']), int(row['Lion_Stock'])]
            final_price, final_stock = self.find_least_price_with_stock(prices, stocks)
            processed_row = row.copy()
            processed_row['Final_Price'] = final_price
            processed_row['Final_Stock'] = final_stock
            processed_data.append(processed_row)
        return processed_data
