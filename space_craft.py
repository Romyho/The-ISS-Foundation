
class Spacecraft(object):
    def __init__(self, name, nation, payload_mass, payload_volume, mass,
                base_costs, fuel_to_weight, mass_per_volume):

        self.name = name
        self.nation = nation
        self.payload_mass = payload_mass
        self.payload_volume = payload_volume
        self.mass = mass
        self.base_costs = base_costs
        self.fuel_to_weight = fuel_to_weight
        self.mass_per_volume = mass_per_volume
    def __str__(self):
        return str(self.name) + ' ' + str(self.nation)
