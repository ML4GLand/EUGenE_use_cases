import torch
import torch.nn as nn
import torch.nn.functional as F
from eugene.models.base import _layers as layers
from eugene.models.base import _blocks as blocks
from eugene.models.base import _towers as towers


class DeepMEL(nn.Module): 
    def __init__(
        self,
        input_len: int,
        output_dim: int,
        conv_kwargs: dict = {},
        recurrent_kwargs: dict = {},
        dense_kwargs: dict = {}
    ):
        super(DeepMEL, self).__init__()

        self.input_len = input_len
        self.output_dim = output_dim
        
        self.conv_kwargs, self.recurrent_kwargs, self.dense_kwargs = self.kwarg_handler(
            conv_kwargs, recurrent_kwargs, dense_kwargs
        )
        self.conv1d_tower = towers.Conv1DTower(**self.conv_kwargs)
        self.recurrent_block = blocks.RecurrentBlock(
            input_dim=self.conv1d_tower.out_channels, 
            **self.recurrent_kwargs
        )
        self.dense_block = blocks.DenseBlock(
            input_dim=self.recurrent_block.out_channels,
            output_dim=output_dim, 
            **self.dense_kwargs
        )

    def forward(self, x, x_rev_comp=None):
        x = self.conv1d_tower(x)
        x = x.transpose(1, 2)
        out, _ = self.recurrent_block(x)
        out = self.dense_block(out[:, -1, :])
        return out

    def kwarg_handler(self, conv_kwargs, recurrent_kwargs, dense_kwargs):
        """Sets default kwargs for conv and fc modules if not specified"""
        conv_kwargs.setdefault("input_len", self.input_len)
        conv_kwargs.setdefault("input_channels", 4)
        conv_kwargs.setdefault("conv_channels", [128])
        conv_kwargs.setdefault("conv_kernels", [20])
        conv_kwargs.setdefault("conv_strides", [1])
        conv_kwargs.setdefault("conv_padding", "valid")
        conv_kwargs.setdefault("pool_kernels", [20])
        conv_kwargs.setdefault("dropout_rates", 0.2)
        conv_kwargs.setdefault("activations", "relu")
        conv_kwargs.setdefault("batchnorm", False)
        recurrent_kwargs.setdefault("unit_type", "lstm")
        recurrent_kwargs.setdefault("hidden_dim", 128)
        #recurrent_kwargs.setdefault("dropout_rates", 0.2)
        recurrent_kwargs.setdefault("bidirectional", True)
        recurrent_kwargs.setdefault("batch_first", True)
        dense_kwargs.setdefault("hidden_dims", [256])
        dense_kwargs.setdefault("dropout_rates", 0.4)
        dense_kwargs.setdefault("batchnorm", False)
        return conv_kwargs, recurrent_kwargs, dense_kwargs