import ZODB, ZODB.config
import BTrees.OOBTree, transaction

path = "./config.xml"
db = ZODB.config.databaseFromURL(path)
connection = db.open()
root = connection.root

root.accounts = BTrees.OOBTree.BTree()
root.transactions = BTrees.OOBTree.BTree()
