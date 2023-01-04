import argparse


def main():
    # Fill this out!


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='hello',
        description='What the program does',
        epilog='Text at the bottom of help'
    )
    args = parser.parse_args()

    main()