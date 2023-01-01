## Project structure
- 'abntest' folder is the root path
- The solution 'part1.ipynb', 'part2.py', and 'part3.py' are in 'src' folder.
- The unit tests are in 'tests' folder
- The data source '.csv' files are in 'src/data' folder
- SQLite database 'src/abn.db' is used in the project. Two tables 'Survey' and 'CountryStartCodingAge' are in the database.
'CountryStartCodingAge' table is used in part2. It was populated with code in part1. 'Survey' table is used in part3. It 
was populated with a helper script 'src/load_survey.py'
- View 'TopLanguagesView' in DB is used for the results of part3. 

## Environment
- This project was developed with python version 3.8
- Run `pipenv install` from the root path to install all required packages.

## Part1
### Data source
The EU GDP data 'src/data/EU_GDP_2021.csv' is downloaded from the "The World Bank": https://databank.worldbank.org/reports.aspx?source=2&series=NY.GDP.MKTP.CD&country=EUU# 

To generate the .csv file, select parameters as below:
- Database:World Development Indicators
- Country:Region:Europe&Central Asia
- Series:GDP per capita (current US$)
- Time:2021

The survey data 'src/data/survey_results_public_2021.csv' is downloaded from https://insights.stackoverflow.com/survey  Year 2021
### Application
Run  `jupyter notebook` from root path and run notebook 'src/part1.ipynb'

**Conclusion**: There is No obvious trend between a country's GDP and its developers first start coding age.
This conclusion is based on the average 'Age1stCode' per country in the survey and the country's GDP, in year 2021.

Table 'CountryStartCodingAge' is created for part2. 
The minimum of 'Age1stCode' per country is stored in 'Age1stCodeYoungest' column 

## Part2
Run  `python part2.py` from 'src' folder. 

Send GET request to the endpoint: `curl http://127.0.0.1:8080/startcoding/<country_code>` 

For example: `curl http://127.0.0.1:8080/startcoding/NLD` will return response in
json format `[{"Country Name": "Netherlands", "Country Code": "NLD", "GDP": 57767.8788108173, "Age1stCodeYoungest": "Younger than 5 years"}]` 


Some suggestions to increase the scalability of the service:
- Cache the response. It can be either in memory or in DB 
- Add read-only mirror DB for 'Get' requests 
- Add relevant index, 'Country Code' for example. 
- Containerize the endpoints' logic as microservices and add a load balancer for the requests

## Part3
Run  `python part3.py` from 'src' folder. 

The program first decides the top 3 languages appearing in the 'LanguageHaveWorkedWith' column. After that it generates the pivot SQL query.  
The results can be checked in 'TopLanguagesView' in DB


## Run Tests
From root path:

- For Linux run `PYTHONPATH=$(pwd)/src/ python -m pytest tests`
- For Windows run `set PYTHONPATH=%cd%\src python -m pytest tests`
