from matplotlib import pyplot as plt
def graphpolardist(polarlist):
    neut, low, plow, shigh, phigh, pgdp, = 0, 0, 0, 0, 0, 0
    xlabs = ['Neutral', 'low', 'pretty low','slightly high','pretty high','pretty gosh darn high']
    for p in polarlist:
        if p == 0:
            neut = neut + 1
        elif abs(p) > 0 and abs(p) < .2:
            low = low + 1
        elif abs(p) > .2 and abs(p) < .4:
            plow = plow + 1
        elif abs(p) > .4 and abs(p) < .6:
            shigh = shigh + 1
        elif abs(p) > .6 and abs(p) < .8:
           phigh = phigh + 1
        elif abs(p) > .8:
            pgdp = pgdp + 1
    with open('My Scripts/data.txt','w') as da:
        da.writelines(["%s\n" % item  for item in polarlist])
    yvals = [neut, low, plow, shigh, phigh, pgdp]
    plt.xlabel("Polarity")
    plt.ylabel("# of tweets")
    plt.bar(xlabs, yvals)
    plt.show()
