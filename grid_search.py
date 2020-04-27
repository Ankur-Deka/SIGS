import os, sys
from csv import writer
import numpy as np

class GridSearch():
	def __init__(self, main_file, compile_func, args):
		self.main_file = main_file
		self.compile_func = compile_func
		self.args = args
	
	def run(self):
		print('Get yourself a cup of coffee while I run grid search')
		# -------- convert range args to list -------- #
		for param,val in self.args.items():
			if type(val) is dict:
				low, high, num = val['min'], val['max'], val['num']
				l = list(np.linspace(low, high, num))
				self.args[param] = l
		print(self.args)



# The following function is adapted from https://thispointer.com/python-how-to-append-a-new-row-to-an-existing-csv-file/
def insert_to_csv(file_name, data):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)