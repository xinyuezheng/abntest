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
The EU GDP data 'src/data/EU_GDP_2021.csv' is downloaded from the "The World Bank": https://databank.worldbank.org/reports.aspx?source=2&series=NY.GDP.MKTP.CD&country=EUU# 

To generate the .csv file, select parameters as below:
- Database:World Development Indicators
- Country:Region:Europe&Central Asia
- Series:GDP per capita (current US$)
- Time:2021

The survey data 'src/data/survey_results_public_2021.csv' is downloaded from https://insights.stackoverflow.com/survey  Year 2021

Run  `jupyter notebook` from root path and open notebook 'src/part1.ipynb'

**Conclusion**: There is No obvious trend between a country's GDP and its developers first start coding age.
This conclusion is based on the average 'Age1stCode' per country in the survey and the country's GDP, in year 2021.

Table 'CountryStartCodingAge' is created for part2. 
The minimum of 'Age1stCode' per country is stored in 'Age1stCodeYoungest' column 

## Part2
Return the 'Country' and its 'Age1stCodeYoungest' in 'CountryStartCodingAge' table as response

Some suggestions to increase the scalability of the service:
- Cache the response. It can be either in memory or in DB 
- Add read-only mirror DB for 'Get' requests 
- Add relevant index, 'Country Code' for example. 
- Containerize the endpoints' logic as microservices and add a load balancer for the requests

## Part3
- Decide the top 3 languages appearing in the 'LanguageHaveWorkedWith' column.
- Generate pivot SQL query to create the view 'TopLanguagesView'


## Run Tests
- Go to the root folder and run `python -m pytest tests`
