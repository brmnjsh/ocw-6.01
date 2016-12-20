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

c = Cascade(sm.Delay(100), Increment(1))
print c.transduce([3,8,2,4,6,5])
c = Cascade(Increment(1),sm.Delay(100))
print c.transduce([3,8,2,4,6,5])