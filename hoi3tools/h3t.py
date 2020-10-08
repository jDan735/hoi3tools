import argparse
from config import dirpath
from lib import find


def main(args):
    if (args.owner is None and
       args.add_core is None and
       args.controller is None and
       args.add_all is None):

       print("Ничего не выбрано!")
       return

    path = find(str(args.prov), dirpath)

    print(path)

    if path is not None:
        with open(path, "a") as conf:
            # print(conf.read())
            if args.owner:
                conf.write(f"\nowner = {args.owner}")

            elif args.controller:
                conf.write(f"\ncontroller = {args.controller}")

            elif args.add_core:
                conf.write(f"\nadd_core = {args.add_core}")

            elif args.add_all:
                conf.write(f"\nowner = {args.add_all}")
                conf.write(f"\ncontroller = {args.add_all}")
                conf.write(f"\nadd_core = {args.add_all}")


def logo():
    print("  _   _         ___    _____    _____                _      ")
    print(" | | | |  ___  |_ _|  |___ /   |_   _|  ___    ___  | | ___ ")
    print(" | |_| | / _ \\  | |     |_ \\     | |   / _ \\  / _ \\ | |/ __|")
    print(" |  _  || (_) | | |    ___) |    | |  | (_) || (_) || |\\__ \\")
    print(" |_| |_| \\___/ |___|  |____/     |_|   \\___/  \\___/ |_||___/")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("prov", type=int, help="Ban")

    parser.add_argument("--owner")
    parser.add_argument("--controller")
    parser.add_argument("--add-core")
    parser.add_argument("--add-all")

    args = parser.parse_args()

    logo()
    main(args)
