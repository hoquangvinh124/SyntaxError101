from flask import Blueprint, render_template
from .utils.CheckCandidateStatus import count_candidate_status, status_dictionary, extract_cv_per_month, static_cv_gender

landing = Blueprint('landing', __name__) 

@landing.route('/')
def sign_up():
    candidate_label, candidate_status = count_candidate_status()
    candidate_dictionary = status_dictionary()
    cv_created_per_month = extract_cv_per_month()
    gender_label, cv_created_per_gender = static_cv_gender()
    return render_template("home.html", candidate_label=candidate_label, candidate_status=candidate_status,
                           pending=candidate_dictionary['pending'], interviewed=candidate_dictionary['interviewed'],
                           hired=candidate_dictionary['hired'], rejected=candidate_dictionary['rejected'],
                           cv_created_per_month=cv_created_per_month, gender_label=gender_label, 
                           cv_created_per_gender=cv_created_per_gender)