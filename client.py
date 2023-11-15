import requests
import argparse


def say_hello(name):
    url = f'http://127.0.0.1:5000/hello?name={name}'
    response = requests.get(url)
    print('/hello:', response.text)


def magic_sum(numbers):
    url = 'http://127.0.0.1:5000/add'
    response = requests.post(url,
                json={'numbers': numbers})
    print('/add:', response.text)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str, help='Name for the hello request', default="Alice")
    parser.add_argument('--numbers', nargs='+', type=int, help='Numbers to sum', default=[1, 2, 3])
    return parser.parse_args()


def main():
    args = get_args()
    if args.name:
        say_hello(args.name)

    if args.numbers:
        magic_sum(args.numbers)


if __name__ == "__main__":
    main()
