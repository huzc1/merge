import pandas as pd
import datetime
'''
只用来合并成品的库存数据
'''

def save_data(data):
    res_name = str(datetime.date.today()) + '婴童仓成品01.xlsx'
    data.to_excel(res_name, sheet_name='Sheet1')


def data_filter1(data):
    data['上期结存'], data['收入'], data['发出'], data['结存'] = data['上期结存|数量'] // data['箱规'], data['本期收入|数量'] // data['箱规'], data['本期发出|数量'] // data['箱规'], data['本期结存|数量'] // data['箱规']
    data = data.drop(['本期结存|数量', '本期收入|数量', '本期发出|数量', '上期结存|数量', '货品规格'], axis=1)
    data['需求差异'] = data['发出'] - data['结存']
    data['缺货比率'] = data['结存'] / data['发出']
    data = data.sort_values('缺货比率')
    save_data(data)


def main():
    b0, d0 = pd.read_csv('base_data/b01.csv').fillna(0), pd.read_csv('d0.csv').fillna(0)
    data = pd.merge(b0, d0, how='right')
    data = data.set_index('货品编码')
    data_filter1(data)


if __name__ == '__main__':
    main()