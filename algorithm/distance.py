import math
import pandas as pd


class GPSDistance:
    def __init__(self, base_lat=0.0, base_long=0.0, dest_lat=0.0, dest_long=0.0):
        self.base_lat = base_lat
        self.base_long = base_long
        self.dest_lat = dest_lat
        self.dest_long = dest_long

    def set_base_gps(self, *args, **kwargs):
        print("args:", args)
        print("kwargs:", kwargs)

        if (str(type(args[0])) == "<class 'dict'>") or (str(type(args[0])) == "<class 'pandas.core.frame.DataFrame'>"):
            kwargs = args[0]
            print(args[0])

        if 'gps_lat' in kwargs:
            self.base_lat = kwargs['gps_lat']
        else:
            self.base_lat = args[0]

        if 'gps_long' in kwargs:
            self.base_long = kwargs['gps_long']
        else:
            self.base_long = args[1]
        print("base", self.base_lat, self.base_long, sep="\n")

    def set_dest_gps(self, *args, **kwargs):
        print("args:", args)
        print("kwargs:", kwargs)

        if (str(type(args[0])) == "<class 'dict'>" or str(type(args[0])) == "<class 'pandas.core.frame.DataFrame'>"):
            kwargs = args[0]
            print(args[0])

        if 'gps_lat' in kwargs:
            self.dest_lat = kwargs['gps_long']
        else:
            self.dest_lat = args[0]

        if 'gps_long' in kwargs:
            self.dest_long = kwargs['gps_long']
        else:
            self.dest_long = args[1]
        print("dest", *args, **kwargs, sep="\n")

    def get_distance(self):
        res = 6371 * math.acos(math.cos(math.radians(self.base_lat)) * math.cos(math.radians(self.dest_lat)) * math.cos(
            math.radians(self.dest_long) - math.radians(self.base_long)) + math.sin(
            math.radians(self.base_lat)) * math.sin(math.radians(self.dest_lat)))
        return res
