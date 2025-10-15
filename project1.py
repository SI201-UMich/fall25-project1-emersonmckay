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
    # will return a dict with crop and avg yield for crop 
    totals = {}
    counts = {}
    
    for row in data:
        crop = row["Crop"]
        yield_value = float(row["Yield_tons_per_hectare"])
        totals[crop] = totals.get(crop, 0.0) + yield_value
        counts[crop] = counts.get(crop, 0) + 1

    averages = {}
    for crop in totals:
        averages[crop] = totals[crop] / counts[crop]
    return averages 


# ************ TEST CASES ************
class TestingAvgYieldByCrop(unittest.TestCase):
    def test_calculate_avg_yield_by_crop(self):
        data = [
            {"Crop": "Wheat", "Yield_tons_per_hectare": 5.0},
            {"Crop": "Wheat", "Yield_tons_per_hectare": 9.5},
            {"Crop": "Rice", "Yield_tons_per_hectare": 4.0}
        ]

        result = calculate_avg_yield_by_crop(data)
        self.assertEqual(result["Wheat"], 7.25)
        self.assertEqual(result["Rice"], 4.0)
    
    def test_single_row(self):
        data = [
            {"Crop": "Soybean", "Yield_tons_per_hectare": 2.0},
            {"Crop": "Cotton", "Yield_tons_per_hectare": 9.0}
        ]

        result = calculate_avg_yield_by_crop(data)
        self.assertEqual(result["Soybean"], 2.0)
        self.assertEqual(result["Cotton"], 9.0)

    def test_string_yields(self):
        data = [
            {"Crop": "Barley", "Yield_tons_per_hectare": "5.5"},
            {"Crop": "Barley", "Yield_tons_per_hectare": "6.5"}
        ]

        result = calculate_avg_yield_by_crop(data)
        self.assertEqual(result["Barley"], 6.0)

    
    def test_zeroes(self):
        data = [
            {"Crop": "Maize", "Yield_tons_per_hectare": 0.0},
            {"Crop": "Maize", "Yield_tons_per_hectare": 2.0},
        ]

        result = calculate_avg_yield_by_crop(data)
        self.assertEqual(result["Maize"], 1.0)

if __name__ == "__main__":
    unittest.main()
