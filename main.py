import logging
import dotenv
import get_env_vars as env
import database.db_connect as db_conn

def main():

    # declare logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # load from .env if exists
    dotenv.load_dotenv()

    # load env secrets
    db_tier = env.get_db_tier()
    db_server = env.get_db_server()
    db_user = env.get_db_user()
    db_pass = env.get_db_pass()

    database_connection = db_conn.getDbConnection(db_tier, db_server, "DemandManagement", db_user, db_pass)

    print("Test")

if __name__ == "__main__":
    main()