-- CREATE TABLE `CAR_INFO` (
-- 	`PK_CAR_ID`	VARCHAR(50)	NOT NULL,
-- 	`CAR_NAME`	VARCHAR(255)	NULL,
-- 	`FK_COMMON_CODES_COMPANY`	VARCHAR(50)	NULL,
-- 	`FK_COMMON_CODES_YEARS`	VARCHAR(50)	NULL
-- );

-- CREATE TABLE `COMMON_CODES` (
-- 	`FK_COMMON_CODES`	VARCHAR(50)	NOT NULL,
-- 	`PART_NAME`	VARCHAR(255)	NULL,
-- 	`NAME`	VARCHAR(255)	NULL
-- );

-- ALTER TABLE `CAR_INFO` ADD CONSTRAINT `PK_CAR_INFO` PRIMARY KEY (
-- 	`PK_CAR_ID`
-- );

-- ALTER TABLE `COMMON_CODES` ADD CONSTRAINT `PK_COMMON_CODES` PRIMARY KEY (
-- 	`FK_COMMON_CODES`
-- );

INSERT INTO `COMMON_CODES` (`FK_COMMON_CODES`, `PART_NAME`, `NAME`) VALUES
('C001', 'COMPANY', 'Hyundai'),
('C002', 'COMPANY', 'Kia'),
('Y001', 'YEARS', '2020'),
('Y002', 'YEARS', '2021');

SELECT * FROM `COMMON_CODES`;
-- FK_COMMON_CODES,PART_NAME,NAME
-- C001,COMPANY,Hyundai
-- C002,COMPANY,Kia
-- Y001,YEARS,2020
-- Y002,YEARS,2021

INSERT INTO `CAR_INFO` (`PK_CAR_ID`, `CAR_NAME`, `FK_COMMON_CODES_COMPANY`, `FK_COMMON_CODES_YEARS`) VALUES
('CAR001', 'Sonata', 'C001', 'Y002'),
('CAR002', 'Sorento', 'C002', 'Y002'),
('CAR003', 'Elantra', 'C001', 'Y001'),
('CAR004', 'Sportage', 'C002', 'Y001');

SELECT * FROM `CAR_INFO`;
-- PK_CAR_ID,CAR_NAME,FK_COMMON_CODES_COMPANY,FK_COMMON_CODES_YEARS
-- CAR001,Sonata,C001,Y002
-- CAR002,Sorento,C002,Y002
-- CAR003,Elantra,C001,Y001
-- CAR004,Sportage,C002,Y001

SELECT CI.PK_CAR_ID, CI.CAR_NAME, CC_COMPANY.NAME AS COMPANY, CC_YEARS.NAME AS YEAR
FROM `CAR_INFO` CI
JOIN `COMMON_CODES` CC_COMPANY ON CI.FK_COMMON_CODES_COMPANY = CC_COMPANY.FK_COMMON_CODES
JOIN `COMMON_CODES` CC_YEARS ON CI.FK_COMMON_CODES_YEARS = CC_YEARS.FK_COMMON_CODES
ORDER BY CI.PK_CAR_ID;
-- PK_CAR_ID,CAR_NAME,COMPANY,YEAR
-- CAR001,Sonata,Hyundai,2021
-- CAR002,Sorento,Kia,2021
-- CAR003,Elantra,Hyundai,2020
-- CAR004,Sportage,Kia,2020
