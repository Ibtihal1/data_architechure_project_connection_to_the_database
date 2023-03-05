select district,count(incident_number)as crime_count from boston_crime group by district order by crime_count desc;

select reporting_area,count(incident_number)as crime_count from boston_crime group by (reporting_area) order by crime_count desc;

select street,count(incident_number)as crime_count from boston_crime group by (street) order by crime_count desc;

select district,offense_code_group,count(incident_number)as crime_count from boston_crime group by (district,offense_code_group) order by crime_count desc;

select reporting_area,offense_code_group,count(incident_number)as crime_count from boston_crime group by (reporting_area,offense_code_group) order by crime_count desc;

select street,offense_code_group,count(incident_number)as crime_count from boston_crime group by (street,offense_code_group) order by crime_count desc;