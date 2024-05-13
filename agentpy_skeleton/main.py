"""
BSD 3-Clause License

Copyright (c) 2020-2021 Joël Foramitti

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import networkx as nx
import matplotlib.pyplot as plt
import agentpy as ap
import numpy as np

class Agent(ap.Agent):
    """ Represents an agent in the simulation. """

    def setup(self):
        """ Set-up agent and its characteristics. """
        """ Called at the start of the simulation (t==0). """
        pass

    def step(self):
        """ Decision-making and actions that an agent performs. """
        """ Called during every time-step (excluding t==0). """
        pass

    def update(self):
        """ Record dynamic variables and perform updates if applicable. """
        """ Called after every time-step (including t==0). """
        pass

    def end(self):
        """ Evaluation or other reporting. """
        """ Called at the end of the simulation. """
        pass


class MyModel(ap.Model):

    def setup(self):
        """ Initiate a list of new agents. """
        self.agents = ap.AgentList(self, self.p.agents, Agent)

    def step(self):
        """ Call a method for every agent. """
        self.agents.step()

    def update(self):
        """ Record a dynamic variable. """
        self.agents.update()

    def end(self):
        """ Repord an evaluation measure. """
        self.agents.end()


parameters = {
    'agents':100,
    'steps':100
}

""" Uncomment either 'Single Run' or 'Multiple Runs'. """

"""
# SINGLE RUN
model = MyModel(parameters)
results = model.run()
print("Simulation completed.")
#data = results.variables.MyModel
"""

"""
# MULTIPLE RUNS
exp = ap.Experiment(MyModel, parameters, record=True, iterations=20)
# Run experiment and store data in a DataDict()
results = exp.run()
# Create panda.DataFrame of all variables and parameters
data_all = results.arrange_variables()
# Save DataFrame to .csv
data_all.to_csv(path_or_buf="/INSERT FILE PATH AND NAME HERE")
"""
