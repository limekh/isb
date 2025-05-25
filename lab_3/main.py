import argparse
import json

from hybridCryptosystem import *


def parse_args():
    parser = argparse.ArgumentParser(description="Hybrid Crypto System")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', action='store_true', help='Keys Generator')
    group.add_argument('-enc', '--encryption', action='store_true', help='Encrypt Data')
    group.add_argument('-dec', '--decryption', action='store_true', help='Decrypt Data')
    return parser.parse_args()


def load_settings():
    with open("settings.json") as file:
        return json.load(file)


def main():
    settings = load_settings()
    args = parse_args()

    initial_file = settings["initial_file"]
    encrypted_file = settings["encrypted_file"]
    decrypted_file = settings["decrypted_file"]
    symmetric_key = settings["symmetric_key"]
    public_key = settings["public_key"]
    private_key = settings["private_key"]

    if args.generation:
        keys_generator(symmetric_key, public_key, private_key)
    elif args.encryption:
        encrypt(private_key, initial_file, encrypted_file, symmetric_key)
    elif args.decryption:
        decrypt(private_key, encrypted_file, symmetric_key, decrypted_file)


if __name__ == "__main__":
    main()
