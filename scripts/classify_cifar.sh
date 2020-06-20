python ./CIFAR_main.py --nBlocks 7 7 7 --nStrides 1 2 2 --nChannels 32 64 128 --coeff 0.9 --batch 128 --dataset cifar10 --init_ds 1 --inj_pad 13 --powerIterSpectralNorm 1 --save_dir ./results/zca_clf_full_cifar10_wrn22_inj_pad_coeff09 --nonlin elu --optimizer sgd --vis_server your.server.local --vis_port your_port_nr



// 20200617, parameters to replicate the CIFAR10 results with different c
python ./CIFAR_main.py --nBlocks 18 18 18 --nStrides 1 2 2 --nChannels 32 64 128 --coeff 0.9 --batch 128 --dataset cifar10 --init_ds 1 --inj_pad 13 --powerIterSpectralNorm 1  --nonlin elu --optimizer sgd --GPUs 0

python ./CIFAR_main.py --nBlocks 13 13 13 --nStrides 1 2 2 --nChannels 32 64 128 --coeff 0.9 --batch 128 --dataset cifar10 --init_ds 1 --inj_pad 13 --powerIterSpectralNorm 1  --nonlin elu --optimizer sgd --GPUs 1

python ./CIFAR_main.py --nBlocks 13 13 13 --nStrides 1 2 2 --nChannels 32 64 128 --coeff 0.8 --batch 128 --dataset cifar10 --init_ds 1 --inj_pad 13 --powerIterSpectralNorm 1  --nonlin elu --optimizer sgd --GPUs 2

python ./CIFAR_main.py --nBlocks 18 18 18 --nStrides 1 2 2 --nChannels 32 64 128 --coeff 0.8 --batch 128 --dataset cifar10 --init_ds 1 --inj_pad 13 --powerIterSpectralNorm 1  --nonlin elu --optimizer sgd --GPUs 3

python ./CIFAR_main.py --nBlocks 18 18 18 --nStrides 1 2 2 --nChannels 32 64 128 --coeff 0.5 --batch 128 --dataset cifar10 --init_ds 1 --inj_pad 13 --powerIterSpectralNorm 1  --nonlin elu --optimizer sgd --GPUs 4

python ./CIFAR_main.py --nBlocks 13 13 13 --nStrides 1 2 2 --nChannels 32 64 128 --coeff 0.5 --batch 128 --dataset cifar10 --init_ds 1 --inj_pad 13 --powerIterSpectralNorm 1  --nonlin elu --optimizer sgd --GPUs 5

Conclusion: 

// 20200618, basic structure is right, try MNIST dataset
python ./CIFAR_main.py --nBlocks 13 13 13 --nStrides 1 2 2 --nChannels 32 64 128 --coeff 0.5 --batch 128 --dataset cifar10 --init_ds 1 --inj_pad 13 --powerIterSpectralNorm 1  --nonlin elu --optimizer sgd --GPUs 5