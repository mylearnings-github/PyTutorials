import csv

html_output = ''
names = []

''' This method is what people use mostly '''
def parse_csv_using_reader():
    with open('Experiment/mini_sample_names.csv','r') as csv_file:    
        csv_reader = csv.reader(csv_file)    

        for line in csv_reader: 
            if line[0] == 'first_name':
                continue
            elif line[0] == 'No Reward':
                break
            names.append(f'{line[0]} {line[1]}')

''' This is a better way which Corey Suggests '''
def parse_csv_using_dict_reader():
    with open('Experiment/mini_sample_names.csv','r') as name_file:
        field_names = ['first_name','last_name','company_name','address','city','county','state','zip','phone1','phone2','email','web']
        csv_reader = csv.DictReader(name_file,fieldnames=field_names)
        
        for line in csv_reader:
            if line['first_name'] == 'first_name':
                continue
            elif line['first_name'] == 'No Reward':
                break
            names.append(f"{line['first_name']} {line['last_name']}")
                


# parse_csv_using_reader()
parse_csv_using_dict_reader()

for name in names:
    print(name)

html_output += f'<p> There are currently {len(names)} public contributors. Thank you! </p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)

