-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 15, 2023 at 04:39 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `prototype`
--

-- --------------------------------------------------------

--
-- Table structure for table `config`
--

CREATE TABLE `config` (
  `id` int(11) NOT NULL,
  `environment` varchar(255) DEFAULT NULL,
  `section` varchar(255) DEFAULT NULL,
  `key` varchar(255) DEFAULT NULL,
  `value` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `config`
--

INSERT INTO `config` (`id`, `environment`, `section`, `key`, `value`) VALUES
(1, 'development', 'database', 'connectionString', 'Server=(devdb)\\mssqllocaldb;Database=IdentityServer4Admin;Trusted_Connection=True;MultipleActiveResultSets=true'),
(2, 'development', 'database', 'maxConnections', '24'),
(3, 'development', 'database', 'timeout', '34'),
(4, 'development', 'database', 'backupEnabled', '2'),
(5, 'development', 'database', 'backupFrequency', 'daily'),
(6, 'development', 'logging', 'level', 'debugging'),
(7, 'development', 'logging', 'logToFile', '1'),
(8, 'development', 'logging', 'logFilePath', '/var/log/app_dev.logger'),
(9, 'development', 'logging', 'maxFileSize', '12MB'),
(10, 'development', 'api', 'baseUrl', 'http://api.dev.example.com'),
(11, 'development', 'api', 'timeout', '999'),
(12, 'development', 'api', 'corsEnabled', '1'),
(13, 'development', 'api', 'maxRequestPerMinute', '7000'),
(14, 'development', 'email', 'smtpServer', 'smtp.dev.example.com'),
(15, 'development', 'email', 'port', '908'),
(16, 'development', 'email', 'username', 'user@example.com'),
(17, 'development', 'email', 'password', 'dev_email_password'),
(18, 'development', 'email', 'senderEmail', 'noreply@dev.example.com'),
(19, 'development', 'email', 'defaultTemplate', 'default_template.html'),
(20, 'development', 'cache', 'enabled', '1'),
(21, 'development', 'cache', 'maxSize', '100MB'),
(22, 'development', 'cache', 'expirationTime', '600'),
(23, 'development', 'api2', 'baseUrl', 'http://api.dev.example.com'),
(24, 'development', 'api2', 'timeout', '999'),
(25, 'development', 'api2', 'corsEnabled', '1'),
(26, 'development', 'api2', 'maxRequestPerMinute', '7000'),
(27, 'development', 'api2', 'maxFileSize1', '12MB'),
(28, 'QA', 'database', 'connectionString', 'Server=(qadb)\\mssqllocaldb;Database=IdentityServer4Admin;Trusted_Connection=True;MultipleActiveResultSets=true'),
(29, 'QA', 'database', 'maxConnections', '100'),
(30, 'QA', 'database', 'timeout', '20'),
(31, 'QA', 'database', 'backupEnabled', '1'),
(32, 'QA', 'database', 'backupFrequency', 'weekly'),
(33, 'QA', 'logging', 'level', 'info'),
(34, 'QA', 'logging', 'logToFile', '1'),
(35, 'QA', 'logging', 'logFilePath', '/var/log/app_qa.log'),
(36, 'QA', 'logging', 'maxFileSize', '5MB'),
(37, 'QA', 'api', 'baseUrl', 'http://api.qa.example.com'),
(38, 'QA', 'api', 'timeout', '3000'),
(39, 'QA', 'api', 'corsEnabled', '0'),
(40, 'QA', 'api', 'maxRequestPerMinute', '599945'),
(41, 'QA', 'api', 'maxFileSize2', '5MB'),
(42, 'QA', 'email', 'smtpServer', 'smtp.qa.example.com'),
(43, 'QA', 'email', 'port', '587'),
(44, 'QA', 'email', 'username', 'user@example.com'),
(45, 'QA', 'email', 'password', 'qa_email_password'),
(46, 'QA', 'email', 'senderEmail', 'noreply@qa.example.com'),
(47, 'QA', 'email', 'defaultTemplate', 'default_template.html'),
(48, 'QA', 'cache', 'enabled', '1'),
(49, 'QA', 'cache', 'maxSize', '50MB'),
(50, 'QA', 'cache', 'expirationTime', '900'),
(51, 'production', 'database', 'connectionString', 'Server=(proddb)\\mssqllocaldb;Database=IdentityServer4Admin;Trusted_Connection=True;MultipleActiveResultSets=true'),
(52, 'production', 'database', 'maxConnections', '200'),
(53, 'production', 'database', 'timeout', '15'),
(54, 'production', 'database', 'backupEnabled', '1'),
(55, 'production', 'database', 'backupFrequency', 'monthly'),
(56, 'production', 'logging', 'level', 'warning'),
(57, 'production', 'logging', 'logToFile', '0'),
(58, 'production', 'logging', 'maxFileSize', '20MB'),
(59, 'production', 'api', 'baseUrl', 'https://api.example.com'),
(60, 'production', 'api', 'timeout', '1000'),
(61, 'production', 'api', 'corsEnabled', '1'),
(62, 'production', 'api', 'maxRequestPerMinute', '2000'),
(63, 'production', 'email', 'smtpServer', 'smtp.example.com'),
(64, 'production', 'email', 'port', '587'),
(65, 'production', 'email', 'username', 'user_name@example.com'),
(66, 'production', 'email', 'password', 'prod_email_password'),
(67, 'production', 'email', 'senderEmail', 'noreply@example.com'),
(68, 'production', 'email', 'defaultTemplate', 'default_template.html'),
(69, 'production', 'cache', 'enabled', '1'),
(70, 'production', 'cache', 'maxSize', '200MB'),
(71, 'production', 'cache', 'expirationTime', '1200');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `config`
--
ALTER TABLE `config`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `config`
--
ALTER TABLE `config`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=72;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
