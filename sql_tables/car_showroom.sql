-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: car_showroom
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `автомобіль`
--

DROP TABLE IF EXISTS `автомобіль`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `автомобіль` (
  `ІД` int NOT NULL AUTO_INCREMENT,
  `IД складу` int NOT NULL,
  `Марка` varchar(45) NOT NULL,
  `Модель` varchar(45) NOT NULL,
  `Тип` varchar(45) NOT NULL,
  `Макс. швидкість` int NOT NULL,
  `Колір` varchar(45) NOT NULL,
  `Ціна` double NOT NULL,
  PRIMARY KEY (`ІД`,`IД складу`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `автомобіль`
--

LOCK TABLES `автомобіль` WRITE;
/*!40000 ALTER TABLE `автомобіль` DISABLE KEYS */;
INSERT INTO `автомобіль` VALUES (1,1,'BMW','M5','passenger',305,'red',125993),(2,1,'Nissan','Almera','passenger',184,'white',5900),(3,1,'Man','F2000','freight',110,'white',10500),(4,2,'Mazda','6','passenger',220,'red',30455),(5,2,'Ford','Tourneo','minibus',157,'grey',33592),(6,2,'Mercedes','C-class','Coupe',249,'black',52080),(7,2,'Mitsubishi','L200','Pickup',167,'black',31248),(8,2,'Volvo','V40','Hatchback',210,'cream',26040);
/*!40000 ALTER TABLE `автомобіль` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `договір`
--

DROP TABLE IF EXISTS `договір`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `договір` (
  `ІД` int NOT NULL AUTO_INCREMENT,
  `IBAN` varchar(45) DEFAULT NULL,
  `ІД автомобіля` int NOT NULL,
  `Статус` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ІД`,`ІД автомобіля`),
  KEY `Покупка_idx` (`ІД автомобіля`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `договір`
--

LOCK TABLES `договір` WRITE;
/*!40000 ALTER TABLE `договір` DISABLE KEYS */;
INSERT INTO `договір` VALUES (1,'32547897563216',1,'Виконано'),(2,'84621956385092',4,'В процесі'),(3,'74839236126473',5,'Виконано');
/*!40000 ALTER TABLE `договір` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `замовлення`
--

DROP TABLE IF EXISTS `замовлення`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `замовлення` (
  `ІД` int NOT NULL AUTO_INCREMENT,
  `ІД складу` int NOT NULL,
  `IBAN` varchar(45) NOT NULL,
  `Дата доставки` date NOT NULL,
  `Статус` varchar(45) NOT NULL,
  `Кількість` int NOT NULL,
  `Деталі` varchar(200) NOT NULL,
  PRIMARY KEY (`ІД`,`IBAN`,`ІД складу`),
  KEY `Замовлення_idx` (`ІД складу`),
  KEY `Постачальник_idx` (`IBAN`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `замовлення`
--

LOCK TABLES `замовлення` WRITE;
/*!40000 ALTER TABLE `замовлення` DISABLE KEYS */;
INSERT INTO `замовлення` VALUES (1,2,'74635297431209','2021-04-06','Виконано',4,'BMW GT, green'),(2,1,'74836534219856','2021-05-13','В процесі',3,'Volvo S90, blue');
/*!40000 ALTER TABLE `замовлення` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `постачальник`
--

DROP TABLE IF EXISTS `постачальник`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `постачальник` (
  `IBAN` varchar(45) NOT NULL,
  `Назва` varchar(45) NOT NULL,
  `Адреса` varchar(45) NOT NULL,
  `Телефон` varchar(45) NOT NULL,
  PRIMARY KEY (`IBAN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `постачальник`
--

LOCK TABLES `постачальник` WRITE;
/*!40000 ALTER TABLE `постачальник` DISABLE KEYS */;
INSERT INTO `постачальник` VALUES ('74635297431209','\"Star\"','вул. Абжанова 12','+38(095)-345-26-78'),('74836534219856','\"CarMeh\"','вул. Герзонська 4','+38(050)-629-45-77');
/*!40000 ALTER TABLE `постачальник` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `склад`
--

DROP TABLE IF EXISTS `склад`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `склад` (
  `ІД` int NOT NULL,
  `Кількість авто` int NOT NULL,
  PRIMARY KEY (`ІД`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `склад`
--

LOCK TABLES `склад` WRITE;
/*!40000 ALTER TABLE `склад` DISABLE KEYS */;
INSERT INTO `склад` VALUES (1,3),(2,5);
/*!40000 ALTER TABLE `склад` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-08 23:27:27
