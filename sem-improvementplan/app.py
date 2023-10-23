from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from function import suggest_improvement_plan

app = Flask(__name__)
CORS(app, origins="*")

@app.route('/')
def improvement_plan():
    try:
        attendance_1 = int(request.args.get('attendance_1'))
        attendance_2 = int(request.args.get('attendance_2'))
        attendance_3 = int(request.args.get('attendance_3'))
        attendance_4 = int(request.args.get('attendance_4'))
    except(TypeError, ValueError):
        abort(400, description="Invalid request. Attendance values and cut-off must be integers.")
    if not(0 <= attendance_1 <= 33 and 0 <= attendance_2 <= 22 and 0 <= attendance_3 <= 44 and 0 <= attendance_4 <= 55):
        abort(400, description="Invalid request. Attendance values are out of range.")

    suggestions = suggest_improvement_plan(attendance_1, attendance_2, attendance_3, attendance_4)

    return jsonify({'improvement_plan': suggestions})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)