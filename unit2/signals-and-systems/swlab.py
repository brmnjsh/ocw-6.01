import lib601.sm as sm

class Cascade(sm.SM):
	def __init__(self,sm1,sm2):
		self.m1 = sm1
		self.m2 = sm2
		self.startState = (sm1.startState,sm2.startState)

	def getNextValues(self,state,inp):
		(s1,s2) = state
		(newS1, o1) = self.m1.getNextValues(s1, inp)
		(newS2, o2) = self.m2.getNextValues(s2, o1)
		return ((newS1,newS2), o2)

class Increment(sm.SM):
	def __init__(self, incr):
		self.incr = incr
	def getNextState(self, state, inp):
		return sm.safeAdd(inp, self.incr)

#c = Cascade(sm.Delay(100), Increment(1))
#print c.transduce([3,8,2,4,6,5])
#c = Cascade(Increment(1),sm.Delay(100))
#print c.transduce([3,8,2,4,6,5])


def test(inp):
	return "here you go " + inp

# class PureFunction(sm.SM):
# 	startState = None
# 	def __init__(self, f):
# 		self.f = f
# 	def getNextValues(self,state,inp):
# 		return (state, self.f(inp))

#c = PureFunction(test)
#print c.transduce(['judy!'])

class BA1(sm.SM):
	startState = 0
 	def getNextValues(self, state, inp):
		if inp != 0:
			newState = state * 1.02 + inp - 100
		else:
 			newState = state * 1.02
 		return (newState, newState) 

class BA2(sm.SM):
	startState = 0
 	def getNextValues(self, state, inp):
		newState = state * 1.01 + inp
		return (newState, newState) 

def maximum(inp):
	if inp[0] >  inp[1]:
		return inp[0]
	else:
		return inp[1]

#ba1 = BA1()
#ba2 = BA2()
#maxAccount = sm.Cascade(sm.Parallel(ba1,ba2),sm.PureFunction(maximum))
#print maxAccount.transduce([10])

# def invest1(inp):
# 	if inp > abs(3000):
# 		return inp
# 	else:
# 		return 0

# def invest2(inp):
# 	if inp < abs(3000):
# 		return inp
# 	else:
# 		return 0

# def invest(inp):
# 	if inp > 3000:
# 		return (inp, 0)
# 	else:
# 		return (0, inp)


# ba1 = BA1()
# ba2 = BA2()
# switchAccount = sm.Cascade(sm.PureFunction(invest), sm.Parallel2(ba1,ba2))

# print switchAccount.transduce([10, 5000])
class CharTSM (sm.SM):
	startState = False
	def __init__(self, c):
		self.c = c
	def getNextValues(self, state, inp):
		return (True, self.c)
	def done(self, state):
		return state

class ConsumeFiveValues(sm.SM):
	startState = (0, 0) # count, total
	def getNextValues(self, state, inp):
		(count, total) = state
		if count == 4:
			return ((count + 1, total + inp), total + inp)
		else:
			return ((count + 1, total + inp), None)
	def done(self, state):
		(count, total) = state
		return count == 5

# a = CharTSM('a')
# a4 = sm.Repeat(a, 4)
# print a4.run()

#print sm.Repeat(CharTSM('a'), 4).transduce(range(100))
#print sm.Repeat(ConsumeFiveValues(), 3).transduce(range(100))
#print sm.Repeat(ConsumeFiveValues(), 3).run()

class SumTSM(sm.SM):
	startState = (0,0)

	def getNextValues(self,state,inp):
		(count,total) = state
		return ((count + 1, total + inp), total + inp)

	def done(self,state):
		(count,total) = state
		return total > 100

#s = SumTSM()
#print s.transduce(range(100))

#fourTimes = sm.Repeat(SumTSM(), 4)
#print fourTimes.transduce(range(100))

class CountUpTo(sm.SM):
	startState = (0,0)

	def __init__(self,c):
		self.c = c

	def getNextValues(self,state,inp):
		(count,total) = state
		return ((count + 1, total + 1), total + 1)

	def done(self,state):
		(count,total) = state
		return total == self.c

#c = CountUpTo(3)
#print c.run(n=20)

def makeSequenceCounter(arr):
	return sm.Sequence([CountUpTo(i) for i in arr])

print makeSequenceCounter([2,5,3]).run(n=20)