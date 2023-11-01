# Tweet Mining & The Golden Globes

Repository for the first project in the course ' Natural Language Processing ' at Northwestern University

## Description

Extract information about Golden Globes in tweets.

## Getting Started

### Dependencies

* We use Python 3.10 for experiment.
* Please refter to [requirement.txt](./requirement.txt) to install related modules.

### Installing

* Please download our code as a zip file
* You can also clone our git repo
  ```shell
  git clone https://github.com/Tizzzzy/CS337_northwestern.git
  ```

### Executing program

* Create a virtual environment if needed and activate the environment

* Install all required dependency

  ```shell
  pip install -r requirements.txt
  ```
- Put "ggYYYY.json" files in the root directory, such as gg2013.json or gg2015.json

- Run gg_api.pyto get the results

  ```shell
  python gg_api.py
  ```

- Run autograder.py to get completeness and spelling scores

  ```shell
  python autograder.py
  ```

## Authors

[Dong Shu](dongshu2024@u.northwestern.edu) KJJ8053

[Ding Zhang](dingzhang2025@u.northwestern.edu) KVK9920

[Haoran Zhao](haoranzhao2024@u.northwestern.edu) OUA1078

## References

* [amitadate/EECS-337-NLP-Project-01](https://github.com/amitadate/EECS-337-NLP-Project-01/blob/0899202832e0b8c64e308f3be851cc8d6387a47a/src/gg_api.py)
