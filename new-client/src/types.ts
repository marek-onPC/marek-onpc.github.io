import type { IconDefinition } from '@fortawesome/free-brands-svg-icons';

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

export interface UnsavedCheatSheetType {
  title: string;
  categories?: Array<string>;
  is_published: boolean;
}

export interface UpdateCheatSheetType extends UnsavedCheatSheetType {
  content?: string;
}

export interface CheatSheetCardType extends UnsavedCheatSheetType {
  id: string;
}

export interface CheatSheetWithContentType extends CheatSheetCardType {
  content?: string;
}

export enum HTTPMethods {
  POST = 'POST',
  GET = 'GET',
  PATCH = 'PATCH',
  DELETE = 'DELETE'
}
