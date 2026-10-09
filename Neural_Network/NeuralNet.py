import Layer

class NeuralNet:
    def __init__(self, layers):
        self.layers = layers

    def calc_output(self):
        self.outputs = []
        for layer in self.layers:
            pass