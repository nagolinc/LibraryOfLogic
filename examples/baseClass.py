import random
from abc import ABC, abstractmethod

class LibraryOfLogicBaseClass(ABC):
    @abstractmethod
    def describeRules(self):
        pass

    @abstractmethod
    def makePrettyState(self, state):
        pass

    @abstractmethod
    def generateExampleProblem(self):
        pass

    @abstractmethod
    def getNextStep(self, problem):
        pass

    def generateConversation(self, num_steps=10,please="Please solve this problem step by step:", keep_going_phrases=["please keep going", "continue"]):
        # Setup
        print("USER:")
        rules_dict = self.describeRules()
        print(rules_dict['rules'])
        print(please)
        problem_dict = self.generateExampleProblem()
        print(problem_dict['pretty_state'])
        next_step_dict = self.getNextStep(problem_dict['state'])

        # First step
        print("ASSISTANT:")
        print(next_step_dict.get('message', ""))
        print(next_step_dict['pretty_state'])
        print(next_step_dict['status'])

        # Remaining steps
        step_count = 1
        while next_step_dict['status'] == 'Continue' and step_count < num_steps:
            print(f"USER:\n{random.choice(keep_going_phrases)}")
            print("ASSISTANT:")
            next_step_dict = self.getNextStep(next_step_dict['state'])
            if 'message' in next_step_dict:
                print(next_step_dict['message'])
            print(next_step_dict['pretty_state'])
            step_count += 1

            #break if status is invalid or finished
            if next_step_dict['status'] != 'Continue':
                break

     