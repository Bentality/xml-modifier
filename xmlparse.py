import sys
import xml.etree.ElementTree as ET

fileName = sys.argv[1]                        # read file name first argument
itemToChange = sys.argv[2]                    # item to modify the price
percentChange = (float(sys.argv[3]) * .01)    # percent to change price

# check to see if the percent to change is valid
while True: 
    if percentChange < -.90 or percentChange > 1:
        percentChange = float(input("Please enter a number between -90 and 100: "))
    break

tree = ET.parse(fileName)
root = tree.getroot()

# loop to find the name of the plant and then update the price of said plant
for plant in root.findall("PLANT"):
    if (plant.find("COMMON").text == itemToChange):
        plantPrice = float(plant.find("PRICE").text)
        plantPrice *= (1 + percentChange)
        plant.find("PRICE").text = str(plantPrice)

tree.write("plant_catalog.xml")