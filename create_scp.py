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

def create_scp(scp_root, **data_dir):
    for k,v in data_dir.items():
        scp_file = os.path.join(scp_root, f"{k}.scp")
        with open(scp_file, 'w') as f: #w - opens the file for writing (it overwrites existing content or creates a new file if needed)
            
            for root, dirs, files in os.walk(v):
                                
                for file in sorted(files): # sort files to ensure the order is predictable
                    f.write(file + ' ' + root + '/' + file) # structure -> "file absolute_path"
                    f.write('\n')
                    

def handle_scp(scp_file: str) -> dict:
    '''
        input: scp file
        output: scp dictionary -> {'.wav':'absolute path'}
    '''
    scp_data = dict()

    open with(scp_file, 'r') as f:
        for line_num, line in enumerate(f, start=1):
            scp_line = line.strip.split()
            if len(scp_line) != 2:
                raise RuntimeError(f"For {scp_file}, format error in line {line_num}: {scp_line}")
            k,v = scp_line
            if k in scp_data:
                raise ValueError(f"Duplicated key '{k}' exists in line {line_num} on {scp_file}")
            
            scp_data[k] = v
            
    return scp_data
    
if __name__ == "__main__":
    
    #Directory where scp files are saved, end with '/'
    scp_root = '../data/'

    # Set the paths for your SCP files and the corresponding data directories.
    create_scp(scp_root, 
               train_mix = '../wsj0-2mix/2speakers/wav8k/min/tr/mix',
               train_s1 = '../wsj0-2mix/2speakers/wav8k/min/tr/s1',
               train_s2 = '../wsj0-2mix/2speakers/wav8k/min/tr/s2',
               
               test_mix = '../wsj0-2mix/2speakers/wav8k/min/tt/mix',
               test_s1 = '../wsj0-2mix/2speakers/wav8k/min/tt/s1',
               test_s2 = '../wsj0-2mix/2speakers/wav8k/min/tt/s2',
               
               cv_mix = '../wsj0-2mix/2speakers/wav8k/min/cv/mix',
               cv_s1 = '../wsj0-2mix/2speakers/wav8k/min/cv/s1',
               cv_s2 = '../wsj0-2mix/2speakers/wav8k/min/cv/s2',
               )

    scp_file = '../data/train_mix.scp'
    scp_dict = handle(scp_file)
    print(type(scp_dict)）

    for k, v in list(scp_dict.items())[:5]:
    print(k,v)
