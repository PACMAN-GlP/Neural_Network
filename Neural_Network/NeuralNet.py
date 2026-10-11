import Layer

class NeuralNet:
    def __init__(self, neural_net_dimensions): # [InputLayer, layer1, layer2, ..., layern, OutputLayer] - [10, 100, 100, 5]
        self.neural_net_dimensions=neural_net_dimensions
        self.layers=[]
        self.inputs=[]
        self.outputs=[]
        self.biases=[]
        self.weights=[]


        for i in range(len(neural_net_dimensions)-2):
            layer=i+1
            self.layers.append(Layer.Layer(self.neural_net_dimensions[layer], self.neural_net_dimensions[layer-1]))

    def conf_neural_net(self, weights, biases):
        self.weights=weights
        self.biases=biases
        for i in range(len(self.layers)-2):
            self.layers[i+1].conf_layer(self.weights[i], self.biases[i])

    def calc_result(self, inputs):
        self.inputs=inputs
        layer_output=self.inputs
        for i in range(len(self.neural_net_dimensions)):
            layer_output=self.layers[i].calc_layer_output(self.inputs)
        self.outputs=layer_output
        return self.outputs