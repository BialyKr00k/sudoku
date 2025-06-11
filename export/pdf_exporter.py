from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas 
from database.db import Session
from database.models import GameResult, User
from pathlib import Path
import os

def export_results_pdf(user, level):
    session = Session()
    results = (
        session.query(GameResult).filter_by(difficulty=level).join(User).order_by(GameResult.score.desc()).all()
    )

    downloads_path = Path.home() / "Downloads"
    filename = f"{user.username}_{level}_results.pdf"
    file_path = downloads_path / filename

    c = canvas.Canvas(str(file_path), pagesize=A4)
    width, height = A4
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 50, f"Sudoku - {level.capitalize()} Results")

    c.setFont("Helvetica", 12)
    y = height - 100
    c.drawString(50, y, "Username")
    c.drawString(200, y, "Score")
    c.drawString(300, y, "Time (s)")
    y -= 20

    for result in results:
        c.drawString(50, y, result.user.username)
        c.drawString(200, y, str(result.score))
        c.drawString(300, y, str(result.time_seconds))
        y -= 20

        if y < 50:
            c.showPage()
            y = height - 50

    c.save()
    session.close()
    
    return str(file_path)
