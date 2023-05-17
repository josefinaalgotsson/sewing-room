class Fabric():
    def __init__(self, width, length, weavetype, thickness):
        self.width = width
        self.length = length
        self.weave = weavetype
        self.thickness = thickness
        
    def cutgarment(self,garment):
        if self.length > garment.garmentamount:
            self.length -= garment.garmentamount
            self.show_length()
        else:
            print('Not enough fabric!')
    
    def cutfabric(self,amount):
        if self.length > amount:
            self.length -= amount
            self.show_length()
        else:
            print('Not enough fabric!')
            
    def addgarment(self,garment):
        self.length += garment.garmentamount
        self.show_length()
    
    def addfabric(self,amount):
        self.length +=amount
        self.show_length()
            
    def show_length(self):
        print(f'You have {self.length} meters fabric left')
        
class Pattern():
    def __init__(self, garmenttype, garmentamount):
        self.garmenttype = garmenttype
        self.garmentamount = garmentamount
        
    def __add__(self, other):
        return self.garmentamount + other.garmentamount
        
        
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
sheetfabric.cutgarment(babysheet)
print('Changed my mind, adding back garment')
sheetfabric.addgarment(babysheet)
print('buying more fabric')
sheetfabric.addfabric(2)
print('cutting fabric for two sheets at once')
sheetfabric.cutfabric(babysheet+babysheet2)