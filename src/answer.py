from pprint import pprint

import eav_model
from load_data import SessionLocal

db = SessionLocal()


def get_data_example():
    # ORM:sqlalchemy
    test_data: eav_model.EAV = (
        db.query(eav_model.EAV)
        .filter(eav_model.EAV.id == 1)
        .first()
    )
    pprint((test_data.id, test_data.e_id, test_data.attribute, test_data.value))


if __name__ == "__main__":
    get_data_example()
