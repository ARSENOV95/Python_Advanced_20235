text = tuple(sorted([x for x in input()]))

symbols = {}

for symbol in text:
    if symbol not in symbols.keys():
        symbols[symbol] = text.count(symbol)

    print(f'{symbol}: {symbols[symbol]} time/s')

