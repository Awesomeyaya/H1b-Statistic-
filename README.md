# Insight Code Chanllenge

1. [Problem](README.md#problem)
2. [Approach](README.md#input-dataset)
3. [Run Instructions](README.md#instructions)

# Problem
Based on researching the immigration data, one should find the top 10 occupations and top 10 states which hold the most H1B (H-1B,H-1B1,E-3) visa each year. The code should be clean, modular and reusable for future. 

# Approach  

There are three features in this problem: 
case status, occupation name associated with the standard SOC code and worksite states. 

Step 1 : Based on the fact that the features of case status, occupation name and worksite states may vary in different years, I created three lists to store the possible value of these three features.

Step 2 : To read the data line by line, I used csv reader and store the name of columns in fields. In each line, I extracted the index in the fields of the features. When the case status is certified, I used dictionaries to store the occupation name and worksite state respectively. Also I counted the total number of certified cased after reading each line.

Step 3 : I used the sorted funtion and lambda expression to sort the dictionaries and picked the top 10 occupations and top 10 states. Then I calculated the percentage of each occupation of state of the total number of certified cases. At last, I wrote them to two txt files, which named top_10_occupations and top_10_states respectively.

# Run Instruction 
I used Python 3 to solve this problem. And I have tested it on H1b_FY_2014.csv, H1b_FY_2015.csv and H1b_FY_2016.csv. The results are correct. 
