/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.33 : Database - eanganavadissss
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`eanganavadissss` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `eanganavadissss`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values 
(1,'pbkdf2_sha256$260000$pIGJ9lkVbzTUMRuqXnocDA$EnMEdnQJejrQV94z3S/c2NmWF+pUm4H8Sq+jn8jZlk8=','2023-11-19 10:09:40.665126',1,'admin','','','admin@gmail.com',1,1,'2023-11-08 10:39:22.171431');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('1kvd9k3na7fawgdfvqv40a8o4b2y01s6','.eJxVjDEOgzAMRe-SuYpwQtO4Y3fOgOzYKbSISASmqndvkVhY33v_f8w0irm7i-lpW4d-q7r0OzFgTowpvXXehbxofhabyrwuI9s9sYettiui0-NoTwcD1eG_VoexJfIBIQZBjgAuYMKsN4wqlCO7hq4eAjMjpRYyKTmQSOwlN-b7A1Q8Oqo:1r4DZE:tOel6STk4t678qsf27XCBXVLUXw31IWdiTan-zssbZE','2023-12-02 05:08:28.725422'),
('98cudtht6ww6nweoa8kj25l7gsjohfz7','.eJxVjDEOgzAMRe-SuYpwQtO4Y3fOgOzYKbSISASmqndvkVhY33v_f8w0irm7i-lpW4d-q7r0OzFgTowpvXXehbxofhabyrwuI9s9sYettiui0-NoTwcD1eG_VoexJfIBIQZBjgAuYMKsN4wqlCO7hq4eAjMjpRYyKTmQSOwlN-b7A1Q8Oqo:1r1gGY:IR6ZjT2B1xYz6Gz5MkE4mBdovwKRdmEtbvU0API8mZg','2023-11-25 05:10:42.799708'),
('apmd4agr8xpu5puag0d3mdo9poe7lsdg','.eJxVjEsOwjAMBe-SNYrqpISYJfueIbJjhxSqVupnhbg7VOqm25l572OGXszdX0yiba1pW3ROOzFgTowpv3XchbxofE42T-M692z3xB52sd0kOjyO9nRQaan_tTqMLZEPCDEIcgRwATMWvWFUoRLZNXT1EJgZKbdQSMmBRGIvpTHfH1ToOqs:1r0gAX:aYbx6BcC64-Bo2XPDoFdDxWpuaWnUFw_aZ-hCoYVPnM','2023-11-22 10:52:21.112584'),
('miw5oasabxoq6otqrdcro783rulj2fzm','.eJxVjDEOgzAMRe-SuYpwQtO4Y3fOgOzYKbSISASmqndvkVhY33v_f8w0irm7i-lpW4d-q7r0OzFgTowpvXXehbxofhabyrwuI9s9sYettiui0-NoTwcD1eG_VoexJfIBIQZBjgAuYMKsN4wqlCO7hq4eAjMjpRYyKTmQSOwlN-b7A1Q8Oqo:1r0gBu:qnEyAqKYF3Bj3qvxr60cL53NVafef1-CGTZ83RzI2ac','2023-11-22 10:53:46.042901');

/*Table structure for table `eanaganavadiapp_anganwadi_table` */

DROP TABLE IF EXISTS `eanaganavadiapp_anganwadi_table`;

