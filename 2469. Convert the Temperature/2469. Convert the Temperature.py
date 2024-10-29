class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        List2 = []

        kelvin = celsius+273.15
        Fahrenheit = celsius * 1.80 + 32.00

        List2.append(kelvin)
        List2.append(Fahrenheit)

        return List2

# method=>2

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        

        kelvin = celsius+273.15
        Fahrenheit = celsius * 1.80 + 32.00

        

        return [kelvin,Fahrenheit]
