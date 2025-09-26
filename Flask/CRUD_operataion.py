from flask import Flask, request,jsonify
app = Flask(__name__)
students = {}

#create post
@app.route('/student',methods=['POST'])
def create_student():
	data = request.get_json()
	student_id = str(len(students) + 1)
	students[student_id] = data
	return jsonify({'id':student_id,'msg':'student created'}),201

#read get
@app.route('/student/<id>',methods=['GET'])
def get_student(id):
	student = students.get(id)
	if not student:
		return jsonify({"error":"student not found"}),404
	return jsonify({id:student})

#update put
@app.route('/student/<id>',methods=['PUT'])
def update_student(id):
	if id not in students:
		return jsonify({"error":"student not found"}),404
	data = request.get_json()
	students[id] = data
	return jsonify({'id':id,'msg':'student update success'})

#delete delete
@app.route('/student/<id>',methods = ['DELETE'])
def delete_student(id):
	if id not in students:
		return jsonify({'id':id,'msg':'student not found'}),404
	del students[id]
	return jsonify({'id':id,'msg':'student deleted success'})

if __name__ == '__main__':
	app.run()


for run a code use this
#pip install httpie
#http POST http://127.0.0.1:5000/student name=Aakash age=25 course=Python
#http GET  http://127.0.0.1:5000/student/1
#http PUT  http://127.0.0.1:5000/student/1 name="Aakash Pawar" age=26 course="Data Science"
#http DELETE http://127.0.0.1:5000/student/1
