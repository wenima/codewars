"""Solution for codewars kata Scraping: Codewars Top 500 Users"""

from bs4 import BeautifulSoup
import requests
import re
from itertools import islice


class User(object):
    """Create User objects for storage in a Leaderboard Object.
    Attributes:
    name:       user's username
    clan:       user's clan affiliation
    honor:      user's honor points as an integer
    """
    def __init__(self, user=None):
        """Initialize a User object."""
        if user:
            self.name, self.clan, self.honor = user
        else:
            self.name = None
            self.clan = None
            self.honor = None


class Leaderboard(object):
    """Create a Leaderboard object.
    Attributes:
    _size:          The length of the position property
    Properties:
    position:       returns a list of objects of users

    """
    def __init__(self, list_of_users=None):
        """Intialize a Leaderboard Object."""
        self.position = None
        if list_of_users:
            self.position = list_of_users


class CustomList(list):
    """Create a subclass of list with len() being ovewritten to be able to
    return the first element by using 1 instead of 0."""
    def __len__(self):
        len = 0
        for i in self:
            len += 1
        return len - 1


url = 'https://www.codewars.com/users/leaderboard'


def get_clean_username(s):
    patterns = [r'kyu(.*)', r'dan(.*)']
    for pattern in patterns:
        match = re.search(pattern, s)
        if match:
            return match.group(1)
        else:
            continue


def create_users_from_soup(soup):
    users = []
    for user in soup.find_all('tr', {"data-username": lambda x: x}):
        users.append([col.text for col in user.find_all('td')])
    user_objs = CustomList()
    user_objs.append('')
    for user in users:
        user[1] = get_clean_username(user[1])
        user[3] = int(user[3])
        user_objs.append(User([field for field in islice(user, 1, None)]))
    return user_objs


def solution():
    response = requests.get(url)
    html_file = response.text
    soup = BeautifulSoup(html_file,'lxml')
    user_objs = create_users_from_soup(soup)
    leaderboard = Leaderboard(user_objs)
    return leaderboard
