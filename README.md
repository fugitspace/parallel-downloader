# Parallel Files Downloader
----

You can use this tool to easily download multiple files fast.
It is useful for cases when you have multiple URLs to download from.

## Requirements
You need Python 3 and urllib3 module which comes in standard with Python.

## Configuration
in downloader.py you need to make a few configurations

* `urls = [] ` a list of URLs do download.

* `delimiter = '/'` this is what marks the beginning of the file name. it defaults to a /

* `workers = 2` depending on how many URLs you have, you may want to increase this number, or just set it to one
for cases when you only have one URL

* `path = '.'` set this to the directory where you want the downloaded files to be saved. your account has to have write permissions
this defaults to the the current directory

## Running
After you have the configurations, you can simply run the script as
```python downloader.py```

Sit back and relax your files download.