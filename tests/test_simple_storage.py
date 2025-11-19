from brownie import SimpleStorage, accounts

def test_deploy():
    # Arrange -> organizar
    account = accounts[0]

    # Act -> hacer algo
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0

    # Assert -> comprobar que algo ha ido bien
    assert starting_value == expected


def test_updating_storage():
    # Arrange
    account = accounts[0]

    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    tx = simple_storage.store(12, {"from": account})
    tx.wait(1)
    expected = 12

    # Assert
    assert simple_storage.retrieve() == expected


