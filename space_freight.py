import csv
from space_craft import Spacecraft
from cargo import Cargo

class spacefreight():
    def __init__(self, list):

        # call the files that are needed for the operation
        self.ships = self.load_ships(f"spacecraft.txt")
        self.cargo = self.load_cargo(f"CargoLists/Cargo{list}.csv")

    def load_cargo(self, filename):
        list_cargo = []
        with open(filename) as f:
            while True:
                lines = f.readlines()
                for line in lines:
                    if len(line) < 26:
                        line = line.split(',')
                        parcel_id = line[0]
                        mass = float(line[1])
                        volume = float(line [2])
                        mass_per_vol = mass / volume
                        cargo_data = Cargo(parcel_id, mass, volume,
                                           mass_per_vol)
                        list_cargo.append(cargo_data)
                if not lines:
                    break
        return list_cargo
    def load_ships(self, filename):
        list_ships = []
        with open(filename) as f:
            while True:
                lines = f.readlines()
                for line in lines:
                    line = line.split(',')
                    ship_name = line[0]
                    ship_location = line[1]
                    ship_pay_mass = line[2]
                    ship_pay_vol = line[3]
                    ship_mass = line[4]
                    ship_base_costs = line[5]
                    costs = ship_base_costs.split('M')
                    ship_base_costs = int(costs[0]) * 1000000
                    ship_fuel = line[6]
                    mass_per_volume = int(ship_pay_mass) / float(ship_pay_vol)
                    ship_data = Spacecraft(ship_name, ship_location,
                                           ship_pay_mass, ship_pay_vol,
                                           ship_mass, ship_base_costs,
                                           ship_fuel, mass_per_volume)
                    list_ships.append(ship_data)
                if not lines:
                    break
        return list_ships

if __name__ == "__main__":
    space_freight = spacefreight('List1')
