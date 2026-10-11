import Neuron

class Layer:
    def __init__(self, layer_dimension, input_dimension):
        self.layer_inputs=[]
        self.input_dimension=input_dimension
        self.outputs=[]
        self.neurons=[]
        self.layer_dimension=layer_dimension
        self.biases=[]
        self.weights=[]

        for i in range(self.layer_dimension):
            one_neuron_weights=[0]*self.input_dimension
            self.neurons.append(Neuron.Neuron(name=i, weights=one_neuron_weights, bias=0))
            self.biases.append(0)
            self.weights.append(one_neuron_weights)

    def conf_layer(self, weights, biases):
        self.weights=weights
        self.biases=biases
        for i in range(len(self.neurons)):
            self.neurons[i].conf_neuron(self.weights[i], self.biases[i])

    def calc_layer_output(self, layer_inputs):
        self.layer_inputs=layer_inputs
        self.outputs=[]
        for i in range(self.layer_dimension):
            self.outputs.append(self.neurons[i].calc_neuron_output(layer_inputs))
        return self.outputs