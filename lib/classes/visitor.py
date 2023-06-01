class Visitor: 

    def __init__(self, name):
        self.name = name

    # Properties 
    @property 
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if (isinstance(name, str)
            and 1 <= len(name) <= 15
            and not hasattr(self, "name")):
            self._name = name 
        else: 
            raise Exception("Name must be a string between 2-15 chars")
        
    # Instance methods
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor is self]
    
    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})
    
    def count_park_trips(self, park):
        return len([trip for trip in self.trips() 
                    if trip.national_park is park])

from classes.trip import Trip