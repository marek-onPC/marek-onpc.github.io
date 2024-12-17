import {
  PUBLIC_APP_LOCAL_STORAGE_TOKEN,
  PUBLIC_APP_LOCAL_STORAGE_EXPIRY
} from '$env/static/public';
import type { AuthToken } from '../types';

const setTokenInMemory = ({ token, expiry }: AuthToken): void => {
  window.localStorage.setItem(PUBLIC_APP_LOCAL_STORAGE_TOKEN, token);
  window.localStorage.setItem(PUBLIC_APP_LOCAL_STORAGE_EXPIRY, expiry.toISOString());
};

const getTokenFromMemory = (): AuthToken => {
  const token = window.localStorage.getItem(PUBLIC_APP_LOCAL_STORAGE_TOKEN) || '';
  const expiry = window.localStorage.getItem(PUBLIC_APP_LOCAL_STORAGE_EXPIRY) || '';

  let expiryDate = new Date();

  if (expiry) {
    expiryDate = new Date(expiry);
  }
  return {
    token: token,
    expiry: expiryDate
  };
};

const removeTokenInMemory = (): void => {
  window.localStorage.removeItem(PUBLIC_APP_LOCAL_STORAGE_TOKEN);
  window.localStorage.removeItem(PUBLIC_APP_LOCAL_STORAGE_EXPIRY);
};

export { setTokenInMemory, getTokenFromMemory, removeTokenInMemory };
