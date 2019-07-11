-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jul 11, 2019 at 06:02 PM
-- Server version: 10.3.16-MariaDB
-- PHP Version: 7.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hospt`
--

-- --------------------------------------------------------

--
-- Table structure for table `Appointments`
--

CREATE TABLE `Appointments` (
  `Hekim_Adı` text NOT NULL,
  `Tarih` date NOT NULL,
  `Saat` enum('09:10','09:20','09:30','09:40','09:50','10:00','10:10','10:20','10:30','10:40','10:50','11:00','11:10','11:20','11:30','11:40','11:50','12:00','12:10','12:20','13:40','13:50','14:00','14:10','14:20','14:30','14:40','14:50','15:00','15:10','15:20','15:30','15:40','15:50') DEFAULT NULL,
  `Department` text NOT NULL,
  `TC` bigint(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Date_Time`
--

CREATE TABLE `Date_Time` (
  `Date_Time` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Date_Time`
--

INSERT INTO `Date_Time` (`Date_Time`) VALUES
('09:10'),
('09:20'),
('09:30'),
('09:40'),
('09:50'),
('10:00'),
('10:10'),
('10:20'),
('10:30'),
('10:40'),
('10:50'),
('11:00'),
('11:10'),
('11:20'),
('11:30'),
('11:40'),
('11:50'),
('12:00'),
('12:10'),
('12:20'),
('13:40'),
('13:50'),
('14:00'),
('14:10'),
('14:20'),
('14:30'),
('14:40'),
('14:50'),
('15:00'),
('15:10'),
('15:20'),
('15:30'),
('15:40'),
('15:50');

-- --------------------------------------------------------

--
-- Table structure for table `Departments`
--

CREATE TABLE `Departments` (
  `Departments` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Departments`
--

INSERT INTO `Departments` (`Departments`) VALUES
('BESLENME VE DİYET'),
('BEYİN VE SİNİR CERRAHİSİ'),
('ÇOCUK ALERJİSİ'),
('ÇOCUK CERRAHİSİ'),
('ÇOCUK ENDOKRİNOLOJİSİ'),
('ÇOCUK ENFEKSİYON'),
('ÇOCUK GÖĞÜS HASTALIKLARI'),
('ÇOCUK HEMATOLOJİSİ'),
('ÇOCUK KARDİYOLOJİSİ'),
('ÇOCUK METABOLİZMA'),
('ÇOCUK NEFROLOJİSİ'),
('ÇOCUK NÖROLOJİSİ'),
('ÇOCUK PSİKİYATRİSİ'),
('ÇOCUK SAĞLIĞI VE HASTALIKLARI'),
('ÇOCUK ÜROLOJİSİ'),
('DERMATOLOJİ (CİLDİYE)'),
('ENDOKRİNOLOJİ VE METABOLİZMA'),
('ENFEKSİYON HASTALIKLARI'),
('FİZİKSEL TIP VE REHABİLİTASYON'),
('GASTROENTEROLOJİ'),
('GELENEKSEL VE TAMAMLAYICI TIP(GETAMER)'),
('GENEL CERRAHİ'),
('GERİATRİ'),
('GÖĞÜS CERRAHİSİ'),
('GÖĞÜS HASTALIKLARI'),
('GÖZ HASTALIKLARI'),
('HEMATOLOJİ'),
('İÇ HASTALIKLARI'),
('KADIN HASTALIKLARI VE DOĞUM'),
('KALP VE DAMAR CERRAHİSİ'),
('KARDİYOLOJİ'),
('KEMİK YOĞUNLUĞU ÖLÇÜMÜ'),
('KULAK-BURUN-BOĞAZ HASTALIKLARI'),
('NEFROLOJİ'),
('NÖROLOJİ'),
('ORTOPEDİ VE TRAVMATOLOJİ'),
('PLASTİK REKONSTRÜKTİF VE ESTETİK CERRAHİ'),
('PSİKİYATRİ'),
('RADYASYON ONKOLOJİSİ'),
('TIBBİ GENETİK'),
('TIBBİ PATOLOJİ'),
('ÜROLOJİ');

-- --------------------------------------------------------

--
-- Table structure for table `Docs`
--

CREATE TABLE `Docs` (
  `Name` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Docs`
--

INSERT INTO `Docs` (`Name`) VALUES
('Fatma Özlem Acar'),
('Özde Acarkan'),
('Atahan Adanır'),
('Hacı Mehmet'),
('Mükerrem Zeynep'),
('Bestami Ağırağaç'),
('Aykanat Ağıroğlu'),
('Şennur Ağnar'),
('Tutkum Ahmadı'),
('Mügenur Ahmet'),
('Sevinç Ak'),
('Kayıhan Nedim'),
('Lemi Akarçay'),
('Cihan Akarpınar'),
('Rafi Akaş'),
('Mehmetcan Akay'),
('Nuhaydar Akbilmez'),
('Emine Münevver'),
('Servet Akçagunay'),
('Çilem Akçay'),
('Recep Ali Samet'),
('Emre Ayberk'),
('Kerime Hacer'),
('Ercüment Akıncılar'),
('Sarper Akış'),
('Berker Akkiray'),
('İclal Akkoyun'),
('Lemis Akküt'),
('Ahmet Polat'),
('Ata Kerem'),
('Ahmet Raşit'),
('Ecem Hatice'),
('Nüket Aksan'),
('Senem Aksevim'),
('Ayşen Aksoy'),
('Pekcan Aksöz'),
('Bedirhan Lütfü'),
('Semina Aktuna'),
('Eda Sena Akyıldız'),
('Müyesser Kınar'),
('Selinti Al'),
('Bahar Özlem'),
('İlma Aldağ'),
('Kutlu Alibeyoğlu'),
('Nesibe Nurefşan'),
('Ömer Buğra'),
('Hiba Alpuğan'),
('Mazlum Altan'),
('Elif Tuğçe'),
('Ahmet Ruken'),
('Yaşar Utku'),
('Rana Altınoklu'),
('Fethullah Altınöz'),
('Burak Tatkan'),
('Merve Ece Altıok'),
('Rima Altıparmak'),
('Elif Dilay'),
('Sırma Begüm'),
('Nefse Altunbulak'),
('Büşra Gül'),
('Erna Aluç'),
('Hikmet Nazlı'),
('İsmail Umut'),
('İlkay Ramazan'),
('Nebahat Ansen'),
('İlyas Umut'),
('Halim Aral'),
('Yasin Şükrü'),
('Cansev Arat'),
('Memet Ali'),
('Deniz Dilay'),
('İzlem Arınç'),
('Öget Arif'),
('Şeyda Nur'),
('Zeki Yiğithan'),
('Nunazlı Arpacı'),
('Ferdacan Aruca'),
('Şerife Asil'),
('Mustafa Burhan'),
('Ali Tayyip'),
('Mustafa Burkan');

-- --------------------------------------------------------

--
-- Table structure for table `patients`
--

CREATE TABLE `patients` (
  `TC` bigint(11) NOT NULL,
  `AD` text CHARACTER SET utf8mb4 COLLATE utf8mb4_turkish_ci NOT NULL,
  `SOYAD` text CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `ANA_ADI` text CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `CINSIYET` tinytext CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `DATE` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `patients`
--
ALTER TABLE `patients`
  ADD UNIQUE KEY `TC` (`TC`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
