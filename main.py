import os

from plot import plot_ticker
from utility import get_indices, get_indices_data, calculate_relative_performance, \
    calculate_yield

indices = get_indices()
data = get_indices_data()
output_dir = "output"
os.makedirs(os.path.join(output_dir, "images"), exist_ok=True)

plots = {
    'Europe vs. US': {
        'SXXP EQW vs. SPX EQW': ['SXXEWP Index', 'SPW Index'],
        'SXXP vs. SPX': ['SXXP Index', 'SPX Index'],
    },
    'Emerging Markets vs. STOXX Europe 600 EQW & S&P 500 EQW': {
        'EM vs. SPX EQW': ['MXEF Index', 'SPW Index'],
        'EM vs. SXXP EQW': ['MXEF Index', 'SXXEWP Index'],
    },
    'Cyclicals vs. Defensives': {
        'US': ['MU704866 Index', 'MU704865 Index'],
        'EU': ['GSXECYCL Index', 'GSXEDEFS Index'],
    },
    'Growth vs. Value': {
        'US': ['DJUSGL Index', 'DJUSVL Index'],
        'EU': ['MXEU000G Index', 'MXEU000V Index'],
    },
    'US Non Profitable Tech vs. Mega Cap': ['GSXUNPTC Index', 'GSTMTMEG Index'],
    'EU Countries vs. STOXX Europe 600 EQW': {
        'DE': ['DAX Index', 'SXXEWP Index'],
        'UK': ['UKX Index', 'SXXEWP Index'],
        'IT': ['FTSEMIB Index', 'SXXEWP Index'],
        'CH': ['SMI Index', 'SXXEWP Index'],
        'FR': ['CAC Index', 'SXXEWP Index'],
        'ES': ['IBEX Index', 'SXXEWP Index'],
        'PL': ['WIG20 Index', 'SXXEWP Index'],
        'NL': ['AEX Index', 'SXXEWP Index'],
    },
    'US Indices vs. S&P 500 EQW': {
        'NASDAQ': ['NDX Index', 'SPW Index'],
        'RUSSEL': ['RTY Index', 'SPW Index'],
    },
    'Satellites Investments': {
        'BIT Biotech': 'BCBIOII GR Equity',
        'BIT Global Internet': 'HAL30II GR Equity',
        'JP Small Cap': 'PARJSCI LX Equity',
        'GS Funds': 'GSINDAI LX Equity',
        'D&R Aktien': 'DRAKTIV GR Equity'
    },
    'US Sectors vs. S&P 500': {
        'Energy': ['S5ENRS Index', 'SPX Index'],
        'Materials': ['S5MATR Index', 'SPX Index'],
        'Industrials': ['S5INDU Index', 'SPX Index'],
        'Consumer Discretionary': ['S5COND Index', 'SPX Index'],
        'Consumer Staples': ['S5CONS Index', 'SPX Index'],
        'Health Care': ['S5HLTH Index', 'SPX Index'],
        'Financials': ['S5FINL Index', 'SPX Index'],
        'IT': ['S5INFT Index', 'SPX Index'],
        'Communication Services': ['S5TELS Index', 'SPX Index'],
        'Utilities': ['S5UTIL Index', 'SPX Index'],
        'Real Estate': ['S5RLST Index', 'SPX Index'],
    },
    'EU Sectors I vs. STOXX Europe 600': {
        'Media': ['SXMP Index', 'SXXP Index'],
        'Food Beverage': ['S600FOP Index', 'SXXP Index'],
        'Personal Care': ['S600PDP Index', 'SXXP Index'],
        'Health Care': ['SXDP Index', 'SXXP Index'],
        'Financial Services': ['SXFP Index', 'SXXP Index'],
        'Banks': ['SX7P Index', 'SXXP Index'],
        'Insurance': ['SXIP Index', 'SXXP Index'],
        'Telecommunication': ['SXKP Index', 'SXXP Index'],
        'Utilities': ['SX6P Index', 'SXXP Index'],
        'Real Estate': ['SX86P Index', 'SXXP Index']
    },
    'EU Sectors II vs. STOXX Europe 600': {
        'Automobile & Parts': ['SXAP Index', 'SXXP Index'],
        'Travel & Leisure': ['SXTP Index', 'SXXP Index'],
        'Basic Resources': ['SXPP Index', 'SXXP Index'],
        'Technology': ['SX8P Index', 'SXXP Index'],
        'Chemicals': ['SX4P Index', 'SXXP Index'],
        'Industrial Goods': ['SXNP Index', 'SXXP Index'],
        'Construction': ['SXOP Index', 'SXXP Index'],
        'Retail': ['SXRP Index', 'SXXP Index'],
        'Consumer Products': ['S600CPP Index', 'SXXP Index'],
        'Energy': ['S600ENP Index', 'SXXP Index'],
    },
    'US Energy': ['S5ENRS Index', 'SPX Index'],
    'US Materials': ['S5MATR Index', 'SPX Index'],
    'US Industrials': ['S5INDU Index', 'SPX Index'],
    'US Consumer Discretionary': ['S5COND Index', 'SPX Index'],
    'US Consumer Staples': ['S5CONS Index', 'SPX Index'],
    'US Health Care': ['S5HLTH Index', 'SPX Index'],
    'US Financials': ['S5FINL Index', 'SPX Index'],
    'US IT': ['S5INFT Index', 'SPX Index'],
    'US Communication Services': ['S5TELS Index', 'SPX Index'],
    'US Utilities': ['S5UTIL Index', 'SPX Index'],
    'US Real Estate': ['S5RLST Index', 'SPX Index'],
    'EU Media': ['SXMP Index', 'SXXP Index'],
    'EU Food Beverage': ['S600FOP Index', 'SXXP Index'],
    'EU Personal Care': ['S600PDP Index', 'SXXP Index'],
    'EU Health Care': ['SXDP Index', 'SXXP Index'],
    'EU Financial Services': ['SXFP Index', 'SXXP Index'],
    'EU Banks': ['SX7P Index', 'SXXP Index'],
    'EU Insurance': ['SXIP Index', 'SXXP Index'],
    'EU Telecommunication': ['SXKP Index', 'SXXP Index'],
    'EU Utilities': ['SX6P Index', 'SXXP Index'],
    'EU Real Estate': ['SX86P Index', 'SXXP Index'],
    'EU Automobile & Parts': ['SXAP Index', 'SXXP Index'],
    'EU Travel & Leisure': ['SXTP Index', 'SXXP Index'],
    'EU Basic Resources': ['SXPP Index', 'SXXP Index'],
    'EU Technology': ['SX8P Index', 'SXXP Index'],
    'EU Chemicals': ['SX4P Index', 'SXXP Index'],
    'EU Industrial Goods': ['SXNP Index', 'SXXP Index'],
    'EU Construction': ['SXOP Index', 'SXXP Index'],
    'EU Retail': ['SXRP Index', 'SXXP Index'],
    'EU Consumer Products': ['S600CPP Index', 'SXXP Index'],
    'EU Energy': ['S600ENP Index', 'SXXP Index'],
}


if __name__ == '__main__':

    for title, groups in plots.items():

        if isinstance(groups, dict):
            labels = []
            series_list = []

            for sub_title, tickers in groups.items():

                if isinstance(tickers, list):
                    first = data[tickers[0]]
                    second = data[tickers[1]]
                    first_name = indices["name"][tickers[0]]
                    second_name = indices["name"][tickers[1]]
                    label = f'{first_name} vs. {second_name}'
                    relative_performance = calculate_relative_performance(first, second)
                    labels.append(label)
                    series_list.append(relative_performance)
                elif isinstance(tickers, str):
                    first = data[tickers]
                    first_name = indices["name"][tickers]
                    relative_performance = calculate_yield(first)
                    labels.append(first_name)
                    series_list.append(relative_performance)

            plot_ticker(title=title, labels=labels, data=series_list, output_dir=output_dir)
        elif isinstance(groups, list):
            first = data[groups[0]]
            second = data[groups[1]]
            first_name = indices["name"][groups[0]]
            second_name = indices["name"][groups[1]]
            label = f'{first_name} vs. {second_name}'
            relative_performance = calculate_relative_performance(first, second)
            plot_ticker(title=title, labels=[label], data=[relative_performance], output_dir=output_dir)