CREATE TABLE `eanaganavadiapp_anganwadi_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `anganwadiname` varchar(90) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `place` varchar(90) NOT NULL,
  `post` varchar(90) NOT NULL,
  `pin` bigint NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(90) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `eanaganavadiapp_anganwadi_table` */

insert  into `eanaganavadiapp_anganwadi_table`(`id`,`anganwadiname`,`photo`,`place`,`post`,`pin`,`phone`,`email`) values 
(1,'ushas','hero-bg_Cf0BaTY.jpg','kozhikode','kozhikode',678678,9876543210,'ushas@gmail.com'),
(2,'pre yyyy','preschool_26TGj9X.jpeg','Edappal','Edappal',679576,8888999955,'preschool76@gmail.com'),
(5,'Aswathi','Default_HgTpygZ.jpg','sadfdf','hgfd',670645,9876543210,'aWrf@gmail.com');

/*Table structure for table `eanaganavadiapp_assign_table` */

DROP TABLE IF EXISTS `eanaganavadiapp_assign_table`;

CREATE TABLE `eanaganavadiapp_assign_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `ANGANWADI_id` bigint NOT NULL,
  `STAFF_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Eanaganavadiapp_assi_ANGANWADI_id_5928c258_fk_Eanaganav` (`ANGANWADI_id`),
  KEY `Eanaganavadiapp_assi_STAFF_id_1c23b468_fk_Eanaganav` (`STAFF_id`),
  CONSTRAINT `Eanaganavadiapp_assi_ANGANWADI_id_5928c258_fk_Eanaganav` FOREIGN KEY (`ANGANWADI_id`) REFERENCES `eanaganavadiapp_anganwadi_table` (`id`),
  CONSTRAINT `Eanaganavadiapp_assi_STAFF_id_1c23b468_fk_Eanaganav` FOREIGN KEY (`STAFF_id`) REFERENCES `eanaganavadiapp_staff_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `eanaganavadiapp_assign_table` */

insert  into `eanaganavadiapp_assign_table`(`id`,`date`,`ANGANWADI_id`,`STAFF_id`) values 
(1,'2023-11-08',1,1),
(2,'2023-11-11',2,2);

/*Table structure for table `eanaganavadiapp_chat_table` */

DROP TABLE IF EXISTS `eanaganavadiapp_chat_table`;

CREATE TABLE `eanaganavadiapp_chat_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `fromid_id` bigint NOT NULL,
  `toid_id` bigint NOT NULL,
  `message` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Eanaganavadiapp_chat_fromid_id_a640c58e_fk_Eanaganav` (`fromid_id`),
  KEY `Eanaganavadiapp_chat_toid_id_6a0975cb_fk_Eanaganav` (`toid_id`),
  CONSTRAINT `Eanaganavadiapp_chat_fromid_id_a640c58e_fk_Eanaganav` FOREIGN KEY (`fromid_id`) REFERENCES `eanaganavadiapp_login_table` (`id`),
  CONSTRAINT `Eanaganavadiapp_chat_toid_id_6a0975cb_fk_Eanaganav` FOREIGN KEY (`toid_id`) REFERENCES `eanaganavadiapp_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `eanaganavadiapp_chat_table` */

insert  into `eanaganavadiapp_chat_table`(`id`,`date`,`fromid_id`,`toid_id`,`message`) values 
(1,'2023-11-11',4,5,'Hiiii'),
(2,'2023-11-11',5,4,'Hii');

/*Table structure for table `eanaganavadiapp_complaints_table` */

DROP TABLE IF EXISTS `eanaganavadiapp_complaints_table`;

CREATE TABLE `eanaganavadiapp_complaints_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `complaint` varchar(90) NOT NULL,
  `date` date NOT NULL,
  `reply` varchar(90) NOT NULL,
  `STUDENT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Eanaganavadiapp_comp_STUDENT_id_cbbf7726_fk_Eanaganav` (`STUDENT_id`),
  CONSTRAINT `Eanaganavadiapp_comp_STUDENT_id_cbbf7726_fk_Eanaganav` FOREIGN KEY (`STUDENT_id`) REFERENCES `eanaganavadiapp_student_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `eanaganavadiapp_complaints_table` */

insert  into `eanaganavadiapp_complaints_table`(`id`,`complaint`,`date`,`reply`,`STUDENT_id`) values 
(2,'Improper guiding','2023-11-18','Let me check',3);

/*Table structure for table `eanaganavadiapp_feedback_table` */

DROP TABLE IF EXISTS `eanaganavadiapp_feedback_table`;

CREATE TABLE `eanaganavadiapp_feedback_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `feedback` varchar(90) NOT NULL,
  `date` date NOT NULL,
  `rating` int NOT NULL,
  `STUDENT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Eanaganavadiapp_feed_STUDENT_id_eb86a332_fk_Eanaganav` (`STUDENT_id`),
  CONSTRAINT `Eanaganavadiapp_feed_STUDENT_id_eb86a332_fk_Eanaganav` FOREIGN KEY (`STUDENT_id`) REFERENCES `eanaganavadiapp_student_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `eanaganavadiapp_feedback_table` */

