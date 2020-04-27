import os, sys
from csv import writer
import numpy as np
import multiprocessing

class GridSearch():
	def __init__(self, main_file, compile_func, args, num_process = 2):
		self.main_file = main_file
		self.compile_func = compile_func
		self.args = args
		self.num_process = num_process

	def call_main(self, args_list):
		for args in args_list:
			print('args', args)
			num1, num2 = args
			cmd = 'python {} --num1 {} --num2 {}'.format(self.main_file, num1, num2)
			print('cmd', cmd)
			result = os.system(cmd)
			print('result', result)
	def run(self):
		print('Get yourself a cup of coffee while I run grid search')
		
		num_configs = 1
		# -------- convert range args to list -------- #
		for param,val in self.args.items():
			if not (type(val) is dict or type(val) is list):
				raise ValueError('args should be a list or dictionary. Please refer to README')
			if type(val) is dict:
				low, high, num = val['min'], val['max'], val['num']
				l = list(np.linspace(low, high, num))
				self.args[param] = l
			num_configs *= len(self.args[param])

		# -------- get list of all configurations -------- #

		# -------- divide into equal parts -------- #
		process_list = []
		args_process = [[[2,3]],[[5,2]]]
		for i in range(self.num_process):
			x = multiprocessing.Process(target=self.call_main, args=(args_process[i],))
			x.start()
			process_list.append(x)
		for i in range(self.num_process):
			x.join()

# The following function is adapted from https://thispointer.com/python-how-to-append-a-new-row-to-an-existing-csv-file/
def insert_to_csv(file_name, data):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)