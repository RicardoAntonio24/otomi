-- phpMyAdmin SQL Dump
-- version 4.8.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 15-05-2019 a las 06:03:52
-- Versión del servidor: 10.1.33-MariaDB
-- Versión de PHP: 7.2.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `webservice_aj`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cabeza`
--

CREATE TABLE `cabeza` (
  `id_palabra_cabeza` int(15) NOT NULL,
  `palabra` varchar(15) NOT NULL,
  `traduccion` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `cabeza`
--

INSERT INTO `cabeza` (`id_palabra_cabeza`, `palabra`, `traduccion`) VALUES
(1, 'nbhjkh', 'vdvcxxvc'),
(2, 'cxvcvc', 'vcxcvx');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `id_cliente` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `apellido_pa` varchar(30) NOT NULL,
  `apellido_ma` varchar(30) NOT NULL,
  `telefono` varchar(30) NOT NULL,
  `email` varchar(50) NOT NULL,
  `utl` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`id_cliente`, `nombre`, `apellido_pa`, `apellido_ma`, `telefono`, `email`, `utl`) VALUES
(9, 'ricordo ', 'antonio', 'martinez', '7751484038', 'ricardo@gmail.com', 'https://www.google.com/maps/d/u/0/viewer?mid=1qaqne8IDKY9Ofjab_AjRTcY-J_v8PskE&ll=20.078204539910285%2C-98.40556204772952&z=15'),
(10, 'merio', 'castañeda', 'jasir', '7751449660', 'mario@gmail.com', 'https://www.google.com/maps/d/u/0/viewer?usp=sharing_eip&mid=1qaqne8IDKY9Ofjab_AjRTcY-J_v8PskE'),
(11, 'brenda', 'diaz', 'martinez', '77754645', 'brenda@gmail.com', 'brendabrenda'),
(12, 'jose', 'matias', 'morelos', '7775465465', 'gaby@gmail.com', 'manuelmanuel'),
(14, 'mario', 'lopez', 'obrador', '7751449660', '1717110251', 'mariomario');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos`
--

