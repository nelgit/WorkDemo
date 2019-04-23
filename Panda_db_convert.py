import os, sys # for file path
import pandas as pd


path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

if not path in sys.path:
    sys.path.insert(1, path)
del path


def convert_to_pd_dataframe():

    import_dir = '/TestData/Copy_Formatted_Files/Test_formatted.csv'  # simple demo, not gonna go thru every file, just this test file

    # Define working directory
    working_dir = ''.join([os.getcwd(), import_dir])

    print(working_dir)

    created_db = pd.read_csv(working_dir, index_col=None, header=None)

    return created_db