insert  into `eanaganavadiapp_feedback_table`(`id`,`feedback`,`date`,`rating`,`STUDENT_id`) values 
(2,'Good','2023-11-11',5,2),
(3,'jhgkg','2023-11-11',4,3);

/*Table structure for table `eanaganavadiapp_fooditems_table` */

DROP TABLE IF EXISTS `eanaganavadiapp_fooditems_table`;

CREATE TABLE `eanaganavadiapp_fooditems_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fooditem` varchar(90) NOT NULL,
  `time` time(6) NOT NULL,
  `day` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `eanaganavadiapp_fooditems_table` */

insert  into `eanaganavadiapp_fooditems_table`(`id`,`fooditem`,`time`,`day`) values 
(1,'biriyani','12:15:00.000000','saturday'),
(2,'rice','12:15:00.000000','monday'),
(3,'Milk','15:30:00.000000','wednesday');

/*Table structure for table `eanaganavadiapp_leaverequest_table` */

DROP TABLE IF EXISTS `eanaganavadiapp_leaverequest_table`;

CREATE TABLE `eanaganavadiapp_leaverequest_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `levedate` date NOT NULL,
  `request` varchar(90) NOT NULL,
  `date` date NOT NULL,
  `STUDENT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Eanaganavadiapp_leav_STUDENT_id_38ee6402_fk_Eanaganav` (`STUDENT_id`),
  CONSTRAINT `Eanaganavadiapp_leav_STUDENT_id_38ee6402_fk_Eanaganav` FOREIGN KEY (`STUDENT_id`) REFERENCES `eanaganavadiapp_student_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `eanaganavadiapp_leaverequest_table` */

insert  into `eanaganavadiapp_leaverequest_table`(`id`,`levedate`,`request`,`date`,`STUDENT_id`) values 
(2,'2023-11-11','cold','2023-11-11',2),
(3,'2023-11-15','fever','2023-11-11',3);

/*Table structure for table `eanaganavadiapp_login_table` */

DROP TABLE IF EXISTS `eanaganavadiapp_login_table`;

CREATE TABLE `eanaganavadiapp_login_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(90) NOT NULL,
  `password` varchar(90) NOT NULL,
  `type` varchar(90) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `eanaganavadiapp_login_table` */

insert  into `eanaganavadiapp_login_table`(`id`,`username`,`password`,`type`) values 
(1,'admin','123','admin'),
(2,'anu','Anu@1234','staff'),
(4,'maya','Mayakk@23','staff'),
(5,'ewaan','Ewaan@123','student'),
(6,'hari','Hari@1234','student');

/*Table structure for table `eanaganavadiapp_staff_table` */

DROP TABLE IF EXISTS `eanaganavadiapp_staff_table`;

CREATE TABLE `eanaganavadiapp_staff_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `firstname` varchar(90) NOT NULL,
  `lastname` varchar(90) NOT NULL,
  `age` int NOT NULL,
  `place` varchar(90) NOT NULL,
  `post` varchar(90) NOT NULL,
  `pin` bigint NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(90) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Eanaganavadiapp_staf_LOGIN_id_c8c212de_fk_Eanaganav` (`LOGIN_id`),
  CONSTRAINT `Eanaganavadiapp_staf_LOGIN_id_c8c212de_fk_Eanaganav` FOREIGN KEY (`LOGIN_id`) REFERENCES `eanaganavadiapp_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `eanaganavadiapp_staff_table` */

insert  into `eanaganavadiapp_staff_table`(`id`,`firstname`,`lastname`,`age`,`place`,`post`,`pin`,`phone`,`email`,`photo`,`LOGIN_id`) values 
(1,'anu','sree',22,'kozhikode','kozhikode',678678,8078261058,'anu@gmail.com','hero-bg_AL81aa7.jpg',2),
(2,'Maya','kk',27,'Kuttippuram','Kuttippuram',679575,9087654321,'maya23@gmail.com','123.jpeg',4);

/*Table structure for table `eanaganavadiapp_student_table` */

