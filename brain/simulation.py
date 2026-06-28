from collections import deque


class BrainSimulation:

    def __init__(self, brain):

        self.brain = brain
        self.queue = deque()

        self.time = 0

        self.total_fired = 0

    def stimulate(self, neuron_id, strength=1.0):

        neuron = self.brain.get(neuron_id)

        if neuron is None:
            return False

        neuron.activation += strength

        self.queue.append(neuron)

        return True

    def step(self):

        self.time += 1

        fired_count = 0

        current_size = len(self.queue)

        visited = set()

        queued = set()
        
        for _ in range(current_size):

            neuron = self.queue.popleft()

            if neuron.refractory > 0:
                neuron.refractory -= 1
                continue

            if neuron.root_id in visited:
                continue

            visited.add(neuron.root_id)

            if neuron.activation < neuron.threshold:
                continue

            fired_count += 1

            self.total_fired += 1

            neuron.activation = 0

            neuron.refractory = 3

            for synapse in neuron.outgoing:

                target = self.brain.get(synapse.target)

                if target is None:
                    continue

                target.activation += synapse.weight

                if (
                    target.root_id not in visited
                    and target.root_id not in queued
                ):
                    self.queue.append(target)
                    queued.add(target.root_id)
        return fired_count