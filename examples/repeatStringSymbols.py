from baseClass import LibraryOfLogicBaseClass
import random
import string

class RepeatStringSymbols(LibraryOfLogicBaseClass):
    def __init__(self, n, k):
        super().__init__()
        self.n = n
        self.k = k

    def describeRules(self):
        return {
            'rules': '''Given a string, the task is to repeat each symbol in the string k times. 
We can solve this problem by working step by step.
We will keep track of our remaining input string and our output string.
On each step, we will remove the first symbol from the input string and add k copies of it to the output string.        
            '''
        }
    

    def makePrettyState(self, state):
        input_string, output_string = state

        if not output_string:
            return f'Input string: {input_string}'

        #if input string is empty, return the output string
        if not input_string:
            return f'There is no input string, Output string: {output_string}'

        return f'Remaining input string: {input_string}, Output string: {output_string}'

    def generateExampleProblem(self):
        random_string = ''.join(random.choice(string.ascii_letters) for _ in range(self.n))
        return {
            'state': [random_string, ''],
            'pretty_state': self.makePrettyState([random_string, ''])
        }    

    def getNextStep(self, state):
        input_string, output_string = state

        if not input_string:
            return {
                'state': [input_string, output_string],
                'pretty_state': self.makePrettyState([input_string, output_string]),
                'message': f'The final output string is {output_string}',
                'status': 'Finished'
            }

        next_char = input_string[0]
        new_output_string = output_string + next_char * self.k

        return {
            'state': [input_string[1:], new_output_string],
            'pretty_state': self.makePrettyState([input_string[1:], new_output_string]),
            'message': f'Add {next_char} to the output string',
            'status': 'Continue'
        }

if __name__ == "__main__":
    n, k = 5, 3
    string_repeater = RepeatStringSymbols(n, k)
    string_repeater.generateConversation(n)
