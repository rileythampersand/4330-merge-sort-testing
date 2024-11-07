import unittest
from time import perf_counter

# Python program for implementation of MergeSort

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]


def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	# create temp arrays
	L = [0] * (n1)
	R = [0] * (n2)

	# Copy data to temp arrays L[] and R[]
	for i in range(0, n1):
		L[i] = arr[l + i]

	for j in range(0, n2):
		R[j] = arr[m + 1 + j]

	# Merge the temp arrays back into arr[l..r]
	i = 0	 # Initial index of first subarray
	j = 0	 # Initial index of second subarray
	k = l	 # Initial index of merged subarray

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	# Copy the remaining elements of L[], if there
	# are any
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	# Copy the remaining elements of R[], if there
	# are any
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, l, r):
	if l < r:

		# Same as (l+r)//2, but avoids overflow for
		# large l and h
		m = l+(r-l)//2

		# Sort first and second halves
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)


# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is")
for i in range(n):
	print("%d" % arr[i],end=" ")

mergeSort(arr, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
	print("%d" % arr[i],end=" ")

print("\n")

# The merge sort code is contributed by Mohit Kumra

class TestMergeSort(unittest.TestCase):

	# Positive cases

	def test_positive0(self):
		arr = [5, 4, 3, 2, 1, 0]
		n = len(arr)
		mergeSort(arr,0,n-1)
		self.assertEqual(arr,[0,1,2,3,4,5])

	def test_positive1(self):
		arr = [3, 10, 83, 45, 103, 9, 71]
		n = len(arr)
		mergeSort(arr,0,n-1)
		self.assertEqual(arr,[3,9,10,45,71,83,103])

	# Negative Cases

	def test_invalid_type(self):
		with self.assertRaises(TypeError):
			arr = "this is a string"
			n = len(arr)
			mergeSort(arr,0,n-1)

	def test_invalid_index(self):
		with self.assertRaises(IndexError):
			arr = [2,5,7,4,3]
			n = len(arr)
			mergeSort(arr,0,n)

	# Performance Cases
	
	def test_large_array_benchmark(self):
		arr = [6, 56, 69, 15, 52, 86, 10, 68, 26, 96, 34, 8, 93, 99, 38, 50, 37, 3, 90, 84, 25, 75, 21, 60, 21, 13, 32, 92, 46, 94, 1, 73, 37, 73, 41, 74, 31, 79, 18, 74, 73, 35, 91, 70, 57, 86, 80, 79, 3, 63, 62, 79, 99, 79, 71, 30, 78, 58, 49, 18, 6, 72, 15, 7, 65, 70, 1, 10, 72, 22, 36, 21, 51, 7, 22, 33, 82, 46, 50, 23, 67, 94, 16, 73, 59, 84, 39, 89, 4, 34, 9, 48, 41, 33, 87, 27, 34, 20, 0, 14]
		n = len(arr)
		time_start = perf_counter()
		mergeSort(arr,0,n-1)
		time_duration = perf_counter() - time_start
		self.assertLess(time_duration, 0.01)

	def test_short_array_benchmark(self):
		arr = [3,2,1]
		n = len(arr)
		time_start = perf_counter()
		mergeSort(arr,0,n-1)
		time_duration = perf_counter() - time_start
		self.assertLess(time_duration, 0.0001)

	# Idempotency Cases

	def test_duplicate_sort_benchmark(self):
		arr = [6, 56, 69, 15, 52, 86, 10, 68, 26, 96, 34, 8, 93, 99, 38, 50, 37, 3, 90, 84, 25, 75, 21, 60, 21, 13, 32, 92, 46, 94, 1, 73, 37, 73, 41, 74, 31, 79, 18, 74, 73, 35, 91, 70, 57, 86, 80, 79, 3, 63, 62, 79, 99, 79, 71, 30, 78, 58, 49, 18, 6, 72, 15, 7, 65, 70, 1, 10, 72, 22, 36, 21, 51, 7, 22, 33, 82, 46, 50, 23, 67, 94, 16, 73, 59, 84, 39, 89, 4, 34, 9, 48, 41, 33, 87, 27, 34, 20, 0, 14]
		n = len(arr)
		arr1 = [6, 56, 69, 15, 52, 86, 10, 68, 26, 96, 34, 8, 93, 99, 38, 50, 37, 3, 90, 84, 25, 75, 21, 60, 21, 13, 32, 92, 46, 94, 1, 73, 37, 73, 41, 74, 31, 79, 18, 74, 73, 35, 91, 70, 57, 86, 80, 79, 3, 63, 62, 79, 99, 79, 71, 30, 78, 58, 49, 18, 6, 72, 15, 7, 65, 70, 1, 10, 72, 22, 36, 21, 51, 7, 22, 33, 82, 46, 50, 23, 67, 94, 16, 73, 59, 84, 39, 89, 4, 34, 9, 48, 41, 33, 87, 27, 34, 20, 0, 14]
		n1 = len(arr1)

		time_start = perf_counter()
		mergeSort(arr,0,n-1)
		time_duration = perf_counter() - time_start

		
		time_start = perf_counter() - time_duration
		mergeSort(arr1,0,n1-1)
		time_duration2 = perf_counter() - time_start

		self.assertEqual(arr,arr1)

		difference = time_duration2 - time_duration
		self.assertLessEqual(difference, 0.001)

	# Boundary Cases

	def test_duplicate_value(self):
		arr = [3,9,9,9,9,0]
		n = len(arr)
		mergeSort(arr,0,n-1)
		self.assertEqual(arr,[0,3,9,9,9,9])

	def test_duplicate_value1(self):
		arr = [0,0,0,0,0,0]
		n = len(arr)
		mergeSort(arr,0,n-1)
		self.assertEqual(arr,[0,0,0,0,0,0])

	def test_empty_array(self):
		arr = []
		n = len(arr)
		mergeSort(arr,0,n-1)
		self.assertEqual(arr,[])
	
	def test_single_element_array(self):
		arr = [0]
		n = len(arr)
		mergeSort(arr,0,n-1)
		self.assertEqual(arr,[0])


if __name__ == '__main__':
    unittest.main()


