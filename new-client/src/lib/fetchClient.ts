import { HTTPMethods } from '../types';
import { PUBLIC_APP_SERVER } from '$env/static/public';

const fetchClientPostWithoutToken = async (url: string, data: object): Promise<any> => {
  const response = await fetch(`${PUBLIC_APP_SERVER}${url}`, {
    method: HTTPMethods.POST,
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  }).then(async (data) => {
    if (data.status !== 200) {
      throw new Error(data.statusText);
    }
    const responseStatus = data.status;
    const responseData = await data.json();

    return {
      status: responseStatus,
      data: responseData
    };
  });

  return response;
};

const fetchClientGetWithoutToken = async (url: string): Promise<any> => {
  const response = await fetch(`${PUBLIC_APP_SERVER}${url}`, {
    method: HTTPMethods.GET,
    headers: {
      'Content-Type': 'application/json'
    }
  }).then(async (data) => {
    if (data.status !== 200) {
      throw new Error(data.statusText);
    }
    const responseStatus = data.status;
    const responseData = await data.json();

    return {
      status: responseStatus,
      data: responseData
    };
  });

  return response;
};

export { fetchClientPostWithoutToken, fetchClientGetWithoutToken };
