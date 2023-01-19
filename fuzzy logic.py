!pip install scikit-fuzzy

import numpy as np import skfuzzy as fuzz
 
from skfuzzy import control as ctrl

quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

quality.automf(3) service.automf(3)

tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])

quality['average'].view() service.view() tip.view()

rule1 = ctrl.Rule(quality['poor'] & service['poor'], tip['low']) rule1.view()
rule2 = ctrl.Rule(quality['average'] & service['average'], tip['medium'
])
rule3 = ctrl.Rule(quality['good'] & service['good'], tip['high'])

tipping_ctrl = ctrl.ControlSystem({rule1, rule2, rule3}) tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

while True:
tipping.input['quality'] = float(input('How much would you like to give us out of 10 for the quality of food? '))
tipping.input['service'] = float(input('How much would you like to give us out of 10 for the service? '))
tipping.compute()
print(f"Your approximate tip will be: {tipping.output['tip']}") tip.view(sim=tipping)
break
