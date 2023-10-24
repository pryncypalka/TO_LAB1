import DataProvider as DP

def main():
    dp = DP.DataProvider()
    dp.url = "https://www.nbp.pl/kursy/xml/lasta.xml"
    dp.get_data()




if __name__ == '__main__':
    main()
