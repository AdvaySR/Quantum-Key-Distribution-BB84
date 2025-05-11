import os
import numpy as np
from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_bloch_vector
from qiskit.quantum_info import Statevector , Pauli
import matplotlib.pyplot as plt

# ===== CONFIG =====
KEY_LENGTH = 16
os.environ['QISKIT_NO_ACCELERATE'] = '1'

def generate_quantum_key():
    """Generate quantum key using BB84 protocol with eavesdropping detection"""
    alice_bits = np.random.randint(2, size=KEY_LENGTH)
    alice_bases = np.random.choice(['+', '×'], size=KEY_LENGTH)
    bob_bases = np.random.choice(['+', '×'], size=KEY_LENGTH)
    eve_bases = np.random.choice(['+', '×'], size=KEY_LENGTH)

    backend = Aer.get_backend('qasm_simulator')
    key = []
    bob_measured_bits = []
    alice_matching_bits = []

    for i in range(KEY_LENGTH):
        # Alice prepares qubit
        qc = QuantumCircuit(1, 1)
        if alice_bases[i] == '×':
            qc.h(0)
        if alice_bits[i] == 1:
            qc.x(0)

        # Eve intercepts
        if eve_bases[i] == '×':
            qc.h(0)
        qc.measure(0, 0)
        result = execute(qc, backend, shots=1).result()
        eve_bit = int(list(result.get_counts().keys())[0])

        # Bob measures
        qc = QuantumCircuit(1, 1)
        if eve_bit:
            qc.x(0)
        if bob_bases[i] == '×':
            qc.h(0)
        qc.measure(0, 0)
        result = execute(qc, backend, shots=1).result()
        bob_bit = int(list(result.get_counts().keys())[0])

        if alice_bases[i] == bob_bases[i]:
            alice_matching_bits.append(alice_bits[i])
            bob_measured_bits.append(bob_bit)
            key.append(str(bob_bit))

    error_rate = np.mean(np.abs(np.array(alice_matching_bits) - np.array(bob_measured_bits))) if alice_matching_bits else 0

    return ''.join(key), error_rate, alice_bits, bob_measured_bits

def visualize_qubit(bit, basis):
    """Visualize qubit state on Bloch sphere"""
    try:
        # Create quantum state
        qc = QuantumCircuit(1)
        if bit == 1:
            qc.x(0)
        if basis == '×':
            qc.h(0)
            
        # Get statevector and convert to Bloch coordinates
        state = Statevector.from_instruction(qc)
        bloch_coords = [
            state.expectation_value(Pauli('X')).real,  # Now Pauli is defined
            state.expectation_value(Pauli('Y')).real,
            state.expectation_value(Pauli('Z')).real
        ]
        
        # Plot and save
        fig = plot_bloch_vector(bloch_coords, title=f"Bit: {bit}, Basis: {basis}")
        fig.savefig("bloch_sphere.png", bbox_inches='tight')
        print(" Bloch sphere saved as 'bloch_sphere.png'")
        plt.close(fig)
        
    except Exception as e:
        print(f" Visualization error: {str(e)}")

def clear_screen():
    """Clear terminal screen cross-platform"""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print("⚛️ QUANTUM KEY DISTRIBUTION SIMULATOR")
    print(f"Generating {KEY_LENGTH}-bit key with BB84 protocol...\n")

    quantum_key, error_rate, alice_bits, bob_bits = generate_quantum_key()

    print(f"Generated Key: {quantum_key}")
    print(f"Estimated Eavesdropping Error Rate: {error_rate:.2%}")

    # Visualize first qubit
    print("\nVisualizing first qubit states:")
    visual_basis = np.random.choice(['+', '×'])
    print(f"Alice's bit 0: {alice_bits[0]} | Basis: {visual_basis}")
    visualize_qubit(alice_bits[0], visual_basis)

    input("\nPress Enter to verify key...")
    clear_screen()

    attempts = 3
    while attempts > 0:
        try:
            print(f"\nAttempts left: {attempts}")
            user_input = input("Enter the key exactly: ").strip()

            if len(user_input) != len(quantum_key):
                print(f"ERROR: Key must be {len(quantum_key)} digits!")
                continue
            if not user_input.isdigit():
                print("ERROR: Only numbers allowed!")
                continue

            if user_input == quantum_key:
                print("\n ACCESS GRANTED!")
                print("Secret message: 'Schrödinger's cat is alive!'")
                break
            else:
                attempts -= 1
                print(" Incorrect key!")

        except KeyboardInterrupt:
            print("\n Session cancelled")
            break

    if attempts == 0:
        print("\n TOO MANY FAILED ATTEMPTS!")
        if error_rate > 0.1:
            print("Warning: High error rate suggests eavesdropping!")

if __name__ == "__main__":
    main()
