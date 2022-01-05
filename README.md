Exercise: Templates
wincpy start 9263bbfddbeb4a0397de231a1e33240a

You'll need the Flask documentation for this exercise:

Flask -- Quickstart
After starting this exercise with Wincpy, you'll find this folder structure:

.
├── __init__.py
├── main.py
├── static
│   └── style.css
├── templates
│   ├── about.html
│   ├── base.html
│   └── index.html
└── test_main.py
You can run this Flask project with the command:

FLASK_APP=main FLASK_DEBUG=1 flask run

Step 1
First, modify the template base.html so that title , where it says <title>PLACEHOLDER</title> now, becomes a variable that Jinja is going to fill in for us later. The contents of this title tag is used to name the browser tab where the page is opened and to name bookmarks that are created of this page.

You can check this with pytest.

Step 2
Now write a Flask app that conforms to the specification in the following table.

Method	Path	Expected Response
GET	/home	302 redirect to /
GET	/	A rendering of the template index.html with the <title>: Index
GET	/about	A rendering of the template about.html with the <title>: About
Up to this point, you can test your work with pytest.

Step 3
Add a third page besides the index and about pages according to the same pattern.

It should have a unique url where it can be found.
It should have a place in the navigation list so that it can navigated to.
It should have a representive title in the <title> tag.
It should make use of base.html to avoid having lots of duplicate code.
There are no tests for this part. You could write your own tests in test_main.py or test visually.

