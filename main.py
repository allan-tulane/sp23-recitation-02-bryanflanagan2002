"""
CMPS 2200  Recitation 2
"""

import time
import tabulate


def simple_work_calc(n, a, b):
  if n == 1:
    return n
  else:
    return a * simple_work_calc(n / b, a, b) + n
	
def test_simple_work():
  assert simple_work_calc(10, 2, 2) == 36
  assert simple_work_calc(20, 3, 2) == 230 
  assert simple_work_calc(30, 4, 2) == 650
  assert simple_work_calc(40, 5, 2) == 5390
  assert simple_work_calc(17, 2, 3) == 31
  assert simple_work_calc(26, 6, 4) == 98

def work_calc(n, a, b, f):
  if n <= 1:
    return f(n)
  else:
    return a * work_calc(n / b, a, b, f) + f(n)


  
def span_calc(n, a, b, f):
  if n <= 1:
    return f(n)
  else:
    return a * span_calc(n / b, a, b, f) + 1
  
def test_work():
  assert work_calc(10, 2, 2,lambda n: 1) == 15
  assert work_calc(20, 1, 2, lambda n: n*n) == 530
  assert work_calc(30, 3, 2, lambda n: n) == 300
  #new tests
  assert work_calc(40, 3, 6,lambda n: 3) == 39
  assert work_calc(32, 3, 5, lambda n: 7) == 91
  assert work_calc(27, 7, 2, lambda n: n) == 3842
  

def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
  
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((n, work_fn1(n), work_fn2(n)))
	return result
  
def print_results(results):
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
  work_fn1 = lambda n: work_calc(n, 2, 3, lambda n: n)
  work_fn2 = lambda n: work_calc(n, 3, 2, lambda n: n)

  

  res = compare_work(work_fn1, work_fn2)
  print_results(res)

# def test_compare_span():
