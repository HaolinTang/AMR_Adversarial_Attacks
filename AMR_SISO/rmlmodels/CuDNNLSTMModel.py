"""CLDNNLike model for RadioML.

# Reference:

- [CONVOLUTIONAL,LONG SHORT-TERM MEMORY, FULLY CONNECTED DEEP NEURAL NETWORKS ]

Adapted from code contributed by Mika.
"""
import os

from keras.models import Model
from keras.layers import Input,Dense,Conv1D,MaxPool1D,ReLU,Dropout,Softmax
from keras.layers import LSTM,CuDNNLSTM,Bidirectional,Flatten,LSTM
from keras.utils.vis_utils import plot_model

def LSTMModel(weights=None,
             input_shape=[128,2],
             classes=11,
             **kwargs):
    if weights is not None and not (os.path.exists(weights)):
        raise ValueError('The `weights` argument should be either '
                         '`None` (random initialization), '
                         'or the path to the weights file to be loaded.')

    input = Input(input_shape,name='input')
    x = input

    #LSTM Unit
    x = CuDNNLSTM(units=128,return_sequences = True)(x)
    x = CuDNNLSTM(units=128)(x)

    #DNN
    x = Dense(classes,activation='softmax',name='softmax')(x)

    model = Model(inputs = input,outputs = x)

    # Load weights.
    if weights is not None:
        model.load_weights(weights)

    return model

import keras
if __name__ == '__main__':
    model = LSTMModel(None,input_shape=(128,2),classes=11)

    adam = keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)
    model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer=adam)
    plot_model(model, to_file='model.png',show_shapes=True) # print model

    print('models layers:', model.layers)
    print('models config:', model.get_config())
    print('models summary:', model.summary())