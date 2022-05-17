
n = 4

candles = [4, 3, -9, 0, 4, 1]

#3 2 1 3
def birthdayCakeCandles(candles):
    g=0
    for i in candles:
        vela_larga=max(candles)
        if i == vela_larga:
            g = g+1
    print (g)

birthdayCakeCandles(candles)