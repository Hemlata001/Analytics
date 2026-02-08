class Factory:
    def __init__(self, material, zips, pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets
reebok = Factory("leather",3,2)
campus = Factory("nylon",3,3)
print(campus.pockets)
print(reebok.zips)
print(campus.material)
print(reebok.material)
