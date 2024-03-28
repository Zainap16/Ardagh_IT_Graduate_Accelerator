from Week_3.Day_3.car import Car
cr1 = Car("Toyota","Camry",2020)
print("Car Name: ", cr1.get_descriptive_name())
print(cr1.read_odoneter())
print(cr1.increment_odometer(10000))
# self refers to this specific instance of the class.

"""
cr1 is object
Here's a simplified analogy to illustrate the relationship between classes and objects:

Class: Blueprint for a house. It defines the structure, layout, and features that every house built from that blueprint will have.
Object (Instance): An actual house built from the blueprint. Each house (object) created from the blueprint (class) may have different colors, furniture arrangements, and occupants, but they all share the same basic structure and features defined by the blueprint.

static veriables are varibale inside a class that doesn't change. declare them as _variableName -- static variables can be changed.
"""