import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

### 1. Implement traditional matrix multiplication

def matrix_multiplication(A, B):
    C = np.zeros((len(A), len(B[0])))
    for n in range(len(A[0])):
        C += np.dot(np.atleast_2d(A[:,n]).T, np.atleast_2d(B[n:]))
    return C

### 2. Function to generate 2D matrix of a siz/dimension specified by variables

def generate_matrix(num_rows, num_cols):
    lowest_int_num = 10
    highest_int_num = 50
    num_of_nums_to_generate = 100

    X = np.random.randint(lowest_int_num, highest_int_num, num_of_nums_to_generate). reshape(num_rows, num_cols)
    return X

# Create a Pandas dataframe

COLS = ["Matrix size", "Run time"]

for matrix_size in range(10, 100, 10):
    A = generate_matrix(matrix_size, matrix_size)
    B = generate_matrix(matrix_size, matrix_size)
    MM_start_time = datetime.now()
    matrix_multiplication(A, B)
    MM_stop_time = datetime.now()
    MM_time = float((MM_stop_time - MM_start_time).total_seconds())


