# RSS Feed Parser to JSON
This project is responsible for reading a specific RSS Feed and transforming it into a JSon file.

## How to install
1) Clone this repository
````
git clone https://github.com/taizarm/parser-feed-to-json-pyramid.git
````
2) Enter in the root folder of project
```
cd parser-feed-to-json-pyramid/
```
3) Create a virtualenv
```
virtualenv -p python3 .venv
```
4) Start virtualenv
```
source .venv/bin/activate
```
5) Install the requirements
````
pip install -r requirements.txt
````
6) Done!

## How to run standalone
1) Run the command:
```
python  python parser_feed_to_json_pyramid/parser/parser.py
```

2) Done! You will see the output in your console.

## How to run as webservice

1) Configure Pyramid project
```
python setup.py develop
```

2) Initialize Pyramid server
```
pserve development.ini --reload
```

3) Done! Access your localhost URL project: http://localhost:6543/. The default username is 'admin' and the default password is '1234admin'.


## How to run tests and see coverage

Be sure virtual env is activated. Run the command:

```
py.test --cov
```

If the coverage is not 100%, run this command to see the lines without tests:

```
coverage report -m
```
