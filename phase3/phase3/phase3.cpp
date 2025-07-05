//pahse3-code
#include <iostream>
#include <mysql_driver.h>
#include <mysql_connection.h>

using namespace std;
using namespace sql;

int main() {
    string server = "localhost";
    string username = "root";
    string password = "manyadammire";
    string database = "project";

    Driver* driver = get_driver_instance();
    Connection* connection = driver->connect("localhost", "root", "manyadammire");
    connection->setSchema(project);