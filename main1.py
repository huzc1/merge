import Supplies
import xlrd
'''
以仓库的需求差异计算包材的需求量
'''
global mat_sum01, mat_sum02, mat_sum03, mat_sum04, mat_sum05, mat_sum06
global ware_data01, ware_data02, ware_data03, ware_data04, ware_data05, ware_data06

def build_dict(list1, list2):
    rst= {}
    for i in range(len(list1)):
        rst[list1[i]] =list2[i]
    return rst

def mat_sum1(item):
    global mat_sum01
    if item['单位'] == '盒':
        item_data = Supplies.Rice_Box(taste=item['口味分类'], deliver=item['需求差异'], standard=item['箱规'])
        mat = item_data.materials()
    elif item['单位'] == '罐':
        item_data = Supplies.Rice_Pot(taste=item['口味分类'], deliver=item['需求差异'], standard=item['箱规'])
        mat = item_data.materials()
    for k, v in mat.items():
        mat_sum01[k] = mat_sum01.get(k, 0) + v

def mat_sum2(item):
    global mat_sum02
    if item['产品系列'] == '直面':
        item_data = Supplies.Noodles(taste=item['口味分类'], deliver=item['需求差异'], standard=item['箱规'])
        mat = item_data.materials()
    elif item['产品系列'] == '蝴蝶面':
        item_data = Supplies.Farfalles(taste=item['口味分类'], deliver=item['需求差异'], standard=item['箱规'])
        mat = item_data.materials()
    elif item['产品系列'] == '面片':
        item_data = Supplies.Facets(taste=item['口味分类'], deliver=item['需求差异'], standard=item['箱规'])
        mat = item_data.materials()
    for k, v in mat.items():
        mat_sum02[k] = mat_sum02.get(k, 0) + v

def mat_sum3(item):
    global mat_sum03
    if item['产品系列'] == '益生菌' and item['箱规'] == 12:
        item_data = Supplies.ProbioticsBig(taste=item['口味分类'], deliver=item['需求差异'], standard=item['箱规'])
        mat = item_data.materials()
    elif item['产品系列'] == '益生菌' and item['箱规'] == 24:
        item_data = Supplies.ProbioticsSmall(taste=item['口味分类'], deliver=item['需求差异'], standard=item['箱规'])
        mat = item_data.materials()
    elif item['产品系列'] == '宝清宁' and item['箱规'] == 12:
        item_data = Supplies.BaoQingNingGuan(taste=item['口味分类'], deliver=item['需求差异'], standard=item['箱规'])
        mat = item_data.materials()
    elif item['产品系列'] == '宝清宁' and item['箱规'] == 24 and item['口味分类'] == '原味':
        item_data = Supplies.BaoQingNingOriginal(taste=item['口味分类'], deliver=item['需求差异'], standard=item['箱规'])
        mat = item_data.materials()
    elif item['产品系列'] == '宝清宁' and item['箱规'] == 24:
        item_data = Supplies.BaoQingNingHe(taste=item['口味分类'], deliver=item['需求差异'], standard=item['箱规'])
        mat = item_data.materials()
    elif item['产品系列'] == '蛋白质':
        item_data = Supplies.Protein(taste=item['口味分类'], deliver=item['需求差异'], standard=item['箱规'])
        mat = item_data.materials()
    elif item['产品系列'] == '葡萄糖' and item['箱规'] == 12:
        item_data = Supplies.Prebiotics(taste=item['口味分类'], deliver=item['需求差异'], standard=item['箱规'])
        mat = item_data.materials()
    elif item['产品系列'] == '葡萄糖' and item['箱规'] == 24:
        item_data = Supplies.Glucosum(taste=item['口味分类'], deliver=item['需求差异'], standard=item['箱规'])
        mat = item_data.materials()
    elif item['产品系列'] == '饮料':
        item_data = Supplies.Minerals(taste=item['口味分类'], deliver=item['需求差异'], standard=item['箱规'])
        mat = item_data.materials()
    for k, v in mat.items():
        mat_sum03[k] = mat_sum03.get(k, 0) + v


