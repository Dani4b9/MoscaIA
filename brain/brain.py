from brain.neuron import Neuron
from brain.synapse import Synapse

class Brain:

    def __init__(self):

        self.neurons = {}

        self.synapses = []

    def add_neuron(self, neuron):

        self.neurons[neuron.root_id] = neuron

    def add_synapse(self, synapse):

        self.synapses.append(synapse)

        if synapse.source in self.neurons:
            self.neurons[synapse.source].outgoing.append(synapse)

        if synapse.target in self.neurons:
            self.neurons[synapse.target].incoming.append(synapse)

    def get(self, root_id):

        return self.neurons.get(root_id)

    def stats(self):

        print()
        print("========== CEREBRO ==========")
        print(f"Neuronas : {len(self.neurons):,}")
        print(f"Sinapsis : {len(self.synapses):,}")
        print("=============================")