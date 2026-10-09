import Neuron

class Layer:
    def __init__(self, name:str, size, input_size, output_size):
        self.input_size = input_size
        self.output_size = output_size
        self.name = name

        self.inputs = []
        self.outputs = []

        self.neurons = []

        for i in range(size):
            self.neurons.append(Neuron.Neuron(name=(name,i), weights=[0]*input_size, bias=0))

    def calc_out(self):
        neuron_output = 0
        for neuron in self.neurons:
            neuron_output =neuron.calc_out()
            self.outputs.append(neuron_output)
        