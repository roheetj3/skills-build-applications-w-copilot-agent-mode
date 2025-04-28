import React, { useEffect, useState } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    fetch('https://skills-build-applications-w-copilot-agent-mode-8000.app.github.dev/api/workouts/')
      .then(response => response.json())
      .then(data => setWorkouts(data))
      .catch(error => console.error('Error fetching workouts:', error));
  }, []);

  return (
    <div className="card shadow mb-4">
      <div className="card-header bg-warning text-dark">
        <h2 className="h4 mb-0">Workouts</h2>
      </div>
      <div className="card-body">
        <table className="table table-striped table-hover">
          <thead className="table-light">
            <tr>
              <th>Name</th>
              <th>Description</th>
            </tr>
          </thead>
          <tbody>
            {workouts.map(workout => (
              <tr key={workout._id}>
                <td>{workout.name}</td>
                <td>{workout.description}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Workouts;
