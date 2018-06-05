# LiTour

LiTour is a simple python script that gets you information about the tournaments on lichess.org. You can also add any upcoming tournament in google calendar all this without leaving your beloved terminal.

## Usage

Run `Litour.py ` with the follwoing options:


    Usage:
        litour.py [-f | -s | -n ]

    Options:
        -h, --help              Show help screen.
        -f, --finished          Show finished tournaments
        -s, --started           Show started tournaments
        -n, --new               Show new/created tournaments


For adding the tournament to your Google calendar all you have to do is provide the id of the tournament.
Id of the tournament can be obtained from the list of new tournaments.

## Example

*  Finished tournament
![alt text](https://github.com/mzfr/LiTour/blob/master/images/finished_tournament.png)

-------------------------------------------------------------------------------

* Started tournaments
![alt text](https://github.com/mzfr/LiTour/blob/master/images/started_tournament.png)

-------------------------------------------------------------------------------

* Created tournaments
![alt text](https://github.com/mzfr/LiTour/blob/master/images/new_tournament.png)

- If you choose new tournaments then you'll have another option of adding a tournament as an event.

 ![alt text](https://github.com/mzfr/LiTour/blob/master/images/new.png)

- If you choose to add an event to your calendar, it will look like:

 ![alt text](https://github.com/mzfr/LiTour/blob/master/images/calendar.png)


## Installation

* You will need python 3
* Run `pip install -r requirements.txt`
* Now you need access to google api. For that follow the steps:
    1) Visit Google's [Python Quickstart](https://developers.google.com/calendar/quickstart/python) page and follow the steps.
    2) You can skip Step 2 i.e ` Install the Google Client Library` because you already installed requirements
    3) On Step 3 i.e `Set up the sample` you'll have to make a small change in example. Change
    `SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'` to
    `SCOPES = 'https://www.googleapis.com/auth/calendar'`
    4) In step 3 we are requesting reading and writing credential for ourself instead of getting just `read-only` credentials.
    5) After completing all the steps you'll have a credentials.json file

    **Note**

    If credentials.json file is not present in the current working directory then check for `.credentials` folder in your `home` directory

    By now you should have a client_secret.json and a credentials.json file.
    If you have them then you are good to go.
