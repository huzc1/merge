import Supplies
import xlrd

def build_dict(list1, list2):
    rst= {}
    for i in range(len(list1)):
        rst[list1[i]] =list2[i]
    return rst

def mat_sum1(item):
    if item['ser'] == 1.1:
        item_data = Supplies.Rice_Box(deliver=item['发出'])
        mat = item_data.materials()
    elif item['ser'] == 1.2:
        item_data = Supplies.Rice_Pot(deliver=item['发出'])
        mat = item_data.materials()
    elif item['ser'] == 1.3:
        item_data = Supplies.Glucose(deliver=item['发出'])
        mat = item_data.materials()
    for k, v in mat.items():
        mat_sum01[k] = mat_sum01.get(k, 0) + v

def mat_sum2(item):
    if item['ser'] == 2.1:
        item_data = Supplies.Noodles(taste=item['口味分类'], deliver=item['发出'])
        mat = item_data.materials()
    elif item['ser'] == 2.2:
        item_data = Supplies.Farfalles(taste=item['口味分类'], deliver=item['发出'])
        mat = item_data.materials()
    elif item['ser'] == 2.3:
        item_data = Supplies.Facets(taste=item['口味分类'], deliver=item['发出'])
        mat = item_data.materials()
    for k, v in mat.items():
        mat_sum02[k] = mat_sum02.get(k, 0) + v

def mat_sum3(item):
    if item['ser'] == 3.1:
        item_data = Supplies.BaoQingNingHe(taste=item['口味分类'], deliver=item['发出'])
        mat = item_data.materials()
    elif item['ser'] == 3.2:
        item_data = Supplies.Minerals(taste=item['口味分类'], deliver=item['发出'])
        mat = item_data.materials()
    for k, v in mat.items():
        mat_sum03[k] = mat_sum03.get(k, 0) + v

def mat_sum4(item):
    if item['ser'] == 4.1:
        item_data = Supplies.BigDHA(deliver=item['发出'])
        mat = item_data.materials()
    elif item['ser'] == 4.2:
        item_data = Supplies.SmallDHA(deliver=item['发出'])
        mat = item_data.materials()
    elif item['ser'] == 4.3:
        item_data = Supplies.MilkCalcium(deliver=item['发出'])
        mat = item_data.materials()
    for k, v in mat.items():
        mat_sum04[k] = mat_sum04.get(k, 0) + v

def mat_sum5(item):
    item_data = Supplies.SolubleBean(taste=item['口味分类'], deliver=item['发出'])
    mat = item_data.materials()
    for k, v in mat.items():
        mat_sum05[k] = mat_sum05.get(k, 0) + v

def mat_sum6(item):
    item_data = Supplies.Puff(taste=item['口味分类'], deliver=item['发出'])
    mat = item_data.materials()
    for k, v in mat.items():
        mat_sum06[k] = mat_sum06.get(k, 0) + v

def mat_sum7(item):
    item_data = Supplies.Cale(deliver=item['发出'])
    mat = item_data.materials()
    for k, v in mat.items():
        mat_sum07[k] = mat_sum07.get(k, 0) + v

def mat_sum8(item):
    item_data = Supplies.Hat(deliver=item['发出'])
    mat = item_data.materials()
    for k, v in mat.items():
        mat_sum08[k] = mat_sum08.get(k, 0) + v

def mat_sum9(item):
    item_data = Supplies.Probiotics(taste=item['口味分类'], deliver=item['发出'])
    mat = item_data.materials()
    for k, v in mat.items():
        mat_sum09[k] = mat_sum09.get(k, 0) + v


def main(item):
    if item['生产企业'] == 1.0 and item['品牌'] == 1 and item['用途分类'] == 1:
        mat_sum1(item)
    elif item['生产企业'] == 2.0 and item['品牌'] == 1 and item['用途分类'] == 1:
        mat_sum2(item)
    elif item['生产企业'] == 3.0 and item['品牌'] == 1 and item['用途分类'] == 1:
        mat_sum3(item)
    elif item['生产企业'] == 4.0 and item['品牌'] == 1 and item['用途分类'] == 1:
        mat_sum4(item)
    elif item['生产企业'] == 5.0 and item['品牌'] == 1 and item['用途分类'] == 1:
        mat_sum5(item)
    elif item['生产企业'] == 6.0 and item['品牌'] == 1 and item['用途分类'] == 1:
        mat_sum6(item)
    elif item['生产企业'] == 7.0 and item['品牌'] == 1 and item['用途分类'] == 1:
        mat_sum7(item)
    elif item['生产企业'] == 8.0 and item['品牌'] == 1 and item['用途分类'] == 1:
        mat_sum8(item)
    elif item['生产企业'] == 9.0 and item['品牌'] == 1 and item['用途分类'] == 1:
        mat_sum9(item)