CREATE TABLE `datos` (
  `nombre` varchar(50) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `mensaje` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `logs`
--

CREATE TABLE `logs` (
  `id_log` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `ip` varchar(16) NOT NULL,
  `access` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `logs`
--

INSERT INTO `logs` (`id_log`, `username`, `ip`, `access`) VALUES
(1, 'admin', '127.0.0.1', '2019-03-19 21:35:05'),
(2, 'admin', '127.0.0.1', '2019-03-19 21:36:41'),
(3, 'axbrenj', '127.0.0.1', '2019-03-19 21:37:45'),
(4, 'admin', '127.0.0.1', '2019-03-19 21:38:01'),
(5, 'axbrenj', '127.0.0.1', '2019-03-19 21:39:32'),
(6, 'axbrenj', '127.0.0.1', '2019-03-19 22:04:47'),
(7, 'axbrenj', '127.0.0.1', '2019-03-19 22:09:56'),
(8, 'axbrenj', '127.0.0.1', '2019-03-19 22:17:28'),
(9, 'axbrenj', '127.0.0.1', '2019-03-19 22:23:27'),
(10, 'axbrenj', '127.0.0.1', '2019-03-20 13:13:50'),
(11, 'axbrenj', '127.0.0.1', '2019-03-21 13:26:43'),
(12, 'axbrenj', '127.0.0.1', '2019-03-21 13:48:56'),
(13, 'axbrenj', '127.0.0.1', '2019-03-21 14:11:33'),
(14, 'axbrenj', '127.0.0.1', '2019-03-21 14:26:26'),
(15, 'axbrenj', '127.0.0.1', '2019-03-21 14:32:56'),
(16, 'axbrenj', '127.0.0.1', '2019-04-03 20:08:31'),
(17, 'axbrenj', '127.0.0.1', '2019-04-03 20:26:49'),
(18, 'axbrenj', '127.0.0.1', '2019-04-04 13:23:48'),
(19, 'axbrenj', '127.0.0.1', '2019-04-04 16:32:26'),
(20, 'axbrenj', '127.0.0.1', '2019-04-04 16:37:50'),
(21, 'axbrenj', '127.0.0.1', '2019-04-06 17:58:32'),
(22, 'axbrenj', '127.0.0.1', '2019-04-10 17:35:30'),
(23, 'axbrenj', '127.0.0.1', '2019-04-10 17:59:53'),
(24, 'axbrenj', '127.0.0.1', '2019-04-10 18:02:04'),
(25, 'axbrenj', '127.0.0.1', '2019-04-11 12:44:29'),
(26, 'axbrenj', '127.0.0.1', '2019-04-11 12:56:36'),
(27, 'axbrenj', '127.0.0.1', '2019-04-11 12:58:13'),
(28, 'axbrenj', '127.0.0.1', '2019-04-11 13:31:08'),
(29, 'axbrenj', '127.0.0.1', '2019-04-11 13:38:03'),
(30, 'axbrenj', '127.0.0.1', '2019-04-11 14:55:27'),
(31, 'axbrenj', '127.0.0.1', '2019-04-11 17:39:15'),
(32, 'axbrenj', '127.0.0.1', '2019-04-11 19:43:33'),
(33, 'axbrenj', '127.0.0.1', '2019-04-14 20:25:21'),
(34, 'axbrenj', '192.168.1.114', '2019-04-14 21:50:17'),
(35, 'axbrenj', '127.0.0.1', '2019-04-14 22:20:49'),
(36, 'axbrenj', '127.0.0.1', '2019-04-14 23:29:16'),
(37, 'axbrenj', '127.0.0.1', '2019-04-14 23:30:46'),
(38, 'axbrenj', '127.0.0.1', '2019-04-15 14:19:47'),
(39, 'axbrenj', '127.0.0.1', '2019-04-15 15:22:19'),
(40, 'axbrenj', '127.0.0.1', '2019-04-15 15:36:10'),
(41, 'axbrenj', '127.0.0.1', '2019-04-15 20:53:25'),
(42, 'axbrenj', '127.0.0.1', '2019-04-16 13:40:53'),
(43, 'axbrenj', '127.0.0.1', '2019-04-16 13:47:03'),
(44, 'axbrenj', '127.0.0.1', '2019-04-16 14:02:45'),
(45, 'axbrenj', '127.0.0.1', '2019-04-16 14:08:01'),
(46, 'axbrenj', '127.0.0.1', '2019-04-16 14:11:04'),
(47, 'axbrenj', '127.0.0.1', '2019-04-16 14:12:48'),
(48, 'xXBARTOLOCOXx', '127.0.0.1', '2019-04-16 14:15:24'),
(49, 'xXBARTOLOCOXx', '127.0.0.1', '2019-04-16 14:20:21'),
(50, 'axbrenj', '127.0.0.1', '2019-04-16 14:26:31'),
(51, 'axbrenj', '127.0.0.1', '2019-04-16 14:33:07'),
(52, 'axbrenj', '127.0.0.1', '2019-04-16 15:55:28'),
(53, 'xXBARTOLOCOXx', '127.0.0.1', '2019-04-16 16:25:18'),
(54, 'axbrenj', '127.0.0.1', '2019-04-16 16:25:32'),
(55, 'axbrenj', '127.0.0.1', '2019-04-16 16:54:14'),
(56, 'axbrenj', '127.0.0.1', '2019-04-16 16:56:46'),
(57, 'axbrenj', '127.0.0.1', '2019-04-16 17:59:01'),
(58, 'xXBARTOLOCOXx', '127.0.0.1', '2019-04-16 23:15:02'),
(59, 'xXBARTOLOCOXx', '127.0.0.1', '2019-04-16 23:17:43'),
(60, 'xXBARTOLOCOXx', '127.0.0.1', '2019-04-16 23:18:04'),
(61, 'xXBARTOLOCOXx', '127.0.0.1', '2019-04-17 01:08:59'),
(62, 'xXBARTOLOCOXx', '127.0.0.1', '2019-04-17 01:12:23'),
(63, 'axbrenj', '127.0.0.1', '2019-04-17 01:21:25'),
(64, 'axbrenj', '127.0.0.1', '2019-04-17 01:26:12'),
(65, 'xXBARTOLOCOXx', '127.0.0.1', '2019-04-29 11:47:32'),
(66, 'xXBARTOLOCOXx', '127.0.0.1', '2019-04-29 13:54:32'),
(67, 'axbrenj', '127.0.0.1', '2019-04-29 16:33:37'),
(68, 'axbrenj', '127.0.0.1', '2019-04-29 16:35:16'),
(69, 'axbrenj', '127.0.0.1', '2019-04-29 17:00:16'),
(70, 'axbrenj', '127.0.0.1', '2019-04-29 17:04:01'),
(71, 'axbrenj', '127.0.0.1', '2019-04-30 12:38:42'),
(72, 'axbrenj', '127.0.0.1', '2019-04-30 13:14:44'),
(73, 'axbrenj', '127.0.0.1', '2019-04-30 13:55:02'),
(74, 'axbrenj', '127.0.0.1', '2019-04-30 19:47:00'),
(75, 'axbrenj', '127.0.0.1', '2019-04-30 19:48:27'),
(76, 'axbrenj', '127.0.0.1', '2019-04-30 20:34:57'),
(77, 'axbrenj', '127.0.0.1', '2019-04-30 20:34:57'),
(78, 'axbrenj', '127.0.0.1', '2019-04-30 20:47:25'),
(79, 'xXBARTOLOCOXx', '127.0.0.1', '2019-04-30 21:33:46'),
(80, 'xXBARTOLOCOXx', '127.0.0.1', '2019-04-30 21:39:58'),
(81, 'xXBARTOLOCOXx', '127.0.0.1', '2019-04-30 21:45:02'),
(82, 'axbrenj', '127.0.0.1', '2019-05-06 20:14:06'),
(83, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-06 20:14:51'),
(84, 'admin', '127.0.0.1', '2019-05-06 20:15:21'),
(85, 'axbrenj', '127.0.0.1', '2019-05-06 20:15:50'),
(86, 'axbrenj', '127.0.0.1', '2019-05-06 20:20:05'),
(87, 'admin', '127.0.0.1', '2019-05-07 15:28:13'),
(88, 'axbrenj', '127.0.0.1', '2019-05-07 15:29:11'),
(89, 'axbrenj', '127.0.0.1', '2019-05-07 16:47:10'),
(90, 'axbrenj', '127.0.0.1', '2019-05-07 16:51:43'),
(91, 'axbrenj', '127.0.0.1', '2019-05-07 16:54:05'),
(92, 'axbrenj', '127.0.0.1', '2019-05-07 16:57:02'),
(93, 'axbrenj', '127.0.0.1', '2019-05-07 17:43:39'),
(94, 'guess', '127.0.0.1', '2019-05-07 17:49:31'),
(95, 'axbrenj', '127.0.0.1', '2019-05-07 17:55:41'),
(96, 'guess', '127.0.0.1', '2019-05-07 17:56:32'),
(97, 'axbrenj', '127.0.0.1', '2019-05-07 17:57:05'),
(98, 'guess', '127.0.0.1', '2019-05-07 18:03:23'),
(99, 'axbrenj', '127.0.0.1', '2019-05-07 18:05:14'),
(100, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-09 17:33:41'),
(101, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-09 17:56:25'),
(102, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-09 18:13:38'),
(103, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-09 18:39:13'),
(104, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-09 18:50:32'),
(105, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-09 19:02:39'),
(106, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-09 22:40:37'),
(107, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-09 22:46:52'),
(108, 'axbrenj', '127.0.0.1', '2019-05-09 23:15:47'),
(109, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-09 23:48:23'),
(110, 'xXBARTOLOCOXx', '192.168.1.114', '2019-05-10 02:10:41'),
(111, 'axbrenj', '192.168.1.114', '2019-05-10 02:12:02'),
(112, 'xXBARTOLOCOXx', '192.168.1.114', '2019-05-10 02:12:42'),
(113, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-13 16:58:03'),
(114, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-13 18:15:59'),
(115, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-13 18:32:44'),
(116, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-13 20:32:09'),
(117, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-14 16:42:30'),
(118, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-14 17:23:32'),
(119, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-14 17:28:36'),
(120, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-14 17:28:36'),
(121, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-14 17:30:01'),
(122, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-14 17:31:09'),
(123, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-14 17:33:15'),
(124, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-14 17:34:44'),
(125, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-14 17:47:21'),
(126, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-14 17:48:37'),
(127, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-14 17:49:50'),
(128, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-14 17:53:01'),
(129, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-14 18:09:20'),
(130, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-14 18:37:20'),
(131, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-14 19:42:16'),
(132, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-14 19:43:39'),
(133, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-14 20:00:07'),
(134, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-14 20:23:50'),
(135, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-14 20:23:50'),
(136, 'xXBARTOLOCOXx', '127.0.0.1', '2019-05-15 03:56:35');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `partes_de_cuerpo`
--

CREATE TABLE `partes_de_cuerpo` (
  `id_palabra` int(5) NOT NULL,
  `palabra` varchar(50) NOT NULL,
  `palabra_otomi` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `partes_de_cuerpo`
--

INSERT INTO `partes_de_cuerpo` (`id_palabra`, `palabra`, `palabra_otomi`) VALUES
(1, 'cabeza', 'ña'),
(2, 'pecho', 'jaya'),
(3, 'manos', 'ye'),
(4, 'pies', 'yowa');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pies`
--

CREATE TABLE `pies` (
  `id_palabra` int(5) NOT NULL,
  `palabra_uno` varchar(50) NOT NULL,
  `palabra_dos` varchar(50) NOT NULL,
  `palabra_tres` varchar(50) NOT NULL,
  `palabra_cuatro` varchar(50) NOT NULL,
  `palabra_oto_uno` varchar(50) NOT NULL,
  `palabra_oto_dos` varchar(50) NOT NULL,
  `palabra_oto_tres` varchar(50) NOT NULL,
  `palabra_oto_cuatro` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sessions`
--

CREATE TABLE `sessions` (
  `session_id` char(128) NOT NULL,
  `atime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `data` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `sessions`
--

INSERT INTO `sessions` (`session_id`, `atime`, `data`) VALUES
('3e05e5a62048000bfa886e9805ccc336be2a00bf', '2019-05-14 20:45:28', 'KGRwMQpTJ2NvdW50JwpwMgpJMApzUydsb2dnZWRpbicKcDMKSTAwCnNTJ2lwJwpwNApWMTI3LjAu\nMC4xCnA1CnNTJ3Nlc3Npb25faWQnCnA2ClMnM2UwNWU1YTYyMDQ4MDAwYmZhODg2ZTk4MDVjY2Mz\nMzZiZTJhMDBiZicKcDcKc1MndXNlcicKcDgKUydhbm9ueW1vdXMnCnA5CnNTJ3ByaXZpbGVnZScK\ncDEwCkktMQpzUydsb2dpbicKcDExCkkwCnMu\n'),
('7d05690f388fe6712f4577a9fe8fbf9e6ecf2fe0', '2019-05-15 03:56:36', 'KGRwMQpTJ2NvdW50JwpwMgpJMApzUyd1c2VybmFtZScKcDMKVnhYQkFSVE9MT0NPWHgKcDQKc1Mn\nbG9nZ2VkaW4nCnA1CkkwMQpzUydpcCcKcDYKVjEyNy4wLjAuMQpwNwpzUydzZXNzaW9uX2lkJwpw\nOApTJzdkMDU2OTBmMzg4ZmU2NzEyZjQ1NzdhOWZlOGZiZjllNmVjZjJmZTAnCnA5CnNTJ3VzZXIn\nCnAxMApTJ2Fub255bW91cycKcDExCnNTJ3ByaXZpbGVnZScKcDEyCkwwTApzUydsb2dpbicKcDEz\nCkkwCnMu\n'),
('9f51f4753b75cbc896c6923e61909c0980f83b0f', '2019-05-14 18:28:00', 'KGRwMQpTJ2NvdW50JwpwMgpJMApzUydsb2dnZWRpbicKcDMKSTAwCnNTJ2lwJwpwNApWMTkyLjE2\nOC4xLjc2CnA1CnNTJ3Nlc3Npb25faWQnCnA2ClMnOWY1MWY0NzUzYjc1Y2JjODk2YzY5MjNlNjE5\nMDljMDk4MGY4M2IwZicKcDcKc1MndXNlcicKcDgKUydhbm9ueW1vdXMnCnA5CnNTJ3ByaXZpbGVn\nZScKcDEwCkktMQpzUydsb2dpbicKcDExCkkwCnMu\n'),
('dd3a693b2db3ff3d043fb0a31b88da7a330d4715', '2019-05-14 17:04:17', 'KGRwMQpTJ2NvdW50JwpwMgpJMApzUydsb2dnZWRpbicKcDMKSTAwCnNTJ2lwJwpwNApWMTkyLjE2\nOC4xLjc2CnA1CnNTJ3Nlc3Npb25faWQnCnA2ClMnZGQzYTY5M2IyZGIzZmYzZDA0M2ZiMGEzMWI4\nOGRhN2EzMzBkNDcxNScKcDcKc1MndXNlcicKcDgKUydhbm9ueW1vdXMnCnA5CnNTJ3ByaXZpbGVn\nZScKcDEwCkktMQpzUydsb2dpbicKcDExCkkwCnMu\n'),
('e468ac8eccc112bf05ac81136ced1c19583fec43', '2019-05-14 17:43:53', 'KGRwMQpTJ2NvdW50JwpwMgpJMApzUydsb2dnZWRpbicKcDMKSTAwCnNTJ2lwJwpwNApWMTkyLjE2\nOC4xLjc2CnA1CnNTJ3Nlc3Npb25faWQnCnA2ClMnZTQ2OGFjOGVjY2MxMTJiZjA1YWM4MTEzNmNl\nZDFjMTk1ODNmZWM0MycKcDcKc1MndXNlcicKcDgKUydhbm9ueW1vdXMnCnA5CnNTJ3ByaXZpbGVn\nZScKcDEwCkktMQpzUydsb2dpbicKcDExCkkwCnMu\n');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `username` varchar(20) NOT NULL,
  `password` varchar(32) NOT NULL,
  `privilege` int(11) NOT NULL DEFAULT '-1',
  `status` int(11) NOT NULL DEFAULT '1',
  `name` varchar(150) NOT NULL,
  `email` varchar(100) NOT NULL,
  `other_data` varchar(50) NOT NULL,
  `user_hash` varchar(32) NOT NULL,
  `change_pwd` int(11) NOT NULL DEFAULT '1',
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`username`, `password`, `privilege`, `status`, `name`, `email`, `other_data`, `user_hash`, `change_pwd`, `created`) VALUES
('admin', '80793b8cc71ae0b004a06aa405c205ac', 0, 1, 'Admin', 'admin@gmail.com', 'TIC:SI', 'dc243fdf1a24cbced74db81708b30788', 0, '2019-03-19 21:28:36'),
('axbrenj', '2324ac45a214915d2446b58d6134e7b5', 0, 1, 'Ricardo Antonio Diaz Martinez', 'alguien@gmail.com', 'nada', '62488a686164e425e5beb305acb738c0', 0, '2019-05-13 17:50:04'),
('guess', 'dbd485102f445e1929d174726d10470b', 1, 1, 'Guess', 'guess@gmail.com', 'TIC:SI', 'eba1c13c68d351dbc1d3f3d76a18d16d', 0, '2019-03-19 21:28:36'),
('xXBARTOLOCOXx', '2324ac45a214915d2446b58d6134e7b5', 0, 1, 'juanito', '1717110251@utectulancingo.edu.mx', 'nada', '4f9a0e5a9c57b9d350b1b8afa6e7f0f6', 0, '2019-05-06 20:14:28');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cabeza`
--
ALTER TABLE `cabeza`
  ADD PRIMARY KEY (`id_palabra_cabeza`);

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id_cliente`);

--
-- Indices de la tabla `logs`
--
ALTER TABLE `logs`
  ADD PRIMARY KEY (`id_log`),
  ADD KEY `username` (`username`);

--
-- Indices de la tabla `partes_de_cuerpo`
--
ALTER TABLE `partes_de_cuerpo`
  ADD PRIMARY KEY (`id_palabra`);

--
-- Indices de la tabla `sessions`
--
ALTER TABLE `sessions`
  ADD UNIQUE KEY `session_id` (`session_id`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`username`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cabeza`
--
ALTER TABLE `cabeza`
  MODIFY `id_palabra_cabeza` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id_cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `logs`
--
ALTER TABLE `logs`
  MODIFY `id_log` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=137;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `logs`
--
ALTER TABLE `logs`
  ADD CONSTRAINT `logs_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
