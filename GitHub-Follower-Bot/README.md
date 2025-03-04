

## Description
This is a GitHub Follow Bot made inside of a Django application. Management of the bot is done inside of Django's default admin center (`/admin`). The bot itself runs in the background of the Django application.

The bot works as the following.

* Runs as a background task in the Django application.
* Management of bot is done in the Django application's web admin center.
* After installing, you must add a super user via Django (e.g. `python3 manage.py createsuperuser`).
* Navigate to the admin web center and add your target user (the user who will be following others) and seeders (users that start out the follow spread).
* After adding the users, add them to the target and seed user list.
* New/least updated users are parsed first up to the max users setting value followed by a random range wait scan time.
* A task is ran in the background for parsed users to make sure they're being followed by target users.
* Another task is ran in the background to retrieve target user's followers and if the Remove Following setting is on, it will automatically unfollow these specific users for the target users.
* Another task is ran that checks all users a target user is following and unfollows the user after *x* days (0 = doesn't unfollow).
* Each follow and unfollow is followed by a random range wait time which may be configured.

## To Do
* Develop a more randomized timing system including most likely active hours of the day.
* See if I can use something better in Django to alter general settings instead of relying on a table in the SQLite database. There are also issues with synchronization due to limitations with Django at this moment. 

## Requirements
The following Python models are required and I'd recommend Python version 3.8 or above since that's what I've tested with.

```
django
aiohttp
```

You can install them like the below.

```bash
# Python < 3
python -m pip install django
python -m pip install aiohttp

pip install django
pip install aiohttp

# Python >= 3
python3 -m pip install django
python3 -m pip install aiohttp

pip3 install django
pip3 install aiohttp
```


## Settings
Inside of the web interface, a settings model should be visible. The following settings should be inserted.

* **enabled** - Whether to enable the bot or not (should be "1" or "0").
* **max_scan_users** - The maximum users to parse at once before waiting for scan time.
* **wait_time_follow_min** - The minimum number of seconds to wait after following or unfollowing a user.
* **wait_time_follow_max** - The maximum number of seconds to wait after following or unfollowing a user.
* **wait_time_list_min** - The minimum number of seconds to wait after parsing a user's followers page.
* **wait_time_list_max** - The maximum number of seconds to wait after parsing a user's followers page.
* **scan_time_min** - The minimum number of seconds to wait after parsing a batch of users.
* **scan_time_max** - The maximum number of seconds to wait after parsing a batch of users.
* **verbose** - Verbose level for stdout (see levels below).
1. \+ Notification when a target user follows another user.
1. \+ Notification when a target user unfollows a user due to being on the follower list or purge.
1. \+ Notification when users are automatically created from follow spread.
* **user_agent** - The User Agent used to connect to the GitHub API.
* **seed** - Whether to seed (add any existing user's followers to the user list).
* **seed_min_free** - If above 0 and seeding is enabled, seeding will only occur when the amount of new users (users who haven't been followed by any target users) is below this value.
* **max_api_fails** - The max amount of GitHub API fails before stopping the bot for a period of time based off of below (0 = disable).
* **lockout_wait_min** - When the amount of fails exceeds max API fails, it will wait this time minimum in minutes until starting up again.
* **lockout_wait_max** - When the amount of fails exceeds max API fails, it will wait this time maximum in minutes until starting up again.
* **seed_max_pages** - The max amount of pages to seed from with each user parse when looking for new users (seeding).

## Installation
Installation should be performed like a regular Django application. This application uses SQLite as the database. You can read more about Django [here](https://docs.djangoproject.com/en/4.0/intro/tutorial01/). I would recommend the following commands.

```bash
# Make sure Django and aiohttp are installed for this user.

# Clone repository.
git clone https://github.com/gamemann/GitHub-Follower-Bot.git

# Change directory to Django application.
cd GitHub-Follower-Bot/src/github_follower

# Migrate database.
python3 manage.py migrate

# Run the development server on any IP (0.0.0.0) as port 8000.
# NOTE - If you don't want to expose the application publicly, bind it to a LAN IP instead (e.g. 10.50.0.4:8000 instead 0f 0.0.0.0:8000).
python3 manage.py runserver 0.0.0.0:8000

# Create super user for admin web interface.
python3 manage.py createsuperuser
```

The web interface should be located at `http://<host/ip>:<port>`. For example.

http://localhost:8000

