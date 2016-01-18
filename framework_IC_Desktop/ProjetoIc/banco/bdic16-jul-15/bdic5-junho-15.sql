-- phpMyAdmin SQL Dump
-- version 4.1.12
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: 04-Jun-2015 às 14:49
-- Versão do servidor: 5.6.16
-- PHP Version: 5.5.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

CREATE SCHEMA IF NOT EXISTS `bdic` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `bdic` ;

--
-- Database: `bdic`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `datasource`
--

CREATE TABLE IF NOT EXISTS `bdic`.`datasource` (
  `idDATASOURCE` int(11) NOT NULL AUTO_INCREMENT,
  `NAME` varchar(45) NOT NULL,
  `MANUFACTURER` varchar(45) DEFAULT NULL,
  `MODEL` varchar(45) DEFAULT NULL,
  `site_idSITE` int(11) DEFAULT NULL,
  PRIMARY KEY (`idDATASOURCE`),
  KEY `fk_datasource_node1_idx` (`site_idSITE`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- Extraindo dados da tabela `datasource`
--

INSERT INTO `bdic`.`datasource` (`idDATASOURCE`, `NAME`, `MANUFACTURER`, `MODEL`, `site_idSITE`) VALUES
(1, 'Nó 1', 'Fabricante 1', 'Modelo 1', 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `django_migrations`
--

CREATE TABLE IF NOT EXISTS `bdic`.`django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estrutura da tabela `radio`
--

CREATE TABLE IF NOT EXISTS `bdic`.`radio` (
  `idRADIO` int(11) NOT NULL AUTO_INCREMENT,
  `ENDREAL` varchar(64) DEFAULT NULL,
  `radioInfo_idRADIOINFO` int(11) NOT NULL,
  `datasource_idDATASOURCE` int(11) DEFAULT NULL,
  PRIMARY KEY (`idRADIO`),
  KEY `fk_radio_radioTipo1_idx` (`radioInfo_idRADIOINFO`),
  KEY `fk_radio_datasource1_idx` (`datasource_idDATASOURCE`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Extraindo dados da tabela `radio`
--

INSERT INTO `bdic`.`radio` (`idRADIO`, `ENDREAL`, `radioInfo_idRADIOINFO`, `datasource_idDATASOURCE`) VALUES
(2, '234324235232423', 1, 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `radioinfo`
--

CREATE TABLE IF NOT EXISTS `bdic`.`radioinfo` (
  `idRADIOINFO` int(11) NOT NULL AUTO_INCREMENT,
  `NAME` varchar(45) NOT NULL,
  `DESCRIPTION` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`idRADIOINFO`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- Extraindo dados da tabela `radioinfo`
--

INSERT INTO `bdic`.`radioinfo` (`idRADIOINFO`, `NAME`, `DESCRIPTION`) VALUES
(1, 'wi-fi', '50m');

-- --------------------------------------------------------

--
-- Estrutura da tabela `site`
--

CREATE TABLE IF NOT EXISTS `bdic`.`site` (
  `idSITE` int(11) NOT NULL AUTO_INCREMENT,
  `NAME` varchar(45) NOT NULL,
  `INFORMATION` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idSITE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `site`
--

INSERT INTO `bdic`.`site` (`idSITE`, `NAME`, `INFORMATION`) VALUES
(1, 'UEFS', 'MODULO1');

-- --------------------------------------------------------

--
-- Estrutura da tabela `snapshot`
--

CREATE TABLE IF NOT EXISTS `bdic`.`snapshot` (
  `idSNAP` int(11) NOT NULL AUTO_INCREMENT,
  `VALUE` float NOT NULL,
  `SNAPSHOT` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `tag_idTAG` int(11) NOT NULL,
  PRIMARY KEY (`idSNAP`),
  KEY `fk_snapshot_tag1_idx` (`tag_idTAG`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tag`
--

CREATE TABLE IF NOT EXISTS `bdic`.`tag` (
  `idTAG` int(11) NOT NULL AUTO_INCREMENT,
  `DEVIATION` float DEFAULT NULL,
  `TIME_MAX` int(11) DEFAULT NULL,
  `CONV_RATE` int(11) DEFAULT NULL,
  `tagInfo_idTAGINFO` int(11) NOT NULL,
  `datasource_idDATASOURCE` int(11) DEFAULT NULL,
  PRIMARY KEY (`idTAG`),
  KEY `fk_tag_tagInfo2_idx` (`tagInfo_idTAGINFO`),
  KEY `fk_tag_datasource1_idx` (`datasource_idDATASOURCE`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=5 ;

--
-- Extraindo dados da tabela `tag`
--

INSERT INTO `bdic`.`tag` (`idTAG`, `DEVIATION`, `TIME_MAX`, `CONV_RATE`, `tagInfo_idTAGINFO`, `datasource_idDATASOURCE`) VALUES
(2, 1.2, 300, 2313, 2, 1),
(3, 1.2, 300, 2131, 3, 1),
(4, 1.2, 300, 2212, 1, 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `taginfo`
--

CREATE TABLE IF NOT EXISTS `bdic`.`taginfo` (
  `idTAGINFO` int(11) NOT NULL AUTO_INCREMENT,
  `NAME` varchar(45) NOT NULL,
  `DESCRIPTION` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idTAGINFO`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

--
-- Extraindo dados da tabela `taginfo`
--

INSERT INTO `bdic`.`taginfo` (`idTAGINFO`, `NAME`, `DESCRIPTION`) VALUES
(1, 'LM-35', 'Sensor de temperatura'),
(2, 'HC-SR04', 'Sensor de distância'),
(3, 'TSL2561', 'Sensor de luminosidade');

-- --------------------------------------------------------

--
-- Estrutura da tabela `values`
--

CREATE TABLE IF NOT EXISTS `bdic`.`values` (
  `idVALUES` int(11) NOT NULL AUTO_INCREMENT,
  `VALUE` float NOT NULL,
  `DATETIME` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `tag_idTAG` int(11) NOT NULL,
  PRIMARY KEY (`idVALUES`),
  KEY `fk_valores_tag1_idx` (`tag_idTAG`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=195 ;

--
-- Extraindo dados da tabela `values`
--

INSERT INTO `bdic`.`values` (`idVALUES`, `VALUE`, `DATETIME`, `tag_idTAG`) VALUES
(102, 1.65, '2012-01-16 03:04:39', 4),
(103, 0.000763, '2012-01-16 03:05:19', 2),
(104, 5, '2012-01-16 03:05:59', 2),
(105, 0, '2012-01-16 03:06:59', 2),
(106, 0.00412, '2012-01-16 03:09:19', 3),
(107, 1.64, '2012-01-16 03:18:40', 4),
(108, 0.00206, '2012-01-16 03:21:20', 2),
(109, 0.0029, '2012-01-16 03:23:21', 3),
(110, 0.00572, '2012-01-16 03:24:01', 2),
(111, 5, '2012-01-16 03:25:21', 2),
(112, 0.00206, '2012-01-16 03:26:01', 2),
(113, 1.63, '2012-01-16 03:32:41', 4),
(114, 0.00412, '2012-01-16 03:38:02', 3),
(115, 0, '2012-01-16 03:40:22', 2),
(116, 1.63, '2012-01-16 03:46:43', 4),
(117, 0.0029, '2012-01-16 03:52:03', 3),
(118, 0.00328, '2012-01-16 03:54:23', 2),
(119, 1.63, '2012-01-16 04:00:44', 4),
(120, 0.00412, '2012-01-16 04:06:04', 3),
(121, 0.000763, '2012-01-16 04:08:05', 2),
(122, 1.65, '2012-01-16 04:14:46', 4),
(123, 0, '2012-01-16 04:20:26', 3),
(124, 0.000763, '2012-01-16 04:22:26', 2),
(125, 1.65, '2012-01-16 04:28:47', 4),
(126, 0.00168, '2012-01-16 04:35:07', 3),
(127, 0.000763, '2012-01-16 04:37:08', 2),
(128, 1.65, '2012-01-16 04:42:48', 4),
(129, 0.00412, '2012-01-16 04:49:28', 3),
(130, 0.0045, '2012-01-16 04:51:09', 2),
(131, 1.63661, '2012-01-16 04:56:50', 4),
(132, 0.00168, '2012-01-16 05:04:10', 3),
(133, 0.0045, '2012-01-16 05:05:30', 2),
(134, 1.62, '2012-01-16 05:10:51', 4),
(135, 0, '2012-01-16 05:18:12', 3),
(136, 0.00328, '2012-01-16 05:19:12', 2),
(137, 1.62, '2012-01-16 05:24:52', 4),
(138, 0.00412, '2012-01-16 05:32:33', 3),
(139, 0.0045, '2012-01-16 05:33:13', 2),
(140, 1.62, '2012-01-16 05:38:53', 4),
(141, 0, '2012-01-16 05:47:34', 2),
(142, 0.000458, '2012-01-16 05:47:14', 3),
(143, 1.65, '2012-01-16 05:52:55', 4),
(144, 0.0029, '2012-01-16 06:01:16', 3),
(145, 0, '2012-01-16 06:01:36', 2),
(146, 1.67, '2012-01-16 06:06:57', 4),
(147, 0, '2012-01-16 06:15:18', 3),
(148, 0.00572, '2012-01-16 06:15:38', 2),
(149, 1.63, '2012-01-16 06:20:58', 4),
(150, 0, '2012-01-16 06:29:19', 3),
(151, 0.00328, '2012-01-16 06:30:19', 2),
(152, 1.61, '2012-01-16 06:34:59', 4),
(153, 0.000458, '2012-01-16 06:43:40', 3),
(154, 0.00328, '2012-01-16 06:44:21', 2),
(155, 1.62, '2012-01-16 06:49:01', 4),
(156, 0, '2012-01-16 06:58:42', 2),
(157, 0.00168, '2012-01-16 06:58:22', 3),
(158, 1.63, '2012-01-16 07:03:02', 4),
(159, 0.00412, '2012-01-16 07:12:43', 3),
(160, 0.000763, '2012-01-16 07:12:23', 2),
(161, 1.62, '2012-01-16 07:17:03', 4),
(162, 0, '2012-01-16 07:26:44', 2),
(163, 0.00412, '2012-01-16 07:26:24', 3),
(164, 1.61, '2012-01-16 07:31:05', 4),
(165, 0.000458, '2012-01-16 07:40:26', 3),
(166, 0, '2012-01-16 07:41:26', 2),
(167, 1.6, '2012-01-16 07:45:06', 4),
(168, 0.00168, '2012-01-16 07:54:47', 3),
(169, 0, '2012-01-16 07:55:27', 2),
(170, 1.62, '2012-01-16 07:59:07', 4),
(171, 0, '2012-01-16 08:09:28', 3),
(172, 0.000763, '2012-01-16 08:09:48', 2),
(173, 1.63, '2012-01-16 08:13:09', 4),
(174, 0.0116, '2012-01-16 08:23:49', 3),
(175, 0, '2012-01-16 08:24:29', 2),
(176, 1.61, '2012-01-16 08:27:10', 4),
(177, 0.0722, '2012-01-16 08:37:51', 3),
(178, 0.0367, '2012-01-16 08:38:31', 2),
(179, 1.67, '2012-01-16 08:41:11', 4),
(180, 0.195926, '2012-01-16 08:51:52', 3),
(181, 0.109712, '2012-01-16 08:52:32', 2),
(182, 1.73808, '2012-01-16 08:55:12', 4),
(183, 0.143969, '2012-01-16 09:05:53', 3),
(184, 0.109712, '2012-01-16 09:06:33', 2),
(185, 1.71832, '2012-01-16 09:09:14', 4),
(186, 0.304112, '2012-01-16 09:19:36', 2),
(187, 0.344396, '2012-01-16 09:19:56', 3),
(188, 0.213245, '2012-01-16 09:22:56', 3),
(189, 1.8545, '2012-01-16 09:23:16', 4),
(190, 0.274357, '2012-01-16 09:33:37', 2),
(191, 0.335088, '2012-01-16 09:35:37', 2),
(192, 0.374075, '2012-01-16 09:35:57', 3),
(193, 0.492256, '2012-01-16 09:36:37', 2),
(194, 0.574502, '2012-01-16 09:36:57', 3);

--
-- Constraints for dumped tables
--

--
-- Limitadores para a tabela `datasource`
--
ALTER TABLE `bdic`.`datasource`
  ADD CONSTRAINT `fk_datasource_node1` FOREIGN KEY (`site_idSITE`) REFERENCES `site` (`idSITE`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limitadores para a tabela `radio`
--
ALTER TABLE `bdic`.`radio`
  ADD CONSTRAINT `fk_radio_datasource1` FOREIGN KEY (`datasource_idDATASOURCE`) REFERENCES `datasource` (`idDATASOURCE`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_radio_radioTipo1` FOREIGN KEY (`radioInfo_idRADIOINFO`) REFERENCES `radioinfo` (`idRADIOINFO`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limitadores para a tabela `snapshot`
--
ALTER TABLE `bdic`.`snapshot`
  ADD CONSTRAINT `fk_snapshot_tag1` FOREIGN KEY (`tag_idTAG`) REFERENCES `tag` (`idTAG`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limitadores para a tabela `tag`
--
ALTER TABLE `bdic`.`tag`
  ADD CONSTRAINT `fk_tag_datasource1` FOREIGN KEY (`datasource_idDATASOURCE`) REFERENCES `datasource` (`idDATASOURCE`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_tag_tagInfo2` FOREIGN KEY (`tagInfo_idTAGINFO`) REFERENCES `taginfo` (`idTAGINFO`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limitadores para a tabela `values`
--
ALTER TABLE `bdic`.`values`
  ADD CONSTRAINT `fk_valores_tag1` FOREIGN KEY (`tag_idTAG`) REFERENCES `tag` (`idTAG`) ON DELETE NO ACTION ON UPDATE NO ACTION;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
