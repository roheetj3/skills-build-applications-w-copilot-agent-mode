import React, { useEffect, useState } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch('https://skills-build-applications-w-copilot-agent-mode-8000.app.github.dev/api/teams/')
      .then(response => response.json())
      .then(data => setTeams(data))
      .catch(error => console.error('Error fetching teams:', error));
  }, []);

  return (
    <div className="card shadow mb-4">
      <div className="card-header bg-info text-white">
        <h2 className="h4 mb-0">Teams</h2>
      </div>
      <div className="card-body">
        <table className="table table-striped table-hover">
          <thead className="table-light">
            <tr>
              <th>Name</th>
              <th>Members</th>
            </tr>
          </thead>
          <tbody>
            {teams.map(team => (
              <tr key={team._id}>
                <td>{team.name}</td>
                <td>
                  {team.members && Array.isArray(team.members)
                    ? team.members.map((member, idx) => (
                        <span key={idx} className="badge bg-secondary me-1">{member.username || member}</span>
                      ))
                    : ''}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Teams;
