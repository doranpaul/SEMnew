from flask import Flask, abort, request, jsonify
from flask_cors import CORS
from function import calculate_risk_of_failure

app = Flask(__name__)
CORS(app, origins="*")

@app.route('/')
def risk_fail():
    try:
        attendance_1 = int(request.args.get('attendance_1'))
        attendance_2 = int(request.args.get('attendance_2'))
        attendance_3 = int(request.args.get('attendance_3'))
        attendance_4 = int(request.args.get('attendance_4'))
        cutoff = int(request.args.get('cut-off'))
    except (TypeError, ValueError):
        abort(400, description="Invalid request. Attendance values and cut-off must be integers.")
        
    if not (0 <= attendance_1 <= 33 and 0 <= attendance_2 <= 22 and 0 <= attendance_3 <= 44 and 0 <= attendance_4 <= 55 and 0 <= cutoff <= 100):
        abort(400, description="Invalid request. Attendance values or cut-off is out of range.")

    student_engagement_score = calculate_risk_of_failure(attendance_1, attendance_2, attendance_3, attendance_4)

    if student_engagement_score >= (cutoff + 8):
        result = {"riskOfFail": "Student is not currently at risk of failure"}
    elif (cutoff + 4) <= student_engagement_score < (cutoff + 8):
        result = {"riskOfFail": "Student is borderline at risk of failure"}
    elif cutoff - 2 < student_engagement_score < (cutoff + 4):
        result = {"riskOfFail": "Student is at risk of failure"}
    else:
        result = {"riskOfFail": "Student is currently failing, you need to improve your attendance!"}

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)