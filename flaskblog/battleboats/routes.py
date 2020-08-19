from flask import Blueprint
from flask import render_template, url_for, flash, redirect, request, abort
from flaskblog.battleboats.forms import BattleBoatsSetUp, PlaceRocks
from flask_login import login_required, current_user
from flaskblog.battleboats.actions import setNumberBoats, setUpBoardSkeleton, randomizeBoard
from flaskblog.models import BattleBoatsGame
from flaskblog import db

battleboats = Blueprint('battleboats', __name__)

@login_required
@battleboats.route('/battleboats_page', methods=['GET','POST'])
def battleboats_page():
    form = BattleBoatsSetUp()
    if form.validate_on_submit():
        rows = form.rows.data
        columns = form.columns.data
        rocks = form.rocks.data
        boatNumber = setNumberBoats(rows, columns)
        #game = BattleBoatsGame(rows=rows, columns=columns, rocks=rocks, boatNumber=boatNumber)
        #db.session.add(game)
        #db.session.commit()
        items = []
        temp_cells, letter_columns = setUpBoardSkeleton(rows, columns, items)
        print(cells)
        cells = randomizeBoard(rows, columns, temp_cells, rocks, boatNumber)

        #return redirect(url_for('battleboats.battleboats_rocks', form=form, cells=cells))
        return render_template('battleboats/battleboats_rocks.html', title="BattleBoatsSetUpRocks", form=form, cells=cells, letter_columns=letter_columns)
    return render_template('battleboats/battleboats_page.html', title="BattleBoats", form=form)

@login_required
@battleboats.route('/battleboats_rocks', methods=['GET','POST'])
def battleboats_rocks():
    #form = PlaceRocks()
    #if form.validate_on_submit():
    #    return render_template('battleboats/battleboats_rocks.html', title="BattleBoatsSetUpRocks", form=form)
    return render_template('battleboats/battleboats_rocks.html', title="BattleBoatsSetUpRocks")
