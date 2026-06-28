from pathlib import Path

import pandas as pd

from brain.brain import Brain
from brain.neuron import Neuron
from brain.synapse import Synapse


class ConnectomeLoader:

    def __init__(self, carpeta):

        self.carpeta = Path(carpeta)

    def cargar(self):

        print("\n==========")
        print("MOSCA IA")
        print("==========\n")

        brain = Brain()

        print("Leyendo neuronas...")

        neurons = pd.read_csv(
            self.carpeta / "neurons.csv.gz"
        )

        cell_types = pd.read_csv(
            self.carpeta / "consolidated_cell_types.csv.gz"
        )

        coordinates = pd.read_csv(
            self.carpeta / "coordinates.csv.gz"
        )

        # Índices rápidos

        tipos = {}

        for _, row in cell_types.iterrows():

            tipos[row.root_id] = (
                row["primary_type"],
                row["additional_type(s)"]
            )

        posiciones = {}

        for _, row in coordinates.iterrows():

            posiciones[row.root_id] = row.position

        # Crear neuronas

        for _, row in neurons.iterrows():

            cell_type, extra = tipos.get(
                row.root_id,
                (None, None)
            )

            neuron = Neuron(

                root_id=row.root_id,

                group=row.group,

                nt_type=row.nt_type,

                cell_type=cell_type,

                additional_types=extra,

                position=posiciones.get(row.root_id)

            )

            brain.add_neuron(neuron)

        print(f"{len(brain.neurons):,} neuronas creadas.")

        print()

        print("Leyendo conexiones...")

        connections = pd.read_csv(
            self.carpeta / "connections_princeton.csv.gz"
        )

        for _, row in connections.iterrows():

            synapse = Synapse(

                source=row.pre_root_id,

                target=row.post_root_id,

                synapses=row.syn_count,

                neuropil=row.neuropil,

                neurotransmitter=row.nt_type

            )

            brain.add_synapse(synapse)

        print(f"{len(brain.synapses):,} conexiones creadas.")

        return brain