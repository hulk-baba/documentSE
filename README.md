# Document Search Engine using Django and C++
Document Search Engine allows you to perform queries among thousands of documents having thousands of words, and producing relevant 
threshold result to tour disposal. This project depends on the physical limitation of single machine as it has not been horizontally scaled.
This Project is fundamentally an algorithmic project with potential scope for pre-processing the document. In this project, emphasis has been given
on working with pdf files is given.

## Prerequisites and Installation
Obviously, like any other python project we nee a virtual environment. You can perform this setup by following instructions
from [here](http://docs.python-guide.org/en/latest/dev/virtualenvs/).
To run this project locally on your system you need following 
```
dj-database-url==0.4.2
Django==1.10.6
django-tastypie==0.13.3
djangorestframework==3.6.2
gunicorn==19.7.1
python-dateutil==2.6.0
python-mimeparse==1.6.0
requests==2.13.0
six==1.10.0
wheel==0.24.0
whitenoise==3.3.0
psycopg2==2.6.2
```
These can also be installed using the command ```pip install -r requirements.txt``` where ```requirements.txt``` has been provided
as part of project. Now we have everything we need to test the waters.
##
##Running and navigating the project
Now, you can clone this project using ```git clone``` command. Change your directory to documentSE using ```cd documentSE```. Now perform
an ```ls``` and you can see ```manage.py```. This is the file django provides you. Perform ```python manage.py runserver```. If everywent went 
okay, it will perform system checks and say ```Starting development server at http://127.0.0.1:8000/``` like [this](https://imgur.com/a/6YWwS). 
At this point we have successfully run the project and see the interface as [here](https://imgur.com/a/Y7pcd).
Now you can explore the features of the project.

## Features
1. SignUp - User can be added to the database.
2. Login - Existing users can log in to the database.
3. Post New Document - Existing user can post a new doucment in the database which can be queried later by anu other user.
4. Filter - Can filter all the documents by four major categories pdf, doc, images and others.
5. Search - Can perform your queries to get relevant results. This depends just on the associated keywords of the document while uploading.
6. Ultra Search - Performs deep search by going through the documents and analyzes frequency of important keywords to give results.


## Algorithmic solution used here 
This projects uses ***Trie data structure*** to store documents the contents of the document which takes linear time in terms of size of
document for each document. Once a trie is built for every document. Query takes just linear time in terms of size of query multiplied by 
number of documents. This is a big save against any pattern matching algorithms like KMP, Aho–Corasick etc. The django project uses external
C++ app to make trie for each document as C++ is fast, this is very helpful. 
[This](https://imgur.com/a/rMKAm) is how dashboard looks.
