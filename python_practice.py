import csv

def main():
    files = return_all_csv(".", ['mlp6'])
    write_data(files, file_type='csv')
    print("{} people used CamelCase for "
            "their team names".format(camel_case_count()))
    print("{} people used spaces in their "
            "team names".format(check_spaces_all_teamnames()))
    write_data(files, file_type='json')

####################
# VOID PROCEDURES  #
####################

def write_data(files, file_type):
    """
    files = [String]
    file_type = String

    Calls helper functions depending on file_type passed in
    csv = concatenates data from files into single csv file 
    json = creates a json file for each file in files array 
    """
    if file_type == 'json':
        write_json_files(files)

    elif file_type == 'csv':
        write_csv_file(files)

    else:
        print("Invalid file type passed in")

def write_json_files(files):
    """
    files = [String]

    Creates a json file for each file in files array
    """
    import json
    import csv
    fields = ("first_name", "last_name", "net_id", \
            "github_username", "team_name")

    for aFile in files:
        with open(aFile, 'r') as csv_file:
            dict_reader = csv.DictReader(csv_file, fields)
            for row in dict_reader:
                # check to make sure row has all appropriate data
                if len(row) != 5:
                    break
                net_id = row["net_id"].strip()
                json_file = open("./{}.json".format(net_id), 'w')
                json.dump(row, json_file)
                json_file.write('\n')
                json_file.close()


def write_csv_file(files):
    """
    files = [String]

    Concatenates data from files into single csv file
    """
    outfile = open("./everyone.csv",'w')
    for aFile in files:
        with open(aFile, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                # check to make sure row has all appropriate data
                if len(row) != 5:
                    break
                outfile.write(','.join(row))
                if row[-1][-1] != '\n':
                    outfile.write('\n')


#######################
# WORKHORSE FUNCTIONS #
#######################

def return_all_csv(filepath, exception=None):
    """
    filepath = String
    exception = String?

    Returns all csv files for a given file path
    Except for files specified in the optional 
    exception parameter 
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
    in everyone.csv file adhere to CamelCase 
    for their last entry
    """
    import csv
    counter = 0
    with open('./everyone.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            # check to make sure row has appropriate data
            if len(row) != 5:
                continue
            team_name = row[-1].strip()
            if contains_space(team_name):
                continue
            elif uses_camel_case(team_name):
                counter += 1
    return counter


def check_spaces_all_teamnames():
    """
    Counts how many of the files given
    in everyone.csv file used a space 
    in their team name
    """
    import csv
    counter = 0
    with open('./everyone.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            # check to make sure row has appropriate data
            if len(row) != 5:
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
    name = String

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
    name = String

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
