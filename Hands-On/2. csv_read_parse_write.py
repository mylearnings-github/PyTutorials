import csv

# Standard Way of Reading CSVs

""" Copy csv file contents by specifying a new delimiter (like tab) """

with open('../Experiment/sample.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('../Experiment/delimited_sample.csv', 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)

""" Read csv file by specifying the delimiter we used in prev. steps """

with open('../Experiment/delimited_sample.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')

    for line in csv_reader:
        print(line)


# Corey's Preference is to use a Dictionary R/W'er

""" Alternative way of reading csv files """

# Dictionary Reader
with open('../Experiment/sample.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line)
        #print(line['Name'])

# Dictionary Writer

with open('../Experiment/sample.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('../Experiment/dict_rw_sample.csv', 'w', newline='') as new_file:
        field_names = ['Name','Team','Height(inches)','Weight(lbs)','Age']

        csv_writer = csv.DictWriter(new_file, fieldnames=field_names, delimiter='/')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['Position']
            csv_writer.writerow(line)