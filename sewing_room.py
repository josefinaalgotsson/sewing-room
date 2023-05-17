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