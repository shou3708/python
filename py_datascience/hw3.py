#
# 在執行本程式之前，請務必在命令列執行 "pip install numpy"
# 以裝入 numpy 套件至 python 環境內
#

#**********************************************

# Name: 江偉綸

# Class: 資管系三年級

# SID: S06490047

# Program Name: hw3.py
 
# Function: 矩陣相乘的多執行速度比較

# Homework: No.3

# Limitations: (1).矩陣大小比較小，且電腦不同，無法看出多執行的速度優勢               

# Date: 2020/04/16

#**********************************************


# ==== 匯入需要的模組 ==== #

import multiprocessing as mp
import threading as td
import numpy as np
import time

# ==== 老師原程式 ==== #

def random_matrix(m, n, low, high):

    return np.random.randint(low, high, size = (m, n))

def create_two_matrices(dim_1, dim_2, low, high):

    A = random_matrix(dim_1, dim_2, low, high)

    B = random_matrix(dim_1, dim_2, low, high)

    print(f'Matrix A = \n {A} \n\nMatrix B = \n {B} \n')

    return (A, B)

def matrix_multiplication(A, B, result):

    start = time.perf_counter()

    '''
    #
    # 傳統寫法一：使用迴圈
    #
    # iterating by row of A 
    for i in range(len(A)): 
  
        # iterating by coloum by B  
        for j in range(len(B[0])): 
  
            # iterating by rows of B 
            for k in range(len(B)): 

                result[i][j] += A[i][k] * B[k][j]

    #print(result)   
    '''
    
    #
    # 傳統寫法二：使用Comprehension
    #
    result += [[sum(a*b for a,b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]

    #print(result)

    end = time.perf_counter()

    return (result, end - start)

# ==== 要執行的工作 ==== #

def job(A, B, result,q):
    
    start = time.perf_counter() #計算開始時間

    #使用Comprehension相乘

    result += [[sum(a*b for a,b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]

    end = time.perf_counter() #計算結束時間

    q.put(result) #將相乘後的結果加入Queue裡

    q.put((end-start)) #將經過時間加入Queue裡

    
    
# ==== 執行multithread區域 ==== #

def multithread(A, B, result):

    q = mp.Queue() #建立Queue來儲存結果和時間，因為老師上課說無法return，所以用這個

    p1 = td.Thread(target = job, args = (A, B, result,q)) #執行multithread方法

    #用老師上課說的套路
    
    p1.start()

    p1.join()

    res1 = q.get() #拿出結果

    time = q.get() #拿出時間

    print('\n======================================================')
    print("\n矩陣相乘的方法二：使用多執行緒方法\n")
    print(f'Result = \n{res1}\n\n所需時間{time:.3}秒...')
    print('\n======================================================')

# ==== 執行multicore區域 ==== #    
    
def multicore(A, B, result):

    q = mp.Queue() #同上

    p1 = mp.Process(target = job, args = (A, B, result,q)) #執行multicore方法

    #用老師上課說的套路
    
    p1.start()

    p1.join()

    res1 = q.get() #拿出結果

    time = q.get() #拿出時間

    print('\n======================================================')
    print("\n矩陣相乘的方法三：使用多程序處理方法\n")
    print(f'Result = \n{res1}\n\n所需時間{time:.3}秒...')
    print('\n======================================================')


# ==== 老師原程式 ==== #

if __name__ == '__main__':

    dim_1 = dim_2 = int(input('\n請輸入一個 n-by-n 正方矩陣的order n (1<n<8) : ')) 

    low = -10

    high = 30

    A, B = create_two_matrices(dim_1, dim_2, low, high)

    result = np.zeros((dim_1, dim_2), dtype = int)

    result2 = np.zeros((dim_1, dim_2), dtype = int)

    result3 = np.zeros((dim_1, dim_2), dtype = int)

    #print(f'Result = \n{result}')

    result1, elasped_time = matrix_multiplication(A, B, result)

    print('\n======================================================')
    print('\n矩陣相乘的方法一：使用傳統方法\n')
    print(f'Result = \n{result1}\n\n所需時間{elasped_time:.3}秒...')
    print('\n======================================================')

    multithread(A, B, result2) #在main加入要執行的函式

    multicore(A, B, result3) #在main加入要執行的函式

    input('\nPress enter key to exit...')
