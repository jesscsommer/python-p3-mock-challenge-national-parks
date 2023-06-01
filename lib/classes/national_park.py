class NationalPark: 

    def __init__(self, name):
        self.name = name 

    # Properties
    @property 
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if (isinstance(name, str)
            and not hasattr(self, "_name")):
            self._name = name 
        else: 
            raise Exception("Name must be a string; name cannot be changed")
    
    # Instance methods
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park is self]
    
    def visitors(self):
        return list({trip.visitor for trip in self.trips()})
    
    # Aggregate and assocation methods
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        visit_counts = [(visitor, visitor.count_park_trips(self)) 
                        for visitor in self.visitors()]
        visit_counts.sort(key=lambda t: t[1], reverse=True)
        return visit_counts[0][0] if visit_counts else "No visits"

from classes.trip import Trip