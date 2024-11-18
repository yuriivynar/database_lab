USE lab4;

INSERT INTO lab4.position (name) VALUES
('Software Engineer'),
('System Administrator'),
('Project Manager'),
('DevOps Engineer'),
('Data Scientist'),
('UI/UX Designer'),
('Business Analyst'),
('Quality Assurance Engineer'),
('Network Administrator'),
('IT Support Specialist'),
('Product Manager'),
('Database Administrator'),
('Security Analyst'),
('Cloud Architect'),
('Mobile Developer');

INSERT INTO lab4.employee (name, surname, pass_number, position_id) VALUES
('Viktor', 'Yaremchuk', 'GG123654', 7),
('Oleksandr', 'Shevchenko', 'AA789456', 1),
('Iryna', 'Kravchenko', 'HH456321', 4),
('Taras', 'Vasylenko', 'MM123456', 7),
('Oksana', 'Shapoval', 'LL321987', 12),
('Olena', 'Melnyk', 'FF987123', 6),
('Mykola', 'Zinchenko', 'II789123', 9),
('Dmytro', 'Tkachenko', 'CC456987', 3),
('Yurii', 'Horobets', 'JJ987456', 3),
('Natalia', 'Kovalenko', 'DD654321', 4),
('Pavlo', 'Soroka', 'KK654789', 11),
('Kateryna', 'Bondarenko', 'BB123789', 7),
('Yuliia', 'Rudenko', 'NN654987', 14),
('Bohdan', 'Marchenko', 'OO987321', 2),
('Andrii', 'Lysenko', 'EE321654', 5);

INSERT INTO lab4.location_type (id, location_name) VALUES
(1, 'Office'),
(2, 'Home');

INSERT INTO lab4.brand (name) VALUES
('Apple'),
('Samsung'),
('Asus'),
('Acer'),
('Dell'),
('Huawei'),
('Sony'),
('Canon'),
('Epson'),
('TP-Link'),
('HP'),
('Xiaomi'),
('LG'),
('Pixel'),
('ZTE');

INSERT INTO lab4.computer (model, cpu, ram, price, brand_id) VALUES
('MacBook Pro', 'Apple M1', '16GB', '2500', 1),
('Predator', 'Intel Core i7', '16GB', '2000', 4),
('Galaxy Book', 'Intel Core i7', '16GB', '1800', 2),
('XPS 13', 'Intel Core i5', '8GB', '1500', 5),
('EliteBook', 'Intel Core i5', '16GB', '1600', 11),
('ROG Strix', 'Intel Core i9', '32GB', '2200', 3),
('VAIO', 'Intel Core i7', '16GB', '1900', 7),
('Workstation', 'Intel Xeon', '64GB', '4000', 8),
('Vivobook', 'AMD Ryzen 9', '32GB', '2800', 3),
('Spectre x360', 'Intel Core i7', '16GB', '1700', 11),
('Mi Notebook Pro', 'Intel Core i5', '8GB', '1300', 12),
('Gram', 'Intel Core i7', '16GB', '1500', 13),
('MacBook Air', 'Apple M2', '16GB', '2300', 1),
('Blade L', 'Intel Core i3', '4GB', '900', 15),
('ZenBook', 'AMD Ryzen 7', '16GB', '1600', 3);

INSERT INTO lab4.router (model, ip_address, price, brand_id) VALUES
('Wi-Fi AX3 Pro', '192.168.1.6', '160', 6),
('ZXHN F660', '192.168.1.15', '90', 15),
('RT-AX58U', '192.168.1.1', '200', 3),
('Archer C80', '192.168.1.11', '110', 10),
('Mi AIoT Router AX3600', '192.168.1.13', '140', 12),
('Predator X5 Router', '192.168.1.4', '180', 4),
('Deco X20', '192.168.1.10', '180', 10),
('EchoLife HG8145V', '192.168.1.8', '140', 6),
('ROG Rapture GT-AX11000', '192.168.1.3', '350', 3),
('F680 V9', '192.168.1.14', '100', 15),
('Nitro Wi-Fi 6', '192.168.1.5', '190', 4),
('Archer AX6000', '192.168.1.9', '230', 10),
('RT-AC66U', '192.168.1.2', '170', 3),
('Mi Router 4C', '192.168.1.12', '60', 12),
('Honor Router 3', '192.168.1.7', '120', 6);

