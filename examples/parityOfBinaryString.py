from baseClass import LibraryOfLogicBaseClass

class ParityOfBinaryString(LibraryOfLogicBaseClass):
    def __init__(self, k=10):
        super().__init__()
        self.k = k
        

    def describeRules(self):
        return {
            'rules': 'Given a binary string, the task is to calculate its parity bit-by-bit. '
                     'The state is represented as [binary_string, accumulator]. '
                     'The accumulator keeps track of the running sum of the parity bit.'
        }

    def generateExampleProblem(self):
        import random
        binary_string = ''.join(random.choice('01') for _ in range(self.k))
        return {
            'state': [binary_string, '0'],
            'pretty_state': f'Binary string: {binary_string}, Accumulator: 0'
        }
    
    def makePrettyState(self, state):
        binary_string, accumulator = state
        return f'Binary string: {binary_string}, Accumulator: {accumulator}'

    def getNextStep(self, state):
        binary_string, accumulator = state

        if not binary_string:
            return {
                'state': [binary_string, accumulator],
                'pretty_state': f'Binary string: {binary_string}, Accumulator: {accumulator}',
                'status': 'Finished',
                'message': f'The final parity is {accumulator}'
            }

        next_bit = binary_string[0]
        new_accumulator = str((int(accumulator) + int(next_bit)) % 2)

        return {
            'state': [binary_string[1:], new_accumulator],
            'pretty_state': f'Binary string: {binary_string[1:]}, Accumulator: {new_accumulator}',
            'message': f'Add {next_bit} to the accumulator',
            'status': 'Continue'
        }
    

if __name__ == "__main__":
    k = 10
    parity_calculator = ParityOfBinaryString(k)
    parity_calculator.generateConversation(k+1)
