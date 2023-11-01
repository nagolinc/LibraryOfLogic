from baseClass import LibraryOfLogicBaseClass

import random

class MatchedParentheses(LibraryOfLogicBaseClass):
    def __init__(self, n):
        super().__init__()
        self.n = n  # Length of the string

    def describeRules(self):
        return {
            'rules': 'Given a string containing only parentheses, the task is to check if they are balanced. '
                     'The state is represented as [input_string, stack].'
        }

    def generate_balanced_parentheses(self,n):
        if n == 0:
            return ''
        if n == 1:
            return '()'
        else:
            choice = random.choice(['split', 'wrap', 'append'])
            if choice == 'split':
                split_point = random.randint(1, n - 1)
                return self.generate_balanced_parentheses(split_point) + self.generate_balanced_parentheses(n - split_point)
            elif choice == 'wrap':
                return '(' + self.generate_balanced_parentheses(n - 1) + ')'
            else:  # append
                return '()' + self.generate_balanced_parentheses(n - 1)

    def generateExampleProblem(self, valid=True):
        if valid:
            input_string = self.generate_balanced_parentheses(self.n // 2)
            if self.n % 2 != 0:
                input_string += random.choice(['(', ')'])
        else:
            parentheses = ['(', ')']
            input_string = ''.join(random.choice(parentheses) for _ in range(self.n))

        return {
            'state': [input_string, []],
            'pretty_state': self.makePrettyState([input_string, []])
        }

    def makePrettyState(self, state):
        input_string, stack = state
        pretty_stack = ' '.join(stack)
        return f'Input string: {input_string} Stack: {pretty_stack}'


    def getNextStep(self, state):
        input_string, stack = state

        if not input_string:
            status = 'Finished' if not stack else 'Invalid'
            message = 'String is balanced.' if status == 'Finished' else 'String is unbalanced.'
            return {
                'state': [input_string, stack],
                'pretty_state': self.makePrettyState([input_string, stack]),
                'status': status,
                'message': message
            }

        next_char = input_string[0]
        message = f'Processing character {next_char}.'
        
        if next_char == '(':
            stack.append('(')
            message += ' Pushing to stack.'
        else:
            if stack and stack[-1] == '(':
                stack.pop()
                message += ' Matching with top of stack and popping.'
            else:
                return {
                    'state': [input_string, stack],
                    'pretty_state': self.makePrettyState([input_string, stack]),
                    'status': 'Invalid',
                    'message': 'No matching open parenthesis. String is unbalanced.'
                }
            
        new_input_string = input_string[1:]
        if not new_input_string:
            status = 'Finished' if not stack else 'Invalid'
            message = 'String is balanced.' if status == 'Finished' else 'String is unbalanced.'
            return {
                'state': [new_input_string, stack],
                'pretty_state': self.makePrettyState([new_input_string, stack]),
                'status': status,
                'message': message
            }

        return {
            'state': [input_string[1:], stack],
            'pretty_state': self.makePrettyState([input_string[1:], stack]),
            'status': 'Continue',
            'message': message
        }

if __name__ == "__main__":
    n = 10
    parentheses_checker = MatchedParentheses(n)
    parentheses_checker.generateConversation(n)
