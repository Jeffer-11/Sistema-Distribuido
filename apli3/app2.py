#!/usr/bin/env python3
from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import numpy as np
import os

app = Flask(__name__)
CORS(app)  # Permite requests desde cualquier origen

# Variables globales para almacenar los DataFrames
movies_df = None
ratings_df = None
tags_df = None

def load_data():
    """Carga los archivos CSV si existen"""
    global movies_df, ratings_df, tags_df
    
    try:
        if os.path.exists('movies.csv'):
            movies_df = pd.read_csv('movies.csv')
        if os.path.exists('ratings.csv'):
            ratings_df = pd.read_csv('ratings.csv')
            # Eliminar timestamp como en el script original
            if 'timestamp' in ratings_df.columns:
                del ratings_df['timestamp']
        if os.path.exists('tags.csv'):
            tags_df = pd.read_csv('tags.csv')
            # Eliminar timestamp como en el script original
            if 'timestamp' in tags_df.columns:
                del tags_df['timestamp']
            # Eliminar valores nulos como en el script original
            tags_df = tags_df.dropna()
    except Exception as e:
        print(f"Error loading data: {e}")

@app.route('/')
def home():
    """Endpoint principal"""
    return jsonify({
        "message": "Pandas Data Analysis API",
        "endpoints": [
            "/series-demo",
            "/dataframe-demo", 
            "/movies/info",
            "/ratings/info",
            "/tags/info",
            "/ratings/statistics",
            "/ratings/filter",
            "/data/null-check"
        ]
    })

@app.route('/series-demo')
def series_demo():
    """Demuestra operaciones con Series de Pandas"""
    # Crear serie como en el script original
    ser = pd.Series(data=[1, 2, 3, 4, 5], index=['tom', 'bob', 'rob', 'ed', 'vik'])
    
    result = {
        "original_series": ser.to_dict(),
        "index": ser.index.tolist(),
        "fabian_in_series": 'fabian' in ser,
        "multiplied_by_2": (ser * 2).to_dict(),
        "power_of_2": (ser ** 2).to_dict()
    }
    
    # Segunda serie
    ser2 = pd.Series(data=[100, 200, 300, 400, 500], index=['tom', 'bob', 'rob', 'ed', 'vik'])
    result["second_series"] = ser2.to_dict()
    result["selected_by_position"] = ser2[[2, 4]].to_dict()
    result["selected_by_name"] = ser2[['tom']].to_dict()
    
    return jsonify(result)

@app.route('/dataframe-demo')
def dataframe_demo():
    """Demuestra operaciones con DataFrame"""
    # Crear DataFrame como en el script original
    df = pd.DataFrame({
        'one': pd.Series(data=[100, 200, 300], index=['apple', 'ball', 'clock']),
        'two': pd.Series(data=[100, 200, 300], index=['apple', 'ball', 'clock'])
    })
    
    df1 = pd.DataFrame(df)
    
    steps = []
    
    # Step 1: DataFrame original
    steps.append({
        "step": "original_dataframe",
        "data": df1.to_dict('index'),
        "index": df1.index.tolist(),
        "columns": df1.columns.tolist()
    })
    
    # Step 2: Agregar columna 'three'
    df1['three'] = df1['one'] * df1['two']
    steps.append({
        "step": "added_three_column",
        "data": df1.to_dict('index')
    })
    
    # Step 3: Agregar columna 'flag'
    df1['flag'] = df1['one'] > 100
    steps.append({
        "step": "added_flag_column",
        "data": df1.to_dict('index')
    })
    
    # Step 4: Remover columna 'three'
    aux = df1.pop('three')
    steps.append({
        "step": "removed_three_column",
        "data": df1.to_dict('index'),
        "removed_data": aux.to_dict()
    })
    
    # Step 5: Eliminar columna 'one'
    del df1['one']
    steps.append({
        "step": "deleted_one_column",
        "data": df1.to_dict('index')
    })
    
    # Step 6: Insertar columna 'copia de dos'
    df1.insert(2, 'copia de dos', df1['two'])
    steps.append({
        "step": "inserted_copy_column",
        "data": df1.to_dict('index')
    })
    
    # Step 7: Agregar 'flag two' y remover 'copia de dos'
    df1['flag two'] = df1['copia de dos'] > 200
    aux2 = df1.pop('copia de dos')
    steps.append({
        "step": "added_flag_two_removed_copy",
        "data": df1.to_dict('index')
    })
    
    # Step 8: Agregar 'twoupperhalf'
    df1['twoupperhalf'] = df1['two'][:2]
    steps.append({
        "step": "added_upper_half",
        "data": df1.to_dict('index')
    })
    
    # Step 9: Agregar 'twodownhalf'
    df1['twodownhalf'] = df1['two'][2:]
    steps.append({
        "step": "added_down_half",
        "data": df1.to_dict('index')
    })
    
    return jsonify({"dataframe_operations": steps})

