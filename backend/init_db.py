from app import engine, Base, session, User, Issue
from datetime import datetime

Base.metadata.create_all(engine)

existing_users = session.query(User).count()
if existing_users == 0:
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
    print('Database already exists!')

print(f'Users: {session.query(User).count()}')
print(f'Issues: {session.query(Issue).count()}')