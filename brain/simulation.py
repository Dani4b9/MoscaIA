from collections import deque


class BrainSimulation:

    def __init__(self, brain):

        self.brain = brain
        self.queue = deque()
        self.time = 0

    def stimulate(self, neuron_id, strength=1.0):

        neuron = self.brain.get(neuron_id)

        if neuron is None:
            return False

        neuron.activation += strength
        self.queue.append(neuron)

        return True

    def step(self):

        self.time += 1

        fired = []

        current = len(self.queue)

        for _ in range(current):

            neuron = self.queue.popleft()

            if neuron.activation < neuron.threshold:
                continue

            neuron.fired = True

            fired.append(neuron.root_id)

            neuron.activation = 0

            for synapse in neuron.outgoing:

                target = self.brain.get(synapse.target)

                if target is None:
                    continue

                target.activation += synapse.weight

                if target.activation >= target.threshold:

                    self.queue.append(target)

        return fired