import numpy as np

class QubitSimulator:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.state = self.initialize_state()

    def initialize_state(self):
        # Initialize qubits in a superposition state
        state = np.ones((2 ** self.num_qubits,)) / np.sqrt(2 ** self.num_qubits)
        return state

    def apply_entropy_modulation(self, entropy_factor):
        # Adjust probabilities based on entropy factor
        noise = np.random.uniform(-entropy_factor, entropy_factor, size=self.state.shape)
        self.state += noise
        self.state /= np.linalg.norm(self.state)  # Normalize the state

    def measure_state(self):
        probabilities = np.abs(self.state) ** 2
        return np.random.choice(len(probabilities), p=probabilities)
