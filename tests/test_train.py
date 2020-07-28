import unittest
import torch
from utils import get_network
from models.resnet import resnet18

class TestTrain(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_readParams(self):

        # net = get_network('resnet18', False)
        net = resnet18()

        for name, param in net.named_parameters():
            print(name, param.shape)


if __name__ == "__main__":
    unittest.main()