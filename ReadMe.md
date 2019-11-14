list of sites we will scrap:
- Jenkinsfile
- travis yml
- gitlab yml
- circle ci yml
- go cd yml


Most of them can be done via search query into csv file. However JenkinsFile will be really hard to search for as it doesn't have a file extension to search for :(


# to run
pip install -r requirements.txt

create .env file with token inside named GITHUB_TOKEN

python main.py to run


## notes from latests meeting (12/11/2019)

how much things differ from standard templates for given languages? for travis and other languages 
- detect snippets as described in docs
- before and after scripts

- comment frequency and single line vs multi line

results need to publishable

do they use build matrices etc.?

what other enviroment variables do they use?

how do they use stages / tasks ? and how are they executed?

groups configuration lines of code distribution 

distribution per language and the length of the ci script


plan:
- finish scrapping the data [ ]
- group the data sets into one large one [ ]
- process the data removing duplicates [ ]
- based on the questions above come up with ways answering from the data
	- get half way through doing that 



csv -> line -> base64 -> text -> yaml


so it seems like it could be possible to create a python set of classes for parsing the yaml
or we could just have them as yaml objects



yaml:
- present:
  - build matrices
  - enviroment varaibles and secrets
- analyses
  - how do they use stages and tasks? what are common names etc. how does this differ per langauge
  - comments lines and line vs blocks of comments
- adv analysis:
  - how much things differ from standard templates for given languages? for travis and other languages 
    - detect snippets as described in docs
    - before and after scripts
- loc 


groups configuration lines of code distribution 

distribution per language and the length of the ci script
