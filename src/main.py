# find ../lib -name *tsp -type f | xargs -I% python main.py %
import sys
import os
from lib import tspUtil, nn
"""
メイン関数
args[1] 問題ファイルのパス
"""
def main():
    args = sys.argv
    if len(args) < 2:
        fileName = 'lib/tsp/a280.tsp' #動作確認用
    else:
        fileName = args[1]
    print('file:', fileName)
    try:
        cities = tspUtil.read_file(fileName)
    except Exception as inst:
        print(inst)
        return 1

    print('nn:', tspUtil.tour_length(nn(cities), cities))

    return 0

if __name__ == "__main__":
    sys.exit(main())
