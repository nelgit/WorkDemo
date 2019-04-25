import pandas as pd
from sqlalchemy import create_engine
import os, sys # for file path
import mysql.connector # not used but included just in case
import fnmatch as wildcardhandler # to remove files in copy directory

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

if not path in sys.path:
    sys.path.insert(1, path)
del path

def convert_mysql_to_csv():

    DataDirectory = '/TestData'  # )  recycled file path of test results

    working_dir = ''.join([os.getcwd(), DataDirectory, '/']) # )  recycled file path of test results

    write_directory = ''.join([working_dir, 'Mysql_Generated_CSV_Files', '/']) #directory to hold mysql to CSV files

    # define connection settings(assuming all permissions are set correctly on mysql server end)
    conString = 'mysql+mysqlconnector://{user}:{passwd}@{host}:{port}/{db}'.format(
        user='WorkDemo',
        passwd='WorkDemo123',
        host='localhost',
        port='3306',
        db='WorkDemo'
    )

    # create engine for managing database conenctions
    engine = create_engine(conString)

    # Open database connection
    connection = engine.connect()

    # Query server to show result of dataframe to mysql server push
    query = 'SELECT * FROM WorkDemo.WorkDemo;'
    sql_return = pd.read_sql(query, engine)


    # Make files in new directory, Remove and remake files if already there

    exist_dircheck = os.path.isdir(write_directory) # recycled directory making logic
    exist_filecheck = os.path.isfile(
        wildcardhandler.fnmatch(''.join([write_directory, 'csv_made_from_mysql.csv']), '*'))  # added wildcard for multi types
    filecheck_path = ''.join([write_directory, 'csv_made_from_mysql.csv'])

    if exist_dircheck:
        if exist_filecheck:

            try:
                os.remove(wildcardhandler.fnmatch(filecheck_path, '*'))  # remove dupes if any
            except:
                pass
    else:
        os.mkdir(write_directory)

    #Export to CSV to new directory
    sql_return.to_csv(''.join([write_directory, 'csv_made_from_mysql.csv']), index =False, header=False)


    # Close database connection when done
    connection.close()

    # Close out any remaining connections in memory by removing engine.
    engine.dispose()

    return