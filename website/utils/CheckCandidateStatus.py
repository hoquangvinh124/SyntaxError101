from .JsonFactory import JsonFileFactory
from .class_info.Candidate import Candidate
from datetime import datetime


def count_candidate_status():
    count_dict = {}
    arr_data = JsonFileFactory.read_data("website/data/candidates/candidates.json", Candidate)

    for c in arr_data:
        count_dict[c.status] = count_dict.get(c.status, 0) + 1

    capitalized_list = [word.capitalize() for word in count_dict.keys()]

    return capitalized_list, list(count_dict.values())


def status_dictionary():
    count_dict = {}
    arr_data = JsonFileFactory.read_data("website/data/candidates/candidates.json", Candidate)

    for c in arr_data:
        count_dict[c.status] = count_dict.get(c.status, 0) + 1

    return count_dict


def extract_cv_per_month():
    arr_data = JsonFileFactory.read_data("website/data/candidates/candidates.json", Candidate)
    
    monthly_counts = [0] * 12

    for candidate in arr_data:
        created_time = datetime.strptime(candidate.created_date, "%d-%m-%Y %H:%M:%S")
        month_index = created_time.month - 1  
        monthly_counts[month_index] += 1

    return monthly_counts

def static_cv_gender():
    count_dict = {}
    arr_data = JsonFileFactory.read_data("website/data/candidates/candidates.json", Candidate)

    for c in arr_data:
        count_dict[c.gender] = count_dict.get(c.gender, 0) + 1

    capitalized_gender = [word.capitalize() for word in count_dict.keys()]

    return capitalized_gender, list(count_dict.values())

