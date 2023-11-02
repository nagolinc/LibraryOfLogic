from baseClass import LibraryOfLogicBaseClass


class TowerOfHanoi(LibraryOfLogicBaseClass):
    def __init__(self, n):
        super().__init__()
        self.n = n  # Number of disks

    def describeRules(self):
        return {
            'rules': 'The Tower of Hanoi is a mathematical puzzle of the 18th century. '
            'It consists of three rods and a number of disks of different sizes which can slide onto any rod. '
            'The puzzle starts with the disks in a neat stack in ascending order of size on one rod, '
            'the smallest at the top, thus making a conical shape. '
            'The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules: '
            '1. Only one disk can be moved at a time. '
            '2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod. '
            '3. No disk may be placed on top of a smaller disk.'
        }

    def generateExampleProblem(self):
        state = [list(range(self.n, 0, -1)), [], [], 0]
        return {
            'state': state,
            'pretty_state': self.makePrettyState(state)
        }

    def makePrettyState(self, state):
        rod1, rod2, rod3, turn = state
        rods = [rod1, rod2, rod3]
        max_height = max(max(len(rod) for rod in rods), 1)
        pretty_state = ""

        for i in range(max_height - 1, -1, -1):
            for rod in rods:
                if i < len(rod):
                    pretty_state += "|%2d|   " % rod[i]
                else:
                    pretty_state += "|  |   "
            pretty_state += "\n"

        pretty_state += "Rod 1  Rod 2  Rod 3, turn: " + str(turn)
        return pretty_state
    

    def checkValidState(self, state,message=''):
        rod1, rod2, rod3, turn = state

        status = 'Continue'

        # first check if all the rods are in a valid state (i.e. no disk is on top of a smaller disk)
        for rod in [rod1, rod2, rod3]:
            # check if sorted tuple === tuple
            if tuple(sorted(rod,reverse=True)) != tuple(rod):
                status = 'Invalid'
                message = 'Larger disk is on top of a smaller disk.'

        # check if puzzle is solved
        if not rod1 and not rod2:
            status = 'Finished'
            message = 'All disks have been moved to rod 3.'

        return status, message


    def getNextStep(self, state):
        rod1, rod2, rod3, turn = state

        status, message = self.checkValidState(state)
        if status != 'Continue':
            return {
                'state': state,
                'pretty_state': self.makePrettyState(state),
                'status': status,
                'message': message
            }

        

        # get the next move
        #    Move one disk from peg A to peg B or vice versa, whichever move is legal. if turn%3 == 0
        if turn % 3 == 0:
            if not rod1 and not rod2:
                status = 'Invalid'
                message = 'Cannot move from an empty rod.'
            elif not rod1:
                status = 'Continue'
                message = "Move one disk from peg B to peg A"
                rod1.append(rod2.pop())
            elif not rod2:
                status = 'Continue'
                message = "Move one disk from peg A to peg B"
                rod2.append(rod1.pop())
            elif rod1[-1] < rod2[-1]:
                status = 'Continue'
                message = "Move one disk from peg A to peg B"
                rod2.append(rod1.pop())
            else:
                status = 'Continue'
                message = "Move one disk from peg B to peg A"
                rod1.append(rod2.pop())

            turn += 1
            new_state = [rod1, rod2, rod3, turn]

            status, message = self.checkValidState(new_state,message)

            return {
                    'state': new_state,
                    'pretty_state': self.makePrettyState(new_state),
                    'status': status,
                    'message': message
                }


        #    Move one disk from peg A to peg C or vice versa, whichever move is legal. if turn%3 == 1
        if turn % 3 == 1:
            if not rod1 and not rod3:
                status = 'Invalid'
                message = 'Cannot move from an empty rod.'
            elif not rod1:
                status = 'Continue'
                message = "Move one disk from peg C to peg A"
                rod1.append(rod3.pop())
            elif not rod3:
                status = 'Continue'
                message = "Move one disk from peg A to peg C"
                rod3.append(rod1.pop())
            elif rod1[-1] < rod3[-1]:
                status = 'Continue'
                message = "Move one disk from peg A to peg C"
                rod3.append(rod1.pop())
            else:
                status = 'Continue'
                message = "Move one disk from peg C to peg A"
                rod1.append(rod3.pop())

            turn += 1
            new_state = [rod1, rod2, rod3, turn]

            status, message = self.checkValidState(new_state,message)

            return {
                    'state': new_state,
                    'pretty_state': self.makePrettyState(new_state),
                    'status': status,
                    'message': message
                }
            

        #    Move one disk from peg B to peg C or vice versa, whichever move is legal. if turn%3 == 2
        if turn % 3 == 2:
            if not rod2 and not rod3:
                status = 'Invalid'
                message = 'Cannot move from an empty rod.'
            elif not rod2:
                status = 'Continue'
                message = "Move one disk from peg C to peg B"
                rod2.append(rod3.pop())
            elif not rod3:
                status = 'Continue'
                message = "Move one disk from peg B to peg C"
                rod3.append(rod2.pop())
            elif rod2[-1] < rod3[-1]:
                status = 'Continue'
                message = "Move one disk from peg B to peg C"
                rod3.append(rod2.pop())
            else:
                status = 'Continue'
                message = "Move one disk from peg C to peg B"
                rod2.append(rod3.pop())

            turn += 1
            new_state = [rod1, rod2, rod3, turn]

            status, message = self.checkValidState(new_state,message)

            return {
                    'state': new_state,
                    'pretty_state': self.makePrettyState(new_state),
                    'status': status,
                    'message': message
                }
            


if __name__ == "__main__":
    n = 4
    towerOfHanoi = TowerOfHanoi(n)
    towerOfHanoi.generateConversation(2**n)
