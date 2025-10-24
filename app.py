from flask import Flask, render_template, request, make_response
import pdfkit

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    name = request.form['name']
    email = request.form['email']
    education = request.form['education']
    experience = request.form['experience']
    skills = request.form['skills']
    template = request.form['template']

    # Choose the correct template file
    template_file = f"resume_{template}.html"

    # Render HTML from template
    rendered = render_template(template_file,
                               name = name,
                               email = email,
                               education = education,
                               experience = experience,
                               skills = skills)
    
    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
    pdf = pdfkit.from_string(rendered, False, configuration=config)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=resume.pdf'
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1000)


