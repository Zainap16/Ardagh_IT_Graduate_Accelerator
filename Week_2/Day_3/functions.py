# simple functions
def greet():
    print("Hi Player")
    
# parameters
def greeting_name(player_name):
    print(f"Hi {player_name}")

COVERAGE = 5
    
def calculate(height,width):
    cans  = (height * width) / COVERAGE
    return cans 

heights = float(input("Ënter height: "))  
widths = float(input("Ënter width: "))  
    
print(calculate(heights,widths))


