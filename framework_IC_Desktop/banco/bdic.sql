-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: 28-Jan-2016 às 18:28
-- Versão do servidor: 10.1.9-MariaDB
-- PHP Version: 5.5.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bdic`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `datasource`
--

CREATE TABLE `datasource` (
  `idDATASOURCE` int(11) NOT NULL,
  `NAME` varchar(45) NOT NULL,
  `MANUFACTURER` varchar(45) DEFAULT NULL,
  `MODEL` varchar(45) DEFAULT NULL,
  `site_idSITE` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- --------------------------------------------------------

--
-- Estrutura da tabela `radio`
--

CREATE TABLE `radio` (
  `idRADIO` int(11) NOT NULL,
  `ENDREAL` varchar(64) DEFAULT NULL,
  `radioInfo_idRADIOINFO` int(11) NOT NULL,
  `datasource_idDATASOURCE` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Estrutura da tabela `radioinfo`
--

CREATE TABLE `radioinfo` (
  `idRADIOINFO` int(11) NOT NULL,
  `NAME` varchar(45) NOT NULL,
  `DESCRIPTION` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Estrutura da tabela `site`
--

CREATE TABLE `site` (
  `idSITE` int(11) NOT NULL,
  `NAME` varchar(45) NOT NULL,
  `INFORMATION` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- --------------------------------------------------------

--
-- Estrutura da tabela `snapshot`
--

CREATE TABLE `snapshot` (
  `idSNAP` int(11) NOT NULL,
  `VALUE` float NOT NULL,
  `SNAPSHOT` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `tag_idTAG` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;




-- --------------------------------------------------------

--
-- Estrutura da tabela `tag`
--

CREATE TABLE `tag` (
  `idTAG` int(11) NOT NULL,
  `DEVIATION` float DEFAULT NULL,
  `TIME_MAX` int(11) DEFAULT NULL,
  `CONV_RATE` int(11) DEFAULT NULL,
  `CHANNEL` int(11) DEFAULT NULL,
  `tagInfo_idTAGINFO` int(11) NOT NULL,
  `datasource_idDATASOURCE` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- --------------------------------------------------------

--
-- Estrutura da tabela `taginfo`
--

CREATE TABLE `taginfo` (
  `idTAGINFO` int(11) NOT NULL,
  `NAME` varchar(45) NOT NULL,
  `DESCRIPTION` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `taginfo`
--


-- --------------------------------------------------------

--
-- Estrutura da tabela `values`
--

CREATE TABLE `values` (
  `idVALUES` int(11) NOT NULL,
  `VALUE` float NOT NULL,
  `DATETIME` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `tag_idTAG` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--
-- Indexes for dumped tables
--

--
-- Indexes for table `datasource`
--
ALTER TABLE `datasource`
  ADD PRIMARY KEY (`idDATASOURCE`),
  ADD KEY `fk_datasource_node1_idx` (`site_idSITE`);

--
-- Indexes for table `radio`
--
ALTER TABLE `radio`
  ADD PRIMARY KEY (`idRADIO`),
  ADD KEY `fk_radio_radioTipo1_idx` (`radioInfo_idRADIOINFO`),
  ADD KEY `fk_radio_datasource1_idx` (`datasource_idDATASOURCE`);

--
-- Indexes for table `radioinfo`
--
ALTER TABLE `radioinfo`
  ADD PRIMARY KEY (`idRADIOINFO`);

--
-- Indexes for table `site`
--
ALTER TABLE `site`
  ADD PRIMARY KEY (`idSITE`);

--
-- Indexes for table `snapshot`
--
ALTER TABLE `snapshot`
  ADD PRIMARY KEY (`idSNAP`),
  ADD KEY `fk_snapshot_tag1_idx` (`tag_idTAG`);

--
-- Indexes for table `tag`
--
ALTER TABLE `tag`
  ADD PRIMARY KEY (`idTAG`),
  ADD KEY `fk_tag_tagInfo2_idx` (`tagInfo_idTAGINFO`),
  ADD KEY `fk_tag_datasource1_idx` (`datasource_idDATASOURCE`);

--
-- Indexes for table `taginfo`
--
ALTER TABLE `taginfo`
  ADD PRIMARY KEY (`idTAGINFO`);

--
-- Indexes for table `values`
--
ALTER TABLE `values`
  ADD PRIMARY KEY (`idVALUES`),
  ADD KEY `fk_valores_tag1_idx` (`tag_idTAG`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `datasource`
--
ALTER TABLE `datasource`
  MODIFY `idDATASOURCE` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `radio`
--
ALTER TABLE `radio`
  MODIFY `idRADIO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `radioinfo`
--
ALTER TABLE `radioinfo`
  MODIFY `idRADIOINFO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `site`
--
ALTER TABLE `site`
  MODIFY `idSITE` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `snapshot`
--
ALTER TABLE `snapshot`
  MODIFY `idSNAP` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `tag`
--
ALTER TABLE `tag`
  MODIFY `idTAG` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;
--
-- AUTO_INCREMENT for table `taginfo`
--
ALTER TABLE `taginfo`
  MODIFY `idTAGINFO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `values`
--
ALTER TABLE `values`
  MODIFY `idVALUES` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=414;
--
-- Constraints for dumped tables
--

--
-- Limitadores para a tabela `datasource`
--
ALTER TABLE `datasource`
  ADD CONSTRAINT `fk_datasource_node1` FOREIGN KEY (`site_idSITE`) REFERENCES `site` (`idSITE`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limitadores para a tabela `radio`
--
ALTER TABLE `radio`
  ADD CONSTRAINT `fk_radio_datasource1` FOREIGN KEY (`datasource_idDATASOURCE`) REFERENCES `datasource` (`idDATASOURCE`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_radio_radioTipo1` FOREIGN KEY (`radioInfo_idRADIOINFO`) REFERENCES `radioinfo` (`idRADIOINFO`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limitadores para a tabela `snapshot`
--
ALTER TABLE `snapshot`
  ADD CONSTRAINT `fk_snapshot_tag1` FOREIGN KEY (`tag_idTAG`) REFERENCES `tag` (`idTAG`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limitadores para a tabela `tag`
--
ALTER TABLE `tag`
  ADD CONSTRAINT `fk_tag_datasource1` FOREIGN KEY (`datasource_idDATASOURCE`) REFERENCES `datasource` (`idDATASOURCE`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_tag_tagInfo2` FOREIGN KEY (`tagInfo_idTAGINFO`) REFERENCES `taginfo` (`idTAGINFO`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limitadores para a tabela `values`
--
ALTER TABLE `values`
  ADD CONSTRAINT `fk_valores_tag1` FOREIGN KEY (`tag_idTAG`) REFERENCES `tag` (`idTAG`) ON DELETE NO ACTION ON UPDATE NO ACTION;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
