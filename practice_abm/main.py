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
import agentpy as ap
import numpy as np
import matplotlib.pyplot as plt
import random  # Correctly importing the random module

class InnovationAgent(ap.Agent):
    """ Define an agent that can either adopt or not adopt an innovation. """
    def setup(self):
        self.adopted = False  # Initially, no agent has adopted the innovation

    def update(self):
        if not self.adopted:  # Check if the agent has not adopted yet
            neighbors = list(self.network.neighbors(self.id))
            adopted_neighbors = sum(1 for n in neighbors if self.model.agents[n].adopted)
            if adopted_neighbors / len(neighbors) > 0.4:
                self.adopted = True  # Adopt if more than half of the neighbors have adopted

class DiffusionModel(ap.Model):
    """ A model for the diffusion of an innovation in a network of agents. """
    def setup(self):
        # Create a network using the Watts-Strogatz model
        self.network = nx.watts_strogatz_graph(n=200, k=4, p=0.1)  # 100 nodes, each linked to 4 neighbors, 10% rewiring probability
        self.agents = ap.AgentList(self, 200, InnovationAgent)
        for index, agent in enumerate(self.agents):
            agent.network = self.network  # Assign the network to each agent
            agent.id = index  # Explicitly setting the agent's ID to match the network's node ID

        # Randomly set a few agents as adopters
        initial_adopters = random.sample(list(self.agents), 5)
        for agent in initial_adopters:
            agent.adopted = True

    def step(self):
        """ Define what happens in each model step. """
        self.agents.update()

    def end(self):
        """ Optionally, we can define actions at the end of the simulation. """
        # Plotting the network with color coding for adopted agents
        color_map = ['blue' if agent.adopted else 'red' for agent in self.agents]
        pos = nx.spring_layout(self.network)
        nx.draw(self.network, pos, node_color=color_map, node_size=200, with_labels=True)
        plt.show()



# Run the model
parameters = {
    'steps': 100,
}

model = DiffusionModel(parameters)
results = model.run()

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
