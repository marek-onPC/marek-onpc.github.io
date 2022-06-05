import { HTTPMethods } from "../types";

const fetchClientPostWithoutToken = async (
  url: string,
  data: object
): Promise<any> => {
  const response = await fetch(`/api${url}`, {
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

const fetchClientGet = async (
  url: string,
  token: string,
): Promise<any> => {
  const response = await fetch(`/api${url}`, {
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

export { fetchClientPostWithoutToken, fetchClientGet }
