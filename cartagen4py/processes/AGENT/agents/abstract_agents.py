import itertools

class Agent:
    newid = itertools.count()
    id
    lifecycle = None
    satisfaction = 1.0
    constraints=[]
    actions_to_try = []
    deleted = False
    meso_agent = None
    feature = None
    type = ""

    def __init__(self, feature):
        self.id = next(Agent.newid)
        self.feature = feature

    def clean(self):
        self.constraints = []
        self.actions_to_try = []

    # compute the satisfaction of the agent from the satisfactions of its constraints
    def compute_satisfaction(self):
        nb = len(self.constraints)

        if nb == 0 or self.deleted:
            self.satisfaction = 1.0
            return self.satisfaction
        
        sum = 0.0
        imp_sum = 0.0
        for constraint in self.constraints:
            constraint.compute_satisfaction()
            print("satisfaction for constraint {}: {}".format(constraint.type, constraint.satisfaction))
            sum += constraint.satisfaction * constraint.importance
            imp_sum += constraint.importance
        
        if imp_sum == 0:
            self.satisfaction = 1.0
            return self.satisfaction
        
        self.satisfaction = sum / imp_sum

        return self.satisfaction

    # the best action to try is the one whose proposing constraint has 1/ the higher priority and 2/ the higher weight
    # the action proposal is an array with [action, constraint, weight]
    def get_best_action_proposal(self):
        max_priority = float('-inf')
        max_weight = float('-inf')
        best_action = None
        best_index = 0

        for i in range(0,len(self.actions_to_try)):
            action_to_try = self.actions_to_try[i]
            constraint = action_to_try[1]

            # check if constraint is satisfied
            if(constraint.satisfaction >= 100.0):
                continue
            
            # check priority
            if(constraint.priority < max_priority):
                continue
            # check importance
            if(constraint.priority == max_priority and action_to_try[2]<= max_weight):
                continue

            # at this point, action_to_try is the best action to propose
            best_action = action_to_try
            best_index = i
            max_priority = constraint.priority
            max_weight = action_to_try[2]

        del self.actions_to_try[best_index]
        return best_action
    
    # get action proposals from non satisfied constraints and compute priority values
    def update_action_proposals(self):
        if (self.deleted):
            return
        
        self.actions_to_try = []
        for constraint in self.constraints:
            if constraint.satisfaction >= 100:
                continue

            constraint.compute_priority()
            constraint.compute_actions()
            for action in constraint.actions:
                self.actions_to_try.append(action)

    def remove_action_to_try(self, action_to_remove):
        index = 0
        for action in self.actions_to_try:
            if action[0].name == action_to_remove[0].name:
                break
            index += 1
        if index < len(self.actions_to_try):
            del self.actions_to_try[index]