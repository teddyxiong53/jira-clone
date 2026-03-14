#!/bin/bash

# Start both frontend and backend

echo "Starting backend server..."
cd backend
python app.py &
BACKEND_PID=$!
cd ..

echo "Starting frontend..."
npm run dev &
FRONTEND_PID=$!

echo "Backend PID: $BACKEND_PID"
echo "Frontend PID: $FRONTEND_PID"
echo ""
echo "Access the app at: http://localhost:5173"
echo "API is available at: http://localhost:5000/api"
echo ""
echo "Press Ctrl+C to stop both servers"

trap "kill $BACKEND_PID $FRONTEND_PID" EXIT

wait