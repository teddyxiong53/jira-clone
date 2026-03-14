from flask import Flask, jsonify, request
from flask_cors import CORS
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime

app = Flask(__name__)
CORS(app)

DATABASE_URL = 'sqlite:///jira.db'
engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    avatar = Column(String)

    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'email': self.email,
            'avatar': self.avatar or f'https://i.pravatar.cc/150?img={self.id}'
        }


class Issue(Base):
    __tablename__ = 'issues'
    id = Column(Integer, primary_key=True)
    key = Column(String, nullable=False, unique=True)
    summary = Column(String, nullable=False)
    description = Column(String)
    status = Column(String, default='todo')
    priority = Column(String, default='medium')
    assignee_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    reporter_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    labels = Column(String)
    story_points = Column(Integer)
    created = Column(String, default=lambda: datetime.now().isoformat())
    updated = Column(String, default=lambda: datetime.now().isoformat())

    def to_dict(self):
        assignee = session.query(User).get(self.assignee_id) if self.assignee_id else None
        reporter = session.query(User).get(self.reporter_id)
        return {
            'id': str(self.id),
            'key': self.key,
            'summary': self.summary,
            'description': self.description or '',
            'status': self.status,
            'priority': self.priority,
            'assignee': assignee.to_dict() if assignee else None,
            'reporter': reporter.to_dict() if reporter else None,
            'labels': self.labels.split(',') if self.labels else [],
            'storyPoints': self.story_points,
            'created': self.created,
            'updated': self.updated
        }


Base.metadata.create_all(engine)
session = Session()


@app.route('/api/issues', methods=['GET'])
def get_issues():
    issues = session.query(Issue).all()
    return jsonify([issue.to_dict() for issue in issues])


@app.route('/api/issues/<int:issue_id>', methods=['GET'])
def get_issue(issue_id):
    issue = session.query(Issue).get(issue_id)
    if not issue:
        return jsonify({'error': 'Issue not found'}), 404
    return jsonify(issue.to_dict())


@app.route('/api/issues', methods=['POST'])
def create_issue():
    data = request.json
    max_id = session.query(Issue).order_by(Issue.id.desc()).first()
    new_id = (max_id.id + 1) if max_id else 1
    key = f'PROJ-{str(new_id).zfill(4)}'
    
    issue = Issue(
        key=key,
        summary=data.get('summary', ''),
        description=data.get('description', ''),
        status=data.get('status', 'todo'),
        priority=data.get('priority', 'medium'),
        assignee_id=data.get('assignee_id'),
        reporter_id=data.get('reporter_id', 1),
        labels=','.join(data.get('labels', [])),
        story_points=data.get('storyPoints')
    )
    session.add(issue)
    session.commit()
    return jsonify(issue.to_dict()), 201


@app.route('/api/issues/<int:issue_id>', methods=['PUT'])
def update_issue(issue_id):
    issue = session.query(Issue).get(issue_id)
    if not issue:
        return jsonify({'error': 'Issue not found'}), 404
    
    data = request.json
    if 'summary' in data:
        issue.summary = data['summary']
    if 'description' in data:
        issue.description = data['description']
    if 'status' in data:
        issue.status = data['status']
    if 'priority' in data:
        issue.priority = data['priority']
    if 'assignee_id' in data:
        issue.assignee_id = data['assignee_id']
    if 'labels' in data:
        issue.labels = ','.join(data['labels']) if isinstance(data['labels'], list) else data['labels']
    if 'storyPoints' in data:
        issue.story_points = data['storyPoints']
    
    issue.updated = datetime.now().isoformat()
    session.commit()
    return jsonify(issue.to_dict())


@app.route('/api/issues/<int:issue_id>', methods=['DELETE'])
def delete_issue(issue_id):
    issue = session.query(Issue).get(issue_id)
    if not issue:
        return jsonify({'error': 'Issue not found'}), 404
    session.delete(issue)
    session.commit()
    return jsonify({'message': 'Deleted'})


@app.route('/api/users', methods=['GET'])
def get_users():
    users = session.query(User).all()
    return jsonify([user.to_dict() for user in users])


if __name__ == '__main__':
    app.run(port=5000, debug=True)