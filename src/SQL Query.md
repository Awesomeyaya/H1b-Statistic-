Another way to deal with the given problem is to write SQL query.

The following query will be used in this order: 
select, count(*), where, group by, order by (DESC), limit num;

To get the top 10 occupations 

select CASE_STATUS, SOC_NAME, count(*) as CNT from H1B_test 
		where CASE_STATUS = 'CERTIFIED' 
		group by SOC_NAME 
		order by CNT DESC
		limit 10;

To get the top 10 states


select CASE_STATUS, WORKSITE_STATE, count(*) as CNTfrom H1B_test 
	where CASE_STATUS = 'CERTIFIED' 
	group by WORKSITE_STATE 
	order by CNT DESC
		limit 10


And one has to transfer the delimeter ';' to ',' and saved the raw data in a csvfile. 
Also, one has to create a new table in MySQL. The table should have the same fields as the csvfile. 
Then import the CSV file to the table in MySQL.

But the SQL query can not calculate the percentage.
