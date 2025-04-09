import os

'''
This script creates SCP files for your dataset.

For example, if you're working with the wsj0-2mix dataset, here's what your file tree might look like:

wsj0-2mix/
└── 2speakers/
    └── wav8k/
        └── min/
            ├── cv
            │   ├── mix
            │   │   └── 6300370419826092098_00001_1.3679_6306811582279909115_00026_-1.3679.wav
            │   ├── s1
            │   │   └── 6300370419826092098_00001_1.3679_6306811582279909115_00026_-1.3679.wav
            │   └── s2
            │       └── 6300370419826092098_00001_1.3679_6306811582279909115_00026_-1.3679.wav
            ├── tr
            │   └── ... (other files)
            └── tt
                └── ... (other files)

This script will go through your data directory and automatically generate SCP files listing each file's name and full path.
'''

def create_scp(scp_file_path, data_dir):
    
    with open(scp_file_path, 'w+') as f:
        # 'w+' opens the file for writing (it overwrites existing content or creates a new file if needed)
        
        for root, dirs, files in os.walk(data_dir):
            files.sort() # sort files to ensure the order is predictable
            for file in files:
                f.write(file + ' ' + root + '/' + file) # structure -> "file absolute_path"
                f.write('\n')



if __name__ == "__main__":
    
    # Set the paths for your SCP files and the corresponding data directories.
    
    # Scp file
    train_mix_scp = '../tr_mix.scp'
    train_s1_scp = '../tr_s1.scp'
    train_s2_scp = '../tr_s2.scp'
    # Data dir
    train_mix = '../wsj0-2mix/2speakers/wav8k/min/tr/mix'
    train_s1 = '../wsj0-2mix/2speakers/wav8k/min/tr/s1'
    train_s2 = '../wsj0-2mix/2speakers/wav8k/min/tr/s2'
    

    create_scp(train_mix_scp, train_mix)