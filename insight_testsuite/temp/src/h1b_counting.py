import csv
import sys

csvfile = sys.argv[1]
output_occupation = sys.argv[2]
output_state = sys.argv[3]

sep = ';'

STATUS = ['CASE_STATUS','STATUS','Approval_Status']
JOB = ['SOC_NAME','LCA_CASE_SOC_NAME','Occupational_Title']
STATES = ['WORKSITE_STATE','LCA_CASE_WORKLOC1_STATE','State_1']
    
'''
Define a function to find the certified case line by line.
Define maps to store the value of occupations and status. 
Count the total number certified cases.
''' 
def ReadFile(csvfile,sep,STATUS,JOB,STATES):
    job_dir = {}
    state_dir = {}
    count = 0
    
    with open(csvfile,'r') as file:
        reader = csv.reader(file,delimiter = sep)
        fields = next(reader)
        
        for case in STATUS: 
            for field in fields:
                if case == field: 
                    status_index = fields.index(field)
        for name in JOB:
            for field in fields:
                if name == field:
                    job_index = fields.index(field)
                    
        for state in STATES:
            for field in fields:
                if state == field:
                    state_index = fields.index(field)
            
        for line in reader:
            status = line[status_index]
            job = line[job_index]
            state = line[state_index]
        
            if status == 'CERTIFIED':
                if job not in job_dir:
                    job_dir[job] = 1
                else:
                    job_dir[job] += 1 
            
                if state not in state_dir:
                    state_dir[state] = 1 
                else: 
                    state_dir[state] += 1
                
                count += 1 
                
    return job_dir,state_dir,count
'''
Define a function to sort the Top 10 occupations and Top 10 states
'''
def Sorting(num):
    k = num
    job_dir,state_dir,count = ReadFile(csvfile,sep,STATUS,JOB,STATES)
    
    sorted_dir = sorted(job_dir.items(),key = lambda w: -w[1])[:k]
    sorted_state = sorted(state_dir.items(),key = lambda w: -w[1])[:k]
    return sorted_dir,sorted_state 
    
filename1 = output_occupation
filename2 = output_state

num = 10
result = []
job_sorted, state_sorted = Sorting(num)
job_dir, state_dir, count = ReadFile(csvfile,sep,STATUS,JOB,STATES)


with open(filename1,'w') as file:
    file.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE' + '\n')
    for item in job_sorted:
        result = item[0] + sep + str(item[1]) + sep + str("{:.1f}".format(item[1]*100/count)+"%")
        file.write(result + '\n')

with open(filename2,'w') as file:
    file.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE' + '\n')
    for item in state_sorted:
        result = item[0] + sep + str(item[1]) + sep + str("{:.1f}".format(item[1]*100/count)+"%")
        file.write(result + '\n')
