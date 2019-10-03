import argparse


PARSER = argparse.ArgumentParser()
PARSER.add_argument('--enviroment', '-e', help='Send or not the resuts to Logstash', type=str, default='Development')

ARGS = PARSER.parse_args()