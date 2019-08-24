# module get_data
# Examples of how we might get data for templates
#import csv

#def get_growth_table():
#    growth_table = {}
#    with open('state_populations.csv','r') as f:
#        reader = csv.DictReader(f)
#        for row in reader:
#            row = dict(row)
#            code = row["Code"]
#            y2010 = float(row["2010"].replace(",",""))
#            y2018 = float(row["2018"].replace(",",""))
#            growth = y2018 - y2010
#            growth_ratio = growth / y2010
#            growth_pct = int(growth_ratio * 100 + 0.5)
#            growth_table[code] = growth_pct
#    f.close()
#    return(growth_table)

#def get_pop_table():
#    pop_table = {}
#    with open('state_populations.csv','r') as f:
#        reader = csv.DictReader(f)
#        for row in reader:
#            row = dict(row)
#            code = row["Code"]
#            y2018 = int(row["2018"].replace(",",""))
#            pop_table[code] = y2018
#    return(pop_table)