#!/usr/bin/env python3
import os
import pandas as pd
import glob

directory = "logger" # the directory that contains all the logs file
output = "logger_output"
txt_files = os.path.join(directory, '*.log')
extension="csv"
columnsName = "" # column names of your logs, example: ["col1","col2" ...]

for txt_file in glob.glob(txt_files):

    in_txt = pd.read_csv(txt_file, names=columnsName, skiprows=1, delimiter=',')
    df = pd.DataFrame(in_txt,columns=columnsName)
    filename = os.path.splitext(os.path.basename(txt_file))[0] + '.csv'
    filename = os.path.join(output, filename)
    df.to_csv(filename, index=False)


# combining all of the transformed csv to one csv.
all_files=[i for i in glob.glob("logger_output/*.{}".format(extension))]
df=pd.concat([pd.read_csv(file) for file in all_files])
df.to_csv("combined_log.csv",index=False)


