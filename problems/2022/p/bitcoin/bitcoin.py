import requests
import json
import sys


def main():
    btc = get_bitcoin()
    rate = get_usd_rate()
    price = btc * rate

    print(f"${price:,.4f}")


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def get_bitcoin() -> float:
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    elif sys.argv[1].isdigit() or isfloat(sys.argv[1]):
        return float(sys.argv[1])
    else:
        sys.exit("Command-line argument is not a number")


def get_usd_rate():
    try:
        res = requests.get(
            "https://api.coindesk.com/v1/bpi/currentprice.json").json()
    except requests.RequestException:
        sys.exit()

    rate = res["bpi"]["USD"]["rate_float"]

    return rate


if __name__ == '__main__':
    main()
