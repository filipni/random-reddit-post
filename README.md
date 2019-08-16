# Random reddit post
Python script for showing a random post from a specified subreddit.

## Background
This was originally a script I used with the Pythonista widget on my iPhone to show random jokes from [/r/jokes](https://www.reddit.com/r/Jokes/). It can be configured to show posts from any subreddit by changing the `SUBREDDIT` global variable.

## Usage
To use this script, you need to register the application on your reddit account. Go to **User Settings** under your profile and then **Privacy & Security > App authrization**. Create a new app, give it a name, and mark the *script* radio button. Also set the *redirect uri* to `http://localhost:8080`. Use the generated *app id* and *secret* together with your account information to fill in the missing fields in the beginning of the script. If you want longer posts to show, you need to increase the number of rows (`NUM_ROWS`) and/or the maximum row length (`ROW_MAX_LEN`).
