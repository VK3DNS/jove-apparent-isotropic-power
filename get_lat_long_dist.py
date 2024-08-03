from astropy.time import Time
import astropy.units as u
import numpy
from astropy.coordinates import solar_system_ephemeris, EarthLocation, AltAz
from astropy.coordinates import get_body_barycentric, get_body
import datetime

class ObjectData():
    def __init__(self):
        self.lat = "-36"
        self.lon = "144"
        self.elev = "100"


    def update_values(self, time_to_use):
        loc = EarthLocation.from_geodetic(lat=self.lat, lon=self.lon, height=int(self.elev if self.elev.isnumeric() else 0))
        with solar_system_ephemeris.set('builtin'):
            jup = get_body('jupiter', Time(time_to_use), loc)
            jupaltaz = jup.transform_to(AltAz(obstime=Time(time_to_use), location=loc))
            self.distance = str(jup.distance)
            self.ra = str(jup.ra)
            self.dec = str(jup.dec)
            self.alt = str(jupaltaz.alt)
            self.az = str(jupaltaz.az)
