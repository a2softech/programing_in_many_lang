from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()

students = {}

class Student(BaseModel):
	name:str
	age:int
	course:str

#create post
@app.post('/student/')
def create_student(student: Student):
	student_id = str(len(students) + 1)
	students[student_id] = student.dict()
	return {'id':student_id,'msg':'student created'}

#read get
@app.get('/student/{student_id}')
def get_student(student_id:str):
	student = students.get(student_id)
	if not student:
		raise HTTPException(status_code=404,detail='student not found')
	return {student_id: student}

#update put
@app.put('/student/{student_id}')
def update_student(student_id : str, student:Student):
	if student_id not in students:
		raise HTTPException(status_code = 404, detail = 'student not found')
	students[student_id] = student
	return {'id':student_id,'msg':'student update'}

#delete delete
@app.delete('/student/{student_id}')
def delete_student(student_id:str):
	if student_id not in students:
		raise HTTPException(status_code = 404, detail = 'student not found')
	del students[student_id]
	return {'id':student_id,'msg':'student delete'}