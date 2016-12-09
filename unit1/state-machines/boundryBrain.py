import math
import lib601.util as util
import lib601.sm as sm
import lib601.gfx as gfx
from soar.io import io

class MySMClass(sm.SM):
    startState = 'seeking' 
    def getNextValues(self,state,inp):
        #return (state, io.Action(fvel = 0, rvel = 0))

        # if state == 'seeking':
        #     if inp.sonars[2] < 0.54 and inp.sonars[5] < 0.54 and inp.sonars[3] < 0.46 and inp.sonars[4] < 0.46:
        #         return ('rotate', io.Action(fvel = 0.1, rvel = 0))
        #     # elif inp.sonars[5] == 5 and inp.sonars[3] == 5 and inp.sonars[4] == 5 and inp.sonars[7] < 0.5:
        #     #     if inp.sonars[7] < 0.4:
        #     #         (state, io.Action(fvel = 0.1, rvel = 0.1))
        #     #     else:
        #     #         return (state, io.Action(fvel = 0.1, rvel = -0.1))
        #     else:
        #         if inp.sonars[3] < inp.sonars[4]:
        #             return (state, io.Action(fvel = 0.1, rvel = 0.1))
        #         elif inp.sonars[4] < inp.sonars[3] and inp.sonars[5] > inp.sonars[4]:
        #             return (state, io.Action(fvel = 0.1, rvel = -0.1))
        #         elif inp.sonars[4] < inp.sonars[3] and inp.sonars[5] < inp.sonars[4]: 
        #             return (state, io.Action(fvel = 0.1, rvel = 0.1))
        #         else:
        #             return (state, io.Action(fvel = 0.1, rvel = 0))
                
        # if state == 'rotate':
        #     if inp.sonars[7] < 0.47 and inp.sonars[2] > 0.54 and inp.sonars[5] > 0.54 and inp.sonars[3] > 0.46 and inp.sonars[4] > 0.46:
        #         return ('seeking', io.Action(fvel = 0.1, rvel = 0))
        #     elif inp.sonars[6] < inp.sonars[7]:
        #         return (state, io.Action(fvel = 0, rvel = 0.1))
        #     else:
        #         return (state, io.Action(fvel = 0, rvel = 0.1))
        #if inp.sonars[6] < inp.sonars[7]:

        if state == 'seeking':
            if inp.sonars[2] < 0.5 and inp.sonars[5] < 0.5 and inp.sonars[3] < 0.45 and inp.sonars[4] < 0.45:
                return ('rotate', io.Action(fvel = 0, rvel = 0.3))
            elif inp.sonars[7] < 0.5:
                if (0.45 - inp.sonars[7]) < 0: #too far away
                    print 'too far away', inp.sonars[7], 0.4 - inp.sonars[7]
                    return (state, io.Action(fvel = 0.1, rvel = -0.3))
                elif (0.45 - inp.sonars[7]) > 0: #too close:
                    print 'too close', inp.sonars[7], 0.4 - inp.sonars[7]
                    return (state, io.Action(fvel = 0.1, rvel = 0.3))
            else:
                return (state, io.Action(fvel = 0.1, rvel = 0))
        elif state == 'rotate':
            if inp.sonars[7] > 0.45:
                return (state, io.Action(fvel = 0, rvel = 0.3))
            else:
                return ('tracing', io.Action(fvel = 0.1, rvel = 0))
        elif state == 'tracing':
            if inp.sonars[2] < 0.5 and inp.sonars[5] < 0.5 and inp.sonars[3] < 0.45 and inp.sonars[4] < 0.45:
                return ('rotate', io.Action(fvel = 0, rvel = 0.3))
            else:
                if (0.45 - inp.sonars[7]) < 0: #too far away
                    print 'too far away', inp.sonars[7], 0.4 - inp.sonars[7]
                    return (state, io.Action(fvel = 0.1, rvel = -0.3))
                elif (0.45 - inp.sonars[7]) > 0: #too close:
                    print 'too close', inp.sonars[7], 0.4 - inp.sonars[7]
                    return (state, io.Action(fvel = 0.1, rvel = 0.3))



mySM = MySMClass()
mySM.name = 'brainSM'

######################################################################
###
###          Brain methods
###
######################################################################

def plotSonar(sonarNum):
    robot.gfx.addDynamicPlotFunction(y=('sonar'+str(sonarNum),
                                        lambda: 
                                        io.SensorInput().sonars[sonarNum]))

# this function is called when the brain is (re)loaded
def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=False, # slime trails
                                  sonarMonitor=False) # sonar monitor widget
    
    # set robot's behavior
    robot.behavior = mySM

# this function is called when the start button is pushed
def brainStart():
    robot.behavior.start(traceTasks = robot.gfx.tasks())

# this function is called 10 times per second
def step():
    inp = io.SensorInput()
    #print inp.sonars
    robot.behavior.step(inp).execute()
    io.done(robot.behavior.isDone())

# called when the stop button is pushed
def brainStop():
    pass

# called when brain or world is reloaded (before setup)
def shutdown():
    pass
