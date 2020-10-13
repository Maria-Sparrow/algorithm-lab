class SwimmingPool():
    def __init__(self, address, volume_of_water, max_number_of_visitors):
        self.address = address
        self.volume_of_water = volume_of_water
        self.max_number_of_visitors = max_number_of_visitors

    def __str__(self):
        return "address " + self.address + ", volume_of_water " + str(self.volume_of_water) + ", visitors " + str(self.max_number_of_visitors)

    @staticmethod
    def compare(small, deep, tag="volume_of_water", greater_then=True):
        if tag =="volume_of_water":
            return small.volume_of_water > deep.volume_of_water
        else:
            return small.max_number_of_visitors > deep.max_number_of_visitors