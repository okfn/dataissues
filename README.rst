User Stories
============

3 types of use case:

1. Report and manage issues - requires sharing
2. Error logging and analytics - why share?
3. Data quality reporting for data publishers - requires sharing

   * Establish transparency about errors in open data apps (data quality reports)

Store/Log Low-level Errors
--------------------------

As a **Data Wrangler** I want to **Pipe my errors into an online system** so that **I can review them later**

Notes:

* What are errors? Example: Cell B20 in sheet X is empty and should be float


Associate an Error with an Issue
--------------------------------

As a **....** I want to **have an error or set of errors associated with an issue (automatically?)** so that **fix them in bulk**

Generate a Report of Errors
---------------------------

As a **...** I want to **generate an aggregate report of all the errors on a task and their associated issues** so that **I can see patterns**


Create an Issue
------------

As a **Data User** I want to **report a problem with a dataset** so that **it can be fixed by the owner and I can see that it was fixed (or not!)**

Notes:

* An Issue can be an Error (as above) but also can be higher level - e.g. all dates are in yyyy-dd-mm format rather than yyyy-mm-dd

Close an Issue
--------------

As a **Task Owner** I want to **close an issue** so that **I can indicate its fixed (or that it won't be fixed etc)**


Be Notified of an update to an Issue
------------------------------------

...


Design
======

Objects
-------

* Task
* Issue
* Error

Task
~~~~

| id | slug | title | description | owner_name | private_key | api_key

Error
~~~~~

Generating task:

* repo_url - 
* dataset_url - 
* triggering_user
* run_id - 

Info on the actual error:
 
* timestamp
* record_id - row number in most cases
* source_path  - input file name
* dest_path - output file name - ??
* source_field/attribute - 
* dest_field - ??
* query (xpath, sql) - when you do scraping you have xpath or css selector etc
* value - erroneous value
* level - debug, info, error, warning
* error_type - ValidationError, TypeError, ValueError, ... 
* publisher_name
* publisher_id
* dataset_url
* message - JSON structured message with more info?

Issue
~~~~~

| id | dataset_id | title | description | creator | assigned | created | last_modified | status

status = 'open', 'closed'

issue_comment

| id | issue_id | description | action | user_id

action = comment || closing || reopening

