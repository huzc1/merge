class Product():

    def __init__(self, name='name', brand=1, OEM=1, purpose=1, ser=1, series='series', taste='taste', weight=1, standard=1, unit ='盒', deliver=0, balance=0, num_days=1):
        self.name = name            #名称
        self.brand = brand          #品牌
        self.OEM = OEM              #工厂
        self.purpose = purpose      #用途
        self.series = series        #系列
        self.taste = taste          #口味
        self.weight = weight        #净含量
        self.standard = standard    #箱规
        self.unit = unit            #单位
        self.deliver = deliver      #发出数量
        self.balance = balance      #本期结存
        self.num_days =num_days     #天数的系数
        self.ser = ser              #函数分类

class Rice_Box(Product):            #米粉盒
    def materials(self):
        materials = dict()
        base_materials = {'2-24大物流码': 2, '2-24小物流码': 24}
        for k, v in base_materials.items():
            materials[k] = int(self.deliver * self.num_days * v)      #3个月所需物料
        return materials

class Rice_Pot(Product):            #米粉罐
    def materials(self):
        materials = dict()
        base_materials = {'2-12大物流码': 2, '2-12小物流码': 12}
        for k, v in base_materials.items():
            materials[k] = int(self.deliver * self.num_days * v)
        return materials

class Glucose(Product):
    def materials(self):
        materials = dict()
        base_materials = {
            '益生元葡萄糖卷膜': 0.54, '2-12大物流码': 2, '2-12小物流码': 12, '益生元葡萄糖外箱': 1,
            '益生元葡萄糖罐装罐贴': 12, '益生元葡萄糖塑料罐': 12
            }
        for k, v in base_materials.items():
            materials[k] = int(self.deliver * self.num_days * v)
        return materials


class Noodles(Product):            #直面
    def materials(self):
        materials = dict()
        base_materials = {'有机小麦粉': 6.5, '2-24大物流码': 2, '2-24小物流码': 24, '225g'+self.taste+'有机面彩盒': 24,
                          '225g有机直面卷膜': 0.3456, r'225g/210g有机面外箱': 1}
        for k, v in base_materials.items():
            materials[k] = int(self.deliver * self.num_days * v)
        return materials

class Farfalles(Product):           #蝴蝶面
    def materials(self):
        materials = dict()
        base_materials = {'有机小麦粉': 6, '2-24大物流码': 2, '2-24小物流码': 24, '210g'+self.taste+'蝴蝶面彩盒': 24,
                          '210g蝴蝶面卷膜': 0.3528, '210g有机蝴蝶面外箱': 1}
        for k, v in base_materials.items():
            materials[k] = int(self.deliver * self.num_days * v)
        return materials

class Facets(Product):              #面片
    def materials(self):
        materials = dict()
        base_materials = {'有机小麦粉': 6, '2-24大物流码': 2, '2-24小物流码': 24, '210g'+self.taste+'面片彩盒': 24,
                          '210g面片卷膜': 0.2688, r'225g/210g有机面外箱': 1}
        for k, v in base_materials.items():
            materials[k] = int(self.deliver * self.num_days * v)
        return materials



class BaoQingNingHe(Product):           #宝清宁
    def materials(self):
        materials = dict()
        base_materials = {self.taste+'宝清宁卷膜': 0.64, '2-24大物流码': 2, '2-24小物流码': 24,
                          self.taste + '宝清宁彩盒': 24, '156g宝清宁盒装外箱': 1, '宝清宁内托': 24,
                          '益生源封口贴': 48}
        for k, v in base_materials.items():
            materials[k] = int(self.deliver * self.num_days * v)
        return materials


class Minerals(Product):                #复合钙铁锌固体饮料
    def materials(self):
        materials = dict()
        base_materials = {'复合'+self.taste+'固体饮料卷膜': 0.998, '2-48大物流码': 2, '2-48小物流码': 48,
                          '复合钙铁锌固体饮料外箱': 1,  '复合'+self.taste+'固体饮料彩盒': 48, '益生源封口贴': 48}
        for k, v in base_materials.items():
            materials[k] = int(self.deliver * self.num_days * v)
        return materials




class BigDHA(Product):          #DHA（90粒）
    def materials(self):
        materials = dict()
        base_materials = {'2-12大物流码': 2, '2-12小物流码': 12, 'DHA藻油硬盒': 12}
        for k, v in base_materials.items():
            materials[k] = int(self.deliver * self.num_days * v)
        return materials

class SmallDHA(Product):           #DHA(45粒）
    def materials(self):
        materials = dict()
        base_materials = {'2-24大物流码': 2, '2-24小物流码': 24, 'DHA藻油凝胶糖果彩盒及内托': 24}
        for k,v in base_materials.items():
            materials[k] = int(self.deliver * self.num_days * v)
        return materials

class MilkCalcium(Product):         #乳钙
    def materials(self):
        materials = dict()
        base_materials = {'2-36大物流码': 2, '2-36小物流码': 36, '乳钙凝胶糖果彩盒': 36}
        for k, v in base_materials.items():
            materials[k] = int(self.deliver * self.num_days * v)
        return materials

class SolubleBean(Product):             #溶豆
    def materials(self):
        materials = dict()
        base_materials = {'有机溶豆-'+self.taste+'味卷膜': 0.3082, '2-36大物流码': 2, '2-36小物流码': 36,
                          '有机溶豆-'+self.taste+'味彩盒': 36, '有机溶豆外箱': 1, }
        for k, v in base_materials.items():
            materials[k] = int(self.deliver * self.num_days * v)
        return materials

class Puff(Product):                    #泡芙
    def materials(self):
        materials = dict()
        base_materials = {'2-36大物流码': 2, '2-36小物流码': 36, '傲滋有机泡芙外箱': 1, '傲滋有机泡芙膜': 36,
                          '有机大米': 0.756,'有机大豆油': 0.72, '有机玉米粉': 0.414, '有机白砂糖': 0.324,
                          '有机小麦粉': 0.126, '有机全脂奶粉': 0.108}
        for k, v in base_materials.items():
            materials[k] = int(self.deliver * self.num_days * v)
        return materials


class Cale(Product):            #米饼
    def materials(self):
        materials = dict()
        base_materials = {'2-24大物流码': 2, '2-24小物流码': 24}
        for k, v in base_materials.items():
            materials[k] = int(self.deliver * self.num_days * v)      #3个月所需物料
        return materials

class Hat(Product):            #蓝帽子
    def materials(self):
        materials = dict()
        base_materials = {'2-36大物流码': 2, '2-36小物流码': 36}
        for k, v in base_materials.items():
            materials[k] = int(self.deliver * self.num_days * v)      #3个月所需物料
        return materials


class Probiotics(Product):      #益生菌
    def materials(self):
        materials = dict()
        base_materials = {'傲滋益生菌卷膜': 0.82, '2-24大物流码': 2, '2-24小物流码': 24,
                          '傲滋益生菌（'+self.taste+'）彩盒': 24,  '傲滋益生菌外箱': 1
                          }
        for k, v in base_materials.items():
            materials[k] = int(self.deliver * self.num_days * v)
        return materials















