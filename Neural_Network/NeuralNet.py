import Layer

class NeuralNet:
    def __init__(self, neural_net_dimensions): # [InputLayer, layer1, layer2, ..., layern, OutputLayer] - [10, 100, 100, 5]
        self.neural_net_dimensions=neural_net_dimensions
        self.layers=[]
        self.inputs=[]
        self.outputs=[]
        self.biases=[]
        self.weights=[]

        for i in range(len(neural_net_dimensions)-1):
            layer=i+1
            self.layers.append(Layer.Layer(name=i, layer_dimension=self.neural_net_dimensions[layer], input_dimension=self.neural_net_dimensions[layer-1]))

    def conf_neural_net(self, weights, biases):
        self.weights=weights
        self.biases=biases
        for i in range(len(self.neural_net_dimensions)-1):
            self.layers[i].conf_layer(self.weights[i], self.biases[i])

    def calc_result(self, inputs):
        self.inputs=inputs
        layer_output=self.inputs
        for i in range(len(self.neural_net_dimensions)-1):
            layer_output=self.layers[i].calc_layer_output(layer_output)
        self.outputs=layer_output
        return self.outputs

    def show(self):
        print("=" * 50)
        print(f" NEURALES NETZWERK (Architektur: {self.neural_net_dimensions})")
        print("=" * 50)

        for layer_index, layer in enumerate(self.layers):
            print(f"\n[ Layer {layer_index} ] (Anzahl Neuronen: {layer.layer_dimension})")
            print("-" * 40)

            for neuron in layer.neurons:
                # Gibt für jedes Neuron den Namen/Index, die Gewichte und den Bias aus
                print(f"  Neuron {neuron.name}:")
                print(f"    Gewichte: {neuron.weights}")
                print(f"    Bias:     {neuron.bias}")

        print("=" * 50)