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
            self.jup = get_body('jupiter', Time(time_to_use), loc)
            self.jupaltaz = self.jup.transform_to(AltAz(obstime=Time(time_to_use), location=loc))
            self.distance = str(self.jup.distance)
            self.ra = str(self.jup.ra)
            self.dec = str(self.jup.dec)
            self.alt = str(self.jupaltaz.alt)
            self.az = str(self.jupaltaz.az)

            self.sun = get_body('sun', Time(time_to_use), loc)
            self.sunaltaz = self.sun.transform_to(AltAz(obstime=Time(time_to_use), location=loc))
            self.sundistance = str(self.sun.distance)
            self.sunra = str(self.sun.ra)
            self.sundec = str(self.sun.dec)
            self.sunalt = str(self.sunaltaz.alt)
            self.sunaz = str(self.sunaltaz.az)
