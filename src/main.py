# -*- coding: utf-8 -*-

import os
import requests

if __name__ == "__main__":
    print("hello world")

    clubhouse_api_token = os.environ["INPUT_CLUBHOUSE_API_TOKEN"]
    print(clubhouse_api_token)

    open_id = os.environ["INPUT_PR_OPENED"]
    merged_id = os.environ["INPUT_PR_MERGED"]
    closed_id = os.environ["INPUT_PR_CLOSED"]

    print(open_id)
    print(type(open_id))
    print(merged_id)
    print(closed_id)

    # when pr opened with "Fixed [ch-xxxx]" in pr body
    # send request to move ch story

    headers = {"Content-Type": "application/json", "Clubhouse-Token": clubhouse_api_token}

    BASE_URL = "https://api.clubhouse.io/api/v3/stories/"
    parsed_story_id = str(6027)

    request_body = {
        "workflow_state_id" : str(open_id)
    }

    res = requests.put(url=BASE_URL + parsed_story_id, data=request_body, headers=headers)

    print(res.status_code)
    print(res.text)
