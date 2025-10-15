# Emerson McKay
# umid: 68460607
# email: emckayy@umich.edu
# collaborators: 


import csv

def read_csv_file(filename):
    fhand = open(filename)
    headers = fhand.readline().strip().split(",")
    data = []
    for line in fhand:
        values = line.strip().split(",")
        row_dict = dict(zip(headers, values))
        data.append(row_dict)
    fhand.close()
    return data

file_path = "C:/Users/emerm/OneDrive/Desktop/SI 201/fall25-project1-emersonmckay/crop_yield.csv"
data = read_csv_file(file_path)
print(data[:5])
