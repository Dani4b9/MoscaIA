from dataclasses import dataclass

@dataclass
class Synapse:

    source: int

    target: int

    synapses: int

    neuropil: str

    neurotransmitter: str

    weight: float = 1.0