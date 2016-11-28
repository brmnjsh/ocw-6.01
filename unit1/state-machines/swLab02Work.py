import lib601.sm as sm

##################################
# Double Delay SM
##################################

class Delay2Machine(sm.SM):
    def __init__(self, val0, val1):
        self.startState = val0, val1   # fix this
    def getNextValues(self, state, inp):
        return self.getNextState(state,inp)
    def getNextState(self, state, inp):
        ret = None 
        if type(state) is int:
            ret = (self.oldVal, state)
        else:
            ret = (state[1], state[0])
        self.oldVal = inp
        return ret

def runTestsDelay():
    print 'Test1:', Delay2Machine(100, 10).transduce([1,0,2,0,0,3,0,0,0,4])
    print 'Test2:', Delay2Machine(10, 100).transduce([0,0,0,0,0,0,1])
    print 'Test3:', Delay2Machine(-1, 0).transduce([1,2,-3,1,2,-3])
    # Test that self.state is not being changed.
    m = Delay2Machine(100, 10)
    m.start()
    [m.getNextValues(m.state, i) for i in [-1,-2,-3,-4,-5,-6]]
    print 'Test4:', [m.step(i) for i in [1,0,2,0,0,3,0,0,0,4]]

#runTestsDelay()
# execute runTestsDelay() to carry out the testing, you should get:
#Test1: [100, 10, 1, 0, 2, 0, 0, 3, 0, 0]
#Test2: [10, 100, 0, 0, 0, 0, 0]
#Test3: [-1, 0, 1, 2, -3, 1]
#Test4: [100, 10, 1, 0, 2, 0, 0, 3, 0, 0]

##################################
# Comments SM
##################################

x1 = '''def f(x):  # func
   if x:   # test
     # comment
     return 'foo' '''

x2 = '''#initial comment
def f(x):  # func
   if x:   # test
     # comment
     return 'foo' '''


class CommentsSM(sm.SM):
    startState = False  # fix this

    def getNextValues(self, state, inp):
        if inp == '#' and state == False:
            state = True
        elif inp == '\n' or state == False and inp != '#':
            state = False
            inp = None
        return (state, inp)
 

def runTestsComm():
    m = CommentsSM()
    # Return only the outputs that are not None
    print 'Test1:',  [c for c in CommentsSM().transduce(x1) if not c==None]
    print 'Test2:',  [c for c in CommentsSM().transduce(x2) if not c==None]
    # Test that self.state is not being changed.
    m = CommentsSM()
    m.start()
    [m.getNextValues(m.state, i) for i in ' #foo #bar']
    print 'Test3:', [c for c in [m.step(i) for i in x2] if not c==None]
#runTestsComm()
# execute runTestsComm() to carry out the testing, you should get:

#Test1: ['#', ' ', 'f', 'u', 'n', 'c', '#', ' ', 't', 'e', 's', 't', '#', ' ', 'c', 'o', 'm', 'm', 'e', 'n', 't']
#Test2: ['#', 'i', 'n', 'i', 't', 'i', 'a', 'l', ' ', 'c', 'o', 'm', 'm', 'e', 'n', 't', '#', ' ', 'f', 'u', 'n', 'c', '#', ' ', 't', 'e', 's', 't', '#', ' ', 'c', 'o', 'm', 'm', 'e', 'n', 't']
#Test3: ['#', 'i', 'n', 'i', 't', 'i', 'a', 'l', ' ', 'c', 'o', 'm', 'm', 'e', 'n', 't', '#', ' ', 'f', 'u', 'n', 'c', '#', ' ', 't', 'e', 's', 't', '#', ' ', 'c', 'o', 'm', 'm', 'e', 'n', 't']

##################################
# First Word SM
##################################

# Test 1
test1 = '''hi
ho'''
# This can also be writtent as:
# test1 = 'hi\nho'

#Test 2
test2 = '''  hi
ho'''
# This can also be writtent as:
# test2 = '  hi\nho'

#Test 3
test3  = '''

 hi
 ho ho ho

 ha ha ha'''
# This can also be writtent as:
# test3 ='\n\n hi \nho ho ho\n\n ha ha ha'

class FirstWordSM(sm.SM):
    # Your code here
    startState = 0  # fix this

    def getNextValues(self, state, inp):
        if inp == '\n' or state == 0 and inp == ' ':
            return (0, None)
        elif (state == 0 or state == 1) and inp != '\n' and inp != ' ':
            return (1, inp)
        elif state == 1 and inp == ' ' or state == 2:
            return (2, None)


def runTestsFW():
    m = FirstWordSM()
    print 'Test1:', m.transduce(test1)
    print 'Test2:', m.transduce(test2)
    print 'Test3:', m.transduce(test3)
    m = FirstWordSM()
    m.start()
    [m.getNextValues(m.state, i) for i in '\nFoo ']
    print 'Test 4', [m.step(i) for i in test1]

#runTestsFW()
# execute runTestsFW() to carry out the testing, you should get:
#Test1: ['h', 'i', None, 'h', 'o']
#Test2: [None, None, 'h', 'i', None, 'h', 'o']
#Test3: 
#[None, None, None, 'h', 'i', None, None, 'h', 'o', None, None, None, None, None, None, None, None, None, 'h', 'a', None, None, None, None, None, None]
#Test4: ['h', 'i', None, 'h', 'o']


class CountingStateMachine(sm.SM):
    startState = 0

    def getNextValues(self, state, inp):
        state, inp = self.getOutput(inp, state), self.getOutput(inp, state)
        return state, inp

class CountMod5(CountingStateMachine):
    def getOutput(self, state, inp):
        return state % 5 

class AlternateZeros(CountingStateMachine):
    def getOutput(self, state, inp):
        if state % 2 == 0:
            return state
        else:
            return 0

#m = AlternateZeros()
#print m.transduce([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

def add(a,b):
    if b == 0:
        return a
    else:
        return add(a, b - 1) + 1

#print add(-25.35,20)

def sub(a,b):
    if b == 0:
        return a
    else:
        return sub(a, b - 1) - 1

#print sub(5,2)

def slowMod(a,b):
    if a <= 0:
        if a < 0:
            return a + b
        return a
    else:
        return slowMod(a - b, b)

#print slowMod(4,6)

class Hammock():
    def __init__(self):
        self.empty = True
        self.lastRequest = ''
    def sitDown(self, person):
        if self.empty == True:
            self.empty = False
            return "welcome!"
        else:
            if self.lastRequest == person:
                return "welcome!"
            self.lastRequest = person
            return "sorry, no room"
    def leave(self):
        if self.empty == False:
            self.empty = True
            return 1
        else:
            return 0

# myHammock = Hammock()
# print myHammock.sitDown('George')
# print myHammock.sitDown('Bobby')
# print myHammock.sitDown('Bobby')
# print myHammock.leave()
# print myHammock.leave()
# print myHammock.leave()
# print myHammock.sitDown('Martha')
# print myHammock.sitDown('Wilhelm')
# print myHammock.sitDown('Klaus')
# print myHammock.sitDown('Wilhelm')