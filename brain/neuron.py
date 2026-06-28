from dataclasses import dataclass, field

@dataclass
class Neuron:

    root_id: int

    group: str | None = None

    nt_type: str | None = None

    cell_type: str | None = None

    additional_types: str | None = None

    position: str | None = None

    incoming: list = field(default_factory=list)
    outgoing: list = field(default_factory=list)

    activation: float = 0.0

    threshold: float = 1.0

    fired: bool = False

    refractory: int = 0