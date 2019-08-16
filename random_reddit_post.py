import requests, random, re

REDDIT_USER_NAME = ""
REDDIT_PASSWORD = ""
APP_NAME = ""
APP_ID = ""
APP_SECRET = ""
USER_AGENT = f"{APP_NAME} by {REDDIT_USER_NAME}"

REDDIT_BASE_URL = 'https://www.reddit.com/'
OAUTH_BASE_URL = 'https://oauth.reddit.com'

SUBREDDIT = "jokes"
SORT_BY = "hot"

NUM_ROWS = 9
ROW_MAX_LEN = 40
TEXT_MAX_LEN = NUM_ROWS * ROW_MAX_LEN

def get_access_token():
    data = {"grant_type": "password", "username": REDDIT_USER_NAME, "password": REDDIT_PASSWORD}
    auth = requests.auth.HTTPBasicAuth(APP_ID, APP_SECRET)
    response = requests.post(REDDIT_BASE_URL + "api/v1/access_token",
                             data=data,
                             headers={"user-agent": USER_AGENT},
                             auth=auth)
    data = response.json()
    return "bearer " + data["access_token"]

def parse_links(data):
    texts = []
    for child in data["children"]:
        if child["kind"] == "t3":
            link = child["data"]
            text = link["title"].strip()
            if link["selftext"]:
                text += f' - {link["selftext"].strip()}'
            text = re.sub(r"(\n+)", " - ", text)
            if len(text) <= TEXT_MAX_LEN:
                texts.append(text)
    return texts

def format_text(s):
    rows = []
    for i in range(0, len(s), ROW_MAX_LEN):
        next_row_start = i + ROW_MAX_LEN
        new_row = s[i:next_row_start]

        last_char = new_row[-1]
        next_char = s[next_row_start] if next_row_start < len(s) else ""

        if last_char.isalpha() and next_char.isalpha():
            new_row += "-"
        rows.append(new_row.strip())

    return "\n".join(rows)

def __main__():
    try:
        token = get_access_token()
    except:
        print("No connection.")
        exit(1)

    headers = {"Authorization": token, "User-Agent": USER_AGENT}
    response = requests.get(OAUTH_BASE_URL + "/r/" + SUBREDDIT + "/" + SORT_BY, headers=headers)

    if response.status_code == 200:
        data = response.json()["data"]
        texts = parse_links(data)

        if texts:
            chosen_text = random.choice(texts)
            chosen_text = format_text(chosen_text)
            print(chosen_text, end="\n" + ROW_MAX_LEN * "-" + "\n")
        else:
            print("No texts found.")

if __name__ == "__main__":
    __main__()
