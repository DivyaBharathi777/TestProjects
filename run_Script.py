#!/usr/bin/python

import glob
from json2html import *
import sys
import os
from shutil import rmtree
from behave import __main__ as runner_with_options

if __name__ == '__main__':
    sys.stdout.flush()
    reporting_folder_name = 'report_folder'

    # remove if any reporting folder exists
    if os.path.exists(reporting_folder_name):
        rmtree(reporting_folder_name)
    os.makedirs(reporting_folder_name)

    # allure reporting command line arguments
    reporting_allure = ' -f allure_behave.formatter:AllureFormatter -o ' + reporting_folder_name + '  '

    # feature file path
    featureFilePath = ' feature_files_folder/Octopus_People.feature '

    # tag option
    tagOptions = ''
    tagOptions = ' --tags=tag_me '

    # command line argument to capture console output
    commonRunOptions = ' --no-capture --no-capture-stderr -f plain '

    # full list of command line options
    Run_Options = tagOptions + featureFilePath + reporting_allure + commonRunOptions

    # run Behave with Python code
    runner_with_options.main(Run_Options)

    # read result json file
    listOfJsonFiles = glob.glob(reporting_folder_name + "/*.json")
    finalJson = ''
    for cnt in range(0, len(listOfJsonFiles)):
        listOfJsonFiles[cnt] = ' {"' + "Scenario_" + str(cnt) + '"' + ' : ' + open(listOfJsonFiles[cnt], 'r').read() + '}'
        if cnt < (-1 + len(listOfJsonFiles)):
            listOfJsonFiles[cnt] = listOfJsonFiles[cnt] + ','
        finalJson = finalJson + listOfJsonFiles[cnt]
    finalJson = '[ ' + finalJson + ' ]'

    # convert json to html
    html_content = json2html.convert(json=finalJson)
    html_report_file = open(reporting_folder_name + '/' + 'index.html', 'w')
    html_report_file.write(html_content)
    html_report_file.close()
