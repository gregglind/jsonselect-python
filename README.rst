==========================
JSONSelect for Python
==========================

Description
----------------

Search and Mangle JSONable data, using ``css`` style selectors,
and jQuery-like chainable methods.  (Python port)

(based on lloyd's excellent JSONSelect project)

Setup
---------

    pip install jsonselect

Basic Usage
-------------

    >>> from jsonselect import J
    >>> J(".a")({'a':1, 'b': 'a':[1,2,3])
    [1, [1,2,3]]


Testing
--------------

    cd /path/to/json-select
    setup.py test

Develop
------------

* fork this repo 
* clone
* create a topic branch off ``development`` 
* file a bug / pull

cf:  http://blog.mozilla.com/webdev/2011/11/21/git-using-topic-branches-and-interactive-rebasing-effectively/

To grab my changes...

    git remote add gregglind git://github.com/gregglind/jsonselect-python.git
    git rebase gregglind/master  # or upstream/development or whatnot

See Also
------------

* http://jsonselect.org/
