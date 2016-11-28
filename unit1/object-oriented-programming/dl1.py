#2,1
def fib(n):
	i = 0
	fibs = []
	while i < n:
		if i == 0 or i == 1:
			fibs.append(i)
		else:
			fibs.append(fibs[i - 1] + fibs[i - 2])
		i = i + 1
	return fibs[-1]

#print fib(10)

#2.2 - 2.3
class Car:
	color = 'gray'
	def describeCar(self):
		return Car.color
	def describeSelf(self):
		return self.color


#2.4
class V2:
	def __init__(self, x, y):
		self.vectors = [x,y]
	def __str__(self):
		return "V2[" + str(self.vectors[0]) + ", " + str(self.vectors[1]) + "]"
	def getX(self):
		print self.vectors[0]
	def getY(self):
		print self.vectors[1]
	def add(self,other):
		return V2(self.vectors[0] + other.vectors[0],self.vectors[1] + other.vectors[1])
	def mul(self,scalar):
		return V2(self.vectors[0] * scalar, self.vectors[1] * scalar)
	def __add__(self,v):
		return self.add(v)
	def __mul__(self,v):
		return self.mul(v)

#3....
import numpy
class Polynomial:
    # Delete the pass statement below and insert your own code
    def __init__(self,coefficients):
    	self.coefficients = coefficients
    def coeffs(self, i):
    	print self.coefficients[-i - 1]
    def add(self,other):
    	new = []
    	if len(self.coefficients) >= len(other):
    		main = self.coefficients
    		second = other
    	else:
    		main = other
    		second = self.coefficients
    	mi = 0
    	si = 0
    	while mi < len(main):
    		if mi < len(main) - len(second):
    			print main[mi]
    			new.append(main[mi])
    		else:
    			print main[mi]
    			new.append(main[mi] + other[si])
    			si = 1 + si
    		mi = 1 + mi
    	return Polynomial(new)
    def mul(self,other):
    	new = []
    	if len(self.coefficients) >= len(other):
    		main = self.coefficients
    		second = other
    	else:
    		main = other
    		second = self.coefficients
    	mi = 0
    	si = 0
    	while mi < len(main):
    		if mi < len(main) - len(second):
    			print main[mi]
    			new.append(main[mi])
    		else:
    			print main[mi]
    			new.append(main[mi] * other[si])
    			si = 1 + si
    		mi = 1 + mi
    	return Polynomial(new)
    def val(self, v):
    	exp = len(self.coefficients) - 1
    	i = 0
    	val = 0
    	while i < len(self.coefficients):
    		val = val + self.coefficients[i] * v**exp
    		i = i + 1
    		exp = exp - 1
    	return val
    #def hVal(self, v):
    def roots(self):
    	if len(self.coefficients) == 2 or len(self.coefficients) == 3:
    		return numpy.roots(self.coefficients).tolist()
    	else:
    		return "greater than second order, not handled"
	def __str__(self):
		return str(self.coefficients)
	def __add__(self, other):
		return self.add(other)
	def __mul__(self, other):
		return self.mul(other)
	def __call__(self, x):
		return self.val(x)
	def __repr__(self):
		return str(self)
    	
#v = V2(1.1,2.2)
#print V2(1.1,2.2)
#v.getX()
#v.getY()
# a = V2(1.0,2.0)
# b = V2(2.2,3.3)
# print a.add(b)
# print a.mul(2)
# print a.add(b).mul(-1)
#print V2(1.1,2.2) + V2(3.3,4.4)
#print V2(2.0,4.0) * 2
#p = Polynomial([1,-7,10,-4,6])
#p = Polynomial([5,-4,6])
#print p.roots()
#p.coeffs(3)
#print p.add([3,-2,7,1]).coefficients
#print p.mul([3,0,7,1]).coefficients
#print p
#print p.val(2)

#1.4.3
def evenSquares(items):
	return [i**2 for i in items if i % 2 == 0]
#print evenSquares([1,4,7,8])

def sumAbsProd(left,right):
	return sum([abs(r) * abs(l) for l in left for r in right])
#print sumAbsProd([2,-3],[4,-5])

#1.4.4
#p1
class Thing:
	def set(self,v):
		self.x = v
	def get(self):
		return self.x
	def mangle(arg):
		arg.set(arg.get() + 1)
		arg.hasBeenMangled = True
	def clone(self):
		n = Thing()
		n.set(self.get())
		return n
	def __str__(self):
		return "This is a Thing with a value " + str(self.get())
