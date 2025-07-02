import os
import uuid
import json
from flask import Flask, render_template, request, redirect, url_for, send_file, flash
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
from weasyprint import HTML
from io import BytesIO

UPLOAD_FOLDER = 'static/uploads/'
TEMP_DATA_FOLDER = 'temp_data/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(TEMP_DATA_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def form():
    cv_id = request.args.get('cv_id')
    data = None
    if cv_id:
        data_path = os.path.join(TEMP_DATA_FOLDER, f'{cv_id}.json')
        if os.path.exists(data_path):
            with open(data_path) as f:
                data = json.load(f)
            # Procesar datos crudos a la estructura esperada por la plantilla (igual que en view_cv)
            def getlist(key):
                v = data.get(key)
                if isinstance(v, list):
                    return v
                elif v is not None:
                    return [v]
                return []
            if 'education' not in data:
                titles = getlist('education_title')
                years = getlist('education_years')
                data['education'] = list(zip(titles, years))
            if 'skills' not in data:
                skills = getlist('skill_name')
                levels = getlist('skill_level')
                data['skills'] = list(zip(skills, levels))
            if 'languages' not in data:
                data['languages'] = getlist('language')
            if 'experience' not in data:
                titles = getlist('exp_title')
                companies = getlist('exp_company')
                years = getlist('exp_years')
                descs = getlist('exp_desc')
                data['experience'] = [
                    {'title': t, 'company': c, 'years': y, 'desc': d}
                    for t, c, y, d in zip(titles, companies, years, descs)
                ]
            for k in ['name', 'position', 'about', 'phone', 'email', 'linkedin']:
                v = data.get(k)
                if isinstance(v, list):
                    data[k] = v[0] if v else ''
    if request.method == 'POST':
        data = request.form.to_dict(flat=False)
        # Manejo de foto de perfil
        file = request.files.get('photo')
        photo_filename = None
        if file and allowed_file(file.filename):
            ext = file.filename.rsplit('.', 1)[1].lower()
            photo_filename = f"{uuid.uuid4()}.{ext}"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_filename))
        elif 'photo' in data and data['photo']:
            # Si no se subió nueva foto, mantener la anterior
            photo_filename = data['photo'][0] if isinstance(data['photo'], list) else data['photo']
        data['photo'] = photo_filename
        data['created_at'] = datetime.utcnow().isoformat()
        # Generar UUID y guardar datos
        cv_id = str(uuid.uuid4())
        with open(os.path.join(TEMP_DATA_FOLDER, f'{cv_id}.json'), 'w') as f:
            json.dump(data, f)
        return redirect(url_for('view_cv', cv_id=cv_id))
    return render_template('form.html', data=data)

@app.route('/cv/<cv_id>')
def view_cv(cv_id):
    data_path = os.path.join(TEMP_DATA_FOLDER, f'{cv_id}.json')
    if not os.path.exists(data_path):
        return render_template('link_expired.html'), 404
    with open(data_path) as f:
        data = json.load(f)
    # Procesar datos crudos a la estructura esperada por la plantilla
    def getlist(key):
        v = data.get(key)
        if isinstance(v, list):
            return v
        elif v is not None:
            return [v]
        return []
    # Educación
    if 'education' not in data:
        titles = getlist('education_title')
        years = getlist('education_years')
        data['education'] = list(zip(titles, years))
    # Habilidades
    if 'skills' not in data:
        skills = getlist('skill_name')
        levels = getlist('skill_level')
        data['skills'] = list(zip(skills, levels))
    # Idiomas
    if 'languages' not in data:
        data['languages'] = getlist('language')
    # Experiencia
    if 'experience' not in data:
        titles = getlist('exp_title')
        companies = getlist('exp_company')
        years = getlist('exp_years')
        descs = getlist('exp_desc')
        data['experience'] = [
            {'title': t, 'company': c, 'years': y, 'desc': d}
            for t, c, y, d in zip(titles, companies, years, descs)
        ]
    # Campos simples
    for k in ['name', 'position', 'about', 'phone', 'email', 'linkedin']:
        v = data.get(k)
        if isinstance(v, list):
            data[k] = v[0] if v else ''
    return render_template('cv.html', data=data, cv_id=cv_id)

@app.route('/cv/<cv_id>/pdf')
def download_pdf(cv_id):
    data_path = os.path.join(TEMP_DATA_FOLDER, f'{cv_id}.json')
    if not os.path.exists(data_path):
        return render_template('link_expired.html'), 404
    with open(data_path) as f:
        data = json.load(f)
    # Procesar datos crudos a la estructura esperada por la plantilla (igual que en view_cv)
    def getlist(key):
        v = data.get(key)
        if isinstance(v, list):
            return v
        elif v is not None:
            return [v]
        return []
    if 'education' not in data:
        titles = getlist('education_title')
        years = getlist('education_years')
        data['education'] = list(zip(titles, years))
    if 'skills' not in data:
        skills = getlist('skill_name')
        levels = getlist('skill_level')
        data['skills'] = list(zip(skills, levels))
    if 'languages' not in data:
        data['languages'] = getlist('language')
    if 'experience' not in data:
        titles = getlist('exp_title')
        companies = getlist('exp_company')
        years = getlist('exp_years')
        descs = getlist('exp_desc')
        data['experience'] = [
            {'title': t, 'company': c, 'years': y, 'desc': d}
            for t, c, y, d in zip(titles, companies, years, descs)
        ]
    for k in ['name', 'position', 'about', 'phone', 'email', 'linkedin']:
        v = data.get(k)
        if isinstance(v, list):
            data[k] = v[0] if v else ''
    rendered = render_template('cv.html', data=data, cv_id=cv_id, pdf=True)
    pdf_bytes = BytesIO()
    HTML(string=rendered, base_url=request.base_url).write_pdf(pdf_bytes)
    pdf_bytes.seek(0)
    return send_file(pdf_bytes, as_attachment=True, download_name='cv.pdf', mimetype='application/pdf')

@app.errorhandler(413)
def too_large(e):
    return render_template('form.html', error='El archivo es demasiado grande. El máximo permitido es 10MB.'), 413

if __name__ == '__main__':
    app.run(debug=True) 