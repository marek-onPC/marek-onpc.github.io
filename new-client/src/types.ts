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

export interface UnsavedCheetSheetType {
  title: string;
  categories?: Array<string>;
  is_published: boolean;
}

export interface UpdateCheetSheetType extends UnsavedCheetSheetType {
  content?: string;
}

export interface CheetSheetCardType extends UnsavedCheetSheetType {
  id: string;
}

export interface CheetSheetWithContentType extends CheetSheetCardType {
  content?: string;
}

export enum HTTPMethods {
  POST = 'POST',
  GET = 'GET',
  PATCH = 'PATCH',
  DELETE = 'DELETE'
}
