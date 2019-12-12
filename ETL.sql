CREATE TABLE wine_reviews (
id int GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
country TEXT,
description VARCHAR,
designation VARCHAR,
points INT,
price INT,
province TEXT,
region_1 TEXT,
region_2 TEXT,
variety TEXT,
winery TEXT
);


