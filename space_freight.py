import csv
import locale
from space_craft import Spacecraft
from cargo import Cargo

class spacefreight():
    def __init__(self, list):

        # call the files that are needed for the operation
        self.ships = self.load_ships(f"spacecraft.txt")
        self.cargo = self.load_cargo(f"CargoLists/Cargo{list}.csv")

    def load_cargo(self, filename):
        list_cargo = []
        with open(filename) as csv_data:
                reader = csv.reader(csv_data, delimiter=',')
                next(reader)
                val_sorted = sorted(reader, key = lambda\
                                    x:float(x[1])/float(x[2]), reverse=False)
                for line in val_sorted:
                    parcel_id = line[0]
                    mass = float(line[1])
                    volume = float(line[2])
                    mass_per_vol = mass / volume
                    cargo_data = Cargo(parcel_id, mass, volume,
                                       mass_per_vol)
                    list_cargo.append(cargo_data)
                    # print(cargo_data)
        return list_cargo

    def load_ships(self, filename):
        list_ships = []
        with open(filename) as csv_data:
                reader = csv.reader(csv_data, delimiter=',')
                val_sorted = sorted(reader, key = lambda\
                                    x:float(x[2])/float(x[3]), reverse=False)
                for line in val_sorted:
                    ship_name = line[0]
                    ship_location = line[1]
                    ship_pay_mass = int(line[2])
                    ship_pay_vol = float(line[3])
                    ship_mass = int(line[4])
                    ship_base_costs = line[5]
                    costs = ship_base_costs.split('M')
                    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
                    ship_base_costs = locale.currency(int(costs[0]) * 1000000,
                                                      grouping=True)
                    ship_fuel = float(line[6])
                    mass_per_volume = int(ship_pay_mass) / float(ship_pay_vol)
                    ship_data = Spacecraft(ship_name, ship_location,
                                           ship_pay_mass, ship_pay_vol,
                                           ship_mass, ship_base_costs,
                                           ship_fuel, mass_per_volume)
                    list_ships.append(ship_data)
                    # print(ship_data)
        return list_ships
if __name__ == "__main__":
    space_freight = spacefreight('List1')
