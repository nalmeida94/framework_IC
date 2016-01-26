-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: 23-Abr-2015 às 01:24
-- Versão do servidor: 5.6.21
-- PHP Version: 5.5.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `bdic`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `datasource`
--

CREATE TABLE IF NOT EXISTS `datasource` (
`idESTACAO_METEO` int(11) NOT NULL,
  `NOME_ESTACAO` varchar(45) DEFAULT NULL,
  `FABRICANTE` varchar(45) DEFAULT NULL,
  `MODELO` varchar(45) DEFAULT NULL,
  `node_idNODE` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `datasource`
--

INSERT INTO `datasource` (`idESTACAO_METEO`, `NOME_ESTACAO`, `FABRICANTE`, `MODELO`, `node_idNODE`) VALUES
(1, 'Nó 1', 'Fabricante 1', 'Modelo 1', 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `node`
--

CREATE TABLE IF NOT EXISTS `node` (
`idNODE` int(11) NOT NULL,
  `NOME` varchar(45) DEFAULT NULL,
  `INFORMACOES` varchar(45) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `node`
--

INSERT INTO `node` (`idNODE`, `NOME`, `INFORMACOES`) VALUES
(1, 'Modulo 1', 'Muito Bom');

-- --------------------------------------------------------

--
-- Estrutura da tabela `radio`
--

CREATE TABLE IF NOT EXISTS `radio` (
`idradio` int(11) NOT NULL,
  `endReal` varchar(64) DEFAULT NULL,
  `radioTipo_idradioTipo` int(11) NOT NULL,
  `datasource_idESTACAO_METEO` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `radio`
--

INSERT INTO `radio` (`idradio`, `endReal`, `radioTipo_idradioTipo`, `datasource_idESTACAO_METEO`) VALUES
(2, 'hasudhaushdhausd', 1, 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `radiotipo`
--

CREATE TABLE IF NOT EXISTS `radiotipo` (
`idradioTipo` int(11) NOT NULL,
  `nome` varchar(45) DEFAULT NULL,
  `descricao` varchar(300) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `radiotipo`
--

INSERT INTO `radiotipo` (`idradioTipo`, `nome`, `descricao`) VALUES
(1, 'uaifai', 'legal');

-- --------------------------------------------------------

--
-- Estrutura da tabela `snapshot`
--

CREATE TABLE IF NOT EXISTS `snapshot` (
`idSNAP` int(11) NOT NULL,
  `VALOR` float DEFAULT NULL,
  `SNAPSHOT` timestamp NULL DEFAULT NULL,
  `NOME_TAG` varchar(45) DEFAULT NULL,
  `tag_idTAG` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tag`
--

CREATE TABLE IF NOT EXISTS `tag` (
`idTAG` int(11) NOT NULL,
  `DESVIO` float DEFAULT NULL,
  `TEMPO_MAX` int(11) DEFAULT NULL,
  `CONV_RATE` int(11) DEFAULT NULL,
  `tagInfo_idtagInfo1` int(11) NOT NULL,
  `datasource_idESTACAO_METEO` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `tag`
--

INSERT INTO `tag` (`idTAG`, `DESVIO`, `TEMPO_MAX`, `CONV_RATE`, `tagInfo_idtagInfo1`, `datasource_idESTACAO_METEO`) VALUES
(1, 4.5, 30, 234, 1, 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `taginfo`
--

CREATE TABLE IF NOT EXISTS `taginfo` (
`idtagInfo` int(11) NOT NULL,
  `NOME` varchar(45) DEFAULT NULL,
  `DESCRICAO` varchar(255) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `taginfo`
--

INSERT INTO `taginfo` (`idtagInfo`, `NOME`, `DESCRICAO`) VALUES
(1, 'LM-35', 'Sensor de luminosidade');

-- --------------------------------------------------------

--
-- Estrutura da tabela `valores`
--

CREATE TABLE IF NOT EXISTS `valores` (
`idValores` int(11) NOT NULL,
  `VALOR` float DEFAULT NULL,
  `DATAHORA` timestamp NULL DEFAULT NULL,
  `tag_idTAG` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `datasource`
--
ALTER TABLE `datasource`
 ADD PRIMARY KEY (`idESTACAO_METEO`,`node_idNODE`), ADD KEY `fk_datasource_node_idx` (`node_idNODE`);

--
-- Indexes for table `node`
--
ALTER TABLE `node`
 ADD PRIMARY KEY (`idNODE`);

--
-- Indexes for table `radio`
--
ALTER TABLE `radio`
 ADD PRIMARY KEY (`idradio`), ADD KEY `fk_radio_radioTipo1_idx` (`radioTipo_idradioTipo`), ADD KEY `fk_radio_datasource1_idx` (`datasource_idESTACAO_METEO`);

--
-- Indexes for table `radiotipo`
--
ALTER TABLE `radiotipo`
 ADD PRIMARY KEY (`idradioTipo`);

--
-- Indexes for table `snapshot`
--
ALTER TABLE `snapshot`
 ADD PRIMARY KEY (`idSNAP`), ADD KEY `fk_snapshot_tag1_idx` (`tag_idTAG`);

--
-- Indexes for table `tag`
--
ALTER TABLE `tag`
 ADD PRIMARY KEY (`idTAG`), ADD KEY `fk_tag_tagInfo2_idx` (`tagInfo_idtagInfo1`), ADD KEY `fk_tag_datasource1_idx` (`datasource_idESTACAO_METEO`);

--
-- Indexes for table `taginfo`
--
ALTER TABLE `taginfo`
 ADD PRIMARY KEY (`idtagInfo`);

--
-- Indexes for table `valores`
--
ALTER TABLE `valores`
 ADD PRIMARY KEY (`idValores`), ADD KEY `fk_valores_tag1_idx` (`tag_idTAG`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `datasource`
--
ALTER TABLE `datasource`
MODIFY `idESTACAO_METEO` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `node`
--
ALTER TABLE `node`
MODIFY `idNODE` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `radio`
--
ALTER TABLE `radio`
MODIFY `idradio` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `radiotipo`
--
ALTER TABLE `radiotipo`
MODIFY `idradioTipo` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `snapshot`
--
ALTER TABLE `snapshot`
MODIFY `idSNAP` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `tag`
--
ALTER TABLE `tag`
MODIFY `idTAG` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `taginfo`
--
ALTER TABLE `taginfo`
MODIFY `idtagInfo` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `valores`
--
ALTER TABLE `valores`
MODIFY `idValores` int(11) NOT NULL AUTO_INCREMENT;
--
-- Constraints for dumped tables
--

--
-- Limitadores para a tabela `datasource`
--
ALTER TABLE `datasource`
ADD CONSTRAINT `fk_datasource_node` FOREIGN KEY (`node_idNODE`) REFERENCES `node` (`idNODE`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limitadores para a tabela `radio`
--
ALTER TABLE `radio`
ADD CONSTRAINT `fk_radio_datasource1` FOREIGN KEY (`datasource_idESTACAO_METEO`) REFERENCES `datasource` (`idESTACAO_METEO`) ON DELETE NO ACTION ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_radio_radioTipo1` FOREIGN KEY (`radioTipo_idradioTipo`) REFERENCES `radiotipo` (`idradioTipo`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limitadores para a tabela `snapshot`
--
ALTER TABLE `snapshot`
ADD CONSTRAINT `fk_snapshot_tag1` FOREIGN KEY (`tag_idTAG`) REFERENCES `tag` (`idTAG`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limitadores para a tabela `tag`
--
ALTER TABLE `tag`
ADD CONSTRAINT `fk_tag_datasource1` FOREIGN KEY (`datasource_idESTACAO_METEO`) REFERENCES `datasource` (`idESTACAO_METEO`) ON DELETE NO ACTION ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_tag_tagInfo2` FOREIGN KEY (`tagInfo_idtagInfo1`) REFERENCES `taginfo` (`idtagInfo`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limitadores para a tabela `valores`
--
ALTER TABLE `valores`
ADD CONSTRAINT `fk_valores_tag1` FOREIGN KEY (`tag_idTAG`) REFERENCES `tag` (`idTAG`) ON DELETE NO ACTION ON UPDATE NO ACTION;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
