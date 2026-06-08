import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000";

export const uploadPDF = async (file) => {

  const formData = new FormData();

  formData.append("file", file);

  return axios.post(
    `${API_BASE_URL}/upload/`,
    formData
  );
};

export const getUploadedFiles = async () => {

  return axios.get(
    `${API_BASE_URL}/upload/files`
  );
};

export const sendMessage = async (query) => {

  return axios.post(
    `${API_BASE_URL}/stream-chat/`,
    {
      query
    }
  );
};

export const startNewChat = async () => {

  return axios.post(
    `${API_BASE_URL}/session/new-chat`
  );
};