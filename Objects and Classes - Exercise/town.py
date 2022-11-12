class Town:
    def __init__(self, name_of_the_town: str, latitude="0°N", longitude="0°E"):
        self.name_of_the_town = name_of_the_town
        self.latitude = latitude
        self.longitude = longitude

    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_longitude(self, longitude):
        self.longitude = longitude

    def __repr__(self):
        return f"Town: {self.name_of_the_town} | Latitude: {self.latitude} | Longitude: {self.longitude}"


town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)