INSERT INTO lab4.monitor (model, resolution, price, brand_id) VALUES
('ProArt PA32UCX', '3840x2160', '2000', 3),
('Z32', '3840x2160', '950', 11),
('UltraSharp U3415W', '3440x1440', '850', 5),
('UJ59', '3840x2160', '300', 2),
('Studio Display', '5120x2880', '1600', 1),
('ROG Strix XG27UQ', '3840x2160', '900', 3),
('Omen 27i', '2560x1440', '600', 11),
('Predator X34', '3440x1440', '900', 4),
('P2720D', '2560x1440', '400', 5),
('CJ791', '3440x1440', '700', 2),
('Thunderbolt Display', '2560x1440', '999', 1),
('Odyssey G7', '2560x1440', '800', 2),
('Nitro XV272U', '2560x1440', '450', 4),
('TUF Gaming VG27AQ', '2560x1440', '500', 3),
('Pro Display XDR', '6016x3384', '5000', 1);

INSERT INTO lab4.`type` (name) VALUES
('Inkjet '),
('Laser'),
('Dot Matrix'),
('Thermal'),
('3D');

INSERT INTO lab4.printer (model, price, type_id, brand_id) VALUES
('iP8750', '300', 1, 8),
('Pro M404dn', '450', 2, 11),
('EcoTank L3150', '250', 1, 9),
('Xpress M2020', '200', 2, 2),
('Z20', '1200', 5, 13),
('A500', '550', 3, 3),
('C600', '600', 2, 4),
('B2360dn', '350', 2, 5),
('P200', '320', 1, 6),
('Stylus TX117', '180', 1, 9),
('LBP2900', '400', 2, 8),
('Mi Inkjet 220', '220', 1, 12),
('Fusion', '1400', 5, 11),
('PrintMaster Z30', '310', 4, 15),
('Pro DX100', '380', 3, 7);

INSERT INTO lab4.ip_phone (model, imei, price, brand_id) VALUES
('P60 Pro', '356938035643901', '920', 6),
('Mi 13 Ultra', '356938035643902', '880', 12),
('Wing', '356938035643903', '700', 13),
('iPhone 14', '356938035643904', '600', 1),
('Nubia RedMagic 8 Pro', '356938035643905', '950', 15),
('Xperia 5 V', '356938035643906', '1050', 7),
('Pixel 6a', '356938035643907', '500', 14),
('Galaxy Z Fold 5', '356938035643908', '1800', 2),
('iPhone 16 Pro Max', '356938035643909', '900', 1),
('Nova 11', '356938035643910', '650', 6),
('Poco F5', '356938035643911', '500', 12),
('G8 ThinQ', '356938035643912', '550', 13),
('Pixel 5', '356938035643913', '700', 14),
('Galaxy S24 Ultra', '356938035643914', '1400', 2),
('Blade V40', '356938035643915', '350', 15);

INSERT INTO lab4.access_point (model, ip_address, brand_id) VALUES
('EAP225', '192.168.0.101', 10),
('AP-AC68U', '192.168.0.102', 3),
('AP6010DN', '192.168.0.103', 6),
('ZXHN F670L', '192.168.0.104', 15),
('Airport Extreme', '192.168.0.105', 1),
('Mi AIoT Router', '192.168.0.106', 12),
('W4 AP', '192.168.0.107', 4),
('W-AP 7000', '192.168.0.108', 5),
('Access Point 123', '192.168.0.109', 7),
('WEA-100', '192.168.0.110', 2),
('EAP245', '192.168.0.111', 10),
('Access Point', '192.168.0.112', 14),
('Wireless AP', '192.168.0.113', 9),
('WAP 300', '192.168.0.114', 8),
('Access Point X', '192.168.0.115', 13);

