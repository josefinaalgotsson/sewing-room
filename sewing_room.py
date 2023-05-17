class Fabric():
    def __init__(self, width, length, weavetype, thickness, rate):
        self.width = width
        self.length = length
        self.weave = weavetype
        self.thickness = thickness
        self.rate = rate
            
    def cut(self,amount):
        amount = Pattern.to_amount(amount)
        if self.length > amount:
            self.length -= amount
            self.show_length()
        else:
            print('Not enough fabric!')
    
    def addfabric(self,amount):
        amount = Pattern.to_amount(amount)
        self.length +=amount
        self.show_length()
            
    def show_length(self):
        print(f'You have {round(self.length,2)} meters fabric left')
        
    def show_rate(self):
        print(f'Fabric costs {self.rate} kr/m')
        
            
class Pattern():
    def __init__(self, garmenttype, sizes, cost=0, label=None, store=None):
        self.garmenttype = garmenttype
        self.sizes = sizes
        self.cost = cost
        self.label = label
        self.store = store
    
    @staticmethod
    def to_amount(thing):
        if isinstance(thing, float) or isinstance(thing, int):
            return thing
        elif isinstance(thing, Garment):
            return thing.amount
        
    @staticmethod
    def knit_circle_skirt(waist,length,seamallowance):
        waistradius = waist/(2*3.14) - seamallowance
        skirtradius = waistradius + seamallowance + length
        waistband = waist + 2*seamallowance
        return waistradius, skirtradius, waistband
    
    @staticmethod
    def threepart_circle_skirt(waist,length,seamallowance):
        waistradius = (4*seamallowance + waist)/(2*3.14) - seamallowance
        waistradius2 = (8*seamallowance+ waist)/(2*3.14) - seamallowance
        skirtradius = waistradius + seamallowance + length
        skirtradius2 = waistradius2 + seamallowance + length
        waistband = waist/2 + 2*seamallowance
        waistband2 = waist/4+2*seamallowance
        return waistradius, waistradius2, skirtradius, skirtradius2, waistband, waistband2     
        
        
class Garment():
    def __init__(self,pattern,size,fabric=None):
        self.pattern = pattern
        self.size = size
        self.fabric = fabric
        self.amount = pattern.sizes[size]
        self.cost = self.amount * fabric.rate
        
    def __add__(self, other):
        return self.amount + other.amount
    
    def showcost(self):
        print(f'Garment cost is {self.cost} kr.')

        
# Fabric Inventory
sheetfabric = Fabric(1.4, 5, 'weave','light',50)
flowerfabric = Fabric(1.4, 3, 'weave','medium',150)
print('Showing original length')
sheetfabric.show_length()

# Pattern inventory
cribsheet_pattern = Pattern('linens',{1: 0.92})
Miette = Pattern('skirt',{1:2, 2:2,3:2,4:2,5:2,6:2,7:2.7,8:2.7 },115,'Tilly')

# Garments / Projects
sheet = Garment(cribsheet_pattern,1,sheetfabric)
sheet2 = Garment(cribsheet_pattern,1,sheetfabric)
sheet3 = Garment(cribsheet_pattern,1,flowerfabric)

# Actions
print('cutting cribsheet')
sheetfabric.cut(sheet)
print('Changed my mind, adding back garment')
sheetfabric.addfabric(sheet)
print('buying more fabric')
sheetfabric.addfabric(2)
print('cutting fabric for two sheets at once')
sheetfabric.cut(sheet+sheet2)
print('cutting out sheet with cut')
sheetfabric.cut(sheet)
print('cutting out 3 m with cut')
sheetfabric.cut(3)
print('sheet cost')
print(sheet.cost)
print('sheet cost')
sheet3.showcost()
print('flower fabric rate')
flowerfabric.show_rate()
print()

w,l,wb = Pattern.knit_circle_skirt(0.8,1.3,0.015)
print(w)
print(l)
print(wb)
print()
w,w2,l,l2,wb, wb2 = Pattern.threepart_circle_skirt(0.8,1.3,0.015)
print(w)
print(w2)
print(l)
print(l2)
print(wb)
print(wb2)