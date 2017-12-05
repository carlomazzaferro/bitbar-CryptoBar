#!/usr/bin/env python
# coding=utf-8
#
# <bitbar.title>Multi-Crypto Tracker and Portfolio Calculator</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>carlomazzaferro</bitbar.author>
# <bitbar.author.github>carlomazzaferro</bitbar.author.github>
# <bitbar.desc>Displays current price for top 20 and other coins from coinmarketcap, as well as % change, and
# portfolio value </bitbar.desc>
# <bitbar.image>https://imgur.com/a/Qidf2>
#
# by carlomazzaferro


from cryptobar import utils


holdings = utils.grab_holdings()
global_vals = utils.global_data()
# eth_data = utils.Coin(' ethereum', holdings['ETH'])
total_held = 0

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
st_2 = ('{:>%i}{:>%i}{:>%i}{:>%i}{:>%i}' % (tuple([spacing]*5))).format('Tickers', 'US$', 'Holdings', 'Tokens', '24hr Change')

print(st_2)
for coin in ss:
    print(coin.printing())
