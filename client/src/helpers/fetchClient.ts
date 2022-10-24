import { HTTPMethods, NoteType } from "../types";

const API_URL = window.localStorage.getItem(
  process.env.REACT_APP_SERVER as string
);

const fetchClientPostWithoutToken = async (
  url: string,
  data: object
): Promise<any> => {
  const response = await fetch(`${API_URL}/api${url}`, {
    method: HTTPMethods.POST,
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  })
    .then(async (data) => {
      if (data.status !== 200) {
        throw new Error(data.statusText);
      }
      const responseStatus = data.status;
      const responseData = await data.json();

      return {
        status: responseStatus,
        data: responseData
      };
    })

  return response;
}

const fetchClientGetWithoutToken = async (
  url: string,
): Promise<any> => {
  const response = await fetch(`${API_URL}/api${url}`, {
    method: HTTPMethods.GET,
    headers: {
      "Content-Type": "application/json"
    },
  })
    .then(async (data) => {
      if (data.status !== 200) {
        throw new Error(data.statusText);
      }
      const responseStatus = data.status;
      const responseData = await data.json();

      return {
        status: responseStatus,
        data: responseData
      };
    })

  return response;
}

const fetchClientGet = async (
  url: string,
  token: string,
): Promise<any> => {
  const response = await fetch(`${API_URL}/api${url}`, {
    method: HTTPMethods.GET,
    headers: {
      "Authorization": `Bearer ${token}`,
      "Content-Type": "application/json"
    },
  })
    .then(async (data) => {
      if (data.status !== 200) {
        throw new Error(data.statusText);
      }
      const responseStatus = data.status;
      const responseData = await data.json();

      return {
        status: responseStatus,
        data: responseData
      };
    })

  return response;
}

const fetchClientPost = async (
  url: string,
  token: string,
  payload: NoteType
): Promise<any> => {
  const response = await fetch(`${API_URL}/api${url}`, {
    method: HTTPMethods.POST,
    headers: {
      "Authorization": `Bearer ${token}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload),
  })
    .then(async (data) => {
      if (data.status !== 200) {
        throw new Error(data.statusText);
      }
      const responseStatus = data.status;

      return {
        status: responseStatus,
      };
    })

  return response;
}

export { fetchClientPostWithoutToken, fetchClientGetWithoutToken, fetchClientGet, fetchClientPost }
