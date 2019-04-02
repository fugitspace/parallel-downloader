import urllib3
import os
import concurrent.futures

'''Configuration'''
urls = []
delimiter = '/'
workers = 2
path = '.'

'''XXXXXXXXXXXXXXXXXXXXX-----no editing beyond this point-----XXXXXXXXXXXXXXXX'''
http = urllib3.PoolManager()
def downloads(url):
    file_name = url[url.rindex(delimiter)+1:]
    f = open(path+file_name, 'wb+')
    data = http.request('GET', url, preload_content=False)
    print("Downloading {}".format(file_name))
    size = int(data.getheaders()['Content-Length'])
    done = 0
    for chunk in data.stream():
        done += f.write(chunk)
        print("{} done: {:.2f}%".format(file_name, done/size*100))
    f.close()
    print("Finished downloading {}".format(file_name))

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        executor.map(download, urls)