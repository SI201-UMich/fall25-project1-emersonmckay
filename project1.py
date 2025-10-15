# Emerson McKay
# umid: 68460607
# email: emckayy@umich.edu
# collaborators: 


import csv
import unittest

def read_csv_file(filename):
    fhand = open(filename)
    headers = fhand.readline().strip().split(",")
    data = []
    for line in fhand:
        values = line.strip().split(",")
        row_dict = dict(zip(headers, values))

        if "Yield_tons_per_hectare" in row_dict:
            try:
                row_dict["Yield_tons_per_hectare"] = float(row_dict["Yield_tons_per_hectare"])
            except:
                row_dict["Yield_tons_per_hectare"] = None
        data.append(row_dict)

    return data

file_path = "C:/Users/emerm/OneDrive/Desktop/SI 201/fall25-project1-emersonmckay/crop_yield.csv"
data = read_csv_file(file_path)

def calculate_avg_yield_by_crop(data):
    print("placeholder")


# ************ TEST CASES ************
class TestingCalculation(unittest.Testcase):
    def test_calculate_avg_yield_by_crop(self):
        data = [
            {"Crop": "Wheat", "Yield_tons_per_hectare": 5.0},
            {"Crop": "Wheat", "Yield_tons_per_hectare": 9.5},
            {"Crop": "Ricet", "Yield_tons_per_hectare": 4.0},
        ]

        result = calculate_avg_yield_by_crop(data)
        self.assertEqual(result["Wheat"], 7.25)
        self.assertEqual(result["Rice"], 4.0)
    