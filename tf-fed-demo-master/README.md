# tf-fed-demo
A federated learning demo for AlexNet on CIFAR-10 dataset, basing on Tensorflow.

## Dependence
1. Python 3.7
2. Tensorflow v1.14.x
3. tqdm

## Usage
```bash
cd ./src
python Server.py
``
Result£º
Dataset: train-50000, test-10000
  0%|          | 0/12 [00:00<?, ?it/s]WARNING:tensorflow:From D:\tf-fed-demo-master\tf-fed-demo-master\src\Client.py:69: Variable.load (from tensorflow.python.ops.variables) is deprecated and will be removed in a future version.
Instructions for updating:
Prefer Variable.assign which has equivalent behavior in 2.X.
100%|##########| 12/12 [01:38<00:00,  8.19s/it]
2020-07-08 20:35:32.122000: W tensorflow/core/framework/allocator.cc:107] Allocation of 58982400 exceeds 10% of system memory.
2020-07-08 20:35:32.296000: W tensorflow/core/framework/allocator.cc:107] Allocation of 58982400 exceeds 10% of system memory.
[epoch 1, 600 inst] Testing ACC: 0.1000, Loss: 2.3162
100%|##########| 12/12 [01:22<00:00,  6.90s/it]
2020-07-08 20:36:56.011000: W tensorflow/core/framework/allocator.cc:107] Allocation of 58982400 exceeds 10% of system memory.
2020-07-08 20:36:56.164000: W tensorflow/core/framework/allocator.cc:107] Allocation of 58982400 exceeds 10% of system memory.
[epoch 2, 600 inst] Testing ACC: 0.0850, Loss: 2.3071
100%|##########| 12/12 [01:23<00:00,  6.99s/it]
2020-07-08 20:38:20.715000: W tensorflow/core/framework/allocator.cc:107] Allocation of 58982400 exceeds 10% of system memory.
[epoch 3, 600 inst] Testing ACC: 0.1217, Loss: 2.2990
100%|##########| 12/12 [01:23<00:00,  6.93s/it]
[epoch 4, 600 inst] Testing ACC: 0.1517, Loss: 2.2893
100%|##########| 12/12 [01:22<00:00,  6.92s/it]
  0%|          | 0/12 [00:00<?, ?it/s][epoch 5, 600 inst] Testing ACC: 0.1600, Loss: 2.2514
100%|##########| 12/12 [01:23<00:00,  6.97s/it]
[epoch 6, 600 inst] Testing ACC: 0.1983, Loss: 2.1432
100%|##########| 12/12 [01:22<00:00,  6.91s/it]
[epoch 7, 600 inst] Testing ACC: 0.2250, Loss: 2.1135
100%|##########| 12/12 [01:22<00:00,  6.90s/it]
[epoch 8, 600 inst] Testing ACC: 0.2067, Loss: 2.0898
100%|##########| 12/12 [01:23<00:00,  6.92s/it]
[epoch 9, 600 inst] Testing ACC: 0.2367, Loss: 2.0539
100%|##########| 12/12 [01:23<00:00,  6.94s/it]
[epoch 10, 600 inst] Testing ACC: 0.2250, Loss: 2.0502
100%|##########| 12/12 [01:23<00:00,  6.93s/it]
  0%|          | 0/12 [00:00<?, ?it/s][epoch 11, 600 inst] Testing ACC: 0.2317, Loss: 2.0021