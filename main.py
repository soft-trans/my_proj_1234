def get_last_data():
    lst = ["1st object added 2024-08-08 14:12"]

    return lst[-1]


if __name__ == "__main__":
    latest_data = get_last_data()
    print("===>", latest_data)
