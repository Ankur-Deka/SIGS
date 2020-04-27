import os, sys
from csv import writer

class GridSearch():
	def __init__(self, main_file, compile_func, args):
		self.main_file = main_file
		self.compile_func = compile_func

# The following function is adapted from https://thispointer.com/python-how-to-append-a-new-row-to-an-existing-csv-file/
def insert_to_csv(file_name, data):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)