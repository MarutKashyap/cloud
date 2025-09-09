import json
import urllib.parse
import boto3

print('Loading function')

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE: " + response['ContentType'])
        return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e


        ////////
        #!/bin/bash
# Update and install Apache
apt-get update -y
apt-get install -y apache2

# Create a custom index.html with server details
echo "<h1>Server Details</h1>
<p><strong>Hostname:</strong> $(hostname)</p>
<p><strong>IP Address:</strong> $(hostname -I | cut -d' ' -f1)</p>" > /var/www/html/index.html

# Restart Apache to apply changes
systemctl restart apache2

/////////
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "PublicReadGetObject",
			"Effect": "Allow",
			"Principal": "*",
			"Action": "s3:GetObject",
			"Resource": "arn:aws:s3:::ksbucketnew/*"
		}
	]
}
///////////

CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    marks INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE Student_Audit (
    audit_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    old_marks INT,
    new_marks INT,
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
DELIMITER $$

CREATE TRIGGER after_student_update
AFTER UPDATE ON Students
FOR EACH ROW
BEGIN
    INSERT INTO Student_Audit(student_id, old_marks, new_marks)
    VALUES (OLD.student_id, OLD.marks, NEW.marks);
END$$

DELIMITER ;
DELIMITER $$

CREATE PROCEDURE GetTopStudents(IN min_marks INT)
BEGIN
    SELECT student_id, name, marks
    FROM Students
    WHERE marks >= min_marks
    ORDER BY marks DESC;
END$$

DELIMITER ;
-- Insert sample students
INSERT INTO Students(name, marks) VALUES ('Alice', 80), ('Bob', 60), ('Charlie', 90);

-- Update Bob’s marks (trigger will log the change)
UPDATE Students SET marks = 75 WHERE name = 'Bob';

-- See audit log
SELECT * FROM Student_Audit;

-- Call stored procedure
CALL GetTopStudents(70);


/////
INSERT INTO Students (name, marks) 
VALUES ('Alice', 85);

SELECT * FROM Students;

UPDATE Students 
SET marks = 90 
WHERE student_id = 1;

UPDATE Students 
SET name = 'Bob', marks = 95 
WHERE student_id = 2;

DELETE FROM Students 
WHERE student_id = 3;

SELECT COUNT(*) AS total_students FROM Students;
