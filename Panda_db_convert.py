import os, sys # for file path
import pandas as pd


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

    # adding in header columns that uniquely identify from text file associated with csv

    #created_df['ID_1']=
    #created_df['ID_2']=

    return created_df