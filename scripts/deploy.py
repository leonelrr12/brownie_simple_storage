from brownie import accounts, config
#import os   /// 111

def deploy_simple_storage():
    #account = accounts.load("metamask-acc")
    #account = accounts.add(os.getenv("PRIVATE_KEY"))  /// 111
    account = accounts.add(config["wallets"]["from_key"])
    print("Account: ", account)


def main():
    deploy_simple_storage()