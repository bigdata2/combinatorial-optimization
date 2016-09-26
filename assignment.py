import sys
from string import whitespace
from fractions import gcd
from munkres import Munkres

class product(object):
   """ A class that stores the information about a product 
   """
   def __init__(self, name):
      self.name = name
      self.numLetters = len(filter(lambda x: x.isalpha(), self.name))
      self.isEven = True if (self.numLetters%2 == 0) else False

   def __repr__(self):
        return self.name

   __str__ = __repr__

class customer(object):
   """ A class that stores the information about a customer
   """
   def __init__(self, name):
      self.name = name
      self.numConsonants =  0
      self.numVowels = 0
      self.countVowels()
      self.numConsonants = (len(filter(lambda x: x.isalpha(), self.name)) -
                           self.numVowels)
      self.numLetters = self.numConsonants + self.numVowels

   def __repr__(self):
        return self.name

   __str__ = __repr__

   def countVowels(self):
	vowelsMap = {'A':True,'E':True,"I":True, "O":True, "U":True, "Y":True}
        cnt = 0
        for v in self.name.upper():
		if v in vowelsMap:
			cnt += 1
	self.numVowels = cnt 

class suitabilityscore():
   """ A class that reads customer and product details and 
       assigns products to cusomters to maximize "suitability score" (SS)
   """
   def __init__(self):
      if len(sys.argv) < 2:
	 print "usage: python assignment.py <input sample filename> "
	 exit()
      self.inputFile = sys.argv[1]
      self.customerList = []
      self.productList = []
      self.SSMatrix = []
      self.CostMatrix = []
      self.m = Munkres()

   def readAndComputeSS(self):
      with open(self.inputFile) as inputfile:
         for line in inputfile:
                line = line.strip()
		line = line.translate(None, whitespace)
                if len(line) == 0 :
			continue
                splitline = line.split(";",2)
                customers = splitline[0].split(",")
                products = splitline[1].split(",")
                for c in customers:
			if len(c) == 0:
				continue
			self.customerList.append(customer(c))
                for p in products:
			if len(p) == 0:
				continue
			self.productList.append(product(p))
                if not (self.customerList and self.productList):
			print ("No customer name or product name found,"+ 
				" skipping SS computation.")
		        self.clearAll()
			continue
		self.computeMaxSS()

   def computeMaxSS(self):
                self.populateSSMatrix()
                maxSS = self.findMaxSS()
		self.computeTotalSS(maxSS)
		self.clearAll()
 
   def populateSSMatrix(self):
	for customer in self.customerList:
		SS_row = []
		cost_row = []
		for product in self.productList:
			SS = 0.0
			if product.isEven == True:
				SS = customer.numVowels * 1.5 
			elif product.isEven == False:
				SS = float(customer.numConsonants) 
			if gcd(customer.numLetters, product.numLetters) > 1:
				SS *= 1.5
			SS_row += [SS]
      		self.SSMatrix += [SS_row]
                
   def findMaxSS(self):
	maxSS = self.SSMatrix[0][0]
	for i in range(len(self.SSMatrix)):
		for j in range(len(self.SSMatrix[0])):
			if (maxSS < self.SSMatrix[i][j]):
				maxSS = self.SSMatrix[i][j]
	return maxSS

   def computeTotalSS(self, maxSS):
        cost_matrix = Munkres.make_cost_matrix(self.SSMatrix,
                                       lambda cost: maxSS - cost)
	indexes = self.m.compute(cost_matrix)
	total = 0
	for row, column in indexes:
    		value = self.SSMatrix[row][column]
    		total += value
	print '%.2f' % total
        
   def clearAll(self):
      self.customerList = []
      self.productList = []
      self.SSMatrix = []
      self.CostMatrix = []
					
if __name__ == '__main__':
	ss = suitabilityscore()
	ss.readAndComputeSS()
