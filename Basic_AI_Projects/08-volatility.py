import pandas as pd
import numpy as np

def get_most_volatile(prices):
    """Return the ticker symbol for the most volatile stock.
    
    Parameters
    ----------
    prices : pandas.DataFrame
        a pandas.DataFrame object with columns: ['ticker', 'date', 'price']
    
    Returns
    -------
    ticker : string
        ticker symbol for the most volatile stock
    """
    # TODO: Fill in this function.
    tick = prices.groupby('ticker')
    print(type(tick.groups),tick.groups.keys())
    #for name,group in tick:
     #   print (name)
      #  print (group)
 
    vol = {}
 
    for index in tick.groups.keys():
 
        vol[index] = np.std(np.log(tick.get_group(index)['price']) -np.log(tick.get_group(index)['price']).shift(1))
        print (vol[index])
    return max(vol)


def test_run(filename='08-volatility_data.csv'):
    """Test run get_most_volatile() with stock prices from a file."""
    prices = pd.read_csv(filename, parse_dates=['date'])
    
    print("Most volatile stock: {}".format(get_most_volatile(prices)))


if __name__ == '__main__':
    test_run()
