import ipinfo

from config import IPINFO_ACCESS_TOKEN as access_token

handler = ipinfo.getHandler(access_token)

def get_info_from_ip(ip):
    details = handler.getDetails(ip)

    toReturn = {
        'city': details.city,
        'country': details.country,
        'hostname': details.hostname,
        'ip': ip,
        'latitude': details.latitude,
        'longitude': details.longitude,
        'region': details.region,
        'timezone': details.timezone
    }

    return toReturn