def mat_sum4(item):
    global mat_sum04
    if item['箱规'] == 12:
        item_data = Supplies.BigDHA(taste=item['口味分类'], deliver=item['需求差异'], standard=item['箱规'])
        mat = item_data.materials()
    elif item['箱规'] == 24:
        item_data = Supplies.SmallDHA(taste=item['口味分类'], deliver=item['需求差异'], standard=item['箱规'])
        mat = item_data.materials()
    elif item['箱规'] == 36:
        item_data = Supplies.MilkCalcium(taste=item['口味分类'], deliver=item['需求差异'], standard=item['箱规'])
        mat = item_data.materials()
    for k, v in mat.items():
        mat_sum04[k] = mat_sum04.get(k, 0) + v

def mat_sum5(item):
    global mat_sum05
    item_data = Supplies.SolubleBean(taste=item['口味分类'], deliver=item['需求差异'], standard=item['箱规'])
    mat = item_data.materials()
    for k, v in mat.items():
        mat_sum05[k] = mat_sum05.get(k, 0) + v

def mat_sum6(item):
    global mat_sum06
    item_data = Supplies.Puff(taste=item['口味分类'], deliver=item['需求差异'], standard=item['箱规'])
    mat = item_data.materials()
    for k, v in mat.items():
        mat_sum06[k] = mat_sum06.get(k, 0) + v



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

def raw_material():
    global mat_sum01, mat_sum02, mat_sum03, mat_sum04, mat_sum05, mat_sum06
    global ware_data01, ware_data02, ware_data03, ware_data04, ware_data05, ware_data06
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


def main1():
    global ware_data01, ware_data02, ware_data03, ware_data04, ware_data05, ware_data06
    ls_name = [r'rst1.xlsx', r'rst2.xlsx', r'rst3.xlsx', r'rst4.xlsx', r'rst5.xlsx', r'rst6.xlsx']
    for i in range(6):
        with xlrd.open_workbook(ls_name[i]) as f:
            sheet = f.sheet_by_name('Sheet1')
            base_name = sheet.row_values(0)
            for r in range(1, sheet.nrows):
                item = build_dict(base_name, sheet.row_values(r))
                if i == 0:
                    ware_data01[item['货品名称']] = item[r'实际库存']
                elif i == 1:
                    ware_data02[item['货品名称']] = item[r'实际库存']
                elif i == 2:
                    ware_data03[item['货品名称']] = item[r'实际库存']
                elif i == 3:
                    ware_data04[item['货品名称']] = item[r'实际库存']
                elif i == 4:
                    ware_data05[item['货品名称']] = item[r'实际库存']
                elif i == 5:
                    ware_data06[item['货品名称']] = item[r'实际库存']

if __name__ == '__main__':
    global mat_sum01, mat_sum02, mat_sum03, mat_sum04, mat_sum05, mat_sum06
    global ware_data01, ware_data02, ware_data03, ware_data04, ware_data05, ware_data06
    mat_sum01 = {}
    mat_sum02 = {}
    mat_sum03 = {}
    mat_sum04 = {}
    mat_sum05 = {}
    mat_sum06 = {}
    ware_data01 = {}
    ware_data02 = {}
    ware_data03 = {}
    ware_data04 = {}
    ware_data05 = {}
    ware_data06 = {}
    print('企业编号,货品名称,实际数量,需求数量')
    with xlrd.open_workbook(r'rst0.xlsx') as f:
        sheet = f.sheet_by_name('Sheet1')
        base_name = sheet.row_values(0)
        for r in range(1, sheet.nrows):
            item = build_dict(base_name, sheet.row_values(r))
            if item['需求差异'] > 0:
                main(item)
    main1()
    raw_material()