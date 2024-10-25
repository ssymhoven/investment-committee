import os

import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.dates as dates
import matplotlib.ticker as ticker


def plot_ticker(title: str, labels: list, data: list, output_dir: str) -> str:
    series_with_labels = list(zip(data, labels))
    series_with_labels.sort(key=lambda x: x[0].iloc[-1], reverse=True)
    sorted_data, sorted_labels = zip(*series_with_labels)

    fig, ax = plt.subplots(figsize=(12, 8))

    ax.spines.top.set_visible(False)
    ax.spines.right.set_visible(False)
    ax.xaxis.set_major_locator(dates.MonthLocator(interval=1))
    ax.xaxis.set_major_formatter(dates.DateFormatter('%b %Y'))

    ax.yaxis.set_major_locator(ticker.AutoLocator())
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())
    ax.yaxis.set_major_formatter(ticker.PercentFormatter())

    ax.axhline(0, color='grey', linestyle='--', linewidth=0.5)

    colors = ["#124877", "#74c0c5", "#6f99ed", "#b2b2b1", "#018c7d", '#7fbd39', "#539eb9", "#31c1ba", "#c5b27d", "#6cb5df"]
    linestyles = ['-', '--', ':']

    for i, series in enumerate(sorted_data):
        ax.plot(series.index, series, color=colors[i % len(colors)],
                linestyle=linestyles[i // len(colors) % len(linestyles)], label=sorted_labels[i])

    ax.set_xlim(min([min(series.index) for series in sorted_data]), max([max(series.index) for series in sorted_data]))

    plt.title(title)
    ncol = max(3, len(labels) // 6)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.075), frameon=False, ncol=ncol)

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.3)

    path = os.path.join(output_dir, "images", f'{title.replace(" ", "_")}.png')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    plt.savefig(path)
    plt.close()

    return path

