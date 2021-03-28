import flask
from flask import jsonify, request

from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_news():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict()
                 for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['GET'])
def get_one_jobs(jobs_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(jobs_id)
    if not jobs:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'jobs': jobs.to_dict()
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return flask.jsonify({'error': 'Empty request'})
    elif not all(
            key in request.json for key in ['id', 'team_leader', 'job', 'work_size', 'collaborators', 'is_finished']):
        return flask.jsonify({'error': 'Bad request'})
    session = db_session.create_session()
    if session.query(Jobs).get(request.json['id']):
        return flask.jsonify({'error': ' Id already exists'})
    jobs = Jobs(id=request.json['id'], team_leader=request.json['team_leader'],
                job=request.json['job'],
                work_size=request.json['work_size'],
                collaborators=request.json['collaborators'],
                is_finished=request.json['is_finished'])
    session.add(jobs)
    session.commit()
    return flask.jsonify({'success': 'OK'})

@blueprint.route('/api/jobs/<int:jobs_id>', methods=['DELETE'])
def delete_jobs(jobs_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(jobs_id)
    if not job:
        return jsonify({'error': 'Not found'})
    db_sess.delete(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})

