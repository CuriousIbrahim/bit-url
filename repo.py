from sqlalchemy.orm import sessionmaker

from db import engine, Url
from ip import get_info_from_ip


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
        return result[0].original_url

    def increment_visit(self, short_url):
        result = self.session.query(Url).filter_by(id=short_url).all()
        url = result[0]
        url.times_visited += 1
        self.session.add(url)
        self.session.commit()
        print("now", url.times_visited)

    def insert_ip_address_and_its_visit(self, ip, short_url):
        ip_info = get_info_from_ip(ip)





