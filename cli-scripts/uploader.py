import argparse
import json
import os
import time
from os import getenv
from os.path import expanduser, join

from common.model_upload import upload_model


def read_config():
    config_path = getenv('INFERNO_CONFIG_PATH', join(expanduser("~"), '.inferno'))
    with open(config_path) as config_file:
        config = json.load(config_file)
    return config


def model_version_t(value):
    value = int(value)
    if value <= 0:
        raise argparse.ArgumentTypeError("Model version must be a positive integer")
    return value


def part_size_t(value):
    try:
        value = int(value)
        if value < 5 or value > 5000:
            raise Exception
    except Exception:
        raise argparse.ArgumentTypeError("Part size must be integer between 5 and 5000")
    return value


def main():
    parser = argparse.ArgumentParser(description='Inferno Model Uploader')
    parser.add_argument('file_path', type=str,
                        help='Path to file with model to upload')
    parser.add_argument('model_name', type=str,
                        help='Name of uploaded model')
    parser.add_argument('model_version', type=model_version_t,
                        help='Version of uploaded model')
    parser.add_argument('tenant', type=str,
                        help='Tenant which is uploading model')
    parser.add_argument('--part', type=part_size_t, default=500,
                        help='Size of data chunk in MB sent in a single upload request '
                             '(acceptable values: 5-5000, default: 500)')

    config = read_config()
    headers = {'Authorization': config['id_token']}
    args = parser.parse_args()
    params = {
        'model_name': args.model_name,
        'model_version': args.model_version,
        'file_path': os.path.abspath(args.file_path),
    }
    url = f"http://{config['management_api_address']}:{config['management_api_port']}" \
          f"/tenants/{args.tenant}"

    start_time = time.time()
    upload_model(url, params, headers, args.part)
    end_time = time.time()
    print("Time elapsed: " + str(end_time - start_time))


if __name__ == "__main__":
    main()