# -------- import GridSearch and define/import the compile function -------- #
from grid_search import GridSearch, insert_to_csv

# -------- main file to run and function to compile -------- #
main_file = 'dummy_main.py'
compile_func = insert_to_csv

# -------- define dictionary of arguments for grid search -------- #
args = {'num1': [2,5,6],
		'nums2': {'min':1, 'max':2, 'num': 5}}

# -------- create GridSearch object and run -------- #
myGridSearch = GridSearch(main_file, compile_func, args, num_process=2)
myGridSearch.run()