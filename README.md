# AMR_Adversarial_Attacks
This is a repository includes the source codes of paper "Security Hardening of Intelligent Reflecting Surfaces Against Adversarial Machine Learning Attacks". (F. O. Catak, M. Kuzlu, H. Tang, E. Catak and Y. Zhao, in IEEE Access, vol. 10, pp. 100267-100275, 2022, doi: 10.1109/ACCESS.2022.3206012) 

## Installation & Usage
* **Run AMR for SISO Dataset:**
1. Download the SISO dataset (See [RML2016.10a](https://www.dropbox.com/scl/fo/md1b7n1xibyf500sdt8nq/h?dl=0&rlkey=y2b7ph8aozkyci7xgb3lv2z7t)) and save it under AMR_SISO folder. RML2016.10a has been used in most research as a benchmark dataset. It contains 220,000 signal samples, each associated with one specific modulation (11 modulations in total) at a particular Signal-to-Noise Ratio (SNR range: -20dB:2:18dB). Each sample input is a vector of size 256, which corresponds to 128 in-phase and 128 quadrature components.

2. Change the dataset filename in line 55 in `rmldataset2016.py`. 



* **Run AMR for SISO NEW Dataset:**
1. Download the SISO dataset (See [RML2016.10b](https://www.dropbox.com/s/pohcm3tft4kwk6h/RML2016.10b.dat?dl=0)) and save it under AMR_SISO folder.

2. Change the dataset filename in line 55 in `rmldataset2016.py`. 
