.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet FROM students WHERE color='blue' AND pet='dog';

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song FROM students WHERE color='blue' AND pet='dog';


CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color FROM students AS a, students AS b 
  WHERE a.pet = b.pet AND a.song = b.song AND a.time < b.time;


CREATE TABLE sevens AS
  SELECT stu.seven FROM students AS stu, numbers AS num 
  WHERE stu.time = num.time AND stu.number = 7 AND num.'7' = "True";



CREATE TABLE favpets AS
  SELECT pet, COUNT(pet) as tot from students GROUP BY pet ORDER BY tot desc LIMIT 10;


CREATE TABLE dog AS
  SELECT pet, COUNT(pet) FROM students WHERE pet='dog';


CREATE TABLE bluedog_agg AS
  SELECT song, COUNT(song) as tot FROM bluedog_songs GROUP BY song ORDER BY tot desc;


CREATE TABLE instructor_obedience AS
  SELECT seven, instructor, COUNT(*) FROM students WHERE seven='7' GROUP BY instructor;

