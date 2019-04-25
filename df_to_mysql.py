import Panda_df_convert as produced_df # to generated a panda df
import pandas as pd # for pandas method pd.read_sql()
from sqlalchemy import create_engine # to use create_engine and other engine methods
import mysql.connector # not used but included just in case


def convert_to_mysql():

    #define connection settings(assuming all permissions are set correctly on mysql server end)
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

    #Get a dataframe from csv convert to df file, panda_df_convert
    dataframe_to_convert = produced_df.convert_to_pd_dataframe()

    #Convert dataframe to sql
    dataframe_to_convert.to_sql(name='WorkDemo', con=engine, if_exists='replace', index=False)

    # Query server to show result of dataframe to mysql server push
    query = 'SELECT * FROM WorkDemo.WorkDemo;'
    #print(pd.read_sql(query, engine))
    sql_return = pd.read_sql(query, engine)

    # Close database connection when done
    connection.close()

    # Close out any remaining connections in memory by removing engine.
    engine.dispose()

    return sql_return