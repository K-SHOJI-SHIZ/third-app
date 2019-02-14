from .. import dist

"""
最近近傍法によりTSPの解を求める関数を提供するモジュール
"""
def nearest_neighbor(cities: list, start: int = 0) -> list:
    """
    最近近傍法で求めた巡回路を返す関数
    @param 都市リスト
    @return 巡回路
    """
    #巡回路のリストを生成
    tour = list()
    #訪問済の都市リストを生成
    isVisited = [False] * len(cities)
    #巡回路に最初の都市を追加
    tour.append(start)
    #最初の都市を訪問済みに変更
    isVisited[start] = True
    for iteration in range(1, len(cities)):
        #現在の都市を取得
        currentCity = tour[iteration - 1]
        nearestCity = ''
        minDist = 0
        #現在の都市から最も近い都市を探す
        for city in range(len(cities)):
            #訪問済の都市は除外する
            if isVisited[city]:
                continue
            distance = dist(cities[currentCity], cities[city])
            if distance < minDist or nearestCity == '':
                nearestCity = city
                minDist = distance
        tour.append(nearestCity)
        isVisited[nearestCity] = True
    return tour
