"""General interface for a cognitive manager.
"""

import abc


class CogMan:
    """An abstract cognitive manager for Leap
    """
    def __init__(self):
        self._pre_strategists = []
        self._pre_strategists_names = []

        self._post_strategists = []
        self._post_strategists_names = []

        self._plan = [(None, True)] ## pairs of (operation, effect/preimage)
        self._subproblems = [] ## pairs of domain and problem PDDL files

    @abc.abstractmethod
    def __call__(self, domain_file, problem_file, timeout=10):
        """ Takes in a PDDL domain and problem file.
            Just return the next operation if there is one and  
                if current state satisfy the preimage of the next operation
            Else, 
                Process with a sequence of pre-strategists.
                Makes a set of (partial) plans. 
                Process with a sequence of post-strategists. 
                Decide on one (partial) plan. 
                Returns the first operation.
        """
        raise NotImplementedError("Override me!")

    def init_pre_strategists(self, domain_file, problem_file, pre_strategists_names):
        """ Initiate the pre-strategists based on the 
                domain : types, predicates, operators
                and 
                problem : objects, init state, goal state
            Initiate some post-strategists associated with specific pre-
        """
        raise NotImplementedError("Override me!")

    def init_post_strategists(self, domain_file, problem_file, post_strategists_names):
        """ Initiate extra post-strategists based on the given list of names
        """
        raise NotImplementedError("Override me!")