import csv
import urllib.request

class Request:
    def __init__(self):
        self.items = []

    def enqueue(self, request):
        self.items.insert(0, request)

    def size(self):
        return len(self.items)

class Server:
    def __init__(self):
        self.items = []

    def enqueue(self, process):
        self.items.insert(0, process)

    def size(self):
        return len(self.items)

def main(file):

    list = []
    response = urllib.request.urlopen(URL)
    weblog = response.read().decode('utf-8')
    weblog_lines = weblog.split("\r\n")
    csv_reader = csv.reader(weblog_lines, delimiter=',')

    list = [lines for lines in csv_reader]

    return list

if __name__ == "__main__":
    URL = 'http://s3.amazonaws.com/cuny-is211-spring2015/requests.csv'

    request_times = []
    process_times = []

    list_of_requests = main(URL)

    for items in list_of_requests:
        request_times.append(items[0])
        process_times.append(items[2])
    request_times = (list(map(int, request_times)))
    process_times = (list(map(int, process_times)))

    request = Request()
    for i in range (len(request_times)):
        request.enqueue(request_times[i])

    process = Server()
    for i in range(len(process_times)):
        process.enqueue((process_times[i]))

    length_of_request = request.size()
    length_of_process = process.size()

    if length_of_process == length_of_request:
        length = length_of_request = request.size()

    wait_time = []

    for i in range(length-1):
        if request.items[i] - request.items[i+1] < process.items[i]:
            wait_time.append(process.items[i])
    print("The average wait time is: " "%.1fs" % (sum(wait_time) /length))