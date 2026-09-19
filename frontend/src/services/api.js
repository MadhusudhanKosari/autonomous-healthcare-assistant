import axios from "axios";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "https://autonomous-healthcare-assistant-qt45.onrender.com";

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