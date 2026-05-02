from getpass import getpass

import keyring

SERVICE_NAME = "form-load-tests"


def main() -> None:
    password = getpass("Enter the shared password for all test users: ")

    for index in range(1, 11):
        alias = f"u{index:03d}"
        keyring.set_password(SERVICE_NAME, alias, password)
        print(f"Saved password for {alias}")


if __name__ == "__main__":
    main()
