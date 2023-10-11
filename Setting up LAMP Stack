Steps:
Go to the Amazon EC2 console and click Launch Instance.
Select an Amazon Linux AMI
Choose an instance type t2.micro
Configure the instance details, including the key pair and security group.
Click Launch Instances.
Connect to the EC2 instance.
Once the EC2 instance was launched,connect to it using SSH keypair
Updated the package managerusing following command
sudo yum update

Performed following commands to Install the LAMP software:
Installing Apache web server and the MariaDB database server:
sudo yum install httpd mariadb-server php72

To Start the Apache web server and the MariaDB database server:

sudo systemctl start httpd mariadb

Create a MySQL user account for your web application:

mysql -u root -p
Enter the MySQL root password when prompted.

CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
EXIT

Create a database for your web application:

mysql -u root -p
Enter the MySQL root password when prompted.

CREATE DATABASE my_database;
EXIT

Edit the Apache configuration file:
sudo nano /etc/httpd/conf/httpd.conf

Add the following lines to the configuration file:

DocumentRoot "/var/www/html"
<Directory "/var/www/html">
    AllowOverride All
</Directory>
Save and close the configuration file.

Restart the Apache web server:
sudo systemctl restart httpd

To Test the LAMP stack open a web browser and navigate to the public DNS name of your EC2 instance.
