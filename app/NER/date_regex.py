import re
import datetime


def find_date(text):
  return None

def later_date(date):
    now = datetime.datetime.now()
    date_parsed = datetime.datetime.strptime(date, '%B %d, %Y')
    return now < date_parsed


if __name__ == '__main__':
    # Test your stuff.
    print find_date('June 15, 2018')
    # print find_date('There is no date in this sentence.')
    # print find_date('I would like to book a flight on 05/11/2018, please.')
