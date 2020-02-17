from flask import request, jsonify
from . models import Match, Team, db
from strafe import app
import json
from datetime import datetime

@app.route('/teams', methods = ['GET'])
def getTeams():
    teams = Team.query.all()
    return jsonify(result=[team.serialize() for team in teams])

@app.route('/teams', methods = ['POST'])
def createTeam():
    data = get_json()
    try:
        name = data['name']
        team = Team(name)
        db.session.add(team)
        db.session.commit()
        return {}, 201
    except Exception as error:
        print(error)
        return {}, 500


@app.route('/teams/<tid>', methods = ['DELETE'])
def deleteTeam(tid):
    team = Team.query.get(tid)
    try:
        db.session.delete(team)
        db.session.commit()
        return {}, 201
    except Exception as error:
        print(Exception)
        return {}, 500


@app.route('/teams/<tid>', methods = ['PUT'])
def updateTeam(tid):
    team = Team.query.get(tid)
    data = request.get_json()
    try:
        team.name = data['name']
        db.session.commit()
        return {}, 201
    except Exception as error:
        print(error)
        return {}, 500

@app.route('/matches', methods = ['GET'])
def getMatches():
    matches = Match.query.all()
    return jsonify(result=[match.serialize() for match in matches])



@app.route('/matches', methods = ['POST'])
def createMatch():
    data = request.get_json()
    try:
        name = data['name']
        guest_team = data['guest_team']
        home_team = data['home_team']
        date_time = datetime.strptime(data['date_time'], "%Y-%m-%dT%H:%M:%S.%fZ")
        match = Match(name, home_team, guest_team, date_time)
        db.session.add(match)
        db.session.commit()
        return {}, 201
    except Exception as error:
        print(error)
        return {}, 500


@app.route('/matches/<mid>', methods = ['DELETE'])
def deleteMatch(mid):
    match = Match.query.get(mid)
    try:
        db.session.delete(match)
        db.session.commit()
        return {}, 201
    except Exception as error:
        print(error)
        return {}, 500


@app.route('/matches/<mid>', methods = ['PUT'])
def updateMatch(mid):
    match = Match.query.get(mid)
    data = request.get_json()
    try:
        match.name = data['name']
        match.home_score = data['home_score']
        match.guest_score = data['guest_score']
        match.date_time = datetime.strptime(data['date_time'], "%Y-%m-%dT%H:%M:%S.%fZ")
        db.session.commit()
        return {}, 201
    except Exception as error:
        print(error)
        return {}, 500
