import asyncio
import datetime
import urllib.request
import concurrent.futures



def process_api_request(index):
    try:
        print(f"start api request {index}")
        filename = "sample.pdf"
        location1 = "./download/" + str(datetime.datetime.now().timestamp()) + filename
        location2 = "./download/" + str(index) + filename
        resp = urllib.request.urlretrieve('ftp://user:password@ftp.byethost14.com/htdocs/rb/sample.pdf', location1) #TODO change user and password
        print(f"end api request {index}")
        return resp
    except Exception as e:
        print(f"error: {str(e)}")
        return None
        
        
if __name__ == "__main__":
    concurrent_requests = 300
    from multiprocessing.dummy import Pool as ThreadPool
    pool = ThreadPool(concurrent_requests)
    results = pool.map(process_api_request, range(concurrent_requests))
    print("finished")
    
