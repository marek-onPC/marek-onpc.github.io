export type AuthCredentials = {
  username: string;
  password: string;
};

export type DynamicContext = {
  [key: string]: any
}

export enum HTTPMethods {
  POST = "POST",
  GET = "GET",
  DELETE = "DELETE"
}