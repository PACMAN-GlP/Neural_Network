import NeuralNet

net = NeuralNet.NeuralNet([2, 3, 1])  # 2 Inputs, 1 Hidden Layer mit 3 Neuronen, 1 Output-Neuron

# (Für Layer 1: 3 Neuronen, jedes hat 2 Gewichte; Für Layer 2: 1 Neuron mit 3 Gewichten)
weights = [
    [[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]],  # Layer 1
    [[0.7, 0.8, 0.9]]                      # Layer 2
]
biases = [
    [0.1, 0.2, 0.3],  # Layer 1
    [0.4]             # Layer 2
]

net.conf_neural_net(weights, biases)
ergebnis = net.calc_result([1.0, 0.5])
print("Netzwerk-Ausgabe:", ergebnis)