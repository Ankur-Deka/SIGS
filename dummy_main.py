import sys
import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser('Parse dummy arguments')
	parser.add_argument('--num1', type=float, help='First number')
	parser.add_argument('--num2', type=float, help='Second number')
	args = parser.parse_args()
	print(args)

	# -------- This is where you'd do you calculation -------- #
	data = args.num1*args.num2

	# -------- You'd need to return data -------- #
	sys.exit(data)

