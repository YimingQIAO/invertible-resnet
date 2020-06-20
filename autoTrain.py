import os
from multiprocessing import Process,Manager
import numpy as np
import signal
import time

cmd = []


classification_base_cmd = 'python ./CIFAR_main.py --nBlocks 18 18 18 --nStrides 1 2 2 --nChannels 32 64 128 --coeff 0.9 --batch 128 --dataset cifar10 --init_ds 1 --inj_pad 13 --powerIterSpectralNorm 1 --save_dir ./results/zca_clf_full_cifar10_wrn22_inj_pad_coeff09 --nonlin elu --optimizer sgd'

dens_base_cmd = 'python CIFAR_main.py --nBlocks 16 16 16 --nStrides 1 2 2 --nChannels 512 512 512 --coeff 0.9 -densityEstimation -multiScale --lr 0.003 --weight_decay 0. --numSeriesTerms 5 --dataset cifar10 --batch 128 --warmup_epochs 1 --save_dir ./results/dens_est_cifar'

nBlocks = 18
coeffs = [0.9]
dataset = 'cifar10'

for coeff in coeffs:
    cmd.append('python CIFAR_main.py --original_resnet {original} --epochs 20 --nBlocks 16 16 16 --nStrides 1 2 2 --nChannels 512 512 512 --coeff {coeff} -densityEstimation -multiScale --lr 0.003 --weight_decay 0. --numSeriesTerms 5 --dataset cifar10 --batch 128 --warmup_epochs 1 --save_dir ./results/density_estimation_cifar_coeff{coeff}_orig{original}_0619'.format(coeff=coeff, original=1) + ' --GPUs 0 1 2 3')
    
#     cmd.append('python CIFAR_main.py --original_resnet {original} --epochs 20 --nBlocks 16 16 16 --nStrides 1 2 2 --nChannels 512 512 512 --coeff {coeff} -densityEstimation -multiScale --lr 0.003 --weight_decay 0. --numSeriesTerms 5 --dataset cifar10 --batch 128 --warmup_epochs 1 --save_dir ./results/density_estimation_cifar_coeff{coeff}_orig{original}_0619'.format(coeff=coeff, original=0) + ' --GPUs 4 5 6 7')
    
#     cmd.append('python ./CIFAR_main.py -densityEstimation --epochs 2 --nBlocks {nBlocks} {nBlocks} {nBlocks} --nStrides 1 2 2 --nChannels 32 64 128 --coeff {coeff} --batch 128 --dataset {dataset} --init_ds 1 --inj_pad 13 --powerIterSpectralNorm 1 --save_dir ./results/classication_dataset{dataset}_coeff{coeff}_nBlocks{nBlocks} --nonlin elu --optimizer sgd'.format(nBlocks=nBlocks, coeff=coeff, dataset=dataset) + ' --GPUs {}')







def run(command, gpu_id, gpu_state):
    # os.system(command.format(gpu_id))
    os.system(command)
    gpu_state[str(gpu_id)] = True

def terminate_handler():
    print('Terminate process {}'.format(os.getpid()))
    try:
        print('The processes is {}'.format(processes))
        for p in processes:
            print('Process {} terminates'.format(p.pid))
            p.terminate()
    except Exception as e:
        print(str(e))
        
if __name__ == '__main__':
    signal.signal(signal.SIGTERM, terminate_handler)
    
    gpu_state = Manager().dict({str(i): True for i in range(1, 8)})
    processes = []
    index = 0
    
    while index < len(cmd):
        for gpu_id in range(1, 8):
            if gpu_state[str(gpu_id)] == True:
                gpu_state[str(gpu_id)] = False
                p = Process(target=run, args=(cmd[index], gpu_id, gpu_state), name=str(gpu_id))
                p.start()
                print(gpu_state)
                processes.append(p)
                index += 1
                break
                
    for p in processes:
        p.join()