INSERT INTO lab4.address (city, street, house_number, office_number) VALUES
('Kyiv', 'Khreshchatyk', '10', '301'),
('Lviv', 'Virmenska', '3', '0'),
('Odesa', 'Derybasivska', '5', '403'),
('Kharkiv', 'Sumska', '12', '0'),
('Dnipro', 'Yavornytskoho', '7', '305'),
('Zaporizhzhia', 'Sobornyi', '21', '102'),
('Lviv', 'Halytska', '15', '202'),
('Ternopil', 'Vasylianivska', '8', '0'),
('Cherkasy', 'Shevchenka', '14', '201'),
('Mykolaiv', 'Naucova', '9', '104'),
('Vinnytsia', 'Franka', '6', '110'),
('Uzhhorod', 'Korzo', '4', '202'),
('Chernivtsi', 'Kotsyubynskoho', '16', '0'),
('Sumy', 'Tarnavskoho', '18', '302'),
('Rivne', 'Sahaidachnoho', '11', '400');

INSERT INTO lab4.office (address_id, location_type_id) VALUES
(3, 1),
(7, 1),
(5, 1),
(1, 1),
(9, 1),
(2, 2),
(15, 1),
(4, 2),
(8, 2),
(11, 1),
(6, 1),
(10, 1),
(3, 1),
(13, 2),
(7, 1),
(12, 1);

INSERT INTO lab4.workplace (employee_id, office_id) VALUES
(3, 5),
(12, 9),
(1, 14),
(7, 2),
(11, 10),
(4, 8),
(15, 6),
(2, 13),
(9, 1),
(10, 3),
(8, 12),
(14, 7),
(6, 4),
(5, 15),
(13, 11);
;

INSERT INTO lab4.computer_in_workplace (computer_id, workplace_id) VALUES
(5, 10),
(2, 8),
(3, 1),
(6, 4),
(9, 7),
(1, 12),
(15, 2),
(11, 5),
(4, 6),
(8, 3),
(7, 14),
(10, 9),
(12, 11),
(13, 6),
(14, 1);

INSERT INTO lab4.monitor_in_workplace (workplace_id, monitor_id) VALUES
(14, 3),
(13, 2),
(9, 12),
(5, 9),
(2, 10),
(6, 11),
(15, 7),
(3, 14),
(12, 9),
(4, 1),
(10, 6),
(11, 12),
(7, 10),
(2, 8),
(14, 11);

INSERT INTO lab4.ip_phone_in_workplace (workplace_id, ip_phone_id) VALUES
(3, 13),
(1, 2),
(6, 8),
(2, 14),
(4, 5),
(10, 12),
(11, 4),
(8, 9),
(9, 3),
(7, 5),
(12, 10),
(5, 15),
(15, 8),
(13, 7),
(4, 2);

INSERT INTO lab4.router_in_workplace (workplace_id, router_id) VALUES
(3, 8),
(4, 15),
(11, 6),
(8, 10),
(13, 1),
(1, 4),
(9, 14),
(6, 7),
(7, 13),
(2, 12),
(14, 6),
(5, 3),
(10, 1),
(11, 8),
(8, 7);

INSERT INTO lab4.access_point_in_workplace (workplace_id, access_point_id) VALUES
(1, 11),
(14, 12),
(11, 3),
(6, 15),
(8, 13),
(3, 10),
(9, 1),
(2, 6),
(10, 4),
(7, 2),
(5, 14),
(15, 11),
(12, 5),
(14, 9),
(2, 1);

INSERT INTO lab4.printer_in_workplace (workplace_id, printer_id) VALUES
(14, 12),
(11, 3),
(6, 15),
(8, 13),
(3, 10),
(9, 1),
(2, 6),
(10, 4),
(7, 2),
(5, 14),
(15, 11),
(12, 5),
(14, 9),
(2, 1),
(3, 8);

