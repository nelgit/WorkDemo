import os, sys # for file path
import pandas as pd # for creating pd dataframe
import re # for cleaning txt file data
import numpy as np # for handling missing data placeholder

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

if not path in sys.path:
    sys.path.insert(1, path)
del path


def convert_to_pd_dataframe():

    import_dir = '/TestData/Copy_Formatted_Files/'  # marks where the created files are stored
    csv_file='Test_formatted.csv'  # for simple demo purposes
    txt_file='Test_formatted_unmatched_columns.txt' # for simple demo purposes

    # Define working directory
    csv_file_part_of_df = ''.join([os.getcwd(), import_dir, csv_file])
    txt_file_part_of_df = ''.join([os.getcwd(), import_dir, txt_file])

    created_df = pd.read_csv(csv_file_part_of_df, index_col=None, header=None)

    # adding in header columns that uniquely identify from text file associated with csv, other other misc info

    # retrieve txt info
    with open(txt_file_part_of_df, 'r', newline='') as file_data:  # this is the read file
        listconversion = list(file_data)
        split_list = [elements.split(',') for elements in listconversion]  # split list into elements

        # iterate over each list element
        for elements in split_list:

            # do some data cleaning
            string_convert = str(elements)
            string_convert = re.sub(r'\[', '', string_convert)  # regex strip list marker left from string
            string_convert = re.sub(r'\]', '', string_convert)  # regex strip list marker right from string
            string_convert = re.sub(r'\\n', '', string_convert)  # regex strip newline from list
            string_convert = re.sub(r'\'', '', string_convert) # regex strip single '
            string_convert = string_convert.rstrip()  # remove right side end white spaces, or whatever pattern you put into strip function
            string_convert = string_convert.lstrip()  # remove left side lead  whitespaces or whatever pattern you put into strip function
            string_convert = re.sub(r'\,+$', '', string_convert)  # regex strip last misc coma

            # Create a new dynamic header and insert it into the existing dataframe, it can be anything, setting it to first element of list
            # in case, the format is header, listinfo1, listinfo2, listinfo3, etc.  Again this is just a demo.

            listconversion = string_convert.split(',')
            header = listconversion[0]

            if len(listconversion)==1: # set everything in the column uniformly if 1 element long
                created_df[header]=listconversion[0]

            elif 1: #  some arbitrary condition only for demo  # case txt file unmatching columns are meant to be single column data
                # use more complex logic to set to length and fill null if its a different format
                # combine unmatching lengths by throwing another dataframe into another dataframe

                #data = {header: listconversion[1:]} # skip slice [0] because that is the header value
                data = {header: [1,2,3,4,5,5]} # to illustrate example
                temp_df = pd.DataFrame(data) # create temp dataframe to house values

                created_df[header] = np.nan # create column to fill, default np.nan values (missing data)
                created_df = created_df.combine_first(temp_df) # combine both dataframe into single dataframe.
                                                           # Allows for creation of dataframe with mismatched column length
                                                           # if original data entry was messed up to begin with.
                                                           # This demo assumes messed up data was single column data not multi column
                                                           # data, which would require a different process

            else: # case unmatching columns are meant to be additional column data

    return created_df