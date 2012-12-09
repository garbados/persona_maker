# Readme

In the marketing track of [Boston Startup School](http://www.bostonstartupschool.com/), we spend considerable time gathering data on our users and prospects online to study their activities, build user personas, and target messaging. Unfortunately, such research takes time and attention this slothful creature has in short supply, so I made robots do it for me.

Persona Maker is a Python script that uses [Requests](http://docs.python-requests.org/en/latest/) and [FullContact](http://www.fullcontact.com/) to aggregate user data, returning a list of topics your users are interested in or authoritative on, sorted by what appeared the most among your users.

# Installation

Install from github and get dependencies from pip:

  git clone git@github.com:garbados/persona_maker.git
  cd persona_maker
  virtualenv venv
  source venv/bin/activate
  pip install -r requirements.txt
  
# Configuration

You'll need a list of your users' emails in a format like this:

  ["bob@example.com", "unicorns@friendshipisland.com", "lolcats@inter.net"]
  
Then, rename `settings.py.example` to `settings.py` and, inside of it, change...

* `api_key` to your FullContact API key. If you don't have one, head over to FullContact, sign up for [a free account](http://www.fullcontact.com/developer/pricing/), and they'll give you one.
* `email_list` to a relative path from the project's root to the file containing your list of user emails.

That should be it for setup. 

# Usage

To construct your user persona:

  python miner.py
  python parser.py
  
`parser.py` should return output like this:

  [(u'Games', 10), (u'Cambridge', 8), (u'Internet Startups', 7), (u'Money', 5), (u'Kickstarter', 4)]
  
The number next to each phrase indicates the number of times that phrase appears in the topics your users are interested in or knowledgeable on. So, a report like the above shows that "Games" showed up 10 times among my users. [What nerds](http://www.maxthayer.org/games) :P

# License

Copyright (c) 2012 Max Thayer

Some rights reserved.

Redistribution and use of this software and associated documentation (the "Software") in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

The names of the contributors may not be used to endorse or promote products derived from this software without specific prior written permission.

If the Author of the Software (the "Author") needs a place to crash and you have a sofa available, you should maybe give the Author a break and let him sleep on your couch.

If you are caught in a dire situation wherein you only have enough time to save one person out of a group, and the Author is a member of that group, you must save the Author.