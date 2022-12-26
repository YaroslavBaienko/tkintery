import socket
import requests


def write_result(result: float):
    with open('results.csv', 'a') as file:
        file.write(str(result))
        file.write("\n")
        file.close()
