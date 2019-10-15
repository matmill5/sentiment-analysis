-- MySQL Workbench Forward Engineering

-- -----------------------------------------------------
-- Table `mydb`.`User`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `capstone$mydb`.`User` ;

CREATE TABLE IF NOT EXISTS `capstone$mydb`.`User` (
  `idUser` INT NOT NULL,
  `First_Name` VARCHAR(45) NULL,
  `Last_Name` VARCHAR(500) NULL,
  `Email` VARCHAR(500) NULL,
  `Phone_Number` VARCHAR(45) NULL,
  `Department` VARCHAR(45) NULL,
  `Occupation` VARCHAR(45) NULL,
  `User_Type` VARCHAR(45) NULL,
  `Member_Since` VARCHAR(45) NULL,
  `Total_Transaction_Request` VARCHAR(45) NULL,
  PRIMARY KEY (`idUser`));


-- -----------------------------------------------------
-- Table `mydb`.`Transaction`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `capstone$mydb`.`Transaction` ;

CREATE TABLE IF NOT EXISTS `capstone$mydb`.`Transaction` (
  `idTransaction` INT NOT NULL,
  `idUser` INT NULL,
  `Data_Tag` VARCHAR(500) NULL,
  `Date_Time_Client` VARCHAR(500) NULL,
  `Number_Of_Records` VARCHAR(500) NULL,
  `Date_Time_Server` VARCHAR(500) NULL,
  `idBody` INT NULL,
  `User_idUser` INT NOT NULL,
  PRIMARY KEY (`idTransaction`),
  CONSTRAINT `fk_Transaction_User`
    FOREIGN KEY (`User_idUser`)
    REFERENCES `capstone$mydb`.`User` (`idUser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `mydb`.`Body`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `capstone$mydb`.`Body` ;

CREATE TABLE IF NOT EXISTS `capstone$mydb`.`Body` (
  `idBody` INT NULL,
  `TransID` VARCHAR(45) NULL,
  `Text` LONGTEXT NULL,
  `Transaction_idTransaction` INT NOT NULL,
  PRIMARY KEY (`idBody`),
  CONSTRAINT `fk_Body_Transaction1`
    FOREIGN KEY (`Transaction_idTransaction`)
    REFERENCES `capstone$mydb`.`Transaction` (`idTransaction`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `mydb`.`Data_Type_Relation`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `capstone$mydb`.`Data_Type_Relation` ;

CREATE TABLE IF NOT EXISTS `capstone$mydb`.`Data_Type_Relation` (
  `idData_Type_Relation` INT NOT NULL,
  `idTransaction` INT NULL,
  `Course_Evaluation` VARCHAR(500) NULL,
  `Twitter` VARCHAR(500) NULL,
  `Reviews` VARCHAR(500) NULL,
  `Surveys` VARCHAR(45) NULL,
  `Transaction_idTransaction` INT NOT NULL,
  PRIMARY KEY (`idData_Type_Relation`, `Transaction_idTransaction`),
  CONSTRAINT `fk_Data_Type_Relation_Transaction1`
    FOREIGN KEY (`Transaction_idTransaction`)
    REFERENCES `capstone$mydb`.`Transaction` (`idTransaction`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
