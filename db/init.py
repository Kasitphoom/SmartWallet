import sys
import ZODB, ZODB.config
import BTrees.OOBTree, transaction
from pathlib import Path

# append a new directory to sys.path
sys.path.append(str(Path(__file__).parent.parent))

from obj.account import Account
from obj.transaction import Transaction

# from account import Account

if __name__ == "__main__":
    path = "./db/config.xml"
    db = ZODB.config.databaseFromURL(path)
    connection = db.open()
    root = connection.root

    root.accounts = BTrees.OOBTree.BTree()
    root.transactions = BTrees.OOBTree.BTree()

    root.accounts["123456789"] = Account("John Doe", 1000, "123456789", "c72811a3c777b8bf78740b3d3433b0b9aee7a601644ad5387f35ba6132577e20", "admin@email.com", 15_000, "cc23b4553ba29c1b81fb8d4b1e3efc9d3ced792e66fefec756bd940e684bc745")
    root.accounts["874043489"] = Account("Phong Kit", 100000, "874043489", "c72811a3c777b8bf78740b3d3433b0b9aee7a601644ad5387f35ba6132577e20", "phong@email.com", 20_000, "cc23b4553ba29c1b81fb8d4b1e3efc9d3ced792e66fefec756bd940e684bc745")

    transaction.commit()