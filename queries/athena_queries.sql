-- Create Athena Table for Meta Data
CREATE EXTERNAL TABLE IF NOT EXISTS media_analytics.meta_data (
    account_id STRING,
    name STRING,
    impressions BIGINT,
    clicks BIGINT,
    engagement_rate DOUBLE
) 
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
STORED AS TEXTFILE
LOCATION 's3://media-etl-data-bucket/processed/';

-- Query for Engagement Rate
SELECT name, SUM(impressions) AS total_impressions, AVG(engagement_rate) AS avg_engagement
FROM media_analytics.meta_data
GROUP BY name;
