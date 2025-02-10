from flask import request, jsonify
import os
from model.complaintModel import create_complaint, get_complaints_by_user_id, get_all_complaints,delete_complaint,create_customer_feedback,get_all_feedbacks as model_get_all_feedbacks


def submit_complaint_s():
    try:
        complaint_text = request.form.get('complaintText')
        laptop_name = request.form.get('laptopName')
        laptop_brand = request.form.get('laptopBrand')
        laptop_price = request.form.get('laptopPrice')

        # Check if a file is included in the request
        if 'image' in request.files:
            image_file = request.files['image']
            image_url = os.path.join("public/images", image_file.filename)
            image_file.save(image_url)
        else:
            image_url = None

        complaint_id = create_complaint(complaint_text, laptop_name, laptop_brand, laptop_price,  image_url)

        return jsonify({'success': True, 'complaintId': complaint_id}), 201
    except Exception as error:
        print(error)
        return jsonify({'success': False, 'error': 'Internal Server Error'}), 500

def get_user_complaint_s(user_id):
    try:
        complaints = get_complaints_by_user_id(user_id)
        return jsonify({'success': True, 'complaints': complaints}), 200
    except Exception as error:
        print(error)
        return jsonify({'success': False, 'error': 'Internal Server Error'}), 500

def get_all_complaint_s():
    try:
        complaints = get_all_complaints()
        return jsonify({'success': True, 'complaints': complaints}), 200
    except Exception as error:
        print(error)
        return jsonify({'success': False, 'error': 'Internal Server Error'}), 500

def delete_complaint_s(complaint_id):
    try:
        success = delete_complaint(complaint_id)
        if success:
            return jsonify({'success': True, 'message': 'Complaint deleted successfully'}), 200
        else:
            return jsonify({'success': False, 'error': 'Failed to delete complaint'}), 400
    except Exception as error:
        print(error)
        return jsonify({'success': False, 'error': 'Internal Server Error'}), 500

def submit_feedback(complaint_id):
    try:
        data = request.json
        feedback_text = data.get('feedback_text')

        # Check if feedback_text is provided
        if not feedback_text:
            return jsonify({'success': False, 'error': 'Missing feedback text'}), 400
        
        feedback_id = create_customer_feedback(complaint_id, feedback_text)

        # Return success response with feedback id
        return jsonify({'success': True, 'feedbackId': feedback_id}), 201

    except Exception as error:
        print(error)
        return jsonify({'success': False, 'error': 'Internal Server Error'}), 500

def get_all_feedbacks():
    try:
        feedbacks = model_get_all_feedbacks()
        return jsonify({'success': True, 'Feedback': feedbacks}), 200
    except Exception as error:
        print(error)
        return jsonify({'success': False, 'error': 'Internal Server Error'}), 500