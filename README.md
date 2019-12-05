# bi-lstm-crf-ner-tf2.0

Named Entity Recognition (NER) task using Bi-LSTM-CRF model implemented in Tensorflow2.0.


# Requirements

- python >3.6
- tensorflow==2.0.0
- tensorflow-addons==0.6.0

# data 
data example 

    １	B-TIME
    ９	I-TIME
    ９	I-TIME
    ７	I-TIME
    年	E-TIME
    ，	O
    是	O
    中	B-LOC
    国	E-LOC
    发	O
    展	O
    历	O
    史	O
    上	O
    非	O
    常	O
    重	O
    要	O
    的	O
    很	O
    不	O
    平	O
    凡	O
    的	O
    一	O
    年	O
    。	O
    end

# Usage

## train
    $ # pip install requirement.txt
    $ python3 train.py
    
    ...
    [-INFO-] 2019-12-05 21:11:15,037 24300 epoch   1, step 575, loss  5.0533 , accuracy --
    [-INFO-] 2019-12-05 21:11:34,002 24300 epoch   1, step 576, loss  6.2023 , accuracy --
    [-INFO-] 2019-12-05 21:11:52,543 24300 epoch   1, step 577, loss  4.3899 , accuracy --
    [-INFO-] 2019-12-05 21:12:11,175 24300 epoch   1, step 578, loss  3.1313 , accuracy --
    [-INFO-] 2019-12-05 21:12:29,661 24300 epoch   1, step 579, loss  6.4625 , accuracy --
    [-INFO-] 2019-12-05 21:12:48,233 24300 epoch   1, step 580, loss  5.5159 , accuracy --
    [-INFO-] 2019-12-05 21:12:48,325 24300 model saved
    ...
    
## predict 

    $ python3 predict.py
    
    
    input: 中共中央总书记、国家主席江泽民发表１９９８年新年讲话
    
    [
        {
            "end": 4,
            "words": "中共中央",
            "type": "ORG",
            "begin": 1
        },
        {
            "end": 15,
            "words": "江泽民",
            "type": "PER",
            "begin": 13
        },
        {
            "end": 22,
            "words": "１９９８年",
            "type": "TIME",
            "begin": 18
        }
    ]
    

