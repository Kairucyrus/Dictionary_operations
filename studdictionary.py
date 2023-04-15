# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 20:09:43 2023
Function rarest_age accepts the names to ages of students from a students' dictionary and returns 
the least frequently occurring age.
@author: Kairu Cyrus
"""

def rarest_age(students):
    # Create a dictionary to store the frequency of each age
    age_frequency = {}
    for age in students.values():
        if age in age_frequency:
            age_frequency[age] += 1
        else:
            age_frequency[age] = 1
    
    # Find the least frequent age
    rarest_age = None
    least_freq_count = float('inf')
    for age, freq in age_frequency.items():
        if freq < least_freq_count:
            rarest_age = age
            least_freq_count = freq
    
    return rarest_age
students = {'Mpweke': 20, 'Wanyo': 22, 'Manzi': 20, 'Davis': 17, 'Eilene': 33, 'Tyler': 22}
rarest_age = rarest_age(students)
print("The least frequently occurring age is:", rarest_age) # returns 17