DROP TABLE IF EXISTS `eanaganavadiapp_student_table`;

CREATE TABLE `eanaganavadiapp_student_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `firstname` varchar(90) NOT NULL,
  `lastname` varchar(90) NOT NULL,
  `age` int NOT NULL,
  `place` varchar(90) NOT NULL,
  `post` varchar(90) NOT NULL,
  `parentname` varchar(90) NOT NULL,
  `pin` bigint NOT NULL,
  `phone` bigint NOT NULL,
  `photo` varchar(100) NOT NULL,
  `email` varchar(90) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  `STAFF_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Eanaganavadiapp_stud_LOGIN_id_989049da_fk_Eanaganav` (`LOGIN_id`),
  KEY `Eanaganavadiapp_stud_STAFF_id_518ec3da_fk_Eanaganav` (`STAFF_id`),
  CONSTRAINT `Eanaganavadiapp_stud_LOGIN_id_989049da_fk_Eanaganav` FOREIGN KEY (`LOGIN_id`) REFERENCES `eanaganavadiapp_login_table` (`id`),
  CONSTRAINT `Eanaganavadiapp_stud_STAFF_id_518ec3da_fk_Eanaganav` FOREIGN KEY (`STAFF_id`) REFERENCES `eanaganavadiapp_staff_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `eanaganavadiapp_student_table` */

insert  into `eanaganavadiapp_student_table`(`id`,`firstname`,`lastname`,`age`,`place`,`post`,`parentname`,`pin`,`phone`,`photo`,`email`,`LOGIN_id`,`STAFF_id`) values 
(2,'Ewaan','Abeesh',3,'Edappal','Edappal','Abeesh',679576,7776665554,'kids.jpeg','abeesh54@gmail.com',5,2),
(3,'Hari','krishna',4,'kozhikode','kozhikode','Divya',673001,9876543210,'download.jpeg','divya@gmail.com',6,1);

/*Table structure for table `eanaganavadiapp_studymaterials_table` */

DROP TABLE IF EXISTS `eanaganavadiapp_studymaterials_table`;

CREATE TABLE `eanaganavadiapp_studymaterials_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `studymaterials` varchar(100) NOT NULL,
  `title` varchar(90) NOT NULL,
  `STAFF_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Eanaganavadiapp_stud_STAFF_id_096aedf8_fk_Eanaganav` (`STAFF_id`),
  CONSTRAINT `Eanaganavadiapp_stud_STAFF_id_096aedf8_fk_Eanaganav` FOREIGN KEY (`STAFF_id`) REFERENCES `eanaganavadiapp_staff_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `eanaganavadiapp_studymaterials_table` */

insert  into `eanaganavadiapp_studymaterials_table`(`id`,`studymaterials`,`title`,`STAFF_id`) values 
(1,'COMMUNITY SEEKERS_yk7x7TK.docx','Eng',1),
(2,'E-Anganwadi_abstract.pdf','Malayalam',2);

/*Table structure for table `eanaganavadiapp_syllabus_table` */

DROP TABLE IF EXISTS `eanaganavadiapp_syllabus_table`;

CREATE TABLE `eanaganavadiapp_syllabus_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `subject` varchar(90) NOT NULL,
  `syllabus` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `eanaganavadiapp_syllabus_table` */

insert  into `eanaganavadiapp_syllabus_table`(`id`,`subject`,`syllabus`) values 
(1,'English','ABSTRACT_jgokC07.docx'),
(2,'Malayalam','E-Anganwadi.pdf');

/*Table structure for table `eanaganavadiapp_workingtime_table` */

DROP TABLE IF EXISTS `eanaganavadiapp_workingtime_table`;

CREATE TABLE `eanaganavadiapp_workingtime_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fromtime` time(6) NOT NULL,
  `totime` time(6) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `eanaganavadiapp_workingtime_table` */

insert  into `eanaganavadiapp_workingtime_table`(`id`,`fromtime`,`totime`,`date`) values 
(1,'09:11:00.000000','16:13:00.000000','2023-11-22'),
(4,'10:00:00.000000','16:00:00.000000','2023-11-15');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
