from app import app
from flask import render_template, abort, redirect, url_for
from flask import request

from forms import SubjectColumnAnnotatorForm
from forms import UsernameForm

from TableSelector.SubjectColumnTableSelector import SubjectColumnTableSelector
from model import GoogleSpreadsheet

from taipan.T2D.Sampler import T2DSampler

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/subjectColumnAnnotation', methods=['GET', 'POST'])
def annotateSubjectColumnIndex():
    form = UsernameForm(request.form)
    if request.method == 'POST' and form.validate():
        username = request.form.get('username', '')
        return redirect(url_for('annotateSubjectColumnRandom', username=username))
    return render_template("annotateSubjectColumnIndex.html", form=form)

@app.route('/propertyAnnotation', methods=['GET', 'POST'])
def annotatePropertyIndex():
    form = UsernameForm(request.form)
    if request.method == 'POST' and form.validate():
        username = request.form.get('username', '')
        return redirect(url_for('annotatePropertyRandom', username=username))
    return render_template("annotatePropertyIndex.html", form=form)

@app.route('/help')
def help():
    return render_template("help.html")

@app.route('/table/annotateSubjectColumn/<username>')
def annotateSubjectColumnRandom(username):
    tableSelector = SubjectColumnTableSelector()
    tableId = tableSelector.getRandomTableId()
    return redirect(url_for('annotateSubjectColumn', username=username, tableId=tableId))

@app.route('/table/annotateProperty/<username>')
def annotatePropertyRandom(username):
    t2dSampler = T2DSampler()
    tableIds = t2dSampler.getTablesSubjectIdentificationIds()
    tableId = random.choice(tableIds)
    return redirect(url_for('annotateProperty', username=username, tableId=tableId))

@app.route('/table/annotateSubjectColumn/<username>/<tableId>', methods=['GET', 'POST'])
def annotateSubjectColumn(username, tableId):
    gSpread = GoogleSpreadsheet()
    worksheet = gSpread.createOrGetNamedWorksheet(username)
    if request.method == 'POST':
        noSubjectColumn = request.form.get('noSubjectColumn', "FALSE")
        if noSubjectColumn == 'y':
            noSubjectColumn = "TRUE"
        subjectColumn =  request.form.get('subjectColumn', None)
        tableType =  request.form.get('tableType', None)
        if subjectColumn == '' and noSubjectColumn == "FALSE" and tableType == "Normal":
            pass
        else:
            worksheet.append_row([tableId, subjectColumn, noSubjectColumn, tableType])
            return redirect(url_for('annotateSubjectColumnRandom', username=username))

    numOfAnnotatedTables = worksheet.row_count - 1
    form = SubjectColumnAnnotatorForm()
    tableSelector = SubjectColumnTableSelector()
    table = tableSelector.getTable(tableId)
    return render_template("annotateSubjectColumn.html", form=form, table=table, username=username, tableId=tableId, numOfAnnotatedTables=numOfAnnotatedTables)

@app.route('/table/annotateProperty/<username>/<tableId>', methods=['GET', 'POST'])
def annotateProperty(username, tableId):
    #gSpread = GoogleSpreadsheet()
    #worksheet = gSpread.createOrGetNamedWorksheet(username)
    if request.method == 'POST':
        noSubjectColumn = request.form.get('noSubjectColumn', "FALSE")
        if noSubjectColumn == 'y':
            noSubjectColumn = "TRUE"
        subjectColumn =  request.form.get('subjectColumn', None)
        tableType =  request.form.get('tableType', None)
        if subjectColumn == '' and noSubjectColumn == "FALSE" and tableType == "Normal":
            pass
        else:
            worksheet.append_row([tableId, subjectColumn, noSubjectColumn, tableType])
            return redirect(url_for('annotateSubjectColumnRandom', username=username))

    numOfAnnotatedTables = worksheet.row_count - 1
    form = SubjectColumnAnnotatorForm()
    tableSelector = SubjectColumnTableSelector()
    table = tableSelector.getTable(tableId)
    return render_template("annotateSubjectColumn.html", form=form, table=table, username=username, tableId=tableId, numOfAnnotatedTables=numOfAnnotatedTables)
