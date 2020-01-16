#!/usr/bin/python

import sys


class UtilitiesCustom():

    def __init__(self):
        pass

    def method_utilities_compare_all_success_failure(farg, *args):
        for arg in args:
            if isinstance(arg, list):
                for one_element in arg:
                    if 'failure' in str(one_element):
                        raise Exception(' **** Failure is observed in a particular step')
        print ('All steps executed successfully')
        return
