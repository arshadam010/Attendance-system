-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: class12
-- ------------------------------------------------------
-- Server version	8.0.44

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
-- Table structure for table `b1`
--

DROP TABLE IF EXISTS `b1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `b1` (
  `Roll_no` int NOT NULL,
  `s_id` int NOT NULL,
  `Name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`s_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `b1`
--

LOCK TABLES `b1` WRITE;
/*!40000 ALTER TABLE `b1` DISABLE KEYS */;
INSERT INTO `b1` VALUES (1,10001,'Abhash'),(2,10002,'A N Ashwin Sriram'),(3,10003,'Arshad Ahamad M'),(4,10004,'Bharath'),(5,10005,'Chiranth'),(6,10006,'Darshita'),(7,10007,'D Priya'),(8,10008,'Dhairya Kumar'),(9,10009,'Dhruv Patil'),(10,10010,'Edward P N'),(11,10011,'Hasini V'),(12,10012,'Janavi '),(13,10013,'Joshua D'),(14,10014,'Kevin Pinto'),(15,10015,'L Eshant'),(16,10016,'Lisa Sinha'),(17,10017,'M Trisha'),(18,10018,'Nagisetty Vaghdevi'),(19,10019,'Naman Rangar');
/*!40000 ALTER TABLE `b1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `b2`
--

DROP TABLE IF EXISTS `b2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `b2` (
  `Roll_no` int NOT NULL,
  `s_id` int NOT NULL,
  `Name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`s_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `b2`
--

LOCK TABLES `b2` WRITE;
/*!40000 ALTER TABLE `b2` DISABLE KEYS */;
INSERT INTO `b2` VALUES (1,10020,'Nethra'),(2,10021,'Omkumar Sharma'),(3,10022,'P Daksh Shanthram'),(4,10023,'Prarthana M'),(5,10024,'R Nipun'),(6,10025,'Santosh J'),(7,10026,'Shourya Kumar'),(8,10027,'Utkarsh Gupta'),(9,10028,'V Spandana'),(10,10029,'V Pratap Tejas'),(11,10030,'Vimal kumar V'),(12,10031,'Yashas Y S'),(13,10032,'Sheril S'),(14,10033,'Samradh Verma'),(15,10034,'Navnith J'),(16,10035,'Priyanshu'),(17,10036,'Aditya'),(18,10037,'Amarendra'),(19,10038,'Adith');
/*!40000 ALTER TABLE `b2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profile`
--

DROP TABLE IF EXISTS `profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profile` (
  `user_name` varchar(30) NOT NULL,
  `password` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profile`
--

LOCK TABLES `profile` WRITE;
/*!40000 ALTER TABLE `profile` DISABLE KEYS */;
INSERT INTO `profile` VALUES ('principal','princi@kvnal'),('aary@','@@ry.123'),('riy@','riy.math');
/*!40000 ALTER TABLE `profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teachers`
--

DROP TABLE IF EXISTS `teachers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teachers` (
  `USER_NAME` varchar(50) NOT NULL,
  `NAME` varchar(30) DEFAULT NULL,
  `DESIGNATION` varchar(15) DEFAULT NULL,
  `ASSIGNED_CLASS` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`USER_NAME`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teachers`
--

LOCK TABLES `teachers` WRITE;
/*!40000 ALTER TABLE `teachers` DISABLE KEYS */;
INSERT INTO `teachers` VALUES ('aary@','AARYAN M','PGT CS','B1'),('riy@','RIYA V','PGT MATHS','B2');
/*!40000 ALTER TABLE `teachers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-01-01  3:43:04
