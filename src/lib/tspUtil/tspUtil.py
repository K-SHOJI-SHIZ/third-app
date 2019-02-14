import re
import math

messageReadFileError = "ファイル読み込みに失敗したでち"
messageEdgeWeightTypeError = '枝重み形式:{0}に対応していないでち'
"""
TSPのための基本的な関数を提供するモジュール
"""
#TODO: 巡回路を出力する関数の実装(いらないかも？)
#TODO: 2次元ユークリッド空間以外の距離空間への対応
class City:
    """
    都市クラス
    x: 都市のx座標
    y: 都市のy座標
    """
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

def read_file(fileName: str) -> list:
    """
    問題ファイルを読み込み、都市リストを返す関数
    @param fileName: 問題ファイルのパス
    @return 都市リスト
    """
    try:
        with open(fileName) as file:
            cities = list()
            mode = 'setType'
            for s_line in file:
                stripedLine = s_line.strip()
                if mode == 'setType':
                    data = stripedLine.split(':')
                    if data[0].strip() != 'EDGE_WEIGHT_TYPE':
                        continue
                    type = data[1].strip()
                    if type == 'EUC_2D':
                        mode = 'setData'
                    else:
                        raise Exception(messageEdgeWeightTypeError.replace('{0}', type))
                else:
                    if re.match(r'\d', stripedLine) == None:
                        continue
                    data = re.split(r'\s+', stripedLine)
                    cities.append(City(float(data[1]), float(data[2])))
    except IOError:
        raise Exception(messageReadFileError)
    return cities

def show_city_data(cities: list):
    """
    都市データを表示する関数
    @param cities: 都市リスト
    """
    print("****** cities ******")
    print("number of cities :", len(cities))
    print("n: x y")
    for index, city in enumerate(cities):
        print(str(index) + ':', city.x, city.y)
    print("********************")

def dist(city_a: City, city_b: City) -> float:
    """
    都市間の距離（2次元ユークリッド距離）を返す関数
    @param city_a: 都市
    @param city_b: 都市
    @return 都市間の距離
    """
    x_dist = city_a.x - city_b.x
    y_dist = city_a.y - city_b.y
    return math.sqrt(pow(x_dist, 2) + pow(y_dist, 2))

def tour_length(tour: list, cities: list):
    """
    巡回路長を返す関数
    @param tour: 巡回路
    @param cities: 都市リスト
    @return 巡回路長
    """
    length = 0.0
    for i in range(len(tour)):
        j = (i + 1) % len(tour)
        city_a = cities[tour[i]]
        city_b = cities[tour[j]]
        length += dist(city_a, city_b)
    return length
