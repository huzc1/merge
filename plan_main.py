import xlrd
import Supplies

def build_dict(l1, l2):
    rst = {}
    for i in range(len(l1)):
        rst[l1[i]] = l2[i]
    return rst

def print_plan_data(mat):
    for k, v in mat.items():
        plan_data[k] = plan_data.get(k, 0) + v

def mat_sum1(item):
    if item['单位'] == '盒':
        i = Supplies.Rice_Box(taste=item['口味分类'], deliver=item['计划（件）'], standard=item['箱规'])
        mat = i.materials()
    elif item['单位'] == '罐':
        i = Supplies.Rice_Pot(taste=item['口味分类'], deliver=item['计划（件）'], standard=item['箱规'])
        mat = i.materials()
    print_plan_data(mat)

def mat_sum2(item):
    if item['产品系列'] == '直面':
        i = Supplies.Noodles(taste=item['口味分类'], deliver=item['计划（件）'], standard=item['箱规'])
        mat = i.materials()
    elif item['产品系列'] == '蝴蝶面':
        i = Supplies.Farfalles(taste=item['口味分类'], deliver=item['计划（件）'], standard=item['箱规'])
        mat = i.materials()
    elif item['产品系列'] == '面片':
        i = Supplies.Facets(taste=item['口味分类'], deliver=item['计划（件）'], standard=item['箱规'])
        mat = i.materials()
    print_plan_data(mat)

def mat_sum3(item):
    if item['产品系列'] == '益生菌' and item['箱规'] == 12:
        i = Supplies.ProbioticsBig(taste=item['口味分类'], deliver=item['计划（件）'], standard=item['箱规'])
        mat = i.materials()
    elif item['产品系列'] == '益生菌' and item['箱规'] == 24:
        i = Supplies.ProbioticsSmall(taste=item['口味分类'], deliver=item['计划（件）'], standard=item['箱规'])
        mat = i.materials()
    elif item['产品系列'] == '宝清宁' and item['箱规'] == 12:
        i = Supplies.BaoQingNingGuan(taste=item['口味分类'], deliver=item['计划（件）'], standard=item['箱规'])
        mat = i.materials()
    elif item['产品系列'] == '宝清宁' and item['箱规'] == 24 and item['口味分类'] == '原味':
        i = Supplies.BaoQingNingOriginal(taste=item['口味分类'], deliver=item['计划（件）'], standard=item['箱规'])
        mat = i.materials()
    elif item['产品系列'] == '宝清宁' and item['箱规'] == 24:
        i = Supplies.BaoQingNingHe(taste=item['口味分类'], deliver=item['计划（件）'], standard=item['箱规'])
        mat = i.materials()
    elif item['产品系列'] == '蛋白质':
        i = Supplies.Protein(taste=item['口味分类'], deliver=item['计划（件）'], standard=item['箱规'])
        mat = i.materials()
    elif item['产品系列'] == '葡萄糖' and item['箱规'] == 12:
        i = Supplies.Prebiotics(taste=item['口味分类'], deliver=item['计划（件）'], standard=item['箱规'])
        mat = i.materials()
    elif item['产品系列'] == '葡萄糖' and item['箱规'] == 24:
        i = Supplies.Glucosum(taste=item['口味分类'], deliver=item['计划（件）'], standard=item['箱规'])
        mat = i.materials()
    elif item['产品系列'] == '饮料':
        i = Supplies.Minerals(taste=item['口味分类'], deliver=item['计划（件）'], standard=item['箱规'])
        mat = i.materials()
    print_plan_data(mat)

def mat_sum4(item):
    if item['箱规'] == 12:
        i = Supplies.BigDHA(taste=item['口味分类'], deliver=item['计划（件）'], standard=item['箱规'])
        mat = i.materials()
    elif item['箱规'] == 24:
        i = Supplies.SmallDHA(taste=item['口味分类'], deliver=item['计划（件）'], standard=item['箱规'])
        mat = i.materials()
    elif item['箱规'] == 36:
        i = Supplies.MilkCalcium(taste=item['口味分类'], deliver=item['计划（件）'], standard=item['箱规'])
        mat = i.materials()
    print_plan_data(mat)

def mat_sum5(item):
    i = Supplies.SolubleBean(taste=item['口味分类'], deliver=item['计划（件）'], standard=item['箱规'])
    mat = i.materials()
    print_plan_data(mat)

def mat_sum6(item):
    i = Supplies.Puff(taste=item['口味分类'], deliver=item['计划（件）'], standard=item['箱规'])
    mat = i.materials()
    print_plan_data(mat)

def oem_select(item , n):
    if n == 1:
        mat_sum1(item)
    elif n == 2:
        mat_sum2(item)
    elif n == 3:
        mat_sum3(item)
    elif n == 4:
        mat_sum4(item)
    elif n == 5:
        mat_sum5(item)
    elif n == 6:
        mat_sum6(item)

def open_plan_file(n):
    base_name = 'plan_data/p' + str(n) + '.xlsx'
    with xlrd.open_workbook(base_name) as f:
        sheet = f.sheet_by_name('Sheet1')
        name = sheet.row_values(0)
        for r in range(1, sheet.nrows):
            item = build_dict(name, sheet.row_values(r))
            oem_select(item, n)

def open_ware_file(n):
    base_name = 'w' + str(n) + '.xlsx'
    with xlrd.open_workbook(base_name) as f:
        sheet = f.sheet_by_name('Sheet1')
        name = sheet.row_values(0)
        for r in range(1, sheet.nrows):
            item = build_dict(name, sheet.row_values(r))
            ware_data[item['货品名称']] = item[r'实际库存']

def main(n):
    open_plan_file(n)
    open_ware_file(n)

if __name__ == '__main__':
    plan_data = {}
    ware_data = {}
    try:
        n = int(eval(input('请输入要检测公司的编号：')))
    except Exception as e:
        print('输入的信息有误')
        print(e)
    main(n)
    print('公司编号, 产品名称, 实际库存, 需求数据')
    for k, v in plan_data.items():
        if ware_data[k] < v:
            print(n, k, int(ware_data[k]), v, sep=',')
