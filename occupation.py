import csv
import random

occupation_dict = {}

# populates dictionary from csv file
def read_csv():
    with open('data/occupations.csv', 'rU') as f:
        reader = csv.reader(f, delimiter=",", quotechar='"')
        for row in reader:
            if row[0] == "Job Class": # skips the title row
                continue
            # The value of a key in the dictionary is a list
            # the 0th value of list is the percent
            # the 1st value of list is the link to the occupation
            occupation_dict[row[0]] = [float (row[1]), row[2]]
    return occupation_dict

# returns a random occupation weighted by percent
def ret_rand():
    keys = occupation_dict.keys() # returns a list of all keys in the dict
    rand = random.random() * occupation_dict['Total'][0]
    #print rand
    for key in keys:
        if key == "Total":
            continue
        rand -= occupation_dict[key][0]
        if rand <= 0:
            return key
    return 0;

# checks percent occurence from ret_rand() against percent in occupation_dict
def check_results():
    results = {}
    for key in occupation_dict.keys():
        results[key] = 0
    # tally up frequency of occurence of each occupation
    for i in range(1000):
        occ = ret_rand()
        results[occ] += 1
    # convert to percentage
    total = 0
    for key in results.keys():
        total += results[key]
        results[key] = results[key]/10.0
    results['Total']= total/10.0
    return results

if __name__ == '__main__':
    read_csv()
    print "Original dictionary:"
    print occupation_dict
    print "\nA random occupation:"
    print ret_rand()
    print "\nResults percent:"
    print check_results()
