import mysql.connector
from config.dbConfig import db

def create_complaint(complaint_text, laptop_name, laptop_brand, laptop_price, image_path):
    try:
        query = "INSERT INTO complaints (complaintText, laptopName, laptopBrand, laptopPrice, imagePath) VALUES (%s, %s, %s, %s, %s)"
        values = (complaint_text, laptop_name, laptop_brand, laptop_price, image_path)
        
        cursor = db.cursor()
        cursor.execute(query, values)
        db.commit()

        return cursor.lastrowid
    except Exception as error:
        raise error

def get_all_complaints():
    try:
        query = "SELECT * FROM complaints"
        
        cursor = db.cursor(dictionary=True)
        cursor.execute(query)

        return cursor.fetchall()
    except Exception as error:
        raise error

def get_complaints_by_user_id(user_id):
    try:
        query = "SELECT * FROM complaints WHERE user_id = %s"
        
        cursor = db.cursor(dictionary=True)
        cursor.execute(query, (user_id,))

        return cursor.fetchall()
    except Exception as error:
        raise error

def delete_complaint(complaint_id):
    try:
        query = "DELETE FROM complaints WHERE id = %s"
        
        cursor = db.cursor()
        cursor.execute(query, (complaint_id,))
        db.commit()

        return True
    except Exception as error:
        raise error

def create_customer_feedback(complaint_id,feedback_text):
    try:
        query = "INSERT INTO complaint_feedback (complaint_id,feedback_text) VALUES (%s,%s)"
        values = (complaint_id, feedback_text)
        cursor = db.cursor()
        cursor.execute(query, values)
        db.commit()

        return cursor.lastrowid
    except Exception as e:
        # Handle the error gracefully
        print(f"Error occurred: {e}")
        self.db.rollback()  # Rollback the transaction if an error occurs
        return None  # Return None to indicate failure

def get_all_feedbacks():
    try:
        query = "SELECT * FROM complaint_feedback"
        
        cursor = db.cursor(dictionary=True)
        cursor.execute(query)

        feedbacks = cursor.fetchall()  # Fetch all feedbacks from the database

        return feedbacks  # Return the feedbacks directly
    except Exception as error:
        raise error
