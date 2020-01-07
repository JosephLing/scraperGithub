# questions:
- what naming convention is most common for each config type?
- how spread out is the naming convention stats? and how does the age come into play? (note: age is  a stretch goal)
- proportion of the file that are comments
- what kind of comments are there in each configuration type?
    - header, inline, code comments, todos etc.
    - code to parse the yaml is 99% done
    - how do lines of comment relate to each other??? are the majority of comments just commented out config??
    - TODO: analyse of the data propery!!!
- what stage names are most common overall?
- what stage names get used most commonly together?
- what is the ratio of stage names being used per config type?
- how does yaml configuration differ from jenkins configuration???
- configuration errors
- language and os representation (and then how does that map too information displayed in the wiki)
- proportion of script tags and then names of scripts run (this is where a analysis on common patterns would be useful but stretch goal)
- size of configuration per config type and then size of configuration per language based on the configuration type (e.g. does a github action take up less code than a travis one on avg... depending if the sampling is big enough)

- branches...
- could look into detecting I/O???  

Future work: 
- look into analysis of version numbers e.g. what languages versions are actually being used??? (more in depth analysis of what they are being supported)




Need to refind a bunch of research papers maybe


there was a ncie one which linked the github stats













yaml:
- parse into json
- schema or manual schema fill into the object
- output object of the same type that can be used for comparison
- {key: {value, index}} in order to parse what order the config is written in

this method should be generic enough to be able to use for the other configuration type



-----------

re-run data gathering to make sure that jenkins data is gathered



Concise answerable research questions?

some teasers: different language behaviour in CI
meaty: comment structure, understanding CI
