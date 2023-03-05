select occurred_on_date,count(incident_number)as crime_count from boston_crime group by occurred_on_date;

select year, month,count(incident_number)as crime_count from boston_crime group by (year,month);

select year,count(incident_number)as crime_count from boston_crime group by year order by crime_count desc;

select day_of_week,count(incident_number)as crime_count from boston_crime group by day_of_week order by crime_count desc;

select year,offense_code_group,count(incident_number)as crime_count from boston_crime group by (year,offense_code_group) order by crime_count desc;

select year,district,count(incident_number)as crime_count from boston_crime group by (year,district) order by crime_count desc;