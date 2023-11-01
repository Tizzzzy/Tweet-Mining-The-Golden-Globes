# Tweet Mining & The Golden Globes

Repository for the first project in the course ' Natural Language Processing ' at Northwestern University

## Description

This is the first project for Northwestern's COMP337 - Natural Language Processing class. We are tasked to extract several information (such as hosts, awards, nominees, presenters, and winners) about each year's Golden Globes ceremony based on more than 170,000 tweets. 

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
- Put `ggYYYY.json` files in the root directory, such as `gg2013.json` or `gg2015.json`

- **Within the file `global_var.py`, change the constant `OFFICIAL_AWARDS` to that specific year's ground truth awards**

- Run `gg_api.py` to get the results

  ```shell
  python gg_api.py
  ```

- Run `autograder.py` to get completeness and spelling scores

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
|Spelling   |1.0   |0.8017327400895528   |0.5692918192918193   |0.5   |0.511293567251462   |
|Completeness   |1.0   |0.14782608695652172   |   |0.5   |0.02523999905687549   |

### Best Dressed
 1. Kate Hudson (0.1803921568627451)
   
    <img src='https://www.gotceleb.com/wp-content/uploads/celebrities/kate-hudson/2013-golden-globe-awards-in-beverly-hills/Kate-Hudson---Golden-Globe-Awards-2013--02.jpg' height=300px alt='Kate Hudson 2013 Golden Globes Dress'>


### Worst Dressed
 1. Sienna Miller (0.5833333333333334)
   
    <img src='https://imabeautygeek.com/.image/t_share/MTI3NDY5MjYxNzA5OTQxMjE0/sienna-miller-golden-globes-2015jpg.jpg' height=300px alt='sienna-miller-golden-globes-2015jpg'>
 2. Halle Berry (0.08333333333333333)
   
    <img src='https://s-i.huffpost.com/gen/939572/images/o-HALLE-BERRY-GOLDEN-GLOBES-2013-facebook.jpg' height=300px alt='Halle Berry'>


### Best Joke
 1. James Cameron (0.1048158640226629)
 2. Anne Hathaway (0.0708215297450425)
 3. Tina Fey Amy (0.06326723323890462)
 4. Taylor Swift (0.05193578847969783)
 5. Jennifer Lawrence (0.04343720491029273)
   

### Performer
 1. Anne Hathaway (0.14887640449438203)
 2. Daniel Day (0.07584269662921349)
 3. Les Miserables (0.07303370786516854)
 4. Les Mis (0.05056179775280899)
 5. Hugh Jackman (0.03651685393258427)

## Authors

[Dong Shu](dongshu2024@u.northwestern.edu)

[Ding Zhang](dingzhang2025@u.northwestern.edu)

[Haoran Zhao](haoranzhao2024@u.northwestern.edu)

## References

* [amitadate/EECS-337-NLP-Project-01](https://github.com/amitadate/EECS-337-NLP-Project-01/blob/0899202832e0b8c64e308f3be851cc8d6387a47a/src/gg_api.py)
* [Lukas-Justen/NLP-GoldenGlobes](https://github.com/Lukas-Justen/NLP-GoldenGlobes)
