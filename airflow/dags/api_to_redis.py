import redis
import requests

r = redis.Redis('redis', db=0)
URL = 'https://api.namefake.com/'


def main():
    k = requests.get(URL).json()['name']
    r.set(k, 'bar')

if __name__ == '__main__':
    main()

