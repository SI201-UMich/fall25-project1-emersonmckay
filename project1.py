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
    count = {}
    
    for row in data:
        crop = row["Crop"]
        yield_value = float(row["Yield_tons_per_hectare"])
        totals[crop] = totals.get(crop, 0.0) + yield_value
        count[crop] = count.get(crop, 0) + 1

    averages = {}
    for crop in totals:
        averages[crop] = totals[crop] / count[crop]
    return averages 

def calculate_avg_yield_by_fertilizer(data):
    # will return a nested dict of crop, and then fertilizer value with avg yield
    totals = {}
    count = {}

    for row in data:
        crop = row["Crop"]
        fert = row["Fertilizer_Used"]
        yield_value = float(row["Yield_tons_per_hectare"])

        if crop not in totals:
            totals[crop], count[crop] = {}, {}
        totals[crop][fert] = totals[crop].get(fert, 0.0) + yield_value
        count[crop][fert] = count[crop].get(fert, 0) + 1

    averages = {}
        
    for crop in totals:
        averages[crop] = {}
        for fert in totals[crop]:
            averages[crop][fert] = totals[crop][fert] / count[crop][fert]
    return averages


# ************ TEST CASES ************
class TestingAvgYieldByCrop(unittest.TestCase):
    # general test to make sure function is working the way it should
    def test_calculate_avg_yield_by_crop(self):
        data = [
            {"Crop": "Wheat", "Yield_tons_per_hectare": 5.0},
            {"Crop": "Wheat", "Yield_tons_per_hectare": 9.5},
            {"Crop": "Rice", "Yield_tons_per_hectare": 4.0}
        ]

        result = calculate_avg_yield_by_crop(data)
        self.assertEqual(result["Wheat"], 7.25)
        self.assertEqual(result["Rice"], 4.0)
    
    # testing with just a single row 
    def test_single_row(self):
        data = [
            {"Crop": "Soybean", "Yield_tons_per_hectare": 2.0},
            {"Crop": "Cotton", "Yield_tons_per_hectare": 9.0}
        ]

        result = calculate_avg_yield_by_crop(data)
        self.assertEqual(result["Soybean"], 2.0)
        self.assertEqual(result["Cotton"], 9.0)

    # testing strings to see if they convert 
    def test_string_yields(self):
        data = [
            {"Crop": "Barley", "Yield_tons_per_hectare": "5.5"},
            {"Crop": "Barley", "Yield_tons_per_hectare": "6.5"}
        ]

        result = calculate_avg_yield_by_crop(data)
        self.assertEqual(result["Barley"], 6.0)

    # making sure the function still works with 0s 
    def test_zeroes(self):
        data = [
            {"Crop": "Maize", "Yield_tons_per_hectare": 0.0},
            {"Crop": "Maize", "Yield_tons_per_hectare": 2.0},
        ]

        result = calculate_avg_yield_by_crop(data)
        self.assertEqual(result["Maize"], 1.0)

class TestingYieldByFertilizer(unittest.TestCase):
    # general test to see if function is doing what it should
    def test_calculate_avg_yield_by_fertilizer(self):
        data = [
            {"Crop": "Wheat", "Fertilizer_Used": "True", "Yield_tons_per_hectare": 5.5},
            {"Crop": "Wheat", "Fertilizer_Used": "True", "Yield_tons_per_hectare": 8.0},
            {"Crop": "Wheat", "Fertilizer_Used": "False", "Yield_tons_per_hectare": 2.5},
            {"Crop": "Rice", "Fertilizer_Used": "False", "Yield_tons_per_hectare": 3.0},
            {"Crop": "Rice", "Fertilizer_Used": "False", "Yield_tons_per_hectare": 6.0},
        ]

        result = calculate_avg_yield_by_fertilizer(data)
        self.assertAlmostEqual(result["Wheat"]["True"], 6.75, places=9)
        self.assertAlmostEqual(result["Wheat"]["False"], 2.5, places=9)
        self.assertAlmostEqual(result["Rice"]["False"], 4.5, places=9)

    # making sure things are being converted to strings
    def test_strings(self):
        data = [
            {"Crop": "Wheat", "Fertilizer_Used": "True", "Yield_tons_per_hectare": "5.5"},
            {"Crop": "Wheat", "Fertilizer_Used": "True", "Yield_tons_per_hectare": "8.0"},
            {"Crop": "Wheat", "Fertilizer_Used": "False", "Yield_tons_per_hectare": "2.5"},
            {"Crop": "Rice", "Fertilizer_Used": "False", "Yield_tons_per_hectare": "3.0"},
            {"Crop": "Rice", "Fertilizer_Used": "False", "Yield_tons_per_hectare": "6.0"},
        ]

        result = calculate_avg_yield_by_fertilizer(data)
        self.assertAlmostEqual(result["Wheat"]["True"], 6.75, places=9)
        self.assertAlmostEqual(result["Wheat"]["False"], 2.5, places=9)
        self.assertAlmostEqual(result["Rice"]["False"], 4.5, places=9)

    # making sure everything works even with 0s 
    def test_zeros(self):
        data = [
        {"Crop": "Wheat", "Fertilizer_Used": "True", "Yield_tons_per_hectare": 0},
        {"Crop": "Wheat", "Fertilizer_Used": "True", "Yield_tons_per_hectare": 10},
        {"Crop": "Wheat", "Fertilizer_Used": "False", "Yield_tons_per_hectare": 6},
        {"Crop": "Rice", "Fertilizer_Used": "False", "Yield_tons_per_hectare": 0},
        {"Crop": "Rice", "Fertilizer_Used": "False", "Yield_tons_per_hectare": 4},
        ]

        result = calculate_avg_yield_by_fertilizer(data)
        self.assertAlmostEqual(result["Wheat"]["True"], 5, places=9)
        self.assertAlmostEqual(result["Wheat"]["False"], 6, places=9)
        self.assertAlmostEqual(result["Rice"]["False"], 2, places=9)

    # checking to see if function worked correctly with nested dicts and creating keys 
    def test_nesting(self):
        data = [
            {"Crop": "Barley", "Fertilizer_Used": "True", "Yield_tons_per_hectare": 7.0},
            {"Crop": "Barley", "Fertilizer_Used": "True", "Yield_tons_per_hectare": 9.0},
        ]

        result = calculate_avg_yield_by_fertilizer(data)
        self.assertIn("Barley", result)
        self.assertIn("True", result["Barley"])
        self.assertAlmostEqual(result["Barley"]["True"], 8.0, places=9)
        self.assertNotIn("False", result["Barley"])

if __name__ == "__main__":

    unittest.main()
