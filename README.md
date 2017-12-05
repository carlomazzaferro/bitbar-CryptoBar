# bitbar-CryptoBar
Cryptocurrency tickers, holdings, prices and portfolio ratios plugin for BitBar

## Installation
Install [BitBar](https://getbitbar.com/), and run it. Choose a Plugin Directory (needs to be empty). 
Then download this repo, copy all the contents (except the README.md) to the Plugin Directory.
Fire terminal, navigate to the plugin directory and run `chmod +x main.py`

Depending on your version of python, you may need to install the requests library, which you can easily do by running `pip install requests` on your terminal.

## Configuration
Add your holdings to the `holdings.json` file in order to display your portfolio valuation. More coins can be added
by creating a 16x16 icon base64 encoded and adding its ticker to the `icons.json` file.

The holdings name of the coin must match the one on [coinmarketcap](https://coinmarketcap.com).

## Demo
https://imgur.com/a/Qidf2

Enjoy.



