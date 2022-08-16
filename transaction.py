from datetime import datetime

import pandas

now = datetime.now()
date = now.date()
current_time = now.time()
# transactions = [{"id": [5421], "date": [date], "time": [current_time],
#                  "actions": [{"id": 200, "title": "withdrow"}, {"id": 300, "title": "transform"}],
#                  "account": [{"id": 200, "name": "arezoo", "account_num": 24234523532, "type": "budget"}]
#                  }]
transactions = []


def find_transaction_by_id(id):
    for transaction in transactions:
        if transaction["id"] == id:
            return transaction


def valid_transaction_id(id):
    result = False
    for transaction in transactions:
        if transaction["id"] == id:
            result = True
            break
    return result


def add_transaction(trans_id, time, date, description):
    transaction = {"id": trans_id, "time": time, "date": date, "description": description}
    transactions.append(transaction)


def add_transaction_action(trans_id, action_id, action_title):
    transaction = find_transaction_by_id(trans_id)
    if not transaction:
        print("transaction with id:{0} not found".format(trans_id))
        return
    if "actions" not in transaction:
        transaction["actions"] = []
    transaction["actions"].append({"id": action_id, "name": action_title})


def add_transaction_account(trans_id, account_id, account_name, account_num, type):
    transaction = find_transaction_by_id(trans_id)

    if not transaction:
        print("transaction not found")
        return
    if "account" not in transaction:
        transaction["account"] = []
    transaction["account"].append(
        {"id": account_id, "name": account_name, "account_num": account_num, "type": type})


add_transaction(5421, now.time(), now.date(), "non")
add_transaction(1243, now.time(), now.date(), "non")
add_transaction_action(5421, 20, "withdraw")
add_transaction_action(1243, 40, "transfer")
add_transaction_action(12, 20, "withdraw")
add_transaction_account(5421, 200, "arezoo", 32435645686, "budget")
print(transactions)
a = pandas.DataFrame(transactions)
a.to_csv("out_data.txt")
