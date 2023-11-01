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

## Results
The code will produce two result files. First, it creates a ```results.json``` which contains the results for the autograder. The ```gg_api.py``` will automatically read the content of that file and feed it into the autograder. Secondly, we are creating a ```results.md``` file which is human readable and contains the same results. Furthermore, we added some visualizations to that file which show the results for the additional goals we had.

### Autograder
We achieved the following autograder scores on completeness and spelling:

#### 2013
|   |Hosts   |Awards   |Winners   |Presenters   |Nominees   |
|---|---|---|---|---|---|
|Spelling   |1.0   |0.8017327400895528   |0.5692918192918193   |0.5   |0.025227353449056973   |
|Completeness   |1.0   |0.14782608695652172   |   |0.5   |0.498493567251462   |

### Best Dressed
 0. Kate Hudson (0.11363636363636363)
    <img src='https://static.gofugyourself.com/uploads/2013/01/159422573.jpg' height=300px alt='Kate Hudson 2013 Golden Globes Dress'>
 1. Julia Roberts (0.10606060606060606)
    <img src='https://media1.popsugar-assets.com/files/thumbor/FH31FkzGw5pcpkJhotijvsmou1I/fit-in/1024x1024/filters:format_auto-!!-:strip_icc-!!-/2013/01/03/1/192/1922398/3d2882dc391eefa7_159445965_10/i/Julia-Roberts-presented-Golden-Globes-black-dress.jpg' height=300px alt='Julia Roberts 2013 Golden Globes Dress'>
 2. Lucy Liu (0.08333333333333333)
    <img src='http://applesandonions.com/wp-content/uploads/2013/01/lucy-liu-2013-golden-globes-red-carpet.jpg' height=300px alt='Lucy Liu 2013 Golden Globes Dress'>

### Worst Dressed
 0. Kate Hudson (0.11363636363636363)
    <img src='https://static.gofugyourself.com/uploads/2013/01/159422573.jpg' height=300px alt='Kate Hudson 2013 Golden Globes Dress'>
 1. Julia Roberts (0.10606060606060606)
    <img src='https://media1.popsugar-assets.com/files/thumbor/FH31FkzGw5pcpkJhotijvsmou1I/fit-in/1024x1024/filters:format_auto-!!-:strip_icc-!!-/2013/01/03/1/192/1922398/3d2882dc391eefa7_159445965_10/i/Julia-Roberts-presented-Golden-Globes-black-dress.jpg' height=300px alt='Julia Roberts 2013 Golden Globes Dress'>
 2. Lucy Liu (0.08333333333333333)
    <img src='http://applesandonions.com/wp-content/uploads/2013/01/lucy-liu-2013-golden-globes-red-carpet.jpg' height=300px alt='Lucy Liu 2013 Golden Globes Dress'>

### Best Joke
 0. Kate Hudson (0.11363636363636363)
    <img src='https://static.gofugyourself.com/uploads/2013/01/159422573.jpg' height=300px alt='Kate Hudson 2013 Golden Globes Dress'>
 1. Julia Roberts (0.10606060606060606)
    <img src='https://media1.popsugar-assets.com/files/thumbor/FH31FkzGw5pcpkJhotijvsmou1I/fit-in/1024x1024/filters:format_auto-!!-:strip_icc-!!-/2013/01/03/1/192/1922398/3d2882dc391eefa7_159445965_10/i/Julia-Roberts-presented-Golden-Globes-black-dress.jpg' height=300px alt='Julia Roberts 2013 Golden Globes Dress'>
 2. Lucy Liu (0.08333333333333333)
    <img src='http://applesandonions.com/wp-content/uploads/2013/01/lucy-liu-2013-golden-globes-red-carpet.jpg' height=300px alt='Lucy Liu 2013 Golden Globes Dress'>

### Performer
 0. Kate Hudson (0.11363636363636363)
    <img src='https://static.gofugyourself.com/uploads/2013/01/159422573.jpg' height=300px alt='Kate Hudson 2013 Golden Globes Dress'>
 1. Julia Roberts (0.10606060606060606)
    <img src='https://media1.popsugar-assets.com/files/thumbor/FH31FkzGw5pcpkJhotijvsmou1I/fit-in/1024x1024/filters:format_auto-!!-:strip_icc-!!-/2013/01/03/1/192/1922398/3d2882dc391eefa7_159445965_10/i/Julia-Roberts-presented-Golden-Globes-black-dress.jpg' height=300px alt='Julia Roberts 2013 Golden Globes Dress'>
 2. Lucy Liu (0.08333333333333333)
    <img src='http://applesandonions.com/wp-content/uploads/2013/01/lucy-liu-2013-golden-globes-red-carpet.jpg' height=300px alt='Lucy Liu 2013 Golden Globes Dress'>


## Authors

[Dong Shu](dongshu2024@u.northwestern.edu) KJJ8053

[Ding Zhang](dingzhang2025@u.northwestern.edu) KVK9920

[Haoran Zhao](haoranzhao2024@u.northwestern.edu) OUA1078

## References

* [amitadate/EECS-337-NLP-Project-01](https://github.com/amitadate/EECS-337-NLP-Project-01/blob/0899202832e0b8c64e308f3be851cc8d6387a47a/src/gg_api.py)
