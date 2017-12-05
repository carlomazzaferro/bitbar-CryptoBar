import json
from urllib import urlopen


import os, sys

curr_dir = os.path.join(os.path.dirname(__file__))


def grab_holdings():
    data = os.path.join(curr_dir, 'holdings.json')
    with open(data, 'r') as inf:
        holdings = json.load(inf, encoding='utf-8')

    return holdings


def grab_images():
    data = os.path.join(curr_dir, 'icons.json')
    with open(data, 'r') as inf:
        images = json.load(inf,  encoding='utf-8')
    return images


def global_data():
    return json.loads(urlopen('https://api.coinmarketcap.com/v1/global/').read())


def get_from_cmc(coin_name):
    return json.loads(urlopen('https://api.coinmarketcap.com/v1/ticker/%s/' % coin_name).read())[0]


# holdings = grab_holdings()
images = grab_images()


class Coin(object):

    def __init__(self, name, n_tokens):
        self.name = name
        self.n_tokens = n_tokens
        self._data = self.get_data()
        self.price_usd = float(self._data['price_usd'])
        self.price_btc = float(self._data['price_btc'])
        self.change_24h = float(self._data['percent_change_24h'])
        self.ticker = self._data['symbol']
        self.dollar_value = self.price_usd * self.n_tokens
        self.thumbnail = images[self.ticker]
        self.portfolio_percentage = 0

    def get_data(self):
        return get_from_cmc(self.name)

    """
    data = [['a', 'b', 'c'], ['aaaaaaaaaa', 'b', 'c'], ['a', 'bbbbbbbbbb', 'c']]
    
        
    
    def printing_data(self):
        return [self.ticker + ':','image=' + self.thumbnail, str(self.price_usd), str(self.dollar_value),
                str(self.n_tokens), self.name, ]
    """

    def printing(self):

        base_spacing = (tuple([12]*5))
        if len(self.ticker) == 4:
            spacing = (tuple([8, 9, 10, 11, 11]))
        if len(self.ticker) == 5:
            spacing = (tuple([9, 10, 12, 12, 12]))
        else:
            spacing = base_spacing
        # spacing = 17
        return ('{:>%i}{:>%i.3f}${:>%i.2f}${:>%i}{:>%i}| \
        href=https://coinmarketcap.com/currencies/{} image={} color={} font={}' % spacing).format(
            self.ticker + ':',
            self.price_usd,
            self.dollar_value,
            self.n_tokens,
            self.change_24h,
            self.name,
            self.thumbnail,
         'green' if self.change_24h > 0 else 'red',
            'menlo',
        )

    def __str__(self):
        return '\t{:>15}{:>15}{:>15}{:>15.1f}| href=https://livecoinwatch.com/coins/{} image={}'.format(self.ticker + ':',
                                                                                                      self.price_usd,
                                                                                                      self.dollar_value,
                                                                                                      self.n_tokens,
                                                                                                  #    self.change_24h,
                                                                                                  #    'green',
                                                                                                      self.name,
                                                                                                      self.thumbnail)

        """
        
        return 'image={} \t{:.2f}%\t${:,}\t${:,.2f}'.format(
            # self.thumbnail,
            float(self.thumbnail),
            float(self.price_btc),
            # self.price_eth,
            float(self.dollar_value),
            float(self.portfolio_percentage))
            
            
        return '{:s} \t{:.2f}%\t${:,}\t${:,.2f}\t{} | href=https://livecoinwatch.com/coins/{:s} image={}'.format(
            self.price_usd,
            self.price_btc,
            # self.price_eth,
            self.dollar_value,
            self.portfolio_percentage,
            self.name,
            str(self.thumbnail))
        """
