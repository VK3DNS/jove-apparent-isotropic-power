from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris, EarthLocation
from astropy.coordinates import get_body_barycentric, get_body
import datetime

class JupiterValues():
    def __init__(self):
        self.lat = "-36"
        self.lon = "144"


    def update_values(self, time_to_use):
        loc = EarthLocation.from_geodetic(self.lon, self.lat)
        with solar_system_ephemeris.set('builtin'):
            jup = get_body('jupiter', Time(time_to_use), loc)
            self.distance = str(jup.distance)
            self.ra = str(jup.ra)
            self.dec = str(jup.dec)
