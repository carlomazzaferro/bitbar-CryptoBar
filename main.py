#!/usr/bin/env python
from cryptobar import utils
import json


holdings = utils.grab_holdings()
global_vals = utils.global_data()
# eth_data = utils.Coin(' ethereum', holdings['ETH'])
total_held = 0


# print ('---')
# p
coins = []
for coin, holding in holdings.iteritems():
    coin_class = utils.Coin(coin, holding)
    coins.append(coin_class)


ss = sorted(coins, key=lambda x: x.dollar_value, reverse=True)
print ('| templateImage={}'.format('iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAb1BMVEUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
                                   'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
                                   'AAAAAAAAAAAAAABt6r1GAAAAJXRSTlMAAQIFBwoODxMmKStXW2BmcH+AiJSfpq+ztbi6zdjc3d7l5ufv+yKSPAAAAJJJRE'
                                   'FUeNplj0cShDAQA5sMNsGLCSbH/79xwT7St1GVNBIvWW3O09QZDk/dTSFE0dzKs/cwS8hzkPPwKmoOIJnGCIJZPf5bQnps'
                                   '+xKDvDPqBqharYUPND9MAZSd1rwUhlMAyXr1IQ/idAJhf62JFZwFtO5Ka3GhvtC6rWyoexsv+3ak7q0rFo1TYot9qn/Hfe'
                                   'b/AehKCx0AH3FcAAAAAElFTkSuQmCC'))
print('---')
print('Portfolio Value: {:,.2f}'.format(sum([i.dollar_value for i in ss])))
print('---')
print 'Market Cap:\t${:,}'.format(int(global_vals['total_market_cap_usd']))
print('---')
spacing = 22
# st = ('{:>%i}{:>%i}{:>i%}{:>i%}{:>i%}' % (25,25,25,25,25)).format('Tickers', 'US$', 'Holdings', 'Tokens', '24hr Change')

st_2 = ('{:>%i}{:>%i}{:>%i}{:>%i}{:>%i}' % (tuple([spacing]*5))).format('Tickers', 'US$', 'Holdings', 'Tokens', '24hr Change')

print(st_2)
for coin in ss:
    # color = 'green' if coin.change_24h > 0 else 'red'
    # to_print = coin.printing() + '| {:<15.1f} color={}'.format(coin.change_24h, color)
    print(coin.printing())

# print_data = [i.printing_data() for i in ss]
# col_width = max(len(word) for row in print_data for word in row) + 2  # padding
# for row in print_data:
#     print "".join(word.ljust(col_width) for word in row)

