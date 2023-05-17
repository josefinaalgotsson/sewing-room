class Fabric():
    def __init__(self, width, length, weavetype, thickness):
        self.width = width
        self.length = length
        self.weave = weavetype
        self.thickness = thickness
            
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
        
            
class Pattern():
    def __init__(self, garmenttype, garmentamount):
        self.garmenttype = garmenttype
        self.garmentamount = garmentamount
        
    def __add__(self, other):
        return self.garmentamount + other.garmentamount
    
    @staticmethod
    def to_amount(thing):
        if isinstance(thing, float) or isinstance(thing, int):
            return thing
        elif isinstance(thing, Pattern):
            return thing.garmentamount
        
  
        
# Inventory
sheetfabric = Fabric(1.4, 5, 'weave','light')
print('Showing original length')
sheetfabric.show_length()

# Garments / Projects
babysheet = Pattern('linens',0.92)
babysheet2 = Pattern('linens',0.92)
babysheet3 = Pattern('linens',0.92)

# Actions
print('cutting babysheet')
sheetfabric.cut(babysheet)
print('Changed my mind, adding back Pattern')
sheetfabric.addfabric(babysheet)
print('buying more fabric')
sheetfabric.addfabric(2)
print('cutting fabric for two sheets at once')
sheetfabric.cut(babysheet+babysheet2)
print('cutting babysheet with cut')
sheetfabric.cut(babysheet)
print('cutting 3 with cut')
sheetfabric.cut(3)