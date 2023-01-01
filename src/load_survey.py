import sqlite3
import pandas as pd
import os
import db_constants


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    df_survey = pd.read_csv(os.path.join(dir_path, 'data', 'survey_results_public_2021.csv'))

    # Dump csv file to the 'Survey' table in DB
    with sqlite3.connect(db_constants.DB_NAME, timeout=10) as conn:
        df_survey.to_sql(db_constants.SURVEY_TABLE, conn, if_exists='replace', index=False)
