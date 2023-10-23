from flask import Flask, jsonify
import smtplib, ssl
from email.message import EmailMessage
import requests
import json
import random
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
scheduler = BackgroundScheduler()

value_limits = {
    'Lecture sessions': 33,
    'Lab sessions': 22,
    'Support sessions': 44,
    'Canvas activities': 55,
}

@app.route('/health')
def health_check():
    return jsonify({"status": "ok"}), 200

@app.route('/run-monitoring')
def run_monitoring():
    random_inputs, attendance_only_inputs, expected_outputs, cut_off = generate_random_inputs()
    container_urls = [
        # Your container URLs here
        'http://sem-proxy.40070680.qpc.hal.davecutting.uk/sem-sort',
        'http://sem-proxy.40070680.qpc.hal.davecutting.uk/sem-maxmin',
        'http://sem-proxy.40070680.qpc.hal.davecutting.uk/sem-maxmin',
        'http://sem-proxy.40070680.qpc.hal.davecutting.uk/sem-stdengagement',
        'http://sem-proxy.40070680.qpc.hal.davecutting.uk/sem-riskoffail',
        'http://sem-proxy.40070680.qpc.hal.davecutting.uk/sem-improvementplan'
    ]
    functions = ["Sorted values", "Max and Min Item", "Student Engagement Score", "Risk of Failure", "Total Hours", "Improvement Plan"]
    expected_keys = [["sorted_attendance"], ["max_item", "min_item"], ["student_engagement_score"], ["riskOfFail"], [None], ["improvement_plan"]]

    metrics_list = [
        get_metrics(
            func,
            requests.get(f"{url}?{attendance_only_inputs if 'totalhours' in url else random_inputs}{'&cut-off=' + str(cut_off) if 'riskoffail' in url else ''}"),
            expected_keys[i],
            [expected_outputs.get(key, 'N/A') for key in expected_keys[i]]
        )
        for i, (func, url) in enumerate(zip(functions, container_urls))
    ]
    
    email_content = generate_email_content(metrics_list)
    scheduler.add_job(send_email, 'interval', minutes=360, id="email_job", replace_existing=True, args=[email_content])

    if not scheduler.running:
        scheduler.start()

    return jsonify({"status": "Monitoring run completed"}), 200
    
def generate_random_inputs():
    items = list(value_limits.keys())
    attendance_values = [random.randint(5, value_limits[item]) for item in items]
    random_inputs = "&".join([f"item_{i+1}={item}&attendance_{i+1}={attendance}" for i, (item, attendance) in enumerate(zip(items, attendance_values))])
    attendance_only_inputs = "&".join([f"attendance_{i+1}={attendance}" for i, attendance in enumerate(attendance_values)])
    cut_off = random.randint(40, 60)
    
    # Fetch expected outputs from other containers
    expected_outputs = {
        key: fetch_from_container(url, random_inputs, key)
        for key, url in {
            "sorted_attendance": 'http://sem-proxy.40070680.qpc.hal.davecutting.uk/sem-sort',
            "max_item": 'http://sem-proxy.40070680.qpc.hal.davecutting.uk/sem-maxmin',
            "min_item": 'http://sem-proxy.40070680.qpc.hal.davecutting.uk/sem-maxmin',
            "student_engagement_score": 'http://sem-proxy.40070680.qpc.hal.davecutting.uk/sem-stdengagement',
            "riskOfFail": 'http://sem-proxy.40070680.qpc.hal.davecutting.uk/sem-riskoffail',
            "improvement_plan": 'http://sem-proxy.40070680.qpc.hal.davecutting.uk/sem-improvementplan'
        }.items()
    }
    
    return random_inputs, attendance_only_inputs, expected_outputs, cut_off


def fetch_from_container(url, random_inputs, key):
    try:
        response = requests.get(f'{url}/?{random_inputs}')
        print(f"Status Code for {url}: {response.status_code}")  # Debugging line
        print(f"JSON Response for {url}: {response.json()}")  # Debugging line
        if response.status_code == 200:
            return response.json().get(key, 'N/A')
        else:
            return 'N/A'
    except Exception as e:
        print(f"An error occurred while fetching from {url}: {e}")
        return 'N/A'

def get_metrics(function, http, expected_keys, expected_values):
    print(f"Trying to access URL: {http.url}")
    print(f"Expected Keys: {expected_keys}")  # Debugging line
    print(f"Expected Values: {expected_values}")  # Debugging line
    
    status = "Responsive" if http.status_code == 200 else "Unresponsive"
    print(f"Status Code for {http.url}: {http.status_code}")
    
    response_time = http.elapsed.total_seconds()
    
    actual_values = []
    for expected_key in expected_keys:
        if expected_key is None:  # Special case for total hours
            actual_values.append(http.text)
        else:
            try:
                response_json = http.json()
                print(f"JSON Response: {response_json}")
                
                if expected_key in response_json:
                    actual_values.append(response_json[expected_key])
                else:
                    print(f"Key {expected_key} not found in JSON response.")
                    actual_values.append('N/A')
            except Exception as e:  # Catching all exceptions for debugging
                print(f"An error occurred while processing {http.url}: {e}")
                actual_values.append('N/A')
    
    # Convert to string for comparison
    formatted_actual_values = json.dumps(actual_values, sort_keys=True)
    formatted_expected_values = json.dumps(expected_values, sort_keys=True)
    
    returns_expected_result = "Yes" if formatted_actual_values == formatted_expected_values else "No"

    print(f"Response: {formatted_actual_values}\nExpected: {formatted_expected_values}\nMatch: {returns_expected_result == 'Yes'}")
    
    return [http.url, function, status, response_time, returns_expected_result]



def generate_email_content(metrics_list):
    content = ""
    for i, metrics in enumerate(metrics_list, 1):
        content += f"Container {i}\n"
        content += "\n".join([f"{key}: {value}" for key, value in zip(["URL", "Function", "Status", "Response Time", "Returns Expected Results"], metrics)])
        content += "\n\n"
    return content

def send_email(email_content):
    try:
        msg = EmailMessage()
        msg.set_content(email_content)
        msg["Subject"] = "Student Engagement Monitoring Application Update"
        msg["From"] = "monitoring.sem@outlook.com"
        msg["To"] = "sem.mon.receipt@gmail.com"
        
        smtp_server = "smtp.office365.com"
        smtp_port = 587
        smtp_username = "monitoring.sem@outlook.com"
        smtp_password = "monitoring1"

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, smtp_port) as smtp:
            smtp.starttls(context=context)
            smtp.login(smtp_username, smtp_password)
            smtp.send_message(msg)
        print("Email sent successfully.")
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)