
from region import Region 

class Regions:
    def __init__(self):
        self.valid_regions = []

    def add_region(self, code, name):
        region = Region(code, name)
        self.valid_regions.append(region)

    def get_region_by_code(self, code):
        for region in self.valid_regions:
            if region.code == code:
                return region

    def get_valid_region_codes(self):
        return [region.code for region in self.valid_regions]

    def __str__(self):
        return ", ".join([str(region) for region in self.valid_regions])
