import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text


import wordcloud, palettable
from wordcloud import ImageColorGenerator
from PIL import Image
import numpy as np
import random
import jieba

from word_cloud import build_word_cloud

app = Flask(__name__)
app.config["DEBUG"] = True

# SQLite Connection Configurations to Database
import os
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "scripture.db"))
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


class CUV(db.Model):
    __tablename__ = "CUV"
    id = db.Column('ID', db.Integer, primary_key=True)
    book = db.Column('Book', db.String(10))
    chapter = db.Column('Chapter', db.Integer)
    category = db.Column('Category', db.Integer)
    verse = db.Column('Verse', db.Integer)
    scripture = db.Column('Scripture', db.String(1000))


class Book_Chapters(db.Model):
    __tablename__ = "book_chapters"
    id = db.Column('ID', db.Integer, primary_key=True)
    book = db.Column('Book', db.String(5))
    bookF = db.Column('BookF', db.String(10))
    chapters = db.Column('Chapters', db.Integer)


class Chapter_Verses(db.Model):
    __tablename__ = "chapter_verses"
    id = db.Column('ID', db.Integer, primary_key=True)
    book = db.Column('Book', db.String(5))
    chapter = db.Column('Chapter', db.Integer)
    verses = db.Column('Verses', db.Integer)


db.create_all()
db.session.commit()


@app.route("/", methods=["GET"])
def scripture():
    verses = CUV.query.filter_by(book='詩', chapter=1).all()
    book_chapters = Book_Chapters.query.all()
    return render_template("scripture.html", verses=verses, book_chapters=book_chapters)


@app.route('/reload')
def reload():
    book = request.args.get('jsbook')
    chapter = request.args.get('jschapter')
    if book and chapter:
        verses = CUV.query.filter_by(book=book, chapter=chapter).all()

    return render_template('scripture_content.html', verses=verses)


def separate(content):
    seg_list = jieba.cut(content, cut_all=True)
    return ' '.join(seg_list)


@app.route('/word_cloud')
def word_cloud():
    icon_path = 'static/images/heart.png'
    icon = Image.open(icon_path)
    mask = Image.new("RGB", icon.size, (255,255,255))
    mask.paste(icon, icon)
    mask = np.array(mask)
    color_func = ImageColorGenerator(mask)

    book = request.args.get('jsbook')
    chapter = request.args.get('jschapter')

    if book is None: book = '詩'
    if chapter is None: chapter = 1
    verses = CUV.query.filter_by(book=book, chapter=chapter).all()

    verse_text = ''
    for v in verses:
        verse_text += v.scripture.replace('\u3000', ' ')

    jieba.load_userdict('static/data/scripture_dict.utf8')
    word_list = separate(verse_text)
    cloud_url = build_word_cloud(word_list, mask, color_func);
    return render_template('word_cloud.html', book=book, chapter=chapter, cloud_url=cloud_url)

'''
@app.route("/init_db")
def init_db():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    sql_file = os.path.join(project_dir, "CUV_data.txt")

    for line in open(sql_file, encoding='utf-8-sig'):
        db.engine.execute(text(line))
'''

if __name__ == "__main__":
    app.debug = True
    #init_db()  #Load Records to Database
    app.run()
