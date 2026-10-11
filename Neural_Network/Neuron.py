import math

class Neuron:
    def __init__(self, name, weights, bias):
        self.inputs=[]
        self.weights=weights
        self.bias=bias
        self.output=0

    def conf_neuron(self, weights, bias):
        self.weights=weights
        self.bias=bias

    def calc_neuron_output(self, neuron_inputs):
        self.inputs=neuron_inputs
        self.output=0
        if len(self.inputs) != len(self.weights):
            print("Amount of weights and inputs dont match!")

        for i in range(len(self.inputs)):
            self.output = self.output + (self.inputs[i] * self.weights[i])
        self.output = self.output + self.bias
        return math.tanh(self.output)