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
        'MSCI Europe Small Cap': 'ZPRX GY Equity',
        'Goldman Sachs India': 'GSINDAI LX Equity',
        'Goldman Sachs Emerging Markets': 'GMEPISA LX Equity',
        'MSCI Europe Industrials': 'XSNR GY Equity',
        'D&R Aktien': 'DRAKTIV GR Equity'
    },
    'Sectors': {
        'Energy': {
            'US vs. EU': ['S5ENRS Index', 'S600ENP Index'],
            'US vs. Index': ['S5ENRS Index', 'SXXP Index'],
            'EU vs. Index': ['S600ENP Index', 'SXXP Index'],
        },
        'Materials': {
            'US vs. EU': ['S5MATR Index', 'SXBSCP Index'],
            'US vs. Index': ['S5MATR Index', 'SPX Index'],
            'EU vs. Index': ['SXBSCP Index', 'SXXP Index'],
        },
        'Industrials': {
            'US vs. EU': ['S5INDU Index', 'SXIDUP Index'],
            'US vs. Index': ['S5INDU Index', 'SPX Index'],
            'EU vs. Index': ['SXIDUP Index', 'SXXP Index'],
        },
        'Consumer Discretionary': {
            'US vs. EU': ['S5COND Index', 'S600CDP Index'],
            'US vs. Index': ['S5COND Index', 'SPX Index'],
            'EU vs. Index': ['S600CDP Index', 'SXXP Index'],
        },
        'Consumer Staples': {
            'US vs. EU': ['S5CONS Index', 'S600CSP Index'],
            'US vs. Index': ['S5CONS Index', 'SPX Index'],
            'EU vs. Index': ['S600CSP Index', 'SXXP Index'],
        },
        'Health Care': {
            'US vs. EU': ['S5HLTH Index', 'SXDP Index'],
            'US vs. Index': ['S5HLTH Index', 'SPX Index'],
            'EU vs. Index': ['SXDP Index', 'SXXP Index'],
        },
        'Financials': {
            'US vs. EU': ['S5FINL Index', 'SXFINL Index'],
            'US vs. Index': ['S5FINL Index', 'SPX Index'],
            'EU vs. Index': ['SXFINL Index', 'SXXP Index'],
        },
        'Information Technology': {
            'US vs. EU': ['S5INFT Index', 'SX8P Index'],
            'US vs. Index': ['S5INFT Index', 'SPX Index'],
            'EU vs. Index': ['SX8P Index', 'SXXP Index'],
        },
        'Communication Services': {
            'US vs. EU': ['S5TELS Index', 'SXKP Index'],
            'US vs. Index': ['S5TELS Index', 'SPX Index'],
            'EU vs. Index': ['SXKP Index', 'SXXP Index'],
        },
        'Utilities': {
            'US vs. EU': ['S5UTIL Index', 'SX6P Index'],
            'US vs. Index': ['S5UTIL Index', 'SPX Index'],
            'EU vs. Index': ['SX6P Index', 'SXXP Index'],
        },
        'Real Estate': {
            'US vs. EU': ['S5RLST Index', 'SX86P Index'],
            'US vs. Index': ['S5RLST Index', 'SPX Index'],
            'EU vs. Index': ['SX86P Index', 'SXXP Index'],
        }
    }
}


if __name__ == '__main__':

    for title, groups in plots.items():

        if title == 'Sectors':  # Focus on sectors
            for sector, comparisons in groups.items():  # Loop through sectors
                labels = []
                series_list = []

                # Loop through each comparison in the sector (US vs. EU, US vs. Index, EU vs. Index)
                for comparison, tickers in comparisons.items():
                    if isinstance(tickers, list):
                        first = data[tickers[0]]
                        second = data[tickers[1]]
                        first_name = indices["name"][tickers[0]]
                        second_name = indices["name"][tickers[1]]
                        if first_name == second_name:
                            label = first_name
                        else:
                            label = f'{first_name} vs. {second_name}'
                        relative_performance = calculate_relative_performance(first, second)
                        labels.append(f'{comparison}: {label}')
                        series_list.append(relative_performance)

                # Plot each sector with its comparisons
                plot_ticker(title=f'{sector} Sector', labels=labels, data=series_list, output_dir=output_dir)

        else:
            # Your existing code for non-sector plots
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

