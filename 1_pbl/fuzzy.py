import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


in_pos = float(input("position of car (1-10)"))
in_curve = float(input("curvature of road (1-10)"))

#define universes
pos = ctrl.Antecedent(np.arange(0,11,1), "Distance from left boundary")
curve = ctrl.Antecedent(np.arange(0,11,1), "Curvature")
correction = ctrl.Consequent(np.arange(0,11,1), "Correction")

#define fuzzy sets
pos['left']   = fuzz.trimf(pos.universe, [0,3,5])
pos['middle'] = fuzz.trimf(pos.universe, [3,5,7])
pos['right']  = fuzz.trimf(pos.universe, [5,7,10])

curve['left']  = fuzz.trimf(curve.universe, [0,3,5])
curve['none']  = fuzz.trimf(curve.universe, [3,5,7])
curve['right'] = fuzz.trimf(curve.universe, [5,7,10])

correction['left turn'] = fuzz.trimf(correction.universe, [0,2,5])
correction['drive straight'] = fuzz.trimf(correction.universe, [2,5,8])
correction['right turn'] = fuzz.trimf(correction.universe, [5,8,10])

pos['middle'].view()
input()