a = Thing()
a.x = 6
#print a.get()
b = Thing()
a.set(b)
#print a.x
b.set(7)
#print a.x.x
#print a.get()
#print a.x.get()
#print 3 + a.get().get()
c = a.get()
#print c.x
a.set(1 - a.get().get())
#print a.x
c.set(3)
#print a.get().get()
a = Thing()
b = Thing()
a.set(b)
b.set(a)
#print a.x == b
#print a.x.x == a
#print a.x.x.x == b

#p2
def thingMangle(arg):
	arg.set(arg.get() + 1)
	arg.hasBeenMangled = True
a = Thing()
a.set(5)
thingMangle(a)
#print a.get()
#print a.hasBeenMangled
b = Thing()
b.set(Thing())
b.get().set(3)
thingMangle(b.get())
#print b.get()
#print b.get().get()
c = Thing()
#thingMangle(c)

#p3
a = Thing()
a.set(3)
a.mangle()
#print a.get()

#p4
def mangled(z):
	d = Thing()
	d.set(z)
	d.mangle()
	return d
d = mangled(3)
#print d.get()

#1.4.5
def assignThing(thing1,thing2):
	thing1.set(thing2.get())
def swapThing(thing1,thing2):
	one = thing1.get()
	two = thing2.get()
	thing1.set(two)
	thing2.set(one)
def sumOfthings(thing1,thing2):
	s = thing1.get() + thing2.get()
	new = Thing()
	new.set(s)
	return new
def sumOfAllThings(things):
	s = sum([t.get() if len(things) > 0 else 0 for t in things])
	new = Thing()
	new.set(s)
	return new
a = Thing()
b = Thing()
c = Thing()
a.set(4)
b.set(2)
c.set(6)
n = sumOfAllThings([a,b,c])
#print n.get()

#1.4.6 
a = Thing()
a.set(3)
b = a.clone()
#print b.get()
a = Thing()
a.set(3)
#print a

#1.4.7
def isPalindrome(text):
	l = 0
	while l < len(text) - 1:
		if (l == abs(len(text) / 2)):
			return 'is palidrome'
		if (text[l] != text[- (l + 1)]):
			return "not palindrome"
		l = l + 1

#print isPalindrome("able was I ere I saw elba")

#1.4.8
def isSubstring(mString, subString):
	m = 0
	s = 0
	while m < len(mString):
		if mString[m] == subString[s]:
			if s == len(subString) - 1:
				return True
			s = s + 1
		elif mString[m] != subString[s]:
			s = 0
		m = m + 1
	return False

#print isSubstring("barfobaforfoo","foo")

#1.4.9
def extractTags(tags):
	return [tag[1:-1] for tag in tags.split() if tag[0] == "[" and tag[-1] == "]"]

#print extractTags('[fizz] thing [/fizz] fuzz [zip]')

#1.4.10
class FruitSalad:
	fruits = ['melons','pineapples']
	servings = 4
	def __init__(self,ingredients,numservings):
		self.fruits = ingredients
		self.servings = numservings
	def __str__(self):
		return str(self.servings) + " servings of fruit salad with " + str(self.fruits)
	def add(self,fruit):
		self.fruits.append(fruit)
	def serve(self):
		if self.servings > 0:
			self.servings = self.servings - 1
			return "enjoy"
		else:
			return "sorry"

salad = FruitSalad(['bananas', 'apples'],2)
salad.add('cherries')
# print salad.fruits
# print FruitSalad.fruits
# print salad.serve()
# print salad.serve()
# print salad.serve()
# print salad.servings
# print FruitSalad.servings

#1.4.11
def warehouseProcess(wTotals,transactions):
	if wTotals.has_key(transactions[1]):
		if transactions[0] == 'receive':
			wTotals[transactions[1]] = wTotals[transactions[1]] + transactions[2]
		else:
			wTotals[transactions[1]] = wTotals[transactions[1]] - transactions[2]
	else:
		if transactions[0] == 'receive':
			wTotals[transactions[1]] = transactions[2]
	return wTotals

class Warehouse:
	def __init__(self):
		self.inventory = {}
	def process(self,transactions):
		if self.inventory.has_key(transactions[1]):
			if transactions[0] == 'receive':
				self.inventory[transactions[1]] = self.inventory[transactions[1]] + transactions[2]
			else:
				self.inventory[transactions[1]] = self.inventory[transactions[1]] - transactions[2]
		else:
			if transactions[0] == 'receive':
				self.inventory[transactions[1]] = transactions[2]
		return self.inventory
	def lookup(self,item):
		if self.inventory.has_key(item):
			return self.inventory[item]
		else:
			return 0

#print warehouseProcess({'a':5,'b':10,'c':6},('recieve','d',10))
w = Warehouse()
w.process(('receive', 'a', 10))
w.process(('ship', 'a', 7))
# print w.lookup('a')
# print w.lookup('b')