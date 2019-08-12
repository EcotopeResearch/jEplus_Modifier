# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 08:10:36 2019
@author: Scott
"""

## IMPORT PACKAGES
import pandas as pd

# READ FILES
read_file1=open('add_param.txt', 'r')
read_file2=open('add_idref.txt', 'r')
# OPEN WRITE FILES
write_file1=open('jEplusLines_1.txt','w')
write_file2=open('jEplusLines_2.txt','w')
write_file3=open('jEplusLines_3.txt','w')

# READ CSV INPUTS
inputs = pd.read_csv('inputs.csv')
lines1=read_file1.readlines()
lines2=read_file2.readlines()

## LOOP THROUGH TO WRITE FILES
for j in range(0,len(inputs)):
    for i in range(0,len(lines1)):
        line1=lines1[i].replace('(Number)',str(j+1))
        line1=line1.replace('(Name)',inputs['Name'][j])
        line1=line1.replace('(Description_String)','Description')
        line1=line1.replace('(search_tag)',inputs['search_tag'][j])
        #line1=(j*'  '+line1)
        
        write_file1.write(line1)
    
    for i in range(0,len(lines2)):
        line2=lines2[i].replace('(Number)',str(j+1))
        write_file2.write(line2)
        
    write_file3.write('       </object>\n')
    write_file3.write('       </void>\n')

## CLOSE WRITE FILES
write_file1.close()
write_file2.close()
write_file3.close()





