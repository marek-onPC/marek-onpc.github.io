import { PUBLIC_APP_LOCAL_STORAGE_TOKEN } from "$env/static/public";

const setTokenInMemory = (token: string): void => {
  window.localStorage.setItem(
    PUBLIC_APP_LOCAL_STORAGE_TOKEN, token
  );
}

const getTokenFromMemory = (): string => {
  return window.localStorage.getItem(
    PUBLIC_APP_LOCAL_STORAGE_TOKEN
  ) || "";
}

export {setTokenInMemory, getTokenFromMemory}
