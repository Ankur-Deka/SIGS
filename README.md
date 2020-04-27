# Intro
This script will help you run grid search on any python script. 

# Dependencies
`threading`, `numpy`, `csv`

# File structure
Your code should include the following elements:
1. A main file which accepts arguments with argparse. Let's call is `main.py`.
1. The `main.py` can return a data, eg. accuracy, that you would like to compile across runs for different hyperparameter configuration. There is a file `dummy_main.py` that you can use for reference.
2. A function to compile the data returned by `main.py`, let's call it `compile_func`. This function should be able to take the data points iteratively. An simple function called is already provided and can be imported as `from grid_search import insert_to_csv`. If you don't wish to compile, this can be `None`.

# Instructions
I will walk you through a demo run as described in `dummy_run.py` to explain you the 3 steps for integrating SIGS with your code. Open the file and read the following description. You can use this file as a template. 

1. Import the library `from grid_search import GridSearch`
1. Create a function for compiling result. I am importing the `compile_csv` function from `grid_search`
1. Define arguments for running grid search:
	1. For every parameter you'd need one key containing it's name
	1. Each key can either be a list of all values of that parameter
	1. Or each key can be a dictionary with keys {'min', 'max', 'num'} if you wish to uniformly choose values in a range 
1. Create an object of `GridSearch`. `myGridSearch = GridSearch(main_file, compile_func, args)`
1. Run grid search with `myGridSearch.run()` 

