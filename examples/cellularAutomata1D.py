import random
from baseClass import LibraryOfLogicBaseClass

class CellularAutomata1D(LibraryOfLogicBaseClass):
    def __init__(self, rule_number, width, wrap):
        self.rule_number = rule_number
        self.width = width
        self.wrap = wrap
        self.state = [0] * width
        self.state[width // 2] = 1  # Initialize with one cell in the middle set to 1

    def describeRules(self):
        rules = '''A one-dimensional cellular automaton consists of an array of cells that can be in one of two states (0 or 1).
    Each step involves updating each cell according to its neighbors and a rule.\n'''

        rule_bin = format(self.rule_number, '08b')

        for i in range(8):
            triplet = format(7 - i, '03b')
            new_state = rule_bin[i]
            rules += f"If the cells above are in state {triplet}, then the new cell will be a {new_state}.\n"

        return {'rules': rules}

    def makePrettyState(self, state):
        return ''.join(str(cell) for cell in state)

    def generateExampleProblem(self):
        self.state = [random.choice([0, 1]) for _ in range(self.width)]
        return {'state': self.state, 'pretty_state': self.makePrettyState(self.state)}

    def rule_lookup(self, left, center, right):
        rule_bin = format(self.rule_number, '08b')
        index = int('{}{}{}'.format(left, center, right), 2)
        return int(rule_bin[-(index + 1)])

    def getNextStep(self, problem):
        next_state = []
        for i in range(self.width):
            if self.wrap:
                left = problem[(i - 1) % self.width]
                center = problem[i]
                right = problem[(i + 1) % self.width]
            else:
                left = problem[i - 1] if i - 1 >= 0 else 0
                center = problem[i]
                right = problem[i + 1] if i + 1 < self.width else 0
            
            next_cell = self.rule_lookup(left, center, right)
            next_state.append(next_cell)

        self.state = next_state

        return {'message': 'Next step computed using rule {}'.format(self.rule_number),
                'state': self.state,
                'pretty_state': self.makePrettyState(self.state),
                'status': 'Continue'}
    


if __name__ == "__main__":
    rule_number = 110  # Choose the rule number between 0 and 255
    width = 20  # Choose the width of the automaton
    wrap = True  # Choose whether to wrap around or not
    ca1d = CellularAutomata1D(rule_number, width, wrap)

    # Generate a conversation with up to 20 steps
    ca1d.generateConversation(num_steps=20,please="can you compute the next step for this input?", keep_going_phrases=["please keep going", "continue"])