DROP PROCEDURE IF EXISTS get_access_point_after_workplace;
DELIMITER //
CREATE PROCEDURE get_access_point_after_workplace(IN workplace_id INT)
BEGIN
SELECT ap.id access_point_id, ap.model model, b.name brand
FROM access_point ap
JOIN access_point_in_workplace apw ON ap.id = apw.access_point_id
JOIN brand b ON b.id = ap.brand_id
WHERE apw.workplace_id = workplace_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_workplace_after_access_point;
DELIMITER //
CREATE PROCEDURE get_workplace_after_access_point(IN access_point_id INT)
BEGIN
SELECT w.id workplace_id, e.name, e.surname, e.pass_number
FROM workplace w
JOIN access_point_in_workplace apw ON w.id = apw.workplace_id
JOIN employee e ON w.employee_id = e.id
WHERE apw.access_point_id = access_point_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_computer_after_workplace;
DELIMITER //
CREATE PROCEDURE get_computer_after_workplace(IN workplace_id INT)
BEGIN
SELECT c.id computer_id, c.model model, b.name brand
FROM computer c
JOIN computer_in_workplace cw ON c.id = cw.computer_id
JOIN brand b ON b.id = c.brand_id
WHERE cw.workplace_id = workplace_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_workplace_after_computer;
DELIMITER //
CREATE PROCEDURE get_workplace_after_computer(IN computer_id INT)
BEGIN
SELECT w.id workplace_id, e.name, e.surname, e.pass_number
FROM workplace w
JOIN computer_in_workplace cw ON w.id = cw.workplace_id
JOIN employee e ON w.employee_id = e.id
WHERE cw.computer_id = computer_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_ip_phone_after_workplace;
DELIMITER //
CREATE PROCEDURE get_ip_phone_after_workplace(IN workplace_id INT)
BEGIN
SELECT ip.id ip_phone_id, ip.model model, b.name brand
FROM ip_phone ip
JOIN ip_phone_in_workplace ipw ON ip.id = ipw.ip_phone_id
JOIN brand b ON b.id = ip.brand_id
WHERE ipw.workplace_id = workplace_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_workplace_after_ip_phone;
DELIMITER //
CREATE PROCEDURE get_workplace_after_ip_phone(IN ip_phone_id INT)
BEGIN
SELECT w.id workplace_id, e.name, e.surname, e.pass_number
FROM workplace w
JOIN ip_phone_in_workplace ipw ON w.id = ipw.workplace_id
JOIN employee e ON w.employee_id = e.id
WHERE ipw.ip_phone_id = ip_phone_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_monitor_after_workplace;
DELIMITER //
CREATE PROCEDURE get_monitor_after_workplace(IN workplace_id INT)
BEGIN
SELECT m.id monitor_id, m.model model, b.name brand
FROM monitor m
JOIN monitor_in_workplace mw ON m.id = mw.monitor_id
JOIN brand b ON b.id = m.brand_id
WHERE mw.workplace_id = workplace_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_workplace_after_monitor;
DELIMITER //
CREATE PROCEDURE get_workplace_after_monitor(IN monitor_id INT)
BEGIN
SELECT w.id workplace_id, e.name, e.surname, e.pass_number
FROM workplace w
JOIN monitor_in_workplace mw ON w.id = mw.workplace_id
JOIN employee e ON w.employee_id = e.id
WHERE mw.monitor_id = monitor_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_printer_after_workplace;
DELIMITER //
CREATE PROCEDURE get_printer_after_workplace(IN workplace_id INT)
BEGIN
SELECT p.id printer_id, p.model model, b.name brand
FROM printer p
JOIN printer_in_workplace pw ON p.id = pw.printer_id
JOIN brand b ON b.id = p.brand_id
WHERE pw.workplace_id = workplace_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_workplace_after_printer;
DELIMITER //
CREATE PROCEDURE get_workplace_after_printer(IN printer_id INT)
BEGIN
SELECT w.id workplace_id, e.name, e.surname, e.pass_number
FROM workplace w
JOIN printer_in_workplace pw ON w.id = pw.workplace_id
JOIN employee e ON w.employee_id = e.id
WHERE pw.printer_id = printer_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_router_after_workplace;
DELIMITER //
CREATE PROCEDURE get_router_after_workplace(IN workplace_id INT)
BEGIN
SELECT r.id router_id, r.model model, b.name brand
FROM router r
JOIN router_in_workplace rw ON r.id = rw.router_id
JOIN brand b ON b.id = r.brand_id
WHERE rw.workplace_id = workplace_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_workplace_after_router;
DELIMITER //
CREATE PROCEDURE get_workplace_after_router(IN router_id INT)
BEGIN
SELECT w.id workplace_id, e.name, e.surname, e.pass_number
FROM workplace w
JOIN router_in_workplace rw ON w.id = rw.workplace_id
JOIN employee e ON w.employee_id = e.id
WHERE rw.router_id = router_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_printer_after_type;
DELIMITER //
CREATE PROCEDURE get_printer_after_type(IN type_id INT)
BEGIN
SELECT t.name, b.name, p.model, p.price
FROM printer p
JOIN type t ON p.type_id = t.id
JOIN brand b ON p.brand_id = b.id
WHERE t.id = type_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_address_after_location_type;
DELIMITER //
CREATE PROCEDURE get_address_after_location_type(IN location_type_id INT)
BEGIN
SELECT lt.location_name, a.city, a.street, a.house_number
FROM address a
JOIN office o ON a.id = o.address_id
JOIN location_type lt ON o.location_type_id = lt.id
WHERE o.location_type_id = location_type_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_location_type_after_address;
DELIMITER //
CREATE PROCEDURE get_location_type_after_address(IN address_id INT)
BEGIN
SELECT lt.location_name, a.city, a.street, a.house_number
FROM location_type lt
JOIN office o ON lt.id = o.location_type_id
JOIN address a ON o.address_id = a.id
WHERE o.address_id = address_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_employee_after_position;
DELIMITER //
CREATE PROCEDURE get_employee_after_position(IN position_id INT)
BEGIN
SELECT p.name position, e.name, e.surname, e.pass_number
FROM position p
JOIN employee e ON e.position_id = p.id
WHERE e.position_id = position_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_office_after_employee;
DELIMITER //
CREATE PROCEDURE get_office_after_employee(IN employee_id INT)
BEGIN
SELECT w.office_id, lt.location_name, a.city, a.street, a.house_number
FROM workplace w
JOIN office o ON w.office_id = o.id
JOIN address a ON a.id = o.address_id
JOIN location_type lt ON lt.id = o.location_type_id
WHERE w.employee_id = employee_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_employee_after_office;
DELIMITER //
CREATE PROCEDURE get_employee_after_office(IN office_id INT)
BEGIN
SELECT w.employee_id, lt.location_name, a.city, a.street, a.house_number, e.name, e.surname
FROM workplace w
JOIN office o ON w.office_id = o.id
JOIN address a ON a.id = o.address_id
JOIN location_type lt ON lt.id = o.location_type_id
JOIN employee e ON e.id = w.employee_id
WHERE  w.office_id = office_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_access_point_after_brand_id;
DELIMITER //
CREATE PROCEDURE get_access_point_after_brand_id(IN brand_id INT)
BEGIN
SELECT b.name, ap.model
FROM brand b
JOIN access_point ap ON ap.brand_id = b.id
WHERE b.id = brand_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_computer_after_brand_id;
DELIMITER //
CREATE PROCEDURE get_computer_after_brand_id(IN brand_id INT)
BEGIN
SELECT b.name, c.model
FROM brand b
JOIN computer c ON c.brand_id = b.id
WHERE b.id = brand_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_ip_phone_after_brand_id;
DELIMITER //
CREATE PROCEDURE get_ip_phone_after_brand_id(IN brand_id INT)
BEGIN
SELECT b.name, ip.model
FROM brand b
JOIN ip_phone ip ON ip.brand_id = b.id
WHERE b.id = brand_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_monitor_after_brand_id;
DELIMITER //
CREATE PROCEDURE get_monitor_after_brand_id(IN brand_id INT)
BEGIN
SELECT b.name, m.model
FROM brand b
JOIN monitor m ON m.brand_id = b.id
WHERE b.id = brand_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_printer_after_brand_id;
DELIMITER //
CREATE PROCEDURE get_printer_after_brand_id(IN brand_id INT)
BEGIN
SELECT b.name, p.model
FROM brand b
JOIN printer p ON p.brand_id = b.id
WHERE b.id = brand_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_router_after_brand_id;
DELIMITER //
CREATE PROCEDURE get_router_after_brand_id(IN brand_id INT)
BEGIN
SELECT b.name, r.model
FROM brand b
JOIN router r ON r.brand_id = b.id
WHERE b.id = brand_id;
END //
DELIMITER ;