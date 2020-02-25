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

scraper.py to create the data 

then run main.py with the .env setup to CHECK and then RENDER to create all the things

orca will be required in order to render the plotly sankey graph

`npm install -g electron@1.8.4 orca1`

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
    - need to make this more consistent so we can get a long run for this!!! [X]
- group the data sets into one large one [X]
- process the data removing duplicates [X]
- get the graphs for language and thing type to create sepearte graphs for each thing
    - get that to pick up on when there is no configuration in the % otherwise it is squed
- yaml parser project!

Bugs:
- none so far....

Fixed:
- watchers aren't being picked up properly
- consistent high speed data gathering is hard atm
    - read time out 
    - 502 error
    ```log
    saving >>> drizzleDumper
    saving >>> DZNSegmentedControl
    saving >>> DLCImagePickerController
    Traceback (most recent call last):
      File "main.py", line 254, in <module>
        main()
      File "main.py", line 226, in main
        getReposStuff("raptor_webb", i, i + 100)
      File "main.py", line 185, in getReposStuff
        saveData = saveRepos(page, ["" for i in range(len(page))], name)
      File "main.py", line 42, in saveRepos
        dictionary = dict([(k, fixEncoding(getattr(repo, k))) for k in keys])
      File "main.py", line 42, in <listcomp>
        dictionary = dict([(k, fixEncoding(getattr(repo, k))) for k in keys])
      File "/home/eat/jl653/private/scraperGithub/venv2/lib/python3.6/site-packages/github/Repository.py", line 732, in topics
        self._completeIfNotSet(self._topics)
      File "/home/eat/jl653/private/scraperGithub/venv2/lib/python3.6/site-packages/github/GithubObject.py", line 262, in _completeIfNotSet
        self._completeIfNeeded()
      File "/home/eat/jl653/private/scraperGithub/venv2/lib/python3.6/site-packages/github/GithubObject.py", line 266, in _completeIfNeeded
        self.__complete()
      File "/home/eat/jl653/private/scraperGithub/venv2/lib/python3.6/site-packages/github/GithubObject.py", line 273, in __complete
        self._url.value
      File "/home/eat/jl653/private/scraperGithub/venv2/lib/python3.6/site-packages/github/Requester.py", line 268, in requestJsonAndCheck
        return self.__check(*self.requestJson(verb, url, parameters, headers, input, self.__customConnection(url)))
      File "/home/eat/jl653/private/scraperGithub/venv2/lib/python3.6/site-packages/github/Requester.py", line 279, in __check
        raise self.__createException(status, responseHeaders, output)
    github.GithubException.GithubException: 502 {"message": "Server Error"}
    ``` 
    so probably could but an exception handler around this to ignore it maybe???

- jenkins configuration wasn't being picked up as we were only getting .yml or .yaml file types
    - this should be good validation but do we want data for weird files that don't match???

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
- loc [x] 

what do people use CI for????
testing or deployment or notifications
for deplosy: the tag and maybe string search in noticiations but not 100% reliable as scripts







groups configuration lines of code distribution 

distribution per language and the length of the ci script
