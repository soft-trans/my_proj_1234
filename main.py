def get_last_data():
    lst = [
        "1st object added 2024-08-08 14:12",
        "2st object added 2024-08-08 14:44",
        "pushing directly from ui from pycharm",
        "My Line 4 - Arth1",
        "My line 5 123"
        "added new change from for_arth"
    ]

    return lst[-1]


if __name__ == "__main__":
    latest_data = get_last_data()
    print("===>", latest_data)
