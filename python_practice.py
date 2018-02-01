import csv

def main():
    files = return_all_csv(".", ['mlp6'])
    write_data(files, file_type='csv')
    print("{} people used camel case for their team names".format(camel_case_count()))
    print("{} people used spaces in their team names".format(check_spaces_all_teamnames()))
    write_data(files, file_type='json')

####################
# VOID PROCEDURES  #
####################

def write_data(files, file_type):
    """
    Concatenates data from files into single file
    Calls helper functions depending on file_type passed in
    """
    if file_type == 'json':
        write_json_file(files)

    elif file_type == 'csv':
        write_csv_file(files)

def write_json_file(files):
    """
    Concatenates all files given into a single 
    json file 
    """
    import json
    import csv
    fields = ("first_name", "last_name", "net_id", "github_username", "team_name")

    for aFile in files:
        with open(aFile, 'r') as csv_file:
            dict_reader = csv.DictReader(csv_file, fields)
            for row in dict_reader:
                # make sure all data is present
                if len(row) < 5:
                    break
                net_id = row["net_id"].strip()
                json_file = open("./{}.json".format(net_id), 'w')
                json.dump(row, json_file)
                json_file.write('\n')
                json_file.close()


def write_csv_file(files):
    """
    Concatenates all files given into a single 
    csv file with entries from each file separated 
    by a newline
    """
    outfile = open("./everyone.csv",'w')
    for aFile in files:
        with open(aFile, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                outfile.write(','.join(row))
                outfile.write('\n')


#######################
# WORKHORSE FUNCTIONS #
#######################

def return_all_csv(filepath, exception=None):
    """
    Returns all csv files for a given file path
    Except for files specified in the optional 
    exception parameter (pass in [String])
    """
    import glob as glob
    all_csv = glob.glob('{}/*.csv'.format(filepath))
    if exception != None:
        for ex in exception:
            formatted = "{}/{}.csv".format(filepath, ex)
            all_csv.remove(formatted)
    return all_csv


def camel_case_count():
    """
    Counts how many of the files given
    adhere to CamelCase for their last entry
    (using the everyone.csv file)
    """
    import csv
    counter = 0
    with open('./everyone.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            # check to make sure row has all relevant data
            if len(row) < 5:
                continue
            team_name = row[-1].strip()
            if contains_space(team_name):
                print("{} used a space in their team name!\n".format(row[0]))
            elif uses_camel_case(team_name):
                counter += 1
    return counter


def check_spaces_all_teamnames():
    """
    Counts how many of the files given
    used a space in their team name
    (using the everyone.csv file)
    """
    import csv
    counter = 0
    with open('./everyone.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            # check to make sure row has all relevant data
            if len(row) < 5:
                continue
            team_name = row[-1].strip()
            if contains_space(team_name):
                counter += 1
    return counter

####################
# HELPER FUNCTIONS #
####################

def uses_camel_case(name):
    """
    Takes in string
    Returns True if name contains at least 1 uppercase
    and 1 lowercase value, and only letters are present
    Returns False otherwise
    """
    if name == name.upper() or name == name.lower():
        return False
    for letter in name:
        if not letter.isalpha():
            return False
    return True

def contains_space(name):
    """
    Takes in string
    Returns True if the string contains a space
    Returns False otherwise
    """
    for character in name:
        if character == ' ':
            return True 
    return False


###############################
## END OF FUNCTIONAL SECTION ##
###############################

if __name__ == "__main__":
    main()
