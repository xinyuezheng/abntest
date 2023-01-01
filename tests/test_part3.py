import pytest
import pandas as pd
import os
from src import part3

@pytest.fixture
def df_survey():
    survey_csv = os.path.join('src', 'data', 'survey_results_public_2021.csv')
    df_survey = pd.read_csv(survey_csv)

    return df_survey[['Country', 'Age1stCode', 'LanguageHaveWorkedWith']].head(10)


def test_get_top_languages(df_survey):
    language_list = part3.get_top_languages(df_survey, 3)

    expected = ['JavaScript', 'HTML/CSS', 'Python']
    difference = set(language_list) ^ set(expected)

    assert not difference


def test_create_sql_view(df_survey):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, 'top_languages_view.sql',), 'w') as filetowrite:
        filetowrite.write(part3.create_sql_view(df_survey))