def raw_material():
    for k, v in mat_sum01.items():
        if ware_data01[k] <= v:
            print(1, k, int(ware_data01.get(k, 0)), v, sep=',')
    for k, v in mat_sum02.items():
        if ware_data02[k] <= v:
            print(2, k, int(ware_data02.get(k, 0)), v, sep=',')
    for k, v in mat_sum03.items():
        if ware_data03[k] <= v:
            print(3, k, int(ware_data03.get(k, 0)), v, sep=',')
    for k, v in mat_sum04.items():
        if ware_data04[k] <= v:
            print(4, k, int(ware_data04.get(k, 0)), v, sep=',')
    for k, v in mat_sum05.items():
        if ware_data05[k] <= v:
            print(5, k, int(ware_data05.get(k, 0)), v, sep=',')
    for k, v in mat_sum06.items():
        if ware_data06[k] <= v:
            print(6, k, int(ware_data06.get(k, 0)), v, sep=',')
    for k, v in mat_sum07.items():
        if ware_data07[k] <= v:
            print(7, k, int(ware_data07.get(k, 0)), v, sep=',')
    for k, v in mat_sum08.items():
        if ware_data08[k] <= v:
            print(8, k, int(ware_data08.get(k, 0)), v, sep=',')
    for k, v in mat_sum09.items():
        if ware_data09[k] <= v:
            print(9, k, int(ware_data09.get(k, 0)), v, sep=',')


def main1():
    ls_name = [r'w1.xlsx', r'w2.xlsx', r'w3.xlsx', r'w4.xlsx', r'w5.xlsx', r'w6.xlsx', r'w7.xlsx', r'w8.xlsx', r'w9.xlsx']
    for i in range(1, 10):
        with xlrd.open_workbook(ls_name[i-1]) as f:
            sheet = f.sheet_by_name('Sheet1')
            base_name = sheet.row_values(0)
            for r in range(1, sheet.nrows):
                item = build_dict(base_name, sheet.row_values(r))
                if i == 1:
                    ware_data01[item['货品名称']] = item[r'实际库存']
                elif i == 2:
                    ware_data02[item['货品名称']] = item[r'实际库存']
                elif i == 3:
                    ware_data03[item['货品名称']] = item[r'实际库存']
                elif i == 4:
                    ware_data04[item['货品名称']] = item[r'实际库存']
                elif i == 5:
                    ware_data05[item['货品名称']] = item[r'实际库存']
                elif i == 6:
                    ware_data06[item['货品名称']] = item[r'实际库存']
                elif i == 7:
                    ware_data07[item['货品名称']] = item[r'实际库存']
                elif i == 8:
                    ware_data08[item['货品名称']] = item[r'实际库存']
                elif i == 9:
                    ware_data09[item['货品名称']] = item[r'实际库存']

if __name__ == '__main__':
    mat_sum01 = {}
    mat_sum02 = {}
    mat_sum03 = {}
    mat_sum04 = {}
    mat_sum05 = {}
    mat_sum06 = {}
    mat_sum07 = {}
    mat_sum08 = {}
    mat_sum09 = {}
    ware_data01 = {}
    ware_data02 = {}
    ware_data03 = {}
    ware_data04 = {}
    ware_data05 = {}
    ware_data06 = {}
    ware_data07 = {}
    ware_data08 = {}
    ware_data09 = {}
    print('企业编号,货品名称,实际数量,需求数量')
    with xlrd.open_workbook(r'w0.xlsx') as f:
        sheet = f.sheet_by_name('Sheet1')
        base_name = sheet.row_values(0)
        for r in range(1, sheet.nrows):
            item = build_dict(base_name, sheet.row_values(r))
            main(item)

    main1()
    raw_material()
