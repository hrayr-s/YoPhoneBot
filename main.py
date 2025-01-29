import sys

from config import Config
from yo_bot import YoBot


def main():
    bool_bot = YoBot(Config.BOT_TOKEN)
    no_updates_counter = 0

    try:
        for update in bool_bot.updates_listener(interval=1):
            if update is None:
                no_updates_counter += 1
                sys.stdout.write("\rNo updates %d" % no_updates_counter)
                sys.stdout.flush()
                continue

            no_updates_counter = 0
            print(update)
    finally:
        print("Exiting...")


if __name__ == '__main__':
    main()
