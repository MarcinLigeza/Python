import json
import sys

fileName = (str(sys.argv[1]))

text = open(fileName).read()
jsonData = json.loads(text)

print (str(sys.argv[1]))

array = jsonData['input_list']

print ('Unsorted array: ' )
print (array)

for i in range(len(array)-1):
	for i in range(i):
		if array[i] > array[i+1]:
			temp = array[i]
			array[i] = array[i+1]
			array[i+1] = temp
			
print ('\nSorted array:')
print (array)
