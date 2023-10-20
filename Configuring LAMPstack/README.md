# Setting up a LAMP Server on Amazon EC2

This guide provides step-by-step instructions for setting up a LAMP (Linux, Apache, MySQL, PHP) server on an Amazon EC2 instance using Amazon Linux. LAMP is a popular stack for hosting web applications. Follow these steps to get your LAMP server up and running.

## Prerequisites

Before you start, ensure you have the following in place:

- An [Amazon Web Services (AWS) account](https://aws.amazon.com/).
- Basic knowledge of AWS EC2 and SSH key pairs.
- An EC2 instance launched with an Amazon Linux AMI.

## Step 1: Launch EC2 Instance

1. Go to the [Amazon EC2 console](https://console.aws.amazon.com/ec2/).
2. Click "Launch Instance."
3. Select an "Amazon Linux AMI."
4. Choose an "t2.micro" instance type.
5. Configure the instance details, including the key pair and security group.
6. Click "Launch Instances."

## Step 2: Connect to the EC2 Instance

1. Once the EC2 instance is launched, connect to it using SSH keypair:

   ```bash
   ssh -i YourKeyPair.pem ec2-user@YourInstancePublicIP
   ```

2. Update the package manager:

   ```bash
   sudo yum update
   ```

## Step 3: Install LAMP Software

To set up the LAMP stack, follow these steps:

1. Install Apache web server, MariaDB, and PHP:

   ```bash
   sudo yum install httpd mariadb-server php72
   ```

2. Start the Apache web server and MariaDB:

   ```bash
   sudo systemctl start httpd mariadb
   ```

## Step 4: Create a MySQL User Account

1. Log in to MySQL as the root user:

   ```bash
   mysql -u root -p
   ```

   Enter the MySQL root password when prompted.

2. Create a MySQL user account for your web application:

   ```sql
   CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
   GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost' WITH GRANT OPTION;
   FLUSH PRIVILEGES;
   EXIT
   ```

## Step 5: Create a Database

1. Log in to MySQL as the root user:

   ```bash
   mysql -u root -p
   ```

   Enter the MySQL root password when prompted.

2. Create a database for your web application:

   ```sql
   CREATE DATABASE my_database;
   EXIT
   ```

## Step 6: Configure Apache

1. Edit the Apache configuration file:

   ```bash
   sudo nano /etc/httpd/conf/httpd.conf
   ```

2. Add the following lines to the configuration file:

   ```apache
   DocumentRoot "/var/www/html"
   <Directory "/var/www/html">
       AllowOverride All
   </Directory>
   ```

3. Save and close the configuration file.

## Step 7: Restart Apache

Restart the Apache web server:

```bash
sudo systemctl restart httpd
```

## Step 8: Test the LAMP Stack

To test the LAMP stack, open a web browser and navigate to the public DNS name of your EC2 instance. You should see the default Apache page.

Your LAMP server is now set up and ready to host web applications. You can upload your application files to the `/var/www/html` directory and configure your web application accordingly.
