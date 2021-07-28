#
#
#
#simple hash table
#
#m = HashMap() 			#init
#m.insert(key, value) 	#insert key and value. duplicate keys allowed
#m.find(key) 			#returns a list of values matching key
#m.findMin()			#returns min
#m.findMax()			#returns max
#m.findAvg()			#returns avg of all keys
#
#
#
class HashMap:
	def __init__(self): #init class with default size and map full of none
		self.mapSize = 512 #default map size
		self.maxSize = 384 #defealt threshold before resize
		self.threshold = 0.75
		self.count = 0 #number of pairs in map
		self.map = [None] * self.mapSize
		
	def getHash(self, key): #returns the hash for a given key using the below algorithm
		hash = 0
		temp = int(str(key)[-3:]) % self.mapSize #hasm = (last 3 digits) % size of map
		return temp
		
	def insert(self, key, value): #insert a key with its corresponding value
		keyIndex = self.getHash(key)
		keyValue = [key, value]
		
		if self.map[keyIndex] == None: #if the index of the hash value is empty
			self.map[keyIndex] = list([keyValue])
			self.count = self.count + 1
		else:		
			self.map[keyIndex].append(keyValue)
			self.count = self.count + 1
			
		if self.count >= self.maxSize:
			self.resize()
	
	def find(self, key): #returns value for inputed key
		values = []
		keyIndex = self.getHash(key)
		
		for itr in self.map[keyIndex]:
		    if itr[0] == key:
		        values.append(itr[1])
		
		return values
		
	def findMin(self): #returns the min key
		i = 0
		min = -1
		while i != self.mapSize: #go through every index in hash table
			if self.map[i] != None: #skip indexes with nothing in them
				for itr in self.map[i]: #iterate through the list found at that index
					if min == -1: #make first value found equal to min
						min = itr[0]
					elif min > itr[0]:
						min = itr[0]
			i = i+1
		
		return min
		
	def findMax(self): #returns the max key, similar code to findMin
		i = 0
		max = -1
		while i != self.mapSize: 
			if self.map[i] != None: 
				for itr in self.map[i]: 
					if max == -1: 
						max = itr[0]
					elif max < itr[0]:
						max = itr[0]
			i = i+1
		
		return max
		
	def findAvg(self): #returns the avg of all keys, similar code to findMin
		i = 0
		sum = 0
		avg = 0
		while i != self.mapSize: 
			if self.map[i] != None: 
				for itr in self.map[i]: 
					sum = sum + float(itr[0])
			i = i+1
		
		avg = sum / self.count
		return avg
		
	def resize(self): #resize the map when the number of pairs passes the threshold
		oldSize = self.mapSize #saving the old map size
		self.mapSize = self.mapSize * 2 #new map size
		self.maxSize = int(self.mapSize * self.threshold) #new threshold
		
		oldMap = self.map #saving old map temporarily and resetting current map
		self.map = [None] * self.mapSize
		self.count = 0
		
		i = 0
		while i != oldSize: #iterate through every index in old map
			if oldMap[i] != None:
				for itr in oldMap[i]:
					self.insert(itr[0], itr[1])
			i = i + 1
			
		del oldMap
		del oldSize
