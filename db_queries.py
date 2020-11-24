import os
import tinydb


class dbquery:
    def __init__(self):
        self.state = "statefarm"

    def DBCheck(self, server_name):
        newpath = r'./database/' + server_name
        if not os.path.exists(newpath):
            os.makedirs(newpath)

    def warnUser(self, server_name, user_id, reason):
        self.DBCheck(server_name)
        if reason is None:
            reason = "none given"
        db = tinydb.TinyDB("./database/" + server_name + "/warnings.json")
        db.insert({"username": user_id, "reason": reason})

    def getWarnings(self, server_name, user_id):
        Query = tinydb.Query()
        db = tinydb.TinyDB("./database/" + server_name + "/warnings.json")
        warnings = db.search(Query.username == user_id)
        numWarnings = len(warnings)
        return numWarnings
