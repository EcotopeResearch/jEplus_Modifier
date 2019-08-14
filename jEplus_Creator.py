# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 08:10:36 2019
@author: Scott
"""

## IMPORT PACKAGES
import pandas as pd

# READ FILES
read_file1=open('insert1_start.jep', 'r')
read_file2=open('insert2_start.jep', 'r')
read_file3=open('insert4_start.jep', 'r')
lines1=read_file1.readlines()
lines2=read_file2.readlines()
lines4=read_file3.readlines()

# OPEN WRITE FILES
write_file1=open('insert1.jep','w')
write_file2=open('insert2.jep','w')
write_file3=open('insert3.jep','w')
write_file4=open('insert4.jep','w')

# READ CSV INPUTS
inputs = pd.read_csv('inputs.csv')

## CREATE FIRST VALUE

for i in range(0,len(lines1)):
    line1=lines1[i].replace('(Name)',inputs['Name'][0])
    line1=line1.replace('(Description_String)','Description')
    line1=line1.replace('(search_tag)',inputs['search_tag'][0])

    write_file1.write(line1)

## LOOP THROUGH TO WRITE FILES
for j in range(1,len(inputs)):
    for i in range(0,len(lines2)):
        line2=lines2[i].replace('(Number)',str(j))
        line2=line2.replace('(Name)',inputs['Name'][j])
        line2=line2.replace('(Description_String)','Description')
        line2=line2.replace('(search_tag)',inputs['search_tag'][j])
        #lines2=(j*'  '+line1)
        
        write_file2.write(line2)
    
    for i in range(0,len(lines4)):
        line4=lines4[i].replace('(Number)',str(j))
        write_file4.write(line4)
        
    write_file3.write('       </object>\n')
    write_file3.write('       </void>\n')

## CLOSE WRITE FILES
write_file1.close()
write_file2.close()
write_file3.close()





