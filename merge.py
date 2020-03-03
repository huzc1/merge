import pandas as pd

def save_data(data, num):
    name = 'w' + str(num) + '.xlsx'
    data.to_excel(name, sheet_name='Sheet1')

def data_filter1(data, num):
    data['上期结存'], data['收入'], data['发出'], data['结存'] = data['上期结存|数量'] / data['箱规'], data['本期收入|数量'] / data['箱规'], data['本期发出|数量'] / data['箱规'], data['本期结存|数量'] / data['箱规']
    del data['本期结存|数量'], data['本期收入|数量'], data['本期发出|数量'], data['上期结存|数量'], data['货品规格']
    data['需求差异'] = data['发出'] - data['结存']
    save_data(data, num)

def data_filter2(data, num):
    data['实际库存'] = data['本期结存|数量'] + data['差异']
    save_data(data, num)

def data_select(data, num):
    if num == 0:
        data_filter1(data, num)
    else:
        data_filter2(data, num)

def open_file(base, data, i):
    base = pd.read_csv(base)
    data = pd.read_csv(data)
    if i != 0:
        data = data.drop(['货品规格'], axis=1)
    rst = pd.merge(base, data, how='left')
    rst = rst.fillna(0)
    rst = rst.set_index('货品编码')
    data_select(rst, i)

def main():
    base_name = ['base_data/b0.csv', 'base_data/b1.csv', 'base_data/b2.csv', 'base_data/b3.csv', 'base_data/b4.csv',
                 'base_data/b5.csv', 'base_data/b6.csv','base_data/b7.csv', 'base_data/b8.csv', 'base_data/b9.csv']
    data_name = ['d0.csv', 'd1.csv', 'd2.csv', 'd3.csv', 'd4.csv', 'd5.csv', 'd6.csv'
                 , 'd7.csv', 'd8.csv', 'd9.csv']
    for i in range(10):
        open_file(base_name[i], data_name[i], i)

if __name__ == '__main__':
    main()


