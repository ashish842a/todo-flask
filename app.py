from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []  # Initialize an empty list to store tasks

@app.route('/')
def hello_world():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form.get('title')
    desc = request.form.get('desc')

    if title and desc:
        new_task = {'title': title, 'desc': desc, 'sno': len(tasks) + 1}
        tasks.append(new_task)

    return redirect(url_for('hello_world'))

@app.route('/update_task/<int:sno>', methods=['GET', 'POST'])
def update_task(sno):
    task_to_update = next((task for task in tasks if task['sno'] == sno), None)

    if request.method == 'POST':
        title = request.form.get('title')
        desc = request.form.get('desc')

        if task_to_update:
            task_to_update['title'] = title
            task_to_update['desc'] = desc
            return redirect(url_for('hello_world'))

    return render_template('update.html', task=task_to_update)

@app.route('/delete_task/<int:sno>')
def delete_task(sno):
    task_to_delete = next((task for task in tasks if task['sno'] == sno), None)

    if task_to_delete:
        tasks.remove(task_to_delete)

    return redirect(url_for('hello_world'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
