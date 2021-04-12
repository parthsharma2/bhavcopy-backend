## Project Setup

This project requires the following:
- `python3`
- `redis`

You can install `python3` from the following [link](https://www.python.org/downloads/). To install `redis` follow the following [link](https://redis.io/topics/quickstart).

If you've installed `python3` & `redis` you can begin the project setup by following these steps.

1. Clone this repository and move into the root folder.
```
git clone https://github.com/parthsharma2/bhavcopy-backend.git
cd bhavcopy-backend
```

2. Create a python virtual environment & activate it. (optional, but recommended)
```
python3 -m venv .venv

source .venv/bin/activate
```

3. Install the required python packages
```
pip install -r requirements.txt
```

4. Create a `.env` file to configure the environment variables that this app utilizes. Use the following code snippet as the content of the file & set the 
variable values accordingly.
```
REDIS_HOST="127.0.0.1"
REDIS_PORT="6379"
```

`REDIS_HOST`: hostname/ip address of the server where your redis instance is running. \
`REDIS_POR`: port at which your redis instance is running.

5. Apply unapplied migrations
```
python manage.py migrate
```

6. Now you are ready to run the Django dev server
```
python manage.py runserver
```

## Fetching Bhavcopy Equity Data
To fetch the Bhavcopy Equity Data run the following bash script available in the root folder.
S
**Note:** If you created the python virtual environment mentioned in step 2, make sure your python virtual environment is activated when executing this command.
```
./fetch_equity_data
```

## Scheduling 
I suggest using `crontab` to run the `fetch_equity_data` command at regular intervals. Example `crontab` config
```
0 18 * * * cd /home/bhavcopy/bhavcopy-backend && source .venv/bin/activate && ./fetch_equity_data
```

This runs `cd /home/bhavcopy/bhavcopy-backend && source .venv/bin/activate && ./fetch_equity_data` command every day at 18:00.

`cd /home/bhavcopy/bhavcopy-backend && source .venv/bin/activate && ./fetch_equity_data` command executes in 3 steps:
- Changes directory into `/home/bhavcopy/bhavcopy-backend`, the project root directory in this case.
- Then `source .venv/bin/activate` activates the python virtual environment.
- Finally, `./fetch_equity_data` is executed.

## API Endpoints
- `/api/equity`: This endpoint returns a list of equity records. It accepts a URL paramter `q` where you can specify the query string to filter the equity record. 
For e.g. `/api/equity?q=reli` will return equity records which contains the query string `reli` in the `code` or `name` fields.

## Frontend
[Bhavcopy Frontend](https://github.com/parthsharma2/bhavcopy-frontend) lives in this [repository](https://github.com/parthsharma2/bhavcopy-frontend). Follow the instructions in its README to set it up.
