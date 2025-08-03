import requests


class Client:
    def __init__(self):
        self.addr = "https://api.github.com/octocat"
        self.headers = {
            "content-type": "text/plain",
            "X-GitHub-Api-Version": "2022-11-28",
          }

    def get_cat(self):
        ret = requests.get(self.addr, headers=self.headers)
        return ret.text


if __name__ == '__main__':
    cl = Client()
    print(cl.get_cat())