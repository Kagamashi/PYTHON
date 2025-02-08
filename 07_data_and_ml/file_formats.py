''' CSV (Comma-Separated Values) : csv'''
# Reading CSV Files
import csv

with open('data.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Writing to CSV File
with open('output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 30, "New York"])
    writer.writerow(["Bob", 25, "Los Angeles"])



''' JSON (JavaScript Object Notation) : json '''
# Reading jSON Data
import json

with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)  # Output: Python dictionary

# Writing JSON Data
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

with open('output.json', 'w') as file:
    json.dump(data, file, indent=4)



''' XML (eXtensible Markup Language) : xml.etreee.ElementTree'''
# Reading XML Files
import xml.etree.ElementTree as ET

tree = ET.parse('data.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)

# Writing XML Files
import xml.etree.ElementTree as ET

root = ET.Element("data")
person = ET.SubElement(root, "person", name="Alice")
person.text = "30"

tree = ET.ElementTree(root)
tree.write("output.xml")
