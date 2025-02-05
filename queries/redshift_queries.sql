-- Create Redshift Table for YouTube Analytics
CREATE TABLE youtube_analytics (
    video_id VARCHAR(50),
    title VARCHAR(255),
    views INT,
    likes INT,
    dislikes INT,
    comments INT
);

-- Insert Sample Data
INSERT INTO youtube_analytics (video_id, title, views, likes, dislikes, comments)
VALUES 
('x1y2z3', 'Video A', 10000, 500, 10, 150),
('a1b2c3', 'Video B', 50000, 1200, 20, 500);

-- Query for Top Videos by Engagement
SELECT title, views, likes, comments
FROM youtube_analytics
ORDER BY views DESC
LIMIT 10;
