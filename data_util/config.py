import os

root_dir = os.path.expanduser("~")
# path
dataset_path = "../../../Datasets/MultiWOZ_2.2_v2/"
data_path = "./data/"
vocab_path = data_path + "vocab.txt"
model_save_dir = "./ckpt/"
model_path = "multiwoz_model.bin"
emb_file = "./data/glove.6B.300d.txt"

# model hyperparameters
hidden_dim = 192
emb_dim = 300
emb_dorpout = 0.8
lstm_dropout = 0.5
attention_dropout = 0.1
num_attention_heads = 8

# hyperparameters
max_len = 32
lr_scheduler_gama = 0.5
batch_size= 32
epoch = 20
seed = 9
lr=0.001
eps = 1e-12
use_gpu=True

