# LiTour

LiTour is a simple python script that gets you information about the tournaments on lichess.org You can also add any upcoming tournament in google calendar all this without leaving your beloved terminal.

### Requirement

* python 3
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

### Usage

Run `Litour.py ` with the follwoing options:

    ```
    Usage:
        litour.py [-f | -s | -n ]

    Options:
        -h, --help              Show help screen.
        -f, --finished          Show finished tournaments
        -s, --started           Show started tournaments
        -n, --new               Show new/created tournaments
    ```

For adding the tournament to your Google calendar all you have to do is provide the id of the tournament.
Id of the tournament can be obtained from the list of new tournaments.

### Example

* Run `Litour.py -f`

```
| S.NO | Title                           | variant    | Number-of-players | Winner               |
|------|---------------------------------|------------|-------------------|----------------------|
| 1    | U1700 Bullet Arena              | Standard   | 100               | <winner name>        |
| 2    | Werle Arena                     | Standard   | 30                | <winner name>        |
```


* Run `Litour.py -s`

```
| S.NO | Title                        | variant          | FinishesAt                 | Duration |
|------|------------------------------|------------------|----------------------------|----------|
| 1    | Italian Game Arena           | Standard         | Sat, 02 Jun 2018 23:53:40  | 45       |
| 2    | Blow up Arena                | Atomic           | Sat, 02 Jun 2018 23:56:12  | 40       |
```

* Run `Litour.py -n`

```
| S.NO | Title                           | Tournament id | variant          | StartsAt                   | Duration |
|------|---------------------------------|---------------|------------------|----------------------------|----------|
| 1    | Levitsky Arena                  | j3dvIkgm      | Standard         | Sat, 02 Jun 2018 23:18:59  | 45       |
| 2    | Nurlan Arena                    | x5Qb7tu7      | Standard         | Sat, 02 Jun 2018 23:19:13  | 30       |

Do you want to add any tournament to your calendar ? y/n: y
Enter the id of the tournament you want to add: j3dvIkgm
Event created: <Link to your google calendar event>
```
