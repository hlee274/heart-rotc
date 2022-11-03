#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 10:06:16 2022

@author: laurenji
"""

import math

#Basic contact information (name and different ways to contact user)
name = input('Enter your first and last name: ')
list_name = name.split()
first_name = list_name[0]
last_name = list_name[1]

phone_number = input('Enter phone number: ')
email = input('Enter email: ')
preferred_contact_method = input('Do you prefer to be contacted through phone or email: ')

#Medicine (find out the medicine(s) desired and rank them in order of importance)
medicines_desired = input('Enter the medicine(s) that you are in need of in order of importance from lowest to highest necessity: ')
individual_medicine_list = medicines_desired.split()
amount_of_medicine_desired = len(individual_medicine_list)

#create a dictionary of medicine, with the key value ranking the order of importance of that medicine starting from 1
medicine_dict = []
for i in range(amount_of_medicine_desired-1):
    medicine_dict[i+1] = individual_medicine_list[i]
    
#Location and pickup
location = input('Enter your address with location coordinates. For example 15, 18: ')
list_location = location.split()
longitude = list_location[0]
latitude = list_location[1]
coordinate_point = [longitude, latitude]
willing_distance = input('Enter the amount of distance you are willing to drive in miles')

class Circle:
    '''
    A class to represent a circular area that an app user would be willing to travel.

    Attributes
    ----------
    coordinate_point : list
        list of the x coordinate point, y coordinate point
    willing_distance : int or float
        radius of the circle
        
    Methods
    -------
    __init__ : initializes a Circle object
    calculate_area : calculates the area of a circle, returns the area
    (to make) find_overlap between one circle and another
    '''
    def __init__(self, coordinate_point, willing_distance):
        self.x = coordinate_point[0]
        self.y = coordinate_point[1]
        self.center = coordinate_point
        self.radius = willing_distance
        
    def calculate_area(self):
        area = math.pi * (self.radius ** 2)
        return area
    
