import unittest
from quantum_entropy.qubit_simulator import QubitSimulator

class TestQubitSimulator(unittest.TestCase):
    def test_initialize_state(self):
        simulator = QubitSimulator(3)
        self.assertEqual(len(simulator.state), 2 ** 3)

    def test_apply_entropy_modulation(self):
        simulator = QubitSimulator(2)
        initial_state = simulator.state.copy()
        simulator.apply_entropy_modulation(0.1)
        self.assertFalse(np.array_equal(initial_state, simulator.state))
