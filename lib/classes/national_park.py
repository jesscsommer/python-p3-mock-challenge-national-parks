class NationalPark:

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = set()
        
    def trips(self, new_trip=None):
        from classes.trip import Trip
        if isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return self._trips
    
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        if isinstance(new_visitor, Visitor):
            self._visitors.add(new_visitor)
        return list(self._visitors)
    
    def total_visits(self):
        return len(self._trips)
    
    def best_visitor(self):
        most_visits = 0
        best_visitor = None
        for visitor in self._visitors:
            count = len([trip for trip in self._trips if trip.visitor == visitor])
            if count and count > most_visits:
                most_visits = count
                best_visitor = visitor
        return best_visitor

    # Properties 
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, "name") and type(name) == str:
            self._name = name
        else: 
            raise Exception 