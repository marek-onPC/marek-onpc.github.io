import type { IconDefinition } from '@fortawesome/free-brands-svg-icons';

export type AuthTokenResponse = {
  token: string;
  expiry: number;
};

export type AuthToken = {
  token: string;
  expiry: Date;
};

export type AuthCredentials = {
  username: string;
  password: string;
};

export type DynamicContext = {
  [key: string]: any;
};

export type IconSet = {
  icon: IconDefinition;
  color: string;
};

export type CheatSheetContent = {
  subtitle: string;
  content: string;
};

export interface UnsavedCheatSheetType {
  title: string;
  categories?: Array<string>;
  is_published: boolean;
}

export interface SavedCheatSheetResponseType {
  id: string;
}

export interface UpdateCheatSheetType extends UnsavedCheatSheetType {
  cards?: Array<CheatSheetContent>;
}

export interface CheatSheetCardType extends UnsavedCheatSheetType {
  id: string;
}

export interface CheatSheetWithContentType extends CheatSheetCardType {
  cards?: Array<CheatSheetContent>;
}

export enum HTTPMethods {
  POST = 'POST',
  GET = 'GET',
  PATCH = 'PATCH',
  DELETE = 'DELETE'
}

export type CheatSheetGetFilters = {
  is_published__list?: Array<boolean>;
};
