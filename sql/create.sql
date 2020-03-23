CREATE TABLE url (
    id              text PRIMARY KEY,
    original_url    text NOT NULL,
    times_visited   integer default 0 not null,
    created_at      timestamp with time zone default current_timestamp
);

create table country (
    code text primary key,
    name text not null,
    iso_code_1 text,
    iso_code_2 text
);

create table city (
    name text,
    country_code text references country(code),
    unique(name, country_code),
    primary key (name, country_code)
);

create table timezone (
    name text primary key
);

create table ip_address (
    ip inet primary key,
    hostname text,
    zipcode text,
    latitude real,
    longitude real,
    timezone text references timezone(name),
    region text,
    city_name text,
    country_code text,
    foreign key (city_name, country_code) references city(name, country_code)
--    unique(city_name, country_code)
);

create table visit (
    id serial primary key,
    ip inet references ip_address(ip),
    url_id text references url(id)
);