Sumo Logic Sample Lambda Webhook Function
=========================================

Let's say you wanted to respond to an alert from Sumo Logic, what are your opptions?

* Slack Message

* Pager Duty

* Script Action

* AWS Lambda

The last is something where you can configure AWS lambdas and control their use.

What is possible?
=================

Pretty much anything that is possible with a script, so the first step is understand your response.

For the example in this script, this can create/adjust a VPC, create and add to an ACL.

Other actions could be to add/restrict control on AWS buckets, or stop/start services within your VPC.


Installing the Scripts
=======================

The scripts are CLI based, designed as a stand alone CLI or incorporated in a DevOPs tool such as Chef or Ansible.

Written in python3, all scripts are listed below, and there is a Pipfile to show what modules are required to run.

You will need to use Python 3.6 or higher and the modules listed in the dependency section.  

Please follow the following steps to install:

    1. Download and install python 3.6 or higher from python.org. Append python3 to the LIB and PATH env.

    2. Download and install git for your platform if you don't already have it installed.
       It can be downloaded from https://git-scm.com/downloads
    
    3. Open a new shell/command prompt. It must be new since only a new shell will include the new python 
       path that was created in step 1. Cd to the folder where you want to install the scripts.
    
    4. Execute the following command to install pipenv, which will manage all of the library dependencies:
    
        sudo -H pip3 install pipenv 
 
    5. Clone this repository and change into the directory.

    6. run pipenv to install dependencies (this may take a while as this will download required libraries):

        pipenv install
        
Dependencies
============

See the contents of "pipfile"

Script Names and Purposes
=========================

Scripts and Functions:

    1. ./bin/sumologic_sample_aws_lambda_soar_action.py

NOTE: this is an example. You will need to configure this for yourself.

Recommended Reading
===================

* [AWS Lambda Getting Started](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)

* [Sumo Logic AWS Webhook Setup](https://help.sumologic.com/Manage/Connections-and-Integrations/Webhook-Connections/Webhook_Connection_for_AWS_Lambda)

License
=======

Copyright 2022 Wayne Kirk Schmidt

Licensed under the GNU GPL License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    license-name   GNU GPL
    license-url    http://www.gnu.org/licenses/gpl.html

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Support
=======

Feel free to e-mail me with issues to: 

* wschmidt@sumologic.com

* wayne.kirk.schmidt@gmail.com

I will provide "best effort" fixes and extend the scripts.

