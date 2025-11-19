from brownie import accounts, config, SimpleStorage
#import os   # 111

def deploy_simple_storage():
    #account = accounts.load("metamask-acc")
    #account = accounts.add(os.getenv("PRIVATE_KEY"))  # 111
    account = accounts.add(config["wallets"]["from_key"])

    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage)
    stored_value = simple_storage.retrieve()
    print(stored_value)

    transaction = simple_storage.store(12, {"from": account})
    transaction.wait(1)  # Esto es para esperar al menos una confirmacion
    new_value = simple_storage.retrieve()
    print(new_value)


def main():
    deploy_simple_storage()