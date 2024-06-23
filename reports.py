from flask import Blueprint, send_file
from app.models import Material
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

reports = Blueprint('reports', __name__)

@reports.route('/reports/completed', methods=['GET'])
def completed_report():
    materials = Material.query.filter_by(status='Distribuição').all()
    output = io.BytesIO()
    c = canvas.Canvas(output, pagesize=letter)
    c.drawString(100, 750, "Relatório de Materiais Concluídos")
    y = 700
    for material in materials:
        c.drawString(100, y, f"{material.name} - {material.type} - {material.expiry_date}")
        y -= 20
    c.save()
    output.seek(0)
    return send_file(output, attachment_filename='completed_report.pdf', as_attachment=True)

@reports.route('/reports/failures', methods=['GET'])
def failure_report():
    materials = Material.query.filter(Material.status != 'Distribuição').all()
    df = pd.DataFrame([(m.name, m.type, m.expiry_date, m.status) for m in materials],
                      columns=['Name', 'Type', 'Expiry Date', 'Status'])
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Failures')
    output.seek(0)
    return send_file(output, attachment_filename='failure_report.xlsx', as_attachment=True)
