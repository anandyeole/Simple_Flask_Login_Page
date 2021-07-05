# Flask Login Page

Allowing users to log in to your app is one of the most common features you’ll add to your web application.

# Prerequisites

- Python installed on local environment
- Any code editor such as vscode
- Basic knowledge of Python

# structure

Here is a diagram to provide a sense of what your project’s file structure will look like:

```
.
└── Simple_Flask_Login_Page
    └── project
        ├── __init__.py       # setup our app
        ├── auth.py           # the auth routes for our app
        ├── data.sqlite       # our database
        └── templates
            ├── base.html     # contains common layout and links
            ├── home.html     # show the home page
            ├── login.html    # show the login form
            ├── profile.html  # show the profile page
            ├── signup.html   # show the signup form
            └── 404.html      # show the invalid page
    ├── app.py                # routes for our app and file to run app
    └── requirements.txt      # all package requirements for app

```

# Installation

Clone this repo using

```sh
$ git clone https://github.com/anandyeole/Simple_Flask_Login_Page
```

Enter the directory and install all the requirements using

```sh
$ pip3 install -r requirements.txt
```

Run the app using

```
$ python3 app.py
```

Navigate to 127.0.0.1:5000 to see the Homepage

### © [anandyeole](https://github.com/anandyeole/)
