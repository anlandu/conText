# Daily Progress
### 1.17
Investigated different NLP tools. The plan is to find a good Java one (OpenNLP sounds promising) and build my classes in Java.

### 1.19
Researched Project Gutenberg. Tried to download via mirror; this proved difficult/wget did not work out. Project Gutenberg very deliberately makes it difficult to download things.

### 1.22
Looked around GitHub to see what other Java libraries look like. Many have src, scripts, gradle folder/extensions? But lots of different structures. I'll also have a resources folder to store books in, and scripts for downloading books.

### 1.23
Initial commit! Plus, I continue to work on understanding the wget flags/what mirrors of wget look like.

### 1.24
Spent lots of time getting familiar with Gradle and Maven (which a lot of Java libraries I've looked at appear to have). Lots of stuff to learn about creating build.gradle, etc. Still not sure I know entirely what's happening, but I have a very minimal build.gradle.

### 1.26
Maven install errors have blocked me from installing OpenNLP, which I need for my project. Started work on the skeleton AverageWordLength class; however, because I can't install OpenNLP I have to figure out how to proceed.

### 1.29
Back to figuring out the Gutenberg side of things: Tried to use rsync. Wiped computer :(

### 1.30
Back on track. Began researching BeautifulSoup; don't dare venture down the rsync path again.

### 2.2
Planned out structure of classes. Think I'll focus on 1) word length and 2) part of speech tagging. The plan is to create a table for average word length for top 100 books, another for distribution of parts of speech, then use those to find the closest match in the given Gutenberg file.

### 2.5
Spent the weekend reading through BeautifulSoup documentation, working on scripts. Think it'll be easier to just focus on the top 100 books anyways, so worked on scraping that page.

### 2.6
Switched to Python. Much easier. Rather than all of that gradle business, I just need requirements.txt which is a blessing. Also, finished BeautifulSoup! It really is a fantastic tool.

### 2.7
Successfully created script that can download all 100 books, name them by their book names. Also created an individualized version; this facilitates the download of a single text. Think what I'll do is have that be an "update" type of function, which writes whatever the chosen book is under a specific name, so the other functions can use that file without needing the URL every time they're called.

### 2.8
Completed AverageWordLength.py. Think I might rework so that there's a paramaterized function and a non-paramaterized. We'll see how it's coming together Fri/weekend.


### 2.9
In the interest of preparing for next week, added CONTRIBUTING and CONDUCT. Plan to use the weekend to add documentation and finish up my POS tagging.

### 2.10-2.17

Partner work days!

### 2.19
Reworked the filenaming system, as special characters kept raising issues as I parsed the top 100 books. Still ironing out wrinkles in some files, almost have a complete and accurate dictionary of word lengths--should accomplish this tonight. Hopefully we can reuse lots of this code for top words.
