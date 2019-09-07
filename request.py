import requests
import sys

url = 'https://robotics.ece.pdx.edu/api/announcements.php'
data = {
        'username': 'discordbot',
        'password': 'discordrobotics',
        'data': 'insert data here'
        }

if __name__ == "__main__":
    if len(sys.argv) == 2:
        data['data'] = sys.argv[1]
    x = requests.post(url, data)
