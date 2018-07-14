"""LiTour

Usage:
    litour.py [-f | -s | -n ]

Options:
    -h, --help              Show this screen.
    -f, --finished          Show finished tournaments
    -s, --started           Show started tournaments
    -n, --new               Show new/created tournaments
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

import requests
import datetime
import sys
from terminaltables import AsciiTable
from docopt import docopt


def main():
    args = docopt(__doc__, version='LiTour 1.0.0')
    utils(args)


def utils(args):
    url = "https://lichess.org/api/tournament"
    response = requests.get(url)
    json_data = response.json()

    if args["--new"]:
        table_data = [["S.NO", "Title", "variant", "StartsAt", "finishesAt", "Duration"]]
        table = created(json_data, table_data)
        print_table(table)
        ans = input("Do you want to add any tournament to your calendar ? y/n ")

        if ans.lower() == "y":
            handle_event(table[1:])
        else:
            sys.exit()

    elif args["--finished"]:
        table_data = [["S.NO", "Title", "variant", "Number-of-players", "Winner"]]
        table = finished(json_data, table_data)
        print_table(table)
    elif args["--started"]:
        table_data = [["S.NO", "Title", "variant", "FinishesAt", "Duration"]]
        table = started(json_data, table_data)
        print_table(table)


def finished(json_data, table_data):
    """Gets all the finished tournaments from the JSON data and shows the following:
        - name of the the tournament
        - variant of the tournament
        - winner of the tournament
        - Number of the palyers in the tournament
    """
    finished_tournaments = json_data['finished']
    count = 0
    for tournament in finished_tournaments:
        name = tournament['fullName']
        variant = tournament['variant']['name']
        winner = tournament['winner']['name']
        players = tournament['nbPlayers']
        count += 1
        table_data.append([count, name, variant, players, winner])

    return table_data


def created(json_data, table_data):
    """Gets all the newly created tournaments from JSON data and shows the following:
        - Name of the tournament
        - Time at which the tournament starts
        - Duration of the tournament
        - variant of the tournament
    """
    future_tournaments = json_data['created']
    count = 0
    for tournament in future_tournaments:
        name = tournament['fullName']
        starting_time = epoch_time(tournament['startsAt'])
        Duration = tournament['minutes']
        variant = tournament['variant']['name']
        finishesAt = epoch_time(tournament['finishesAt'])
        count += 1
        table_data.append([count, name, variant, starting_time, finishesAt, Duration])

    return table_data


def started(json_data, table_data):
    """Gets all the started tournaments from lichess.org and shows the following:
        - Name of the tournament
        - Variant of the tournament
        - Finishing time of the tournament
        - Duration of the tournament
    """
    started_tournaments = json_data['started']
    count = 0
    for tournament in started_tournaments:
        name = tournament['fullName']
        finish_time = epoch_time(tournament['finishesAt'])
        Duration = tournament['minutes']
        variant = tournament['variant']['name']
        count += 1
        table_data.append([count, name, variant, finish_time, Duration])

    return table_data


def get_credentials():
    """This gets your credentials from credentials.json file"""
    SCOPES = 'https://www.googleapis.com/auth/calendar'
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)

    return creds


def handle_event(table):
    """ Gets the credential and then authorize them
    """
    credential = get_credentials()
    event = make_events(table)
    service = build('calendar', 'v3', http=credential.authorize(Http()))
    event = service.events().insert(calendarId='primary', body=event).execute()
    print(colors(('Event created: %s' % (event.get('htmlLink'))), 32))


def make_events(table):
    """Makes a dictionary that have
        summary     Name of the tournament
        start       Starting time of the tournament
        end         Finishing time of the tournametn

        This dictionary is send to google calendar for adding an event.
    """
    row_num = input("Enter the row number for the tournament you want to add: ")
    event = {}
    for tournament in table:
        if int(row_num) == tournament[0]:
            event['summary'] = tournament[1]
            print(tournament[3])
            event['start'] = {'dateTime': RFC_time(tournament[3])}
            event['end'] = {'dateTime': RFC_time(tournament[4])}
            return event
    else:
        print(colors(("No tournament exists with id %s" % row_num), 31))


def print_table(table_data):
    """Generate a beautiful ascii table"""
    table = AsciiTable(table_data)
    table.inner_row_border = True
    print("\n")
    print(colors(table.table, 32))


def colors(string, color):
    """Makes thing color full :)"""
    return("\033[%sm%s\033[0m" % (color, string))


def epoch_time(time):
    """Takes milliseconds and then change it to epoch time
        :time: float value of time in milliseconds
        :return: epoch time format
    """
    date_time = datetime.datetime.fromtimestamp(time / 1000).strftime('%a, %d %b %Y %H:%M:%S')
    return date_time


def RFC_time(epoch_time: str):
    """Takes time in form of UTC and then change it into rfc 3339 time

        :epoch_time: string of epoch format i.e Thu, 26 Jul 2018 19:30:00
        :return: string of rfc 3339 format i.e 2018-07-26T19:30:00Z
    """
    rfc_time = datetime.datetime.strptime(epoch_time, '%a, %d %b %Y %H:%M:%S').isoformat("T") + "Z"
    return rfc_time


if __name__ == '__main__':
    main()
