from collections import deque

def calculate_capital_gain(transactions):
    """
    In the code we calculates the total capital gain (or loss) for a sequence of transactions,
    using the FIFO protocol to identify shares.

    Args:
    - transactions: list of tuples, each tuple represents a transaction
                    Format: (transaction_type, number_of_shares, price_per_share)
                    transaction_type: 'buy' or 'sell'
                    number_of_shares: integer
                    price_per_share: integer

    Returns:
    - capital_gain: integer
    """
    capital_gain = 0
    shares_queue = deque()  # Queue to store purchased shares

    for transaction in transactions:
        transaction_type, num_shares, price_per_share = transaction
        if transaction_type == 'buy':
            # Enqueue the purchased shares
            shares_queue.append((num_shares, price_per_share))
        elif transaction_type == 'sell':
            # Dequeue shares from the queue and calculate capital gain
            shares_sold = num_shares
            while shares_sold > 0:
                if not shares_queue:
                    # If no shares are available for sale, break the loop
                    break
                # Dequeue shares from the queue
                shares_in_queue, purchase_price = shares_queue[0]
                if shares_in_queue <= shares_sold:
                    # If all shares in the queue can be sold, calculate capital gain
                    capital_gain += (shares_in_queue * (price_per_share - purchase_price))
                    shares_sold -= shares_in_queue
                    shares_queue.popleft()
                else:
                    # If only a portion of shares in the queue can be sold, update queue and break
                    capital_gain += (shares_sold * (price_per_share - purchase_price))
                    shares_queue[0] = (shares_in_queue - shares_sold, purchase_price)
                    shares_sold = 0

    return capital_gain

# input data:
transactions = [
    ('buy', 100, 20),
    ('buy', 20, 24),
    ('buy', 200, 36),
    ('sell', 150, 30)
]

total_capital_gain = calculate_capital_gain(transactions)
print("Total capital gain:", total_capital_gain)
