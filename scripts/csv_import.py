'''
Created on Nov 24, 2014

@author: sschubiger
'''
from scripting import *

import csv

# get a CityEngine instance
ce = CE()

states = {}

if __name__ == '__main__':
    f = open('/Users/Daniel/Documents/CityEngine/parteien_kantone.csv', 'rt')
    try:
        reader = csv.reader(f)
        for row in reader:
            try:
                states[float(row[1])] = row
            except ValueError:
                pass
    finally:
        f.close()
     
    for state in ce.getObjectsFrom(ce.getObjectsFrom(ce.scene, ce.withName('Kantone'))[0]):
        row = states[ce.getAttribute(state, 'KTNR')]
        
        ce.setAttribute(state, 'FDP', float(row[2]))
        ce.setAttributeSource(state, 'FDP', 'OBJECT')
        
        ce.setAttribute(state, 'CVP', float(row[3]))
        ce.setAttributeSource(state, 'CVP', 'OBJECT')
        
        ce.setAttribute(state, 'SP', float(row[4]))
        ce.setAttributeSource(state, 'SP', 'OBJECT')
        
        ce.setAttribute(state, 'SVP', float(row[5]))
        ce.setAttributeSource(state, 'SVP', 'OBJECT')
        
        ce.setAttribute(state, 'LPS', float(row[6]))
        ce.setAttributeSource(state, 'LPS', 'OBJECT')
        
        ce.setAttribute(state, 'EVP', float(row[7]))
        ce.setAttributeSource(state, 'EVP', 'OBJECT')
        
        ce.setAttribute(state, 'CSP', float(row[8]))
        ce.setAttributeSource(state, 'CSP', 'OBJECT')
        
        ce.setAttribute(state, 'GLP', float(row[9]))
        ce.setAttributeSource(state, 'GLP', 'OBJECT')
        
        ce.setAttribute(state, 'BDP', float(row[10]))
        ce.setAttributeSource(state, 'BDP', 'OBJECT')
        
        ce.setAttribute(state, 'PdA', float(row[11]))
        ce.setAttributeSource(state, 'PdA', 'OBJECT')
        
        ce.setAttribute(state, 'GPS', float(row[12]))
        ce.setAttributeSource(state, 'GPS', 'OBJECT')
        
        ce.setAttribute(state, 'Sol', float(row[13]))
        ce.setAttributeSource(state, 'Sol', 'OBJECT')
        
        ce.setAttribute(state, 'SD', float(row[14]))
        ce.setAttributeSource(state, 'SD', 'OBJECT')
        
        ce.setAttribute(state, 'EDU', float(row[15]))
        ce.setAttributeSource(state, 'EDU', 'OBJECT')
        
        ce.setAttribute(state, 'Lega', float(row[16]))
        ce.setAttributeSource(state, 'Lega', 'OBJECT')
        
        ce.setAttribute(state, 'MCR', float(row[17]))
        ce.setAttributeSource(state, 'MCR', 'OBJECT')
        
        ce.setAttribute(state, 'Uebrige', float(row[18]))
        ce.setAttributeSource(state, 'Uebrige', 'OBJECT')

