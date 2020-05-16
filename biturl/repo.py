from sqlalchemy.orm import sessionmaker
from redis import Redis

from db import engine, Url, IpAddress, Visit
# from ip import get_info_from_ip


Session = sessionmaker(bind=engine)

cache = Redis(host='cache', port=6379, db=0, decode_responses=True)


class Repository:

    def __init__(self):
        self.session = Session()

    def add_url(self, original_url, short_url):
        obj = Url(original_url=original_url, id=short_url)
        self.session.add(obj)
        self.session.commit()
        cache.set(short_url, original_url)

    def get_url(self, short_url):
        url = cache.get(short_url)

        if url is None:
            result = self.session.query(Url).filter_by(id=short_url).all()
            url = result[0].original_url
            cache.set(short_url, url)

        return url

    def increment_visit(self, short_url):
        result = self.session.query(Url).filter_by(id=short_url).all()
        url = result[0]
        url.times_visited += 1
        self.session.add(url)
        self.session.commit()

    def does_ip_already_exit(self, ip):
        result = self.session.query(IpAddress).filter_by(ip=ip).all()
        return len(result) > 0

    def insert_ip_address_and_its_visit(self, ip, short_url, timestamp):
        if not self.does_ip_already_exit(ip):
            obj = IpAddress(ip=ip)
            self.session.add(obj)
            self.session.commit()

        obj = Visit(ip_address=ip, url=short_url, visited_at=timestamp)
        self.session.add(obj)
        self.session.commit()








