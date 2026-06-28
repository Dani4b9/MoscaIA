from brain.loader import ConnectomeLoader
from brain.simulation import BrainSimulation

# Cargar el conectoma
loader = ConnectomeLoader("data/Mosca NeuralScan")

brain = loader.cargar()

brain.stats()

# Obtener una neurona para la prueba
primer_id = next(iter(brain.neurons))

n = brain.get(primer_id)

print()
print("====== PRIMERA NEURONA ======")

print("ID:", n.root_id)
print("Grupo:", n.group)
print("Neurotransmisor:", n.nt_type)
print("Tipo:", n.cell_type)
print("Entradas:", len(n.incoming))
print("Salidas:", len(n.outgoing))

# Simulación
print()
print("===== SIMULACIÓN =====")

sim = BrainSimulation(brain)

sim.stimulate(primer_id)

for paso in range(5):

    dispararon = sim.step()

    print(f"Paso {paso + 1}")
    print(f"Neuronas activadas: {len(dispararon)}")

    if len(dispararon) > 0:
        print(dispararon[:10])

    print()