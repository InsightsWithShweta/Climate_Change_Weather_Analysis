create database Climate_Analysis;
use Climate_Analysis;
select * from climate_data limit 10;

-- Top 5 hottest state
select state,round(avg(avg_temp_c),2) as avg_temp 
from climate_data 
group by state 
order by avg_temp 
desc limit 5;

-- Avg rainfall by region
select region,round(avg(rainfall_mm),2) as avg_rainfall
from climate_data
group by region
order by avg_rainfall desc;

-- Hottest season

select season,round(avg(avg_temp_c),2) as avg_temp
from climate_data
group by season
order by avg_temp desc;

-- year wise temp trend

select year,round(avg(avg_temp_c),2) as avg_temp
from climate_data
group by year
order by year;

-- count records by temp category
select temp_category,count(*) as total_records
from climate_data
group by temp_category;

-- state with avg temp above 25
select state,round(avg(avg_temp_c),2) as avg_temp
from climate_data
group by state
having avg_temp>25
order by avg_temp desc;

-- Rank state by avg_temp
select state,round(avg(avg_temp_c),2) as avg_temp,rank()over(order by avg(avg_temp_c) desc)
as state_rank
from climate_data
group by state;

-- no of states in each region
select region,count(distinct state) as total_states
from climate_data
group by region;

-- state with avg rainfall above overall average
select state,round(avg(rainfall_mm),2)as avg_rainfall
from climate_data
group by state
having avg(rainfall_mm)>
(select avg(rainfall_mm) from climate_data);

-- region with high avg humidity
select region,round(avg(humidity_pct),2) as avg_humidity
from climate_data
group by region
order by avg_humidity desc;


