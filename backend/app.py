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


def init_sample_data():
    if session.query(User).count() == 0:
        users = [
            User(name='John Smith', email='john@example.com', avatar='https://i.pravatar.cc/150?img=1'),
            User(name='Sarah Johnson', email='sarah@example.com', avatar='https://i.pravatar.cc/150?img=2'),
            User(name='Mike Davis', email='mike@example.com', avatar='https://i.pravatar.cc/150?img=3'),
            User(name='Emily Brown', email='emily@example.com', avatar='https://i.pravatar.cc/150?img=4'),
            User(name='Alex Wilson', email='alex@example.com', avatar='https://i.pravatar.cc/150?img=5'),
            User(name='Lisa Chen', email='lisa@example.com', avatar='https://i.pravatar.cc/150?img=6'),
            User(name='David Lee', email='david@example.com', avatar='https://i.pravatar.cc/150?img=7'),
            User(name='Anna Martinez', email='anna@example.com', avatar='https://i.pravatar.cc/150?img=8'),
        ]
        session.add_all(users)
        session.commit()

        issues = [
            Issue(key='PROJ-0001', summary='Set up user authentication system', description='Implement OAuth2 authentication with JWT tokens.', status='todo', priority='highest', assignee_id=1, reporter_id=2, labels='backend,security', story_points=5, created='2026-03-01T10:00:00Z', updated='2026-03-10T14:30:00Z'),
            Issue(key='PROJ-0002', summary='Design dashboard UI components', description='Create reusable dashboard components.', status='inprogress', priority='high', assignee_id=2, reporter_id=1, labels='frontend,ui', story_points=8, created='2026-03-02T09:00:00Z', updated='2026-03-12T11:20:00Z'),
            Issue(key='PROJ-0003', summary='Fix navigation menu dropdown', description='Menu not closing on mobile.', status='done', priority='medium', assignee_id=3, reporter_id=4, labels='bug,mobile', story_points=2, created='2026-03-03T08:00:00Z', updated='2026-03-08T16:45:00Z'),
            Issue(key='PROJ-0004', summary='Implement search functionality', description='Global search with autocomplete.', status='todo', priority='high', assignee_id=4, reporter_id=2, labels='feature,search', story_points=5, created='2026-03-04T10:30:00Z', updated='2026-03-11T09:15:00Z'),
            Issue(key='PROJ-0005', summary='Optimize database queries', description='Improve query performance.', status='inprogress', priority='medium', assignee_id=5, reporter_id=3, labels='backend,performance', story_points=3, created='2026-03-05T14:00:00Z', updated='2026-03-13T10:00:00Z'),
            Issue(key='PROJ-0006', summary='Create user profile page', description='Profile page with editing.', status='todo', priority='low', assignee_id=6, reporter_id=1, labels='frontend,profile', story_points=3, created='2026-03-06T11:00:00Z', updated='2026-03-12T15:30:00Z'),
            Issue(key='PROJ-0007', summary='Add unit tests for API endpoints', description='Write comprehensive unit tests.', status='todo', priority='medium', assignee_id=7, reporter_id=5, labels='testing,backend', story_points=5, created='2026-03-07T09:30:00Z', updated='2026-03-11T13:45:00Z'),
            Issue(key='PROJ-0008', summary='Implement file upload feature', description='Drag and drop file upload.', status='inprogress', priority='high', assignee_id=8, reporter_id=2, labels='feature,upload', story_points=8, created='2026-03-08T08:00:00Z', updated='2026-03-14T10:20:00Z'),
            Issue(key='PROJ-0009', summary='Fix timezone display issue', description='Timestamps showing wrong timezone.', status='done', priority='low', assignee_id=1, reporter_id=6, labels='bug,i18n', story_points=1, created='2026-03-09T10:00:00Z', updated='2026-03-10T14:00:00Z'),
            Issue(key='PROJ-0010', summary='Update documentation', description='Update API docs.', status='todo', priority='lowest', assignee_id=2, reporter_id=7, labels='docs', story_points=2, created='2026-03-10T15:00:00Z', updated='2026-03-12T09:00:00Z'),
            Issue(key='PROJ-0011', summary='Refactor authentication module', description='Clean up auth code.', status='todo', priority='medium', assignee_id=3, reporter_id=1, labels='backend,refactor', story_points=3, created='2026-03-11T11:00:00Z', updated='2026-03-13T08:30:00Z'),
            Issue(key='PROJ-0012', summary='Add dark mode support', description='Theme switching.', status='inprogress', priority='low', assignee_id=4, reporter_id=8, labels='frontend,feature', story_points=5, created='2026-03-12T09:00:00Z', updated='2026-03-14T11:45:00Z'),
            Issue(key='PROJ-0013', summary='Setup CI/CD pipeline', description='GitHub Actions setup.', status='done', priority='high', assignee_id=5, reporter_id=3, labels='devops,automation', story_points=5, created='2026-03-01T08:00:00Z', updated='2026-03-05T16:00:00Z'),
            Issue(key='PROJ-0014', summary='Fix memory leak in dashboard', description='Memory leak when navigating.', status='todo', priority='highest', assignee_id=6, reporter_id=4, labels='bug,performance', story_points=8, created='2026-03-13T10:00:00Z', updated='2026-03-14T09:00:00Z'),
            Issue(key='PROJ-0015', summary='Add email notifications', description='Email notifications for actions.', status='todo', priority='medium', assignee_id=7, reporter_id=5, labels='feature,notifications', story_points=3, created='2026-03-14T08:00:00Z', updated='2026-03-14T12:00:00Z'),
        ]
        session.add_all(issues)
        session.commit()
        print('Database initialized with sample data!')
    else:
        print('Database already exists, skipping init.')


init_sample_data()


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


@app.route('/api/auth/register', methods=['POST'])
def register():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    
    if not name or not email or not password:
        return jsonify({'error': 'Missing required fields'}), 400
    
    existing = session.query(User).filter_by(email=email).first()
    if existing:
        return jsonify({'error': 'Email already registered'}), 400
    
    user = User(
        name=name,
        email=email,
        avatar=f'https://i.pravatar.cc/150?u={email}'
    )
    session.add(user)
    session.commit()
    return jsonify(user.to_dict()), 201


@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    
    if not email:
        return jsonify({'error': 'Email required'}), 400
    
    user = session.query(User).filter_by(email=email).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify(user.to_dict())


@app.route('/api/auth/me', methods=['GET'])
def get_current_user():
    user_id = request.headers.get('X-User-Id')
    if not user_id:
        return jsonify({'error': 'Not authenticated'}), 401
    
    user = session.query(User).get(int(user_id))
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify(user.to_dict())


if __name__ == '__main__':
    app.run(port=5000, debug=True)