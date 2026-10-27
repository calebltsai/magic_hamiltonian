import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import sympy as sym
import time


# MAIN
# envelop in a main to protect running code from being called inadvertently
if __name__ == "__main__":
	# incorporate timer to see runtime, room for optimizing and improvement through data structures and algorithms used
	start_time = time.perf_counter()
	# main simulations, isolated functions

	
	end_time = time.perf_counter()
	elapsed_time = end_time - start_time
	# print time elapsed in console when finished (in fp6)
	print(f"\nExecution time: {elapsed_time:.6f} seconds")