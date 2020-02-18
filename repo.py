from sqlalchemy.orm import sessionmaker

from db import engine, Url


Session = sessionmaker(bind=engine)


class Repository:

    def __init__(self):
        self.session = Session()

    def add_url(self, original_url, short_url):
        obj = Url(original_url=original_url, id=short_url)
        self.session.add(obj)
        self.session.commit()

    def get_url(self, short_url):
        result = self.session.query(Url).filter_by(id=short_url).all()
        print(result.entities['id'])




