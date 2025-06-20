import type { IconDefinition } from '@fortawesome/free-brands-svg-icons';

// Camel case to snake_case conversion
export type CamelToSnakeKeys<KeyToConvert extends string | number | symbol> =
  KeyToConvert extends `${infer FirstPartOfKey}${infer SecondPartOfKey}`
    ? `${FirstPartOfKey extends Capitalize<FirstPartOfKey> ? '_' : ''}${Lowercase<FirstPartOfKey>}${CamelToSnakeKeys<SecondPartOfKey>}`
    : KeyToConvert;

export type CamelCaseObjectToDeepSnake<CamelCaseObject> = {
  [ObjectsKey in keyof CamelCaseObject as CamelToSnakeKeys<ObjectsKey>]: CamelCaseObjectToDeepSnake<
    CamelCaseObject[ObjectsKey]
  >;
};
// Camel case to snake_case conversion

export type AuthToken = {
  accessToken: string;
  tokenType: string;
  expiry: Date;
  refreshToken: string;
};

// export type AuthTokenResponse = CamelCaseObjectToDeepSnake<AuthToken> | { expires_in: number };

export interface AuthTokenResponse extends CamelCaseObjectToDeepSnake<Omit<AuthToken, 'expiry'>> {
  expires_in: number;
}

export type AuthCredentials = {
  grant_type: string;
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
  language?: string;
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
