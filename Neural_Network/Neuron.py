import math

class Neuron:
    def __init__(self, name, weights, bias):
        self.name = name
        self.weights = weights
        self.bias = bias

        self.inputs = []

        self.outputs = []
        self.output = 0
        self.result = 0

    def reset_params(self):
        self.outputs = []
        self.output = 0

    def calc_out(self):
        for i in range(len(self.inputs)):
            self.outputs[i] = self.weights[i]*self.inputs[i]
        for i in range(len(self.outputs)):
            self.output = self.output + self.outputs[i]
        self.output = self.output + self.bias
        self.result = math.tanh(self.output)
        self.reset_params()
        return self.result