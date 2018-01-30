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
        if self.name == 'fiat':
            return {'price_usd': 1, 'price_btc': 0, 'percent_change_24h': 0, 'symbol': 'FIAT'}
        return get_from_cmc(self.name)

    def printing(self):
        base_spacing = (tuple([10]*5))

        if len(self.ticker) == 3:
            spacing = (tuple([13, 10, 10, 8, 9]))
        elif len(self.ticker) == 4:
            spacing = (tuple([11, 9, 10, 8, 9]))
        elif len(self.ticker) == 5:
            spacing = (tuple([10, 8, 10, 8, 9]))
        else:
            spacing = base_spacing

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
