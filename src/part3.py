import pandas as pd
import os
from collections import Counter


def sql_sum_case(language):
    return f"SUM(CASE WHEN LanguageHaveWorkedWith REGEXP '\\b{language}\\b' THEN 1 END) as '{language}'"


def get_top_languages(df_survey, n):
    # Split semicolon separated strings in 'LanguageHaveWorkedWith' column to a list.
    # Flatten a 2-D matrix to collect all languages into a list
    language_list = [val.strip() for sublist in df_survey.LanguageHaveWorkedWith.dropna().str.split(";").tolist() for
                     val in sublist]

    # Get the most frequent used languages
    top_language_list = [language_tuple[0] for language_tuple in Counter(language_list).most_common(n)]

    return top_language_list


def create_sql_view(df_survey):
    top_language_list = get_top_languages(df_survey, 3)
    # For each language generates a SQL 'SUM' case, concatenate each case with ','
    sql_all_cases = ','.join(list(map(sql_sum_case, top_language_list)))

    sql_query = f'SELECT Country, {sql_all_cases} FROM survey GROUP BY Country;'

    # Create view for the pivot query
    return 'CREATE VIEW TopLanguagesView AS ' + sql_query


if __name__ == '__main__':
    survey_csv = os.path.join('data', 'survey_results_public_2021.csv')
    df_survey = pd.read_csv(survey_csv)
    top_languages_view = create_sql_view(df_survey)
    print(top_languages_view)




