from argparse import ArgumentParser
from snapchat_bots import SnapchatBot

class StorifierBot(SnapchatBot):
    def on_snap(self, sender, snap):
        self.post_story(snap)

    def on_friend_add(self, friend):
        self.add_friend(friend)


if __name__ == '__main__':
    parser = ArgumentParser("Storifier Bot")
    parser.add_argument('-u', '--username', required=True, type=str, help="Username of the account to run the bot on")
    parser.add_argument('-p', '--password', required=True, type=str, help="Password of the account to run the bot on")
    parser.add_argument('-t', '--token', required=True, type=str, help="Password of the account to run the bot on")

    args = parser.parse_args()


    bot = StorifierBot(args.username, args.password, args.token)
    bot.listen()
