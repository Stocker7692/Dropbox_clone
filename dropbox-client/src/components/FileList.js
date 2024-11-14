// src/components/FileList.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function FileList() {
  const [files, setFiles] = useState([]);

  const fetchFiles = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/files/');
      setFiles(response.data);
    } catch (error) {
      console.error('Error fetching files:', error);
    }
  };

  const handleFileDownload = async (id, name) => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/api/files/${id}/download/`, {
        responseType: 'blob',
      });
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', name);
      document.body.appendChild(link);
      link.click();
      link.parentNode.removeChild(link);
    } catch (error) {
      console.error('Error downloading file:', error);
    }
  };

  useEffect(() => {
    fetchFiles();
  }, []);

  return (
    <div>
      <h2>Uploaded Files</h2>
      <ul>
        {files.map((file) => (
          <li key={file.id}>
            {file.name} ({file.size} bytes)
            <button onClick={() => handleFileDownload(file.id, file.name)}>Download</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default FileList;
