# Pitch Perfect

## Description
This is  an application that allows users to submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.

## Link to deployed site
 

## user stories
* view pitches
* login
* pitch
* downvote and upvote
* view personal pitches on profile
* comment on pitches

## BDD
| Behavior           | Input                 | Outcome                            |
| -------------------|-----------------------| -----------------------------------|
| request page       | click horuku link url | view othr pitches  & vote          |
| click on a pitch   |                       | vote/comment                       |
| sign in/up         | details pass & user   | view,pitch & comment               |

# Landing page
Welcomes you to the page
![screenshot](app/static/images/whatif.png)

# loging in
When you have an account you log in and when you dont you sign
![screenshot](app/static/images/login.png)

# on your timeline
![screenshot](app/static/images/time.png)




#### Prerequisites
1. Python 3.6
2. Pip
3. virtualenv

## Setup/Installation Requirements
* Internet access
* git clone
* $ cd into Pitch_perfect
* $ python3.6 -m venv virtual (install virtual environment)
* $ source virtual/bin/activate
* $ python3.6 -m pip install -r requirements.txt (install all dependencies)
* Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = * create_app('production') should be app = create_app('development')
* $ ./start.sh
* Open [localhost:5000](http://127.0.0.1:5000/)

## Technologies Used
* Python 3.6.5
* Flask Framework
* HTML/CSS
* JavaScript

## Further help
Contact me at wilsonowino1@gmail.com if you run into any issue or have any questions

### License
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files, to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Copyright (c) wilson owino




