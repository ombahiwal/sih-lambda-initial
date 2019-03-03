from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
#import pandas as pd 
import csv

"""class MyBasemap(Basemap):     
    def printcountries(self, d=3, max_len=12):
        data = pd.io.parsers.read_csv("http://opengeocode.org/cude/download.php?file=/home/fashions/public_html/opengeocode.org/download/cow.txt", 
                                      sep=";", skiprows=28 )
        data = data[(data.latitude > self.llcrnrlat+d) & (data.latitude < self.urcrnrlat-d) & (data.longitude > self.llcrnrlon+d) & (data.longitude < self.urcrnrlon-d)]
        for ix, country in data.iterrows():                            
                plt.text(*self(country.longitude, country.latitude), s=country.BGN_name[:max_len])
path = "path\\to\\data" """	
def calling():
    m = Basemap(projection='mill',
                llcrnrlat = -90,
                llcrnrlon = -180,
                urcrnrlat = 90,
                urcrnrlon = 180,
                resolution='l')

    m.drawcoastlines()
    m.drawcountries(linewidth=2)
    #m.drawstates(color='b')
    #m.drawcounties(color='darkred')
    #m.fillcontinents()
    #m.etopo()
    #m.bluemarble()
    #m.printcountries()

    def get_csv_to_list(file_name):
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            your_list = list(reader)
            f.close()
        return your_list[:len(your_list)]


    list1 = get_csv_to_list("../Integrated/basemap_locations.csv")
    rowlen=len(list1)
    print(list1)
    columnlen=len(list1[0])
    lx, ly = m(float(list1[0][1]), float(list1[0][0]))
    m.plot(lx, ly, 'bo', markersize=8, alpha=1)
    m.drawgreatcircle(0, 0, 0.0003, 0, color='g', linewidth=2, label='Safe')
    m.drawgreatcircle(0, 0, 0.0003, 0, color='r', linewidth=2, label='Malicious')
    for i in range(1,rowlen):
        x, y = m(float(list1[i][1]), float(list1[i][0]))
        if int(list1[i][2]) is 1:
            m.plot(x, y, 'g^', markersize=8, alpha=1)
            m.drawgreatcircle(float(list1[0][1]), float(list1[0][0]), float(list1[i][1]), float(list1[i][0]), color='g', linewidth=2)
        else:
            m.plot(x, y, 'r^', markersize=10, alpha=1)
            m.drawgreatcircle(float(list1[0][1]), float(list1[0][0]), float(list1[i][1]), float(list1[i][0]), color='r', linewidth=2)

    plt.legend(loc=4)
    plt.title('Genysis NAT')
    plt.show()