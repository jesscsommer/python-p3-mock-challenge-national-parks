#!/usr/bin/env python3
import ipdb

from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # Parks 
    p1 = NationalPark("Crater Lake")
    p2 = NationalPark("Olympic")
    p3 = NationalPark("Arches")
    p4 = NationalPark("Acadia")

    # Visitors
    v1 = Visitor("Jess")
    v2 = Visitor("Ava")
    v3 = Visitor("Herm")

    # Trips 

    t1 = Trip(v1, p2, "March 30", "April 1")
    t2 = Trip(v1, p3, "May 15", "May 15")
    t3 = Trip(v1, p2, "August 10", "August 15")
    t4 = Trip(v2, p2, "May 15", "May 27")
    t5 = Trip(v2, p1, "July 27", "July 29")

    ipdb.set_trace()
