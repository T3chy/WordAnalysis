from matplotlib import pyplot as plt
def graphpolardist(polarlist):
    xlabs = ['Neutral', 'low', 'prettylow','slightlyhigh','prettyhigh','prettygoshdarnhigh']
    for p in polarlist:
        if p == 0:
            neut = neut + 1
        elif abs(avgpolar) > 0 and abs(avgpolar) < .2:
            low = low + 1
        elif abs(avgpolar) > .2 and abs(avgpolar) < .4:
            plow = plow + 1
        elif abs(avgpolar) > .4 and abs(avgpolar) < .6:
            shigh = shigh + 1
        elif abs(avgpolar) > .6 and abs(avgpolar) < .8:
           phigh = phigh + 1
        elif abs(avgpolar) > .8:
            pgdp = pgdp + 1
    yvals = [neut, low, plow, shigh, phigh, pgdp]
    plt.plot(xlabs, yvals)
pp = input("pp")
graphpolardist(pp)
