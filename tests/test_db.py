from database.db_singleton import Database

def test_singleton():
    db1 = Database.get_instancia()
    db2 = Database.get_instancia()
    assert db1 is db2
