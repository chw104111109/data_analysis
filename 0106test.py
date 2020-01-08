import pandas
dfs = pandas.read_html('https://rate.bot.com.tw/xrt?Lang=zh-TW')
currency = dfs[0]
#currency.ix[:,0:5]
currency.columns = ['幣別','現今匯率本行買入','現今匯率本行賣出','即期匯率本行買入','即期匯率本行賣出']
print(currency)