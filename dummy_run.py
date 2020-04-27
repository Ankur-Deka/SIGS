from grid_search import GridSearch, compile_csv

# from compile_csv import insert_to_csv
main_file = 'dummy_main.py'
compile_func = insert_to_csv

myGridSearch = GridSearch(main_file, compile_func)
