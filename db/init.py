import os
import ZODB, ZODB.config
import BTrees.OOBTree, transaction
from account import Account

# from account import Account

if __name__ == "__main__":
    path = "./db/config.xml"
    db = ZODB.config.databaseFromURL(path)
    connection = db.open()
    root = connection.root

    root.accounts = BTrees.OOBTree.BTree()
    root.transactions = BTrees.OOBTree.BTree()

    root.accounts[123456789] = Account("John Doe", 1000, 123456789)

    transaction.commit()