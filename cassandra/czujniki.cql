CREATE TABLE measurments 
(
  sens_id TEXT,
  country TEXT,
  city TEXT,
  
  time timestamp,

  temperature FLOAT,
  pm10 FLOAT,
  pm25 FLOAT,
  PRIMARY KEY ((sens_id, country, city),time)
); 
  

--bad

CREATE TABLE usery
(
	username TEXT,
	wiek INT,
	email TEXT,

	PRIMARY KEY (wiek, username, email)
);
