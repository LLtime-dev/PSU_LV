import urllib.request
import pandas as pd
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

def fetch_air_quality_data():
    url = 'https://iszz.azo.hr/iskzl/rs/podatak/export/json?postaja=160&vrijemeOd=03.06.2025&vrijemeDo=17.06.2025'

    data = urllib.request.urlopen(url).read()
    return ET.fromstring(data)

def process_data(root):
    rows = []
    for i, child in enumerate(root):
        mjerenje = float(child.find('mjerenje').text)
        vrijeme = child.find('vrijeme').text
        rows.append({'mjerenje': mjerenje, 'vrijeme': vrijeme})
    df = pd.DataFrame(rows)
    df['vrijeme'] = pd.to_datetime(df['vrijeme'], utc=True)
    df['month'] = df['vrijeme'].dt.month
    df['dayOfweek'] = df['vrijeme'].dt.dayofweek
    return df

def plot_data(df):
    df.plot(x='vrijeme', y='mjerenje')
    plt.show()

def get_top_3_days(df):
    return df.nlargest(3, 'mjerenje')

if __name__ == "__main__":
    root = fetch_air_quality_data()
    df = process_data(root)
    plot_data(df)
    print("Top 3 dana s najvećom koncentracijom PM10:")
    print(get_top_3_days(df))