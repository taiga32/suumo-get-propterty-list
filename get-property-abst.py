import requests
from bs4 import BeautifulSoup
import pandas as pd
import argparse

def extract_property(max_pages, url):
    # ページネーションの上限ページ数（例：2ページまで）

    # データを格納するためのリスト
    property_data = []

    # ページごとのURLを生成して取得
    for page_number in range(1, max_pages + 1):
        # 受け取ったurlを、ページが1から始まるように加工
        remove_target = "pn="
        remove_target_index = url.find(remove_target)
        url = url[:remove_target_index + 3]
        url = url + str(page_number)
        print(url)

        # ページのHTMLを取得
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # 物件情報を含む要素を取得
        property_elements = soup.find_all('div', class_='property_unit-content')
        # print(property_elements)


        # 物件情報を抽出してリストに格納
        for property_element in property_elements:
            # 物件名の取得
            property_name = property_element.find('h2', class_='property_unit-title_wide').find('a').text
            # print(property_name)
            
            
            # 物件価格の取得
            property_value = property_element.find('span', class_="dottable-value--2").text
            # print(property_value)
            
            # 住所の取得
            location = property_element.find('div', class_="dottable dottable--cassette").find_all('div', class_="dottable-line")[1].find('dd').text
            # print(location)
            
            # アクセスの取得
            access = property_element.find('div', class_="dottable dottable--cassette").find_all('div', class_="dottable-line")[2].find('dd').text
            # print(access)
            
            # 間取り
            madori = property_element.find('div', class_="dottable dottable--cassette").find_all('div', class_="dottable-line")[2].find_all('dd')[1].text
            # print(madori)
            
            # 専有面積
            area = property_element.find('div', class_="dottable dottable--cassette").find_all('div', class_="dottable-line")[0].find_all('dd')[1].text
            # print(area)
            
            # バルコニー
            balcony = property_element.find('div', class_="dottable dottable--cassette").find_all('div', class_="dottable-line")[1].find_all('dd')[1].text
            # print(balcony)
            
            # 築年月
            building_old = property_element.find('div', class_="dottable dottable--cassette").find_all('div', class_="dottable-line")[3].find_all('dd')[1].text
            # print(building_old)

            # リストに追加
            property_data.append([property_name, property_value, location, access, madori, area, balcony, building_old, url])
            # print(property_data)
            
    # データをpandasのDataFrameに変換
    columns = ['物件名', '物件価格', '住所', 'アクセス', '間取り', '専有面積', 'バルコニー', '築年月', 'url']
    df = pd.DataFrame(property_data, columns=columns)


    # データをエクセルファイルに書き込み
    df.to_excel('property_list.xlsx', index=False)

if __name__ == "__main__":
    # コマンドライン引数の設定
    parser = argparse.ArgumentParser(description='Webスクレイピングのサンプルプログラム')
    parser.add_argument('--max_pages', type=int, default=10, help='取得する最大ページ数')
    parser.add_argument('--url', required=True, help='物件一覧のurl')

    # コマンドライン引数の解析
    args = parser.parse_args()

    # main関数を呼び出し
    extract_property(args.max_pages, args.url)

