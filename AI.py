import numpy
import scipy.special
import matplotlib.pyplot

class NeuralNetWork:
    def __init__(self,input_nodes,hidden_nodes,output_nodes,lerning_rate):
        self.inodes = input_nodes
        self.hnodes = hidden_nodes
        self.onodes = output_nodes
        # Коэффициент обучения
        self.lr = lerning_rate
        # Матрицы весовых коэфициентов связей wih (между входным и скрытым
        # слоями) и who (между скрытым и выходным слоями)
        # Весовые коэфициентиы связей между узлом i и узлом j следующего слоя
        # обозначены как w_i_j:
        # w11  w21
        # w12  w22 и т.д.
        self.wih = numpy.random.normal (0.0, pow(self.hnodes, -0.5),(self.hnodes,self.inodes))
        self.who = numpy.random.normal (0.0, pow(self.onodes, -0.5),(self.onodes,self.hnodes))
        #использовании сигмоиды в качестве функции активации
        self.activation_function = lambda x: scipy.special.expit(x)
    
    def train(self,inputs_list,targets_list):
        # преобразование списков в двумерные массивы
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list,ndmin=2).T
    
        #рассчитать входящие сигналы для скрытого слоя
        hidden_inputs = numpy.dot(self.wih,inputs)
        #рассчитать исходящие сигналы для скрытого слоя
        hidden_outputs = self.activation_function(hidden_inputs)
    
        #рассчитать входящие сигналы для выходного слоя
        final_inputs = numpy.dot(self.who,hidden_outputs)
        #рассчитать исходящие сигналы для выходного слоя
        final_outputs = self.activation_function(final_inputs)
        
        #ошибки вызодного слоя = (целевое значение - фактическое знаечение)
        output_errors = targets - final_outputs
        #ошибки скрытного слоя - это ошибки output_errors,
        #распределенные пропорционально весовым коэффициентам связей
        #и рекомбинации на скрытых узлах
        hidden_errors = numpy.dot(self.who.T,output_errors)
        
        self.who += self.lr * numpy.dot( (output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
        #обновить весовые коэффициенты для связей между скрытым и выходным слоем
        self.wih += self.lr * numpy.dot( (hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))
        
    def query(self,inputs_list):
        #преобразование в список входных знаечний
        #в двумерный массив
        inputs = numpy.array(inputs_list,ndmin=2).T
        
        #рассчитать входящие сигналы для скрытого слоя
        hidden_inputs = numpy.dot(self.wih, inputs)
        #рассчитать исходящие сигналы для скрытого слоя
        hidden_outputs = self.activation_function(hidden_inputs)
        
        #рассчитать входящие сигналы для выходного слоя
        final_inputs = numpy.dot(self.who,hidden_outputs)
        #рассчитать исходящие сигналы для выходного слоя
        final_outputs = self.activation_function(final_inputs)
        
        return final_outputs
        
        
input_nodes = 784
hidden_nodes = 100
output_nodes = 10
lerning_rate = 0.3

ans = NeuralNetWork(input_nodes,hidden_nodes,output_nodes,lerning_rate)

data_file = open('C:/Users/user1/Desktop/mnist_dataset/mnist_train.csv','r')
data_list = data_file.readlines()
data_file.close()

for record in data_list[0:100]:
    all_values = record.split(',')
    inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    targets = numpy.zeros(onodes) + 0.01
    targets[int(all_values[0])] = 0.99
    
    ans.train(inputs,targets)
    print(targets)
