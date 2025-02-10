from flask import Blueprint, request, jsonify
from controllers.complaintController import submit_complaint_s, get_user_complaint_s, get_all_complaints,delete_complaint_s,submit_feedback,get_all_feedbacks
import os

complaint_routes = Blueprint('complaint_routes', __name__)

# Ensure the destination directory exists; create it if not
destination_folder = "public/images"
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Routes
@complaint_routes.route('/submit', methods=['POST'])
def submit():
    return submit_complaint_s()

@complaint_routes.route('/user/<int:user_id>', methods=['GET'])
def get_user_complaints_route(user_id):
    return get_user_complaint_s(user_id)

@complaint_routes.route('/user', methods=['GET'])
def get_all_complaints_route():
    return get_all_complaints()

@complaint_routes.route('/complaints/<int:complaint_id>', methods=['DELETE'])
def delete_complaint_route(complaint_id):
    return delete_complaint_s(complaint_id)

@complaint_routes.route('/feedback/<int:complaint_id>', methods=['POST'])
def submit_feedback_route(complaint_id):
    return submit_feedback(complaint_id)

@complaint_routes.route('/feedbacks', methods=['GET'])
def get_all_feedbacks_route():
    return get_all_feedbacks()
