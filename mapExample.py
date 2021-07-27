from HashMap import HashMap
import time


arr = [[0]*2 for i in range(4)]

arr[0][0] = '32787.53270551'
arr[0][1] = '20210713'
arr[1][0] = '32809.44997193'
arr[1][1] = '20210714'
arr[2][0] = '31889.78060343'
arr[2][1] = '20210715'
arr[3][0] = '31889.78060343'
arr[3][1] = '20210716'

m = HashMap()


for i in range(4):
	m.insert(arr[i][0], arr[i][1])



print(m.find(arr[3][0]))
print("Avg: ", m.findAvg())
print("Min: ", m.findMin())
print("Max: ", m.findMax())



time.sleep(30)