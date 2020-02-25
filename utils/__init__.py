# encoding: utf-8
# ******************************************************
# Author       : zzw922cn
# Last modified: 2017-12-09 11:00
# Email        : zzw922cn@gmail.com
# Filename     : __init__.py
# Description  : Utils function for Automatic Speech Recognition
# ******************************************************

from utils.calcPER import calc_PER
from utils.functionDictUtils import activation_functions_dict, optimizer_functions_dict
from utils.lnRNNCell import BasicRNNCell as lnBasicRNNCell
from utils.lnRNNCell import GRUCell as lnGRUCell
from utils.lnRNNCell import BasicLSTMCell as lnBasicLSTMCell
from utils.taskUtils import check_path_exists, get_num_classes, dotdict
from utils.utils import setAttrs, getAttrs, describe, dropout, batch_norm, data_lists_to_batches, load_batched_data, list_dirs, get_edit_distance, output_to_sequence, target2phoneme, count_params, logging, list_to_sparse_tensor
from utils.visualization import plotWaveform