@app.route('/movies/info')
def movies_info():
    """Información sobre el dataset de películas"""
    if movies_df is None:
        return jsonify({"error": "Movies dataset not loaded"}), 404
    
    return jsonify({
        "head_2": movies_df.head(2).to_dict('records'),
        "columns": movies_df.columns.tolist(),
        "index": movies_df.index.tolist()[:10],  # Primeros 10 para no sobrecargar
        "shape": movies_df.shape,
        "null_check": movies_df.isnull().any().to_dict()
    })

@app.route('/ratings/info')
def ratings_info():
    """Información sobre el dataset de ratings"""
    if ratings_df is None:
        return jsonify({"error": "Ratings dataset not loaded"}), 404
    
    return jsonify({
        "head_2": ratings_df.head(2).to_dict('records'),
        "tail_5": ratings_df.tail().to_dict('records'),
        "columns": ratings_df.columns.tolist(),
        "index": ratings_df.index.tolist()[:10],  # Primeros 10
        "shape": ratings_df.shape,
        "null_check": ratings_df.isnull().any().to_dict()
    })

@app.route('/tags/info')
def tags_info():
    """Información sobre el dataset de tags"""
    if tags_df is None:
        return jsonify({"error": "Tags dataset not loaded"}), 404
    
    # Iloc examples como en el script original
    iloc_examples = []
    try:
        iloc_examples = tags_df.iloc[[0, 11, min(2000, len(tags_df)-1)]].to_dict('records')
    except:
        iloc_examples = tags_df.iloc[[0, min(11, len(tags_df)-1)]].to_dict('records')
    
    return jsonify({
        "head_2": tags_df.head(2).to_dict('records'),
        "iloc_examples": iloc_examples,
        "columns": tags_df.columns.tolist(),
        "index": tags_df.index.tolist()[:10],
        "shape": tags_df.shape,
        "null_check": tags_df.isnull().any().to_dict()
    })

@app.route('/ratings/statistics')
def ratings_statistics():
    """Estadísticas del dataset de ratings"""
    if ratings_df is None:
        return jsonify({"error": "Ratings dataset not loaded"}), 404
    
    stats = ratings_df['rating'].describe()
    
    return jsonify({
        "statistics": stats.to_dict(),
        "mean": float(ratings_df['rating'].mean()),
        "max": float(ratings_df['rating'].max()),
        "min": float(ratings_df['rating'].min()),
        "raw_data": ratings_df['rating'].tolist()[:1000]  # Primeros 1000 datos para gráficos
    })

@app.route('/ratings/filter')
def ratings_filter():
    """Filtros sobre ratings"""
    if ratings_df is None:
        return jsonify({"error": "Ratings dataset not loaded"}), 404
    
    # Filtro rating > 5.0
    filter_5 = ratings_df['rating'] > 5.0
    # Filtro rating > 0
    filter_0 = ratings_df['rating'] > 0
    
    return jsonify({
        "filter_rating_gt_5": {
            "any_match": bool(filter_5.any()),
            "count": int(filter_5.sum()),
            "percentage": float(filter_5.mean() * 100)
        },
        "filter_rating_gt_0": {
            "any_match": bool(filter_0.any()),
            "count": int(filter_0.sum()),
            "percentage": float(filter_0.mean() * 100)
        }
    })

@app.route('/data/null-check')
def data_null_check():
    """Verificación de valores nulos en todos los datasets"""
    result = {}
    
    if movies_df is not None:
        result["movies"] = {
            "shape": movies_df.shape,
            "null_check": movies_df.isnull().any().to_dict(),
            "null_counts": movies_df.isnull().sum().to_dict()
        }
    
    if ratings_df is not None:
        result["ratings"] = {
            "shape": ratings_df.shape,
            "null_check": ratings_df.isnull().any().to_dict(),
            "null_counts": ratings_df.isnull().sum().to_dict()
        }
    
    if tags_df is not None:
        result["tags"] = {
            "shape": tags_df.shape,
            "null_check": tags_df.isnull().any().to_dict(),
            "null_counts": tags_df.isnull().sum().to_dict()
        }
    
    return jsonify(result)

@app.route('/upload-data', methods=['POST'])
def upload_data():
    """Endpoint para subir datos manualmente (simulación)"""
    data = request.get_json()
    
    if 'ratings' in data:
        global ratings_df
        ratings_df = pd.DataFrame(data['ratings'])
        return jsonify({"message": "Ratings data uploaded successfully"})
    
    return jsonify({"error": "No valid data provided"}), 400

# Endpoint alias: /filters/demo -> /ratings/filter
@app.route('/filters/demo')
def filters_demo():
    return ratings_filter()

# Endpoint alias: /dataset/null-check -> /data/null-check
@app.route('/dataset/null-check')
def dataset_null_check():
    return data_null_check()

if __name__ == '__main__':
    # Cargar datos al iniciar
    load_data()
    
    print("🚀 Pandas Data Analysis API Started!")
    print("📊 Available endpoints:")
    print("   - http://localhost:5000/")
    print("   - http://localhost:5000/series-demo")
    print("   - http://localhost:5000/dataframe-demo")
    print("   - http://localhost:5000/ratings/statistics")
    print("   - http://localhost:5000/ratings/filter")
    print("   - http://localhost:5000/data/null-check")
    
    app.run(debug=True, host='0.0.0.0', port